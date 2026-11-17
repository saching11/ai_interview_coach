import logging
import os 

from openai import OpenAI

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        logger.info("Initializing OpenAI client")

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("OpenAI API Key not configured")
            raise ValueError("OpenAI API key not configured")

        try:
            self.client = OpenAI(api_key=api_key)
        except Exception as e:
            logger.exception("OpenAI client initialization failed!")
            raise
        logger.info("OpenAI client initialized successfully!")
    
    def validate_connection(self):
        logger.info("Validating OpenAI API credentials")

        try:
            self.client.models.list()
            logger.info("OpenAI API authentication verified")

        except Exception:
            logger.exception("OpenAI API validation failed")
            raise