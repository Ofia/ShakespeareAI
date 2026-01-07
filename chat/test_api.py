import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')
django.setup()

from django.conf import settings
import requests

api_key = settings.HUGGINGFACE_API_KEY

print("Testing Hugging Face Router endpoints...\n")

# Test different router URL patterns
test_configs = [
    {
        "url": "https://router.huggingface.co",
        "payload": {
            "model": "gpt2",
            "inputs": "Hello, how are you?",
            "parameters": {"max_length": 50}
        }
    },
    {
        "url": "https://router.huggingface.co/gpt2",
        "payload": {
            "inputs": "Hello, how are you?",
            "parameters": {"max_length": 50}
        }
    }
]

headers_base = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

for i, config in enumerate(test_configs, 1):
    url = config["url"]
    payload = config["payload"]
    headers = headers_base
    
    print(f"Test {i}: {url}")
    print(f"Payload: {payload}")
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.text[:300]}")
        
        if response.status_code == 200:
            print(f"\n✓✓✓ SUCCESS! Use this configuration:")
            print(f"  URL: {url}")
            print(f"  Payload format: {payload}")
            break
        print()
    except Exception as e:
        print(f"  Error: {str(e)[:200]}\n")

print("\n" + "="*50)
print("WAITING FOR YOUR MODEL...")
print("="*50)
print("Please share the model URL that works in your other project!")