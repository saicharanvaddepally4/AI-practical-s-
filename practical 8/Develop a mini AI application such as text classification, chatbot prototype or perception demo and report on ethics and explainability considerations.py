
# Mini AI Chatbot using Python

print("================================")
print("       MINI AI CHATBOT")
print("================================")
print("Chatbot: Hello! How can I help you?")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ").lower()

    # Greeting
    if "hello" in user or "hi" in user:
        print("Bot: Hello! Nice to meet you.")

    # Name
    elif "name" in user:
        print("Bot: I am a Mini AI Chatbot.")

    # Study
    elif "study" in user or "exam" in user:
        print("Bot: Study regularly and practice daily.")

    # Weather
    elif "weather" in user:
        print("Bot: I cannot check live weather.")

    # Thanks
    elif "thank" in user:
        print("Bot: You are welcome!")

    # Help
    elif "help" in user:
        print("Bot: I can answer simple questions.")

    # Exit
    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand.")

print("\nChatbot stopped successfully!")
