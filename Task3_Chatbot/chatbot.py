
import re

# FAQ database
FAQ = {
    "python": "Python is a popular programming language.",
    "internship": "An internship provides practical work experience.",
    "courses": "We offer Python, Java and Full Stack courses.",
    "contact": "You can contact our support team through email.",
    "certificate": "Certificates are provided after successful completion."
}

# Business information
BUSINESS_HOURS = "Our business hours are Monday to Saturday, 9 AM to 6 PM."


def get_response(user_input):

    message = user_input.lower().strip()

    # Empty message
    if not message:
        return "Please enter a message."

    # Exit intent
    if re.search(r"\b(bye|exit|quit)\b", message):
        return "EXIT"

    # Greeting intent
    if re.search(r"\b(hello|hi|hey|good morning|good evening)\b", message):
        return "Hello! Welcome to Python Chatbot. How can I help you?"

    # How are you intent
    if re.search(r"\bhow are you\b", message):
        return "I am doing great! Thank you for asking."

    # Name intent
    if re.search(r"\b(your name|who are you)\b", message):
        return "My name is Python Chatbot."

    # Creator intent
    if re.search(r"\b(who created you|your creator)\b", message):
        return "I was created using Python programming."

    # Business hours intent
    if re.search(r"\b(business hours|opening hours|working hours|timings)\b", message):
        return BUSINESS_HOURS

    # FAQ intent
    for keyword, answer in FAQ.items():
        if re.search(r"\b" + re.escape(keyword) + r"\b", message):
            return answer

    # Thank you intent
    if re.search(r"\b(thank you|thanks)\b", message):
        return "You're welcome! Happy to help."

    # Unknown message
    return "Sorry, I don't understand that. Please try another question."


def main():

    print("===== PYTHON CHATBOT =====")
    print("Hello! I am an improved Python chatbot.")
    print("You can ask questions about Python, courses and internships.")
    print("Type 'bye', 'exit' or 'quit' to end the chat.")

    while True:

        try:
            user_input = input("\nYou: ")

            response = get_response(user_input)

            if response == "EXIT":
                print("Bot: Goodbye! Have a nice day!")
                break

            print("Bot:", response)

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat ended. Goodbye!")
            break

    print("\nChat ended. Thank you!")


if __name__ == "__main__":
    main()