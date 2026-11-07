
print("===== PYTHON CHATBOT =====")
print("Hello! I am a simple chatbot.")
print("You can talk to me.")
print("Type 'bye' to exit.")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thank you.")

    elif user_input == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Please try another message.")

print("\nChat ended. Thank you!")