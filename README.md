# 🚀 Technical ATS Resume Expert

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red)
![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%202.5%20Flash-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

**An intelligent resume analysis tool powered by Google Gemini AI that optimizes resumes for ATS compatibility and provides actionable career insights.**

[🚀 Quick Start](#quick-start) • [📖 Documentation](#documentation) • [🛠️ Features](#features) • [📊 Diagrams](#system-diagrams)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [API Configuration](#api-configuration)
- [Project Structure](#project-structure)
- [System Diagrams](#system-diagrams)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Technical ATS Resume Expert** is a comprehensive resume analysis platform that leverages advanced AI capabilities to help job seekers optimize their resumes for modern Applicant Tracking Systems (ATS). Built with Google Gemini AI, it provides detailed insights, skill gap analysis, and actionable recommendations for career advancement.

### 🌟 Why Choose This Tool?

- **AI-Powered Analysis**: Uses Google's state-of-the-art Gemini 2.5 Flash model
- **ATS Optimization**: Ensures resume compatibility with modern ATS systems
- **Visual Analytics**: Interactive charts and visualizations
- **Comprehensive Reports**: Detailed analysis with downloadable reports
- **User-Friendly Interface**: Intuitive Streamlit-based web application
- **Production Ready**: Robust error handling and logging

---

## 🛠️ Key Features

### 1. 📊 Resume Analysis
- **Comprehensive Evaluation**: Detailed analysis of resume strengths and weaknesses
- **Industry-Specific Insights**: Tailored feedback for different technical domains
- **Professional Assessment**: HR manager perspective evaluation
- **Actionable Recommendations**: Specific improvement suggestions

### 2. 🎯 ATS Matching
- **Percentage Score**: Precise matching percentage with job descriptions
- **Keyword Analysis**: Identification of missing critical keywords
- **Visual Representation**: Interactive pie charts and metrics
- **Gap Identification**: Clear visualization of skill gaps

### 3. 📈 Skill Enhancement
- **Personalized Learning Path**: Customized skill development recommendations
- **Technology Trends**: Insights into emerging industry technologies
- **Certification Guidance**: Relevant certification suggestions
- **Career Roadmap**: Strategic career advancement planning

### 4. 🔧 Technical Features
- **Multi-format Support**: PDF resume processing with image conversion
- **Error Handling**: Comprehensive error management and user feedback
- **Logging System**: Detailed application logging for monitoring
- **Security**: Secure API key management and validation
- **Performance**: Optimized PDF processing and AI interactions

---

## 💻 Technology Stack

### Core Technologies
- **Frontend**: Streamlit 1.29.0 (Python web framework)
- **AI Engine**: Google Gemini 2.5 Flash API
- **PDF Processing**: PyMuPDF (fitz) for document handling
- **Visualization**: Matplotlib for charts and graphs
- **Image Processing**: Pillow (PIL) for image manipulation

### Development & Production
- **Language**: Python 3.8+
- **Configuration**: python-dotenv for environment management
- **Logging**: Built-in Python logging with custom configuration
- **Error Handling**: Comprehensive exception management
- **Code Organization**: Modular architecture with separation of concerns

### External APIs
- **Google Gemini API**: Advanced AI language model for resume analysis
- **Streamlit Cloud**: Deployment platform (optional)

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- 10MB+ available disk space

### Step 1: Clone the Repository
```bash
git clone https://github.com/ivocreates/Technical-ATS-Resume-Expert.git
cd Technical-ATS-Resume-Expert
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your Google Gemini API key
GOOGLE_API_KEY=your_actual_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

---

## 📚 Usage Guide

### 1. Getting Started
1. **Launch Application**: Run `streamlit run app.py`
2. **Access Interface**: Open browser to `http://localhost:8501`
3. **Upload Resume**: Use the file uploader for PDF resumes (max 10MB)
4. **Enter Job Description**: Paste the target job description
5. **Choose Analysis Type**: Select from three analysis options

### 2. Analysis Types

#### 📊 Resume Analysis
- Provides comprehensive resume evaluation
- Identifies strengths and weaknesses
- Offers professional HR perspective
- Generates downloadable reports

#### 🎯 ATS Matching
- Calculates precise matching percentage
- Creates visual pie charts
- Lists missing keywords
- Provides gap analysis

#### 📈 Skill Improvement
- Suggests personalized learning paths
- Recommends relevant certifications
- Highlights emerging technologies
- Offers career advancement strategies

---

## 🔐 API Configuration

### Google Gemini API Setup

1. **Get API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - Copy the generated key

2. **Configure Environment**:
   ```bash
   # .env file
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

---

## 📁 Project Structure

```
Technical-ATS-Resume-Expert/
│
├── 📄 app.py                    # Main Streamlit application
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                # Project documentation
├── 📄 LICENSE                  # MIT license
├── 📄 .env.example             # Environment variables template
├── 📄 .gitignore               # Git ignore rules
│
├── 📁 src/                     # Source code modules
│   ├── 📄 __init__.py          # Package initialization
│   ├── 📄 config.py            # Configuration management
│   ├── 📄 utils.py             # Utility functions
│   ├── 📄 ai_service.py        # AI service integration
│   └── 📄 visualization.py     # Charts and UI components
│
├── 📁 logs/                    # Application logs
│   └── 📄 app.log              # Main application log
│
├── 📁 .devcontainer/           # Development container
│   └── 📄 devcontainer.json    # Container configuration
│
└── 📁 assets/                  # Static assets
    └── 📄 gradient-blur.png     # Background image
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google AI Team** - For providing the powerful Gemini API
- **Streamlit Team** - For the excellent web framework
- **PyMuPDF Team** - For robust PDF processing capabilities
- **Open Source Community** - For the foundational libraries and tools

---

<div align="center">


</div>l Resume Expert - Powered by Gemini-2.5-Flash
A sleek and intelligent resume analyzer built with Gemini-2.5-Flash, designed with full compatibility for modern **ATS (Applicant Tracking Systems)** and **Content Management Systems (CMS)**. This project not only ensures aesthetic excellence but also focuses on boosting your resume’s impact through the following features:

**Resume Matcher**: Intelligently compares resumes with job descriptions to highlight alignment and identify gaps.

**Skill Enhancer**: Suggests key industry-specific skills to improve your resume’s visibility and relevance.

**Insightful Resume Analysis**: Delivers actionable feedback to optimize structure, keywords, and overall presentation.

Ideal for job seekers aiming to stand out in competitive tech domains.
