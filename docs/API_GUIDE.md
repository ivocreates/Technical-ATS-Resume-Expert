# API Integration Guide

## Google Gemini API Integration

### Overview
The Technical ATS Resume Expert integrates with Google's Gemini 2.5 Flash API to provide advanced AI-powered resume analysis capabilities.

### API Configuration

#### 1. Obtaining API Key
```bash
# Visit Google AI Studio
https://makersuite.google.com/app/apikey

# Steps:
1. Sign in with Google account
2. Create new API key
3. Copy the generated key
4. Add to environment variables
```

#### 2. Environment Setup
```bash
# .env file
GOOGLE_API_KEY=your_actual_api_key_here
APP_NAME=Technical ATS Resume Expert
DEBUG_MODE=False
LOG_LEVEL=INFO
```

### API Usage Patterns

#### 1. Service Initialization
```python
class GeminiService:
    def __init__(self):
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
```

#### 2. Content Generation
```python
def generate_response(self, job_description, pdf_content, prompt):
    content_parts = [
        job_description,
        {"mime_type": "image/jpeg", "data": pdf_content},
        prompt
    ]
    response = self.model.generate_content(content_parts)
    return response.text
```

### Error Handling

#### Common Error Scenarios
1. **Invalid API Key**
   - Error: `google.api_core.exceptions.Unauthenticated`
   - Solution: Verify API key validity

2. **Rate Limiting**
   - Error: `google.api_core.exceptions.ResourceExhausted`
   - Solution: Implement exponential backoff

3. **Content Blocked**
   - Error: `genai.types.BlockedPromptException`
   - Solution: Modify content or prompt

4. **Network Issues**
   - Error: `requests.exceptions.ConnectionError`
   - Solution: Retry with timeout

### Rate Limits

#### Free Tier Limits
- **Requests per minute**: 60
- **Requests per day**: 1,500
- **Tokens per request**: Up to 1M tokens

#### Best Practices
- Implement request queuing
- Use exponential backoff
- Cache responses when possible
- Monitor usage metrics

### Prompt Engineering

#### 1. Resume Analysis Prompt
```python
RESUME_ANALYSIS_PROMPT = """
You are an experienced Technical HR Manager...
- Analyze alignment with job requirements
- Identify strengths and weaknesses
- Provide overall fit assessment
"""
```

#### 2. Skill Improvement Prompt
```python
SKILL_IMPROVEMENT_PROMPT = """
You are a Technical Career Advisor...
- Identify skill gaps
- Recommend learning paths
- Suggest certifications
"""
```

#### 3. ATS Matching Prompt
```python
ATS_MATCHING_PROMPT = """
You are an advanced ATS scanner...
- Calculate matching percentage
- List missing keywords
- Provide final thoughts
"""
```

### Response Processing

#### 1. Text Extraction
```python
def extract_match_percentage(response_text):
    patterns = [
        r"Match Percentage[:\s]*(\d+)%",
        r"Match[:\s]*(\d+)%",
        r"(\d+)%\s*match"
    ]
    for pattern in patterns:
        match = re.search(pattern, response_text, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return 0
```

#### 2. Content Parsing
```python
def parse_response(response_text):
    sections = {
        'strengths': extract_section(response_text, 'Strengths'),
        'weaknesses': extract_section(response_text, 'Weaknesses'),
        'recommendations': extract_section(response_text, 'Recommendations')
    }
    return sections
```

### Security Considerations

#### 1. API Key Management
- Store in environment variables
- Never commit to version control
- Rotate keys regularly
- Use different keys for dev/prod

#### 2. Data Privacy
- Minimize data sent to API
- No storage of personal information
- Implement data retention policies
- Comply with privacy regulations

### Monitoring and Analytics

#### 1. Request Tracking
```python
def log_api_request(request_type, response_time, success):
    logger.info(f"API Request: {request_type}, "
               f"Time: {response_time}ms, "
               f"Success: {success}")
```

#### 2. Error Monitoring
```python
def track_api_errors(error_type, error_message):
    logger.error(f"API Error: {error_type} - {error_message}")
    # Send to monitoring service
```

### Future Enhancements

#### 1. Response Caching
- Cache common responses
- Implement cache invalidation
- Reduce API calls

#### 2. Batch Processing
- Process multiple resumes
- Optimize API usage
- Improve performance

#### 3. Alternative Models
- Support for different AI models
- Model selection based on use case
- Performance comparison

### Troubleshooting

#### Common Issues and Solutions

1. **Slow Response Times**
   - Check network connectivity
   - Verify API endpoint status
   - Implement timeout handling

2. **Inconsistent Results**
   - Review prompt engineering
   - Test with various inputs
   - Validate response parsing

3. **Authentication Errors**
   - Verify API key format
   - Check key permissions
   - Ensure proper configuration
