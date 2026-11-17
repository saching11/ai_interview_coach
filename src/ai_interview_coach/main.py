import logging

from dotenv import load_dotenv
from ai_interview_coach.openai_service import OpenAIService
from pathlib import Path 

def main() -> None:
    # Configuring logging service
    project_root = Path(__file__).resolve().parents[2]
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                log_dir / "app.log",
                encoding="utf-8",
            ),
        ],
    )

    logger = logging.getLogger(__name__)
    logger.info("Starting AI Interview Coach")

    load_dotenv()

    try:
        openai_service = OpenAIService()

        openai_service.validate_connection()
        logger.info("Application setup Completed!")
    except Exception:
        logger.exception("Application startup Failed")
        raise


if __name__ == "__main__":
    main()
