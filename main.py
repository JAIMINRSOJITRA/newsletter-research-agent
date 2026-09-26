import sys
from config.settings import GEMINI_API_KEY
from src.agents.research_agent import ResearchAgent
from src.utils.logger import setup_logger

def main():
    logger = setup_logger()
    
    # 1. API key sanity check
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        logger.critical("Error: GEMINI_API_KEY is not defined in the environment or .env file.")
        logger.info("Please set a valid API key from Google AI Studio in the .env file before running.")
        sys.exit(1)

    # 2. Run Pipeline orchestrator
    try:
        agent = ResearchAgent()
        result = agent.run()
        
        # 3. Print execution overview
        print("\n" + "=" * 40)
        print(" pipeline execution overview".upper())
        print("=" * 40)
        print(f"Status:             {'SUCCESS' if result['success'] else 'FAILED'}")
        print(f"Articles Collected: {result['total_articles']}")
        print(f"Articles Cleaned:   {result['unique_articles']}")
        print(f"Articles Analyzed:  {result['analyzed_articles']}")
        if result['digest_path']:
            print(f"Digest PDF:         {result['digest_path']}")
        
        if result['errors']:
            print("\nWarnings/Non-critical Errors:")
            for err in result['errors']:
                print(f"- {err}")
        print("=" * 40 + "\n")
        
        if not result['success']:
            sys.exit(2)
            
    except Exception as e:
        logger.critical(f"Unhandled pipeline orchestration exception: {e}", exc_info=True)
        sys.exit(3)

if __name__ == "__main__":
    main()
