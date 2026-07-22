from chatbot import chatbot_response


print("=" * 40)
print("        SMART RULE BASED CHATBOT")
print("=" * 40)

print("Bot: Hello! I am SmartBot.")
print("Bot: Type 'bye' to end the chat.")


while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() in ["bye", "exit", "quit"]:
        break