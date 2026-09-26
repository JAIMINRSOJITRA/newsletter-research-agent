"""
src/generators/digest_generator.py
──────────────────────────────────────
Phase 9: Digest Generation. Renders the analyzed articles + themes into a
Markdown newsletter, then a paginated PDF with ReportLab.

Per the README's "Crash-Proof & Resiliency" requirements:
  - Table cells are wrapped in Paragraph flowables (not raw strings) with
    fixed column widths, so long text wraps instead of overflowing the
    page and breaking the PDF build.
  - Empty sections render a placeholder line instead of raising.
  - If PDF generation itself fails for any reason, the Markdown digest
    (already written) is still returned rather than losing the whole run.
"""

import logging
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from config.settings import DIGEST_MD_PATH, DIGEST_PDF_PATH

logger = logging.getLogger("research_agent")

_styles = getSampleStyleSheet()
_cell_style = ParagraphStyle("cell", parent=_styles["BodyText"], fontSize=9, leading=11)


def _build_markdown(analyzed_articles: list, themes: dict) -> str:
    today = datetime.utcnow().strftime("%Y-%m-%d")
    top_themes = themes.get("themes", {}).get("top_themes", [])

    lines = [f"# AI Weekly Research Digest — {today}", "", "## Top Themes This Week"]
    lines += [f"- {t}" for t in top_themes] if top_themes else ["- *No themes identified.*"]
    lines += ["", "## Articles"]

    if not analyzed_articles:
        lines.append("*No articles collected this week.*")
    else:
        by_category = {}
        for a in analyzed_articles:
            by_category.setdefault(a.get("category", "Other"), []).append(a)
        for category, items in by_category.items():
            lines.append(f"### {category}")
            for a in items:
                lines.append(
                    f"**[{a.get('title', 'Untitled')}]({a.get('url', '')})** "
                    f"— *{a.get('source', '')}, {a.get('published', '')}* "
                    f"({a.get('importance', 'Low')} importance)"
                )
                lines.append("")
                lines.append(a.get("summary", "") or "*No summary available.*")
                lines.append("")

    return "\n".join(lines)


def _build_pdf(analyzed_articles: list, themes: dict, pdf_path: str):
    doc = SimpleDocTemplate(
        pdf_path, pagesize=LETTER,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    )
    story = []
    today = datetime.utcnow().strftime("%Y-%m-%d")

    story.append(Paragraph(f"AI Weekly Research Digest — {today}", _styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Top Themes This Week", _styles["Heading2"]))

    top_themes = themes.get("themes", {}).get("top_themes", [])
    if top_themes:
        for t in top_themes:
            story.append(Paragraph(f"• {t}", _styles["BodyText"]))
    else:
        story.append(Paragraph("<i>No themes identified.</i>", _styles["BodyText"]))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Articles", _styles["Heading2"]))

    if not analyzed_articles:
        story.append(Paragraph("<i>No articles collected this week.</i>", _styles["BodyText"]))
    else:
        table_data = [["Title", "Source", "Category", "Importance", "Summary"]]
        for a in analyzed_articles:
            table_data.append([
                Paragraph(a.get("title", "Untitled"), _cell_style),
                Paragraph(a.get("source", ""), _cell_style),
                Paragraph(a.get("category", "Other"), _cell_style),
                Paragraph(a.get("importance", "Low"), _cell_style),
                Paragraph(a.get("summary", "") or "-", _cell_style),
            ])

        # Fixed column widths so long cell text wraps instead of overflowing
        # the page — this is the crash-proofing the README calls out.
        col_widths = [1.3 * inch, 0.9 * inch, 0.9 * inch, 0.8 * inch, 2.6 * inch]
        table = Table(table_data, colWidths=col_widths, repeatRows=1)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A365D")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTSIZE", (0, 0), (-1, 0), 9),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")]),
        ]))
        story.append(table)

    def _header_footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(0.75 * inch, LETTER[1] - 0.5 * inch, "AI Weekly Research Digest")
        canvas.drawRightString(LETTER[0] - 0.75 * inch, 0.5 * inch, f"Page {doc_.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=_header_footer, onLaterPages=_header_footer)


def generate_digest(analyzed_articles: list, themes: dict) -> str:
    os.makedirs(os.path.dirname(DIGEST_MD_PATH), exist_ok=True)

    with open(DIGEST_MD_PATH, "w", encoding="utf-8") as f:
        f.write(_build_markdown(analyzed_articles, themes))

    try:
        _build_pdf(analyzed_articles, themes, DIGEST_PDF_PATH)
    except Exception as e:
        logger.warning(f"PDF generation failed, Markdown digest was still saved: {e}")
        return DIGEST_MD_PATH

    logger.info(f"Digest written to {DIGEST_MD_PATH} and {DIGEST_PDF_PATH}")
    return DIGEST_PDF_PATH
