"""
Configuration management for the Technical ATS Resume Expert application.
"""
import os
from dotenv import load_dotenv
import streamlit as st
import logging

# Load environment variables
load_dotenv()

class Config:
    """Application configuration class."""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash"
    
    # Application Configuration
    APP_TITLE = "Technical ATS Resume Expert"
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    SUPPORTED_FORMATS = ["pdf"]
    
    # Visualization Configuration
    CHART_COLORS = ['#4CAF50', '#FF5733']
    EXPLODE_VALUES = (0.1, 0)
    
    @classmethod
    def validate_config(cls):
        """Validate essential configuration."""
        if not cls.GOOGLE_API_KEY:
            st.error("⚠️ Google API Key not found! Please add GOOGLE_API_KEY to your .env file.")
            st.stop()
            return False
        return True
    
    @classmethod
    def setup_logging(cls):
        """Setup application logging."""
        import os
        
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/app.log'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)
