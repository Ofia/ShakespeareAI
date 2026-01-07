# ShakespeareAI

An AI-powered chat application that responds to prompts in either Shakespearean Old English or Biblical Hebrew.

## Features

- Chat with AI in two distinct historical language styles
- Toggle between Shakespearean English and Biblical Hebrew
- Beautiful vintage parchment-style interface
- Powered by Hugging Face's Qwen 2.5 72B model

## Local Development

### 1. Starting the virtual environment
```bash
source venv/Scripts/activate  # Windows Git Bash
# or
source venv/bin/activate      # Linux/Mac
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root:
```
HUGGINGFACE_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the Django development server
```bash
python manage.py runserver 8001
```

### 6. Running the API test script
```bash
python -m chat.test_api
```

## Deployment to Hugging Face Spaces

### Prerequisites
- GitHub account with your code pushed
- Hugging Face account
- Hugging Face API key

### Step-by-Step Deployment

#### 1. Prepare Your GitHub Repository
Make sure all files are committed and pushed:
```bash
git add .
git commit -m "Prepare for Hugging Face Spaces deployment"
git push origin main
```

**Important**: Ensure `.env` is in your `.gitignore` file (don't push sensitive keys!)

#### 2. Create a New Space on Hugging Face

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in the details:
   - **Space name**: `shakespeareai` (or your preferred name)
   - **License**: Choose appropriate license
   - **Select SDK**: Choose **Docker**
   - **Space hardware**: CPU basic (free tier) or upgrade if needed
4. Click **"Create Space"**

#### 3. Connect Your GitHub Repository

In your new Space:

1. Go to **"Settings"** tab
2. Scroll to **"Repository"** section
3. Click **"Link to GitHub"**
4. Select your repository
5. Choose the branch (usually `main`)

#### 4. Configure Environment Variables (Secrets)

In your Space settings:

1. Go to **"Variables and secrets"** section
2. Add the following secrets:
   - `HUGGINGFACE_API_KEY`: Your Hugging Face API key
   - `SECRET_KEY`: A strong random secret key for Django
   - `DEBUG`: Set to `False`
   - `ALLOWED_HOSTS`: `*` (or your specific Space URL)

To generate a secure SECRET_KEY:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 5. Deploy

Hugging Face will automatically:
- Detect the `Dockerfile`
- Build the Docker image
- Deploy your application
- Assign a URL like: `https://your-username-shakespeareai.hf.space`

#### 6. Monitor Deployment

- Go to the **"Logs"** tab to see build progress
- Wait for the build to complete (usually 2-5 minutes)
- Once deployed, click on the **"App"** tab to see your live application

### Troubleshooting Deployment

If deployment fails:

1. **Check logs**: Go to Logs tab in your Space
2. **Common issues**:
   - Missing environment variables
   - Port configuration (ensure using port 7860)
   - Database migrations failing
   - Static files not collected

3. **Debug locally with Docker**:
   ```bash
   docker build -t shakespeareai .
   docker run -p 7860:7860 --env-file .env shakespeareai
   ```

### Updating Your Deployment

To update your deployed app:
1. Make changes to your code locally
2. Commit and push to GitHub
3. Hugging Face will automatically rebuild and redeploy

Or manually trigger rebuild in Space settings.

## Project Structure

```
ShakespeareAI/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration for HF Spaces
├── .dockerignore                # Files to exclude from Docker build
├── startup.sh                   # Container startup script
├── db.sqlite3                   # SQLite database
├── README.md                    # This file
│
├── chatproject/                 # Django project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI application
│   └── asgi.py                  # ASGI application
│
└── chat/                        # Main Django app
    ├── templates/
    │   └── chat/
    │       └── index.html       # Frontend UI
    ├── huggingface_service.py   # AI service integration
    ├── views.py                 # Request handlers
    ├── urls.py                  # App URL patterns
    └── models.py                # Database models
```

## Technology Stack

- **Backend**: Django 6.0
- **Frontend**: HTML5, JavaScript, CSS
- **AI Model**: Hugging Face Qwen 2.5 72B (via Router API)
- **Deployment**: Docker on Hugging Face Spaces
- **Server**: Gunicorn (production)

## License

[Your License Here]
