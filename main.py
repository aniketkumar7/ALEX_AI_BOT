from groq import Groq


def get_api_key():
    """
    Prompts the user to enter their GROQ API key.

    Returns:
        str: The user-provided API key.
    """
    api_key = input("Please enter your GROQ API key: ")
    return api_key


def chat_with_ai():
    """
    Initiates the chat session with the AI tutor.
    """
    print("Welcome to your personal AI tutor Type your questions and I'll do my best to help.")
    print("Type 'exit' to quit.")

    api_key = get_api_key()
    client = Groq(api_key=api_key,)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("See you next time GoodDay! \n")
            break

        # Send the user input to the AI tutor
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=450,
            top_p=0.9,
            stream=False,
            stop="exit",
        )

        # Print the AI tutor's response
        response = chat_completion.choices[0].message.content
        print("AI Tutor: \n", response)


# Start the chat session
if __name__ == "__main__":
    chat_with_ai()
