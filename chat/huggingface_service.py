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
    
    def get_response(self, user_message, language_mode, chat_history=None):
        if chat_history is None:
            chat_history = []

        if language_mode == 'shakespeare':
            system_prompt = "You are an AI assistant that speaks ONLY in Shakespearean English. Use 'thee', 'thou', 'thy', archaic verb forms like 'art', 'doth', 'hath', and poetic language. Never break character."

        else:
            system_prompt = """אתה חייב לענות רק בעברית מקראית עם ניקוד מלא

                            חוקים:
                            - .

                            דוגמאות:
                            ✓ שָׁלוֹם לְךָ
                            ✓ מָה שְׁמֶךָ
                            ✗ שלום לך (לא טוב - אין ניקוד!)

                            כללים:
                            - כל אות עברית חייבת להיות מְנֻקֶּדֶת
                            - השתמש בדקדוק עברית מקראית
                            - אל תכתוב ללא ניקוד לעולם

                            זכור: ניקוד בכל מילה
                            - אל תניח את מין המשתמש (רק אם מפורשות נאמר שזה גבר או נקבה)
                            - כתוב הכל באותיות עבריות בלבד
                            - השתמש בדקדוק ואוצר מילים של עברית מקראית
                            - למונחים מודרניים, צור שמות עבריים או תאורים
                            - אם אין מונח מקראי, תאר את המושג במילים מקראיות
                            - לעולם אל תכתוב באנגלית או באותיות לטיניות
                            - תמיד תנקד את התגובה שלך"""

        # Build messages array with conversation history
        messages = [{"role": "system", "content": system_prompt}]

        # Add conversation history
        messages.extend(chat_history)

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # OpenAI-compatible chat format
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 350
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