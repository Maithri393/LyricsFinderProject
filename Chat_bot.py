import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from datetime import datetime

# Bot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    elif "day" in user_input:
        return f"Today is {datetime.now().strftime('%A')}"
    elif "your name" in user_input:
        return "I'm PyBot, your personal assistant!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! Thanks for asking."
    elif "who made you" in user_input:
        return "I was created by a Python developer just like you."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    elif "what can you do" in user_input:
        return "I can tell you the date, time, day, and answer simple questions. Try asking more!"
    elif "joke" in user_input:
        return "Why don’t scientists trust atoms? Because they make up everything!"
    elif "weather" in user_input:
        return "I'm not connected to the internet, but you can check weather.com for updates."
    elif "age" in user_input:
        return "I'm timeless. Bots don't age!"
    else:
        return "Sorry, I didn't understand that. Try asking about time, date, or something fun like a joke."

# Placeholder management
def add_placeholder(event=None):
    if entry.get() == "":
        entry.insert(0, "Type here...")
        entry.config(foreground="gray")

def remove_placeholder(event):
    if entry.get() == "Type here...":
        entry.delete(0, "end")
        entry.config(foreground="black")

# Send message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "" or user_input == "Type here...":
        return

    chatbox.config(state='normal')
    chatbox.insert("end", f"You: {user_input}\n")
    response = get_bot_response(user_input)
    chatbox.insert("end", f"Bot: {response}\n\n")
    chatbox.config(state='disabled')
    entry.delete(0, 'end')
    add_placeholder()
    chatbox.see("end")

# App setup
app = ttk.Window(title="💬 Python Chatbot", themename="cosmo")  # Try "darkly", "journal", etc.
app.geometry("500x600")
app.resizable(True, True)

# Title
ttk.Label(app, text="💬 PyBot - Your Assistant", font=("Helvetica", 20, "bold")).pack(pady=10)

# Chat display
chatbox = scrolledtext.ScrolledText(app, wrap="word", font=("Consolas", 12), height=25, state="disabled")
chatbox.pack(padx=20, pady=(0, 10), fill="both", expand=True)

# Input frame
input_frame = ttk.Frame(app)
input_frame.pack(fill="x", padx=20, pady=10)

# Entry field with placeholder
entry = ttk.Entry(input_frame, font=("Helvetica", 12), foreground="gray")
entry.insert(0, "Type here...")
entry.bind("<FocusIn>", remove_placeholder)
entry.bind("<FocusOut>", add_placeholder)
entry.bind("<Return>", lambda event: send_message())
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

# Send button
ttk.Button(input_frame, text="Send", bootstyle=SUCCESS, command=send_message).pack(side="right")

# Start app
app.mainloop()
