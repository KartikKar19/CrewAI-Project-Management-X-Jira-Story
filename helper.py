import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
def load_env():
    """Compatibility function so old code still works"""
    return get_openai_api_key()

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key.strip() == "" or api_key.strip().lower().startswith("your_api_key_here"):
        raise ValueError(
            "❌ No valid OpenAI API key found.\n"
            "Please set OPENAI_API_KEY in your .env file, e.g.:\n\n"
            "OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx\n"
        )

    return api_key
