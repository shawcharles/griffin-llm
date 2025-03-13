import os
import requests
import json
from typing import Dict, Any

class LLMClient:
    """Main interface for Griffin LLM operations"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GRIFFIN_ARLIAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set GRIFFIN_ARLIAI_API_KEY environment variable")

        self.base_url = "https://api.arliai.com/v1"
        self.default_headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def chat_completion(self, messages: list, **params) -> Dict[str, Any]:
        """Execute chat completion with error handling"""
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": "Mistral-Nemo-12B-Instruct-2407",
            "messages": messages,
            **params
        }

        try:
            response = requests.post(
                url,
                headers=self.default_headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "Request timed out after 30 seconds"}
        except requests.exceptions.SSLError:
            return {"error": "SSL error - check system certificates"}
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}

class ModelLoader:
    """Handles LLM client initialization"""
    
    @staticmethod
    def from_environment() -> LLMClient:
        """Create client using environment variables"""
        return LLMClient()
