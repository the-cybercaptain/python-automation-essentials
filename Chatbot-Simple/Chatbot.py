# Project : Simple Chatbot


import random

def chatbot():
    responses = {
        "hello": ["Hi!", "Hello!", "Hey!"],
        "how are you": ["I'm good, thanks!", "I'm doing well.", "I'm great!"],
        "what's your name": ["I'm ChatBot!", "My name is ChatBot.", "I'm an AI chatbot."],
    }

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("ChatBot:", random.choice(responses[user_input]))
        elif user_input == "quit":
            print("ChatBot: Bye!")
            break
        else:
            print("ChatBot: Sorry, I didn't understand that.")

# Usage
chatbot()