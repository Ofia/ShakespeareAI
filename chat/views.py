from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .huggingface_service import HuggingFaceService
from django.shortcuts import render

# Create service instance
hf_service = HuggingFaceService()

def index(request):
    # Renders the main chat page
    return render(request, 'chat/index.html')
    # render() combines template with data to create HTML

@csrf_exempt  # Decorator: Disables CSRF protection for this view
# CSRF = Cross-Site Request Forgery protection
# We disable it for simplicity in learning (enable in production!)

def chat(request):
    """
    Handles chat messages via AJAX.
    Expects POST requests with JSON data.
    """
    if request.method == 'POST':  
        # Check if request is POST (sending data)

        try:
            # Parse JSON from request body
            data = json.loads(request.body)
            # request.body is raw bytes, json.loads converts to Python dict
            
            user_message = data.get('message', '')
            language_mode = data.get('language_mode', 'shakespeare')

            # Validate input
            if not user_message:
                return JsonResponse({
                    'error': 'Message is required'
                }, status=400)  # 400 = Bad Request
            
            # Get AI response
            ai_response = hf_service.get_response(user_message, language_mode)
            
            # Return JSON response
            return JsonResponse({
                     'response': ai_response,
                      'language_mode': language_mode
                })
            # JsonResponse automatically converts dict to JSON

        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON'
            }, status=400)
    
    else:
        # Not a POST request
        return JsonResponse({
            'error': 'Only POST requests allowed'
        }, status=405)  # 405 = Method Not Allowed

