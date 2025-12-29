import requests
from djanjo.conf import settings

class HuggingFaceService:
    def __init__(self):
       # Constructor - runs when you create an instance
       self.api_key = settings.HUGGINGFACE_API_KEY
       self.api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
       # This is the model endpoint

       self.headers = {
              "Authorization": f"Bearer {self.api_key}"
           # Bearer token authentication
           "Content-Type": "application/json"
         }

def get_responese(self, user_message, language_mode):
    # System prompts - instructions for the AI
    if language_mode == "Shakespearean":
        system_prompt = "You are an AI assistant that responds only in Shakespearean language."

    # Payload - data we send to the API
    payload = {
        "inputs": f"{system_prompt}\n\nUser: {user_message}\nAssistant:",
            "parameters": {
                "max_new_tokens": 200,  # Max length of response
                "temperature": 0.7,      # Creativity (0=deterministic, 1=creative)
                "top_p": 0.9,           # Nucleus sampling for diversity
                "return_full_text": False  # Only return new generation
            }
        }
    try:
        # Make POST request to API
        response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30  # Wait max 30 seconds
            )
        # Raise exception if request failed (4xx or 5xx status)
        response.raise_for_status()
            
        # Parse JSON response
        result = response.json()

        # Extract generated text from response structure
        if isinstance(result, list) and len(result) > 0:
            return result[0].get('generated_text', 'No response generated')
        else:
            return "Unexpected response format"
        
    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, etc.
        return f"Error communicating with AI: {str(e)}"
    
    
    