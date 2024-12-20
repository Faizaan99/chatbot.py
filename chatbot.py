import nltk # type: ignore
import random
import string
from nltk.chat.util import Chat, reflections # type: ignore

# Download necessary NLTK data (for tokenization and processing)
nltk.download('punkt')

# Define some basic pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]),
    (r"what is your name?", ["I am a chatbot created by OpenAI.", "I don't have a name, but you can call me Chatbot."]),
    (r"how are you?", ["I'm doing great, thank you for asking!", "I'm just a program, but I feel good!"]),
    (r"what can you do?", ["I can chat with you, answer simple questions, and provide some fun facts!", 
                          "I can help you with information, general knowledge, or just chat."]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!",
                        "What did one ocean say to the other ocean? Nothing, they just waved!"]),
    (r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]),
]

# Define the chatbot class
class Chatbot:
    def __init__(self, pairs, reflections):
        self.chatbot = Chat(pairs, reflections)

    def start(self):
        print("Hi! I'm a chatbot. Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            response = self.chatbot.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase?")

# Main function to start the chatbot
if __name__ == "__main__":
    chatbot = Chatbot(pairs, reflections)
    chatbot.start()
