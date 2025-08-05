"""
Technical ATS Resume Expert - Optimized Version
A comprehensive resume analysis tool powered by Google Gemini AI.
"""
import streamlit as st
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from src.config import Config
from src.utils import PDFProcessor, TextAnalyzer
from src.ai_service import GeminiService, PromptManager
from src.visualization import ChartGenerator, UIComponents

# Initialize configuration and services
Config.validate_config()
logger = Config.setup_logging()

# Initialize services
gemini_service = GeminiService()
pdf_processor = PDFProcessor()
text_analyzer = TextAnalyzer()
chart_generator = ChartGenerator()
ui = UIComponents()

def main():
    """Main application function."""
    
    # Streamlit page configuration
    st.set_page_config(
        page_title=Config.APP_TITLE,
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS styling
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            color: #1f77b4;
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .feature-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .metric-container {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #007bff;
            margin: 1rem 0;
        }
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.75rem 2rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Application header
    st.markdown('<h1 class="main-header">🚀 Technical ATS Resume Expert</h1>', unsafe_allow_html=True)
    
    # Feature overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h3>📊 Resume Analysis</h3>
                <p>Get detailed insights about your resume's strengths and weaknesses</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-box">
                <h3>🎯 ATS Matching</h3>
                <p>Check how well your resume matches job descriptions</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-box">
                <h3>📈 Skill Enhancement</h3>
                <p>Receive personalized recommendations for skill improvement</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sidebar for application info
    with st.sidebar:
        st.header("📋 Application Info")
        st.info("""
        **Technical ATS Resume Expert** helps you optimize your resume for:
        
        ✅ Applicant Tracking Systems (ATS)  
        ✅ Technical job requirements  
        ✅ Industry-specific skills  
        ✅ Career advancement  
        
        **Powered by Google Gemini AI**
        """)
        
        st.header("🔧 Features")
        st.markdown("""
        - **Smart Resume Analysis**
        - **ATS Compatibility Check**
        - **Skill Gap Identification**
        - **Career Recommendations**
        - **Visual Analytics**
        """)
    
    # Main input section
    st.header("📝 Input Section")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        job_description = st.text_area(
            "Job Description",
            height=200,
            placeholder="Paste the job description here...",
            help="Enter the complete job description to get accurate analysis"
        )
    
    with col2:
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"],
            help="Upload your resume in PDF format (max 10MB)"
        )
        
        if uploaded_file:
            ui.display_success_message(f"File uploaded: {uploaded_file.name}")
            st.info(f"📄 File size: {uploaded_file.size / 1024:.1f} KB")
    
    # Action buttons
    st.header("🚀 Analysis Actions")
    
    button_col1, button_col2, button_col3 = st.columns(3)
    
    with button_col1:
        analyze_resume = st.button("📊 Analyze Resume")
    
    with button_col2:
        improve_skills = st.button("📈 Improve Skills")
    
    with button_col3:
        match_resume = st.button("🎯 Match with Job")
    
    # Process user actions
    if analyze_resume:
        handle_resume_analysis(job_description, uploaded_file)
    
    elif improve_skills:
        handle_skill_improvement(job_description, uploaded_file)
    
    elif match_resume:
        handle_resume_matching(job_description, uploaded_file)

def handle_resume_analysis(job_description: str, uploaded_file):
    """Handle resume analysis workflow."""
    
    if not validate_inputs(job_description, uploaded_file):
        return
    
    # Process PDF
    pdf_image, pdf_base64 = pdf_processor.process_pdf(uploaded_file)
    if not pdf_image or not pdf_base64:
        return
    
    # Get AI response
    response = gemini_service.generate_response(
        job_description, 
        pdf_base64, 
        PromptManager.get_prompt('analysis')
    )
    
    if response:
        st.header("📊 Resume Analysis Results")
        
        # Display resume image
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(pdf_image, caption="📄 Resume Preview", width=400)
        
        with col2:
            st.markdown("### 🔍 Detailed Analysis")
            st.markdown(response)
        
        # Download option
        ui.create_download_button(
            response, 
            "resume_analysis.txt", 
            "📥 Download Analysis Report"
        )

def handle_skill_improvement(job_description: str, uploaded_file):
    """Handle skill improvement workflow."""
    
    if not validate_inputs(job_description, uploaded_file):
        return
    
    # Process PDF
    pdf_image, pdf_base64 = pdf_processor.process_pdf(uploaded_file)
    if not pdf_image or not pdf_base64:
        return
    
    # Get AI response
    response = gemini_service.generate_response(
        job_description, 
        pdf_base64, 
        PromptManager.get_prompt('improvement')
    )
    
    if response:
        st.header("📈 Skill Improvement Suggestions")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(pdf_image, caption="📄 Resume Preview", width=400)
        
        with col2:
            st.markdown("### 🎯 Personalized Recommendations")
            st.markdown(response)
        
        # Download option
        ui.create_download_button(
            response, 
            "skill_improvement_plan.txt", 
            "📥 Download Improvement Plan"
        )

def handle_resume_matching(job_description: str, uploaded_file):
    """Handle resume matching workflow."""
    
    if not validate_inputs(job_description, uploaded_file):
        return
    
    # Process PDF
    pdf_image, pdf_base64 = pdf_processor.process_pdf(uploaded_file)
    if not pdf_image or not pdf_base64:
        return
    
    # Get AI response
    response = gemini_service.generate_response(
        job_description, 
        pdf_base64, 
        PromptManager.get_prompt('matching')
    )
    
    if response:
        # Extract match percentage
        match_percentage = text_analyzer.extract_match_percentage(response)
        
        st.header("🎯 Resume Matching Results")
        
        # Display key metrics
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        ui.display_metrics(metric_col1, metric_col2, metric_col3, match_percentage, 100, 100 - match_percentage)
        
        # Main content layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(pdf_image, caption="📄 Resume Preview", width=400)
        
        with col2:
            st.subheader("📊 Match Percentage Visualization")
            pie_chart = chart_generator.create_match_pie_chart(match_percentage)
            if pie_chart:
                st.pyplot(pie_chart)
                plt.close(pie_chart)  # Properly close the figure
        
        # Detailed analysis
        st.markdown("### 📋 Detailed Matching Analysis")
        st.markdown(response)
        
        # Download options
        col1, col2 = st.columns(2)
        with col1:
            ui.create_download_button(
                response, 
                "matching_analysis.txt", 
                "📥 Download Match Report"
            )
        
        with col2:
            if pie_chart:
                # Save chart as image for download (optional feature)
                st.info("💡 Chart visualization displayed above")

def validate_inputs(job_description: str, uploaded_file) -> bool:
    """Validate user inputs."""
    
    if not text_analyzer.validate_job_description(job_description):
        return False
    
    if not uploaded_file:
        ui.display_error_message("Please upload your resume (PDF format)")
        return False
    
    return True

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"❌ Application Error: {str(e)}")
        st.info("Please refresh the page and try again.")
        logger.error(f"Application error: {str(e)}")
