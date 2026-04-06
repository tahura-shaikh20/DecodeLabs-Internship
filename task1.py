import random
import datetime

print("🤖 Bot: Hello! I am your AI chatbot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Greetings
    if any(word in user for word in ["hi", "hello", "hey"]):
        responses = ["Hello there! ", "Hey! How can I help you?", "Hi! Nice to meet you!"]
        print("Bot:", random.choice(responses))

    # Asking name
    elif "your name" in user:
        print("Bot: I am DecodeBot, your virtual assistant ")

    # Asking about user
    elif "my name" in user:
        print("Bot: I’d love to know your name! ")

    # How are you
    elif "how are you" in user:
        responses = ["I'm doing great! ", "All good here!", "Running perfectly! "]
        print("Bot:", random.choice(responses))

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Date
    elif "date" in user:
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    # Help
    elif "help" in user:
        print("Bot: You can ask me about time, date, greetings, or just chat!")

    # Joke
    elif "joke" in user:
        jokes = [
            "Why did the computer go to therapy? It had too many bugs! ",
            "Why do programmers prefer dark mode? Because light attracts bugs! ",
            "I told my computer I needed a break... it said no problem and froze! "
        ]
        print("Bot:", random.choice(jokes))

    # Exit
    elif user == "bye":
        print("Bot: Goodbye! Have a great day! ")
        break

    # Default
    else:
        print("Bot: Hmm... I’m not sure about that. Try asking something else! ")