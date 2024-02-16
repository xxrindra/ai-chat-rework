import requests

# Replace with your GPT-4 API key
API_KEY = 'YOUR_API_KEY_HERE'

def get_chatbot_response(user_message):
    try:
        response = requests.post(
            'https://api.openai.com/v1/engines/davinci/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {API_KEY}',
            },
            json={
                'prompt': user_message,
                'max_tokens': 50,  # Adjust as needed
            }
        )
        data = response.json()
        chatbot_response = data['choices'][0]['text']
        return chatbot_response
    except Exception as e:
        print(f"Error fetching chatbot response: {e}")
        return "Oops, something went wrong!"

def main():
    print("Welcome to ChatBot Game!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break

        chatbot_reply = get_chatbot_response(user_input)
        print(f"ChatBot: {chatbot_reply}")

if __name__ == "__main__":
    main()
