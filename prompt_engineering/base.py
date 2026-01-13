from config.openai_client import get_openai_client

client = get_openai_client()

def get_completion(prompt, model="gpt-4.1"):
    response = client.responses.create(model=model, input=prompt)
    return response.output_text

    