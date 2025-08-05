# Deployment Guide

## Overview
This guide covers various deployment options for the Technical ATS Resume Expert application.

## Deployment Options

### 1. Streamlit Cloud (Recommended)

#### Prerequisites
- GitHub repository with the code
- Google Gemini API key
- Streamlit Cloud account

#### Steps
1. **Connect Repository**
   ```bash
   # Push code to GitHub
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push origin main
   ```

2. **Configure Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub account
   - Select repository: `Technical-ATS-Resume-Expert`
   - Set main file path: `app.py`

3. **Set Environment Variables**
   ```bash
   # In Streamlit Cloud dashboard
   GOOGLE_API_KEY = your_actual_api_key_here
   ```

4. **Deploy**
   - Click "Deploy!"
   - Monitor deployment logs
   - Access via provided URL

#### Advantages
- Free hosting for public repositories
- Automatic deployments on code changes
- Built-in monitoring and logs
- Easy environment variable management

### 2. Local Development

#### Prerequisites
- Python 3.8+
- Virtual environment
- Google Gemini API key

#### Setup
```bash
# Clone repository
git clone https://github.com/ivocreates/Technical-ATS-Resume-Expert.git
cd Technical-ATS-Resume-Expert

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API key

# Run application
streamlit run app.py
```

#### Development Commands
```bash
# Run with custom port
streamlit run app.py --server.port 8502

# Run with debug mode
streamlit run app.py --logger.level debug

# Run with specific browser
streamlit run app.py --browser.gatherUsageStats false
```

### 3. Docker Deployment

#### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Docker Commands
```bash
# Build image
docker build -t ats-resume-expert .

# Run container
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY=your_api_key_here \
  ats-resume-expert

# Run with volume mounting (development)
docker run -p 8501:8501 \
  -v $(pwd):/app \
  -e GOOGLE_API_KEY=your_api_key_here \
  ats-resume-expert
```

#### Docker Compose
```yaml
version: '3.8'

services:
  ats-resume-expert:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

### 4. Heroku Deployment

#### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository

#### Setup Files

##### Procfile
```
web: sh setup.sh && streamlit run app.py
```

##### setup.sh
```bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

#### Deployment Commands
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set GOOGLE_API_KEY=your_api_key_here

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Open app
heroku open
```

### 5. AWS EC2 Deployment

#### Instance Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.9
sudo apt install python3.9 python3.9-venv python3.9-dev -y

# Install Git
sudo apt install git -y

# Clone repository
git clone https://github.com/ivocreates/Technical-ATS-Resume-Expert.git
cd Technical-ATS-Resume-Expert

# Setup virtual environment
python3.9 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Add your API key
```

#### Service Configuration
```bash
# Create systemd service
sudo nano /etc/systemd/system/ats-resume-expert.service
```

```ini
[Unit]
Description=ATS Resume Expert
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/Technical-ATS-Resume-Expert
Environment=PATH=/home/ubuntu/Technical-ATS-Resume-Expert/.venv/bin
ExecStart=/home/ubuntu/Technical-ATS-Resume-Expert/.venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable ats-resume-expert
sudo systemctl start ats-resume-expert
sudo systemctl status ats-resume-expert
```

#### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 6. Google Cloud Run

#### Dockerfile (Cloud Run optimized)
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE $PORT

CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

#### Deployment Commands
```bash
# Build and deploy
gcloud run deploy ats-resume-expert \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_api_key_here
```

## Environment Variables

### Required Variables
```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```

### Optional Variables
```bash
APP_NAME=Technical ATS Resume Expert
DEBUG_MODE=False
LOG_LEVEL=INFO
MAX_FILE_SIZE_MB=10
SUPPORTED_FILE_TYPES=pdf
```

## Security Considerations

### Production Checklist
- [ ] API keys stored securely
- [ ] HTTPS enabled
- [ ] Rate limiting implemented
- [ ] Input validation active
- [ ] Error messages sanitized
- [ ] Logging configured properly
- [ ] File upload restrictions set
- [ ] Regular security updates

### Best Practices
1. **Never expose API keys** in client-side code
2. **Use HTTPS** for all production deployments
3. **Implement rate limiting** to prevent abuse
4. **Monitor logs** for suspicious activity
5. **Regular updates** of dependencies
6. **Backup strategies** for data and configurations

## Monitoring and Maintenance

### Health Checks
```python
# Add to app.py for health monitoring
@st.cache_data
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
```

### Log Monitoring
```bash
# Monitor application logs
tail -f logs/app.log

# Monitor system resources
htop
df -h
free -m
```

### Performance Monitoring
- Response times
- Memory usage
- API call frequency
- Error rates
- User engagement metrics

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port
   lsof -i :8501
   # Kill process
   kill -9 <PID>
   ```

2. **Environment Variables Not Loading**
   ```bash
   # Check .env file exists
   ls -la .env
   # Verify content
   cat .env
   ```

3. **API Connection Issues**
   ```bash
   # Test API connectivity
   curl -H "Authorization: Bearer $GOOGLE_API_KEY" \
     https://generativelanguage.googleapis.com/v1/models
   ```

4. **Memory Issues**
   ```bash
   # Monitor memory usage
   free -m
   # Clear cache
   echo 3 > /proc/sys/vm/drop_caches
   ```

### Deployment Verification

After deployment, verify:
- [ ] Application loads without errors
- [ ] File upload works correctly
- [ ] AI analysis functions properly
- [ ] Visualizations display correctly
- [ ] Download features work
- [ ] Error handling is active
- [ ] Logs are being generated
