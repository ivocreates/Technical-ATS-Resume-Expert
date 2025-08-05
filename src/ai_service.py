"""
AI service integration for the Technical ATS Resume Expert application.
"""
import logging
import streamlit as st
import google.generativeai as genai
from typing import Optional, Dict, Any
from src.config import Config

logger = logging.getLogger(__name__)

class GeminiService:
    """Handles Google Gemini AI API interactions."""
    
    def __init__(self):
        """Initialize Gemini service with API configuration."""
        try:
            genai.configure(api_key=Config.GOOGLE_API_KEY)
            self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
            logger.info("Gemini service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini service: {str(e)}")
            st.error("⚠️ Failed to initialize AI service. Please check your API key.")
            st.stop()
    
    def generate_response(self, job_description: str, pdf_content: str, prompt: str) -> Optional[str]:
        """
        Generate AI response for resume analysis.
        
        Args:
            job_description: Job description text
            pdf_content: Base64 encoded PDF content
            prompt: Analysis prompt
            
        Returns:
            Optional[str]: AI response text or None if error
        """
        try:
            # Prepare content for API
            content_parts = [
                job_description,
                {
                    "mime_type": "image/jpeg",
                    "data": pdf_content
                },
                prompt
            ]
            
            # Generate response with error handling
            with st.spinner("🤖 Analyzing your resume with AI..."):
                response = self.model.generate_content(content_parts)
                
                if response and response.text:
                    logger.info("Successfully generated AI response")
                    return response.text
                else:
                    logger.warning("Empty response from AI service")
                    st.warning("⚠️ Received empty response from AI service. Please try again.")
                    return None
                    
        except genai.types.BlockedPromptException:
            error_msg = "⚠️ Content was blocked by AI safety filters. Please try with different content."
            st.error(error_msg)
            logger.error("Content blocked by AI safety filters")
            return None
            
        except genai.types.StopCandidateException:
            error_msg = "⚠️ AI response was stopped due to safety concerns. Please try again."
            st.error(error_msg)
            logger.error("AI response stopped due to safety concerns")
            return None
            
        except Exception as e:
            error_msg = f"⚠️ Error communicating with AI service: {str(e)}"
            st.error(error_msg)
            logger.error(f"Error in AI service: {str(e)}")
            return None

class PromptManager:
    """Manages AI prompts for different analysis types."""
    
    RESUME_ANALYSIS_PROMPT = """
    You are an experienced Technical HR Manager with expertise in talent acquisition and recruitment for technology, finance, and business roles. Your task is to conduct a detailed evaluation of the provided resume against the job description.

    **Analysis Structure:**
    
    🎯 **Alignment with Job Requirements**: Analyze the resume to identify key skills, qualifications, and experiences that match the job requirements. Highlight areas where the candidate excels in fulfilling the role's technical, financial, or business-related expectations.

    💪 **Strengths**: Enumerate the candidate's core strengths, including technical skills, domain knowledge, certifications, achievements, or relevant experiences that align closely with the job description.

    ⚠️ **Weaknesses**: Point out any notable gaps or areas where the candidate's profile does not meet the job requirements, such as missing skills, insufficient experience, or lack of relevant certifications.

    📊 **Overall Fit**: Provide a professional assessment of how well the candidate fits the role, considering both strengths and weaknesses. Offer an overall recommendation (e.g., highly suitable, moderately suitable, not suitable) and explain your reasoning.

    Ensure your evaluation is specific, clear, and actionable, taking into account the nuances of the job role and industry requirements.
    """

    SKILL_IMPROVEMENT_PROMPT = """
    You are a highly experienced Technical Career Advisor with deep expertise in the fields of Data Science, Web Development, Big Data Engineering, DevOps, and other technical domains. Your task is to provide detailed, actionable, and personalized guidance to help the individual improve their skills and advance their career based on the provided resume and job description.

    **Guidance Structure:**

    🔍 **Skill Gap Analysis**: Identify the specific skills, technologies, tools, or certifications that are missing from the candidate's resume but are crucial for excelling in the specified job role.

    📚 **Recommended Learning Path**: Suggest practical steps the candidate can take to acquire the missing skills, such as:
    - Online courses or certifications (e.g., Coursera, Udemy, or official vendor certifications like AWS, Azure, or Google Cloud)
    - Projects or hands-on experiences that can help them gain expertise
    - Open-source contributions or internships for real-world exposure

    🚀 **Emerging Trends and Technologies**: Highlight any emerging trends, tools, or frameworks in the industry that the candidate should explore to stay competitive and future-proof their career.

    🤝 **Improvement in Soft Skills**: If applicable, suggest areas where the candidate can improve soft skills (e.g., communication, teamwork, or leadership) that are essential for success in their chosen domain.

    ⭐ **Overall Guidance**: Provide a summary of the top three actionable steps the candidate should prioritize to achieve significant improvement in their profile.

    Ensure that your response is specific to the candidate's field and the role described in the job description. Provide clear, concise, and actionable advice that the candidate can immediately apply to improve their skills and career prospects.
    """

    ATS_MATCHING_PROMPT = """
    You are a skilled and advanced ATS (Applicant Tracking System) scanner, designed with deep functionality and specialized expertise in roles such as Data Science, Web Development, Big Data Engineering, and DevOps. Your task is to evaluate the provided resume against the job description thoroughly.

    **Output Structure (MUST follow this exact format):**

    **Match Percentage**: XX%

    **Missing Keywords**: 
    - [List missing skills/tools/keywords with bullet points]
    - [Each item on a new line]

    **Final Thoughts**: 
    [Provide a brief, insightful summary of your evaluation, including the candidate's overall suitability for the role, highlighting both key strengths and gaps]

    **Important**: 
    - Provide a precise percentage score (0-100) indicating how well the candidate's profile aligns with the job description
    - List ALL critical skills, technologies, tools, certifications, or keywords mentioned in the job description that are absent from the resume
    - Keep your final thoughts concise but comprehensive
    """
    
    @classmethod
    def get_prompt(cls, prompt_type: str) -> str:
        """
        Get prompt by type.
        
        Args:
            prompt_type: Type of prompt ('analysis', 'improvement', 'matching')
            
        Returns:
            str: Prompt text
        """
        prompts = {
            'analysis': cls.RESUME_ANALYSIS_PROMPT,
            'improvement': cls.SKILL_IMPROVEMENT_PROMPT,
            'matching': cls.ATS_MATCHING_PROMPT
        }
        
        return prompts.get(prompt_type, cls.RESUME_ANALYSIS_PROMPT)
