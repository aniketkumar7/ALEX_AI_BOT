import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def chat_with_ai():
    print("Welcome to your personal AI tutor Type your questions and I'll do my best to help.")
    print("Type 'exit' to quit.")
    

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("See you next time GoodDay! \n")
            break

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

        response = chat_completion.choices[0].message.content        
        print("AI Tutor: \n", response)


if __name__ == "__main__":
    chat_with_ai()
