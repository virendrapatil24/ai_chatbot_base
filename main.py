import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=150):
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

def update_messages(message, messages):
    messages.append(message)

def create_prompt(user_input, messages):
    message = {"role": "user", "content": user_input}
    update_messages(message, messages)
    return messages

def get_bot_response(user_input, messages):
    prompt = create_prompt(user_input, messages)
    bot_response = get_completion_from_messages(prompt)

    if bot_response:
        reply = {"role": "assistant", "content": bot_response}
        update_messages(reply, messages)
    else:
        bot_response = "I apologize, but I do not have a response for that."
    
    return bot_response

def main():
    messages = []
    system_msg = input("What type of chatbot would you like to create?\n")
    messages.append({"role": "system", "content": system_msg})
    
    while True:
        user_input = input("User: ")
        response = get_bot_response(user_input, messages)
        print(f'Bot: {response}')

if __name__ == '__main__':
    main()
