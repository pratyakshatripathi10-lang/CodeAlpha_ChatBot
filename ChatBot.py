def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    message = user_input.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm CodeAlpha Bot, your simple Python chatbot."
    elif message == "help":
        return "You can say: hello, how are you, what is your name, or bye."
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()

