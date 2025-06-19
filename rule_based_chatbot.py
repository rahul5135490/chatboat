def chatbot():
    print("🤖 Chatbot: Hello! I'm your simple rule-based chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print(" Chatbot: Hello there! How can I help you?")

        elif user_input in ["how are you", "how are you doing"]:
            print(" Chatbot: I'm just a bunch of rules, but I'm functioning perfectly!")

        elif user_input in ["what is your name", "who are you"]:
            print(" Chatbot: I'm a simple rule-based chatbot created in Python.")

        elif user_input in ["bye", "exit", "quit"]:
            print(" Chatbot: Goodbye! Have a great day.")
            break

        else:
            print(" Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
