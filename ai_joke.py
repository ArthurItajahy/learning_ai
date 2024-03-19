def chatbot(message):
    if "hello" in message.lower():
        return "Hi there! How can I assist you today?"
    elif "how are you" in message.lower():
        return "I'm just a chatbot, so I don't have feelings, but thanks for asking!"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print(chatbot(user_input))
            break
        
        response = chatbot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()