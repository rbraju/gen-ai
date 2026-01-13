from openai import OpenAI
from config.settings import load_env, get_openai_api_key

def get_openai_client() -> OpenAI:
    load_env()
    return OpenAI(api_key=get_openai_api_key())