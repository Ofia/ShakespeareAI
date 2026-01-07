import requests
from django.conf import settings

class HuggingFaceService:
    def __init__(self):
        self.api_key = settings.HUGGINGFACE_API_KEY
        # CORRECT router endpoint format!
        self.api_url = "https://router.huggingface.co/v1/chat/completions"
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Using Qwen 2.5 - excellent at following instructions
        self.model = "Qwen/Qwen2.5-72B-Instruct"
    
    def get_response(self, user_message, language_mode):
        if language_mode == 'shakespeare':
            system_prompt = "You are an AI assistant that speaks ONLY in Shakespearean English. Use 'thee', 'thou', 'thy', archaic verb forms like 'art', 'doth', 'hath', and poetic language. Never break character."
        
        else:
            system_prompt = """אתה עוזר AI שחייב לענות רק בעברית מקראית.
    
                            חוקים:
                            - כתוב הכל באותיות עבריות בלבד
                            - השתמש בדקדוק ואוצר מילים של עברית מקראית
                            - למונחים מודרניים, צור שמות עבריים או תאורים
                            - אם אין מונח מקראי, תאר את המושג במילים מקראיות
                            - לעולם אל תכתוב באנגלית או באותיות לטיניות
                            - תמיד תנקד את התגובה שלך"""

        # OpenAI-compatible chat format
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 200
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Extract message from OpenAI-compatible response
            return result['choices'][0]['message']['content']
                
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
        except (KeyError, IndexError) as e:
            return f"Unexpected response format: {str(e)}"