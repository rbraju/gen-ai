import os
from dotenv import load_dotenv, find_dotenv

def load_env() -> None:
    load_dotenv(find_dotenv()) # load environment variables from .env file

def get_openai_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise RuntimeError('OPENAI_API_KEY not set. Ensure .env exists and has OPENAI_API_KEY defined.')
    return api_key