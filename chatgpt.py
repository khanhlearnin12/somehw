import openai
import os

openai.api_key = "myapi"
def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        print("Chat with GPT! Type 'quit', 'exit', or 'bye' to end the chat.")
        user_input = input("You: ") 
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("ChatGPT: ", response)
