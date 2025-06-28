import streamlit as st
import base64
import os
import io
import re
import fitz  # PyMuPDF
import matplotlib.pyplot as plt
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Functions
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded PDF file
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf_doc:
            # Get the first page as an image
            first_page = pdf_doc[0].get_pixmap()
            img_byte_arr = io.BytesIO(first_page.tobytes("jpeg"))
            return Image.open(img_byte_arr), base64.b64encode(img_byte_arr.getvalue()).decode()
    else:
        raise FileNotFoundError("No file uploaded")

def extract_match_percentage(response_text):
    match = re.search(r"Match Percentage:\s*(\d+)%", response_text)
    if match:
        return int(match.group(1))
    else:
        return 0

def draw_pie_chart(match_percentage):
    fig, ax = plt.subplots()
    labels = ['Match', 'Remaining']
    sizes = [match_percentage, 100 - match_percentage]
    colors = ['#4CAF50', '#FF5733']
    explode = (0.1, 0)
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    return fig

# Streamlit Configuration
st.set_page_config(page_title="Technical ATS Resume Expert")

# Page Styling
st.markdown(
    """
    <style>
    body {
        background-image: url('gradient-blur.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 2.5em;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: black;'>Technical Resume Expert</h1>", unsafe_allow_html=True)

# Inputs
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully!")

# Buttons
submit1 = st.button("Analyse Resume")
submit2 = st.button("How Can I Improvise my Skills?")
submit3 = st.button("Match Resume with Job Description")

# Prompts
input_prompt1 = """
You are an experienced Technical HR Manager with expertise in talent acquisition and recruitment for technology, finance, and business roles. Your task is to conduct a detailed evaluation of the provided resume against the job description.

Alignment with Job Requirements: Analyze the resume to identify key skills, qualifications, and experiences that match the job requirements. Highlight areas where the candidate excels in fulfilling the role's technical, financial, or business-related expectations.

Strengths: Enumerate the candidate's core strengths, including technical skills, domain knowledge, certifications, achievements, or relevant experiences that align closely with the job description.

Weaknesses: Point out any notable gaps or areas where the candidate's profile does not meet the job requirements, such as missing skills, insufficient experience, or lack of relevant certifications.

Overall Fit: Provide a professional assessment of how well the candidate fits the role, considering both strengths and weaknesses. Offer an overall recommendation (e.g., highly suitable, moderately suitable, not suitable) and explain your reasoning.

Ensure your evaluation is specific, clear, and actionable, taking into account the nuances of the job role and industry requirements.
"""

input_prompt2 = """
You are a highly experienced Technical Career Advisor with deep expertise in the fields of Data Science, Web Development, Big Data Engineering, DevOps, and other technical domains. Your task is to provide detailed, actionable, and personalized guidance to help the individual improve their skills and advance their career based on the provided resume and job description.

1. **Skill Gap Analysis**: Identify the specific skills, technologies, tools, or certifications that are missing from the candidate's resume but are crucial for excelling in the specified job role.

2. **Recommended Learning Path**: Suggest practical steps the candidate can take to acquire the missing skills, such as:
   - Online courses or certifications (e.g., Coursera, Udemy, or official vendor certifications like AWS, Azure, or Google Cloud).
   - Projects or hands-on experiences that can help them gain expertise.
   - Open-source contributions or internships for real-world exposure.

3. **Emerging Trends and Technologies**: Highlight any emerging trends, tools, or frameworks in the industry that the candidate should explore to stay competitive and future-proof their career.

4. **Improvement in Soft Skills**: If applicable, suggest areas where the candidate can improve soft skills (e.g., communication, teamwork, or leadership) that are essential for success in their chosen domain.

5. **Overall Guidance**: Provide a summary of the top three actionable steps the candidate should prioritize to achieve significant improvement in their profile.

Ensure that your response is specific to the candidate's field and the role described in the job description. Provide clear, concise, and actionable advice that the candidate can immediately apply to improve their skills and career prospects.
"""

input_prompt3 = """
You are a skilled and advanced ATS (Applicant Tracking System) scanner, designed with deep functionality and specialized expertise in roles such as Data Science, Web Development, Big Data Engineering, and DevOps. Your task is to evaluate the provided resume against the job description thoroughly.

Matching Percentage: Analyze the resume and provide a precise percentage score indicating how well the candidate's profile aligns with the job description.

Missing Keywords: Identify and list any critical skills, technologies, tools, certifications, or keywords mentioned in the job description that are absent from the resume.

Final Thoughts: Provide a brief, insightful summary of your evaluation, including the candidate's overall suitability for the role, highlighting both key strengths and gaps.

Output Structure:

Match Percentage(bold): XX%
Missing Keywords(bold): 
[List missing skills/tools/keywords]
Final Thoughts(bold): 
[Provide a short summary of strengths and weaknesses and a recommendation if possible.]
"""

# Actions
if submit1:
    if uploaded_file is not None:
        pdf_image, pdf_base64 = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, [{"mime_type": "image/jpeg", "data": pdf_base64}], input_prompt1)
        st.subheader("Analysis")
        st.write(response)
    else:
        st.write("Please upload your resume!")

elif submit2:
    if uploaded_file is not None:
        pdf_image, pdf_base64 = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, [{"mime_type": "image/jpeg", "data": pdf_base64}], input_prompt2)
        st.subheader("Improvement Suggestions")
        st.write(response)
    else:
        st.write("Please upload your resume!")

elif submit3:
    if uploaded_file is not None:
        pdf_image, pdf_base64 = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, [{"mime_type": "image/jpeg", "data": pdf_base64}], input_prompt3)
        match_percentage = extract_match_percentage(response)
        col1, col2 = st.columns(2)
        with col1:
            st.image(pdf_image, caption="Resume First Page", use_container_width=True)
        with col2:
            st.subheader("Match Percentage")
            pie_chart = draw_pie_chart(match_percentage)
            st.pyplot(pie_chart)
        st.subheader("Detailed Analysis")
        st.write(response)
    else:
        st.write("Please upload your resume!")
