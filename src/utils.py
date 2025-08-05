"""
Utility functions for the Technical ATS Resume Expert application.
"""
import re
import io
import base64
import logging
from typing import Tuple, Optional
import fitz  # PyMuPDF
from PIL import Image
import streamlit as st

logger = logging.getLogger(__name__)

class PDFProcessor:
    """Handles PDF file processing operations."""
    
    @staticmethod
    def validate_pdf_file(uploaded_file) -> bool:
        """
        Validate uploaded PDF file.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            bool: True if valid, False otherwise
        """
        if uploaded_file is None:
            return False
            
        if uploaded_file.size == 0:
            st.error("⚠️ The uploaded file is empty.")
            return False
            
        if uploaded_file.size > 10 * 1024 * 1024:  # 10MB limit
            st.error("⚠️ File size exceeds 10MB limit.")
            return False
            
        if not uploaded_file.name.lower().endswith('.pdf'):
            st.error("⚠️ Please upload a PDF file.")
            return False
            
        return True
    
    @staticmethod
    def process_pdf(uploaded_file) -> Tuple[Optional[Image.Image], Optional[str]]:
        """
        Process uploaded PDF file and convert first page to image.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            Tuple[Image, str]: PIL Image and base64 encoded string, or (None, None) if error
        """
        try:
            if not PDFProcessor.validate_pdf_file(uploaded_file):
                return None, None
                
            # Read the uploaded PDF file
            pdf_bytes = uploaded_file.read()
            
            with fitz.open(stream=pdf_bytes, filetype="pdf") as pdf_doc:
                if len(pdf_doc) == 0:
                    st.error("⚠️ The PDF file appears to be empty or corrupted.")
                    return None, None
                    
                # Get the first page as an image
                first_page = pdf_doc[0]
                pixmap = first_page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Higher resolution
                img_byte_arr = io.BytesIO(pixmap.tobytes("jpeg"))
                
                # Create PIL Image
                pil_image = Image.open(img_byte_arr)
                
                # Encode to base64
                img_byte_arr.seek(0)
                base64_encoded = base64.b64encode(img_byte_arr.getvalue()).decode()
                
                logger.info(f"Successfully processed PDF: {uploaded_file.name}")
                return pil_image, base64_encoded
                
        except fitz.FileDataError:
            st.error("⚠️ Invalid PDF file. Please upload a valid PDF.")
            logger.error(f"Invalid PDF file: {uploaded_file.name}")
            return None, None
        except Exception as e:
            st.error(f"⚠️ Error processing PDF: {str(e)}")
            logger.error(f"Error processing PDF {uploaded_file.name}: {str(e)}")
            return None, None

class TextAnalyzer:
    """Handles text analysis operations."""
    
    @staticmethod
    def extract_match_percentage(response_text: str) -> int:
        """
        Extract match percentage from Gemini API response.
        
        Args:
            response_text: Response text from Gemini API
            
        Returns:
            int: Match percentage (0-100)
        """
        try:
            # Try multiple patterns to extract percentage
            patterns = [
                r"Match Percentage[:\s]*(\d+)%",
                r"Match[:\s]*(\d+)%",
                r"Percentage[:\s]*(\d+)%",
                r"(\d+)%\s*match",
                r"Score[:\s]*(\d+)%"
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response_text, re.IGNORECASE)
                if match:
                    percentage = int(match.group(1))
                    # Validate percentage range
                    if 0 <= percentage <= 100:
                        return percentage
                        
            logger.warning("Could not extract match percentage from response")
            return 0
            
        except (ValueError, AttributeError) as e:
            logger.error(f"Error extracting match percentage: {str(e)}")
            return 0
    
    @staticmethod
    def validate_job_description(job_description: str) -> bool:
        """
        Validate job description input.
        
        Args:
            job_description: Job description text
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not job_description or not job_description.strip():
            st.error("⚠️ Please enter a job description.")
            return False
            
        if len(job_description.strip()) < 50:
            st.warning("⚠️ Job description seems too short. Please provide more details.")
            return False
            
        if len(job_description) > 10000:
            st.error("⚠️ Job description is too long. Please keep it under 10,000 characters.")
            return False
            
        return True
