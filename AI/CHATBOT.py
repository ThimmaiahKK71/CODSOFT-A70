def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "who are you" in user_input:
        return "I am a simple chatbot created to assist you with basic queries."

    elif "how are you" in user_input or "how you" in user_input:
        return "I am good, Hope your doing good, how may i help you"

    elif "weather" in user_input:
        return "I can't provide real-time weather updates, but I suggest checking your favorite weather app."

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    elif "day" in user_input:
        from datetime import datetime
        current_day = datetime.now().strftime("%A")
        return f"Today is {current_day}."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! Feel free to ask anything"

    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

print("Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day! Feel free to ask anything")
        break
    else:
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
