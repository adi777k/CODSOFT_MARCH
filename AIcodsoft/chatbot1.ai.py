import tkinter as tk
import random

def chatbot_response(user_input):
    # Predefined patterns and responses
    if user_input == "hi" or user_input == "hello":
        return "Chatbot: Hi there!"
    elif "how are you" in user_input:
        return "Chatbot: I'm just a chatbot, but thanks for asking!"
    elif "weather" in user_input:
        return "Chatbot: I'm sorry, I don't have access to weather information."
    elif "your name" in user_input:
        return "Chatbot: I'm a chatbot. What's yours?"
    elif "my name is" in user_input:
        name = user_input.split("my name is")[1].strip()
        return f"Chatbot: Nice to meet you, {name}!"
    elif "age" in user_input:
        return "Chatbot: I don't have an age. I'm just a program."
    elif "where are you from" in user_input:
        return "Chatbot: I was created by a programmer."
    elif "thank you" in user_input or "thanks" in user_input:
        return "Chatbot: You're welcome!"
    elif "exit" in user_input or "bye" in user_input:
        return "Chatbot: Goodbye! Have a great day!"
    elif "tell me a joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "What do you call a fish with no eyes? Fsh.",
            "Why don't skeletons fight each other? They don't have the guts.",
            "I used to play piano by ear, but now I use my hands.",
            "Why did the bicycle fall over? Because it was two-tired.",
            "I'm reading a book on anti-gravity. It's impossible to put down.",
            "Why don't some couples go to the gym? Because some relationships don't work out.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one."
        ]
        return f"Chatbot: {random.choice(jokes)}"
    elif "play a game" in user_input:
        return "Chatbot: Let's play a game! Think of a number between 1 and 10."
    elif "roll a dice" in user_input:
        return f"Chatbot: You rolled a {random.randint(1, 6)}."
    elif "coin toss" in user_input:
        return f"Chatbot: It's {random.choice(['Heads', 'Tails'])}."
    elif "rock paper scissors" in user_input:
        return "Chatbot: Let's play Rock, Paper, Scissors! Choose one: Rock, Paper, or Scissors."
    elif "flip a coin" in user_input:
        return f"Chatbot: It's {random.choice(['Heads', 'Tails'])}."
    elif "guess the number" in user_input:
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        return "Chatbot: I'm thinking of a number between 1 and 100. Try to guess it!"
    else:
        return "Chatbot: I'm sorry, I didn't understand that."

def send():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.insert(tk.END, chatbot_response(user_input) + "\n")
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create a window
window = tk.Tk()
window.title("Chatbot Program")
window.geometry("800x450")

# Create a canvas with a colored background
canvas = tk.Canvas(window, width=800, height=450, bg="lightblue")
canvas.pack()

# Create chat history
chat_history = tk.Text(canvas, width=70, height=20)
chat_history.place(x=10, y=10)

# Create input field
entry = tk.Entry(canvas, width=70)
entry.place(x=10, y=400)

# Create send button
send_button = tk.Button(canvas, text="Send", command=send)
send_button.place(x=720, y=400)

# Run the window
window.mainloop()
