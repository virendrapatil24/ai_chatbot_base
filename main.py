import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_api_response(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=150):

    try:
        response = client.chat.completions.create(
            model = model,
            messages = messages,
            temperature = temperature,
            max_tokens = max_tokens,
        )

    except Exception as e:
        print('Error', e)

    return response.choices[0].message["content"]

messages = "Hello"
print(get_api_response(messages))