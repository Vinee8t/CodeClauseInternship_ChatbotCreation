import tkinter as tk
from tkinter import scrolledtext
import json
import random

import nltk
from nltk.chat.util import Chat, reflections

# Read intents from JSON file
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Convert patterns to lowercase
for intent in intents['intents']:
    intent['patterns'] = [pattern.lower() for pattern in intent['patterns']]

# Extract patterns and responses from intents
# Extract patterns and responses from intents
pairs = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        responses = intent['responses']
        pairs.append((pattern, responses))

# Print pairs for debugging
print("Pairs:", pairs)

# Create a chatbot instance
chatbot = Chat(pairs,responses)


# Function to handle sending message and receiving response
def send_message():
    user_input = entry.get().lower()  # Convert input to lowercase
    print("User Input:", user_input)  # Debug message
    if user_input == 'quit':
        chat_area.insert(tk.END, "Chat ended.\n")
        entry.delete(0, tk.END)
    else:
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, f"You: {user_input}\n")
        print("Matched Pattern:", response)  # Debug message
        if response:
            chat_area.insert(tk.END, f"Salt: {response}\n")
        else:
            chat_area.insert(tk.END, f"Salt: I'm sorry, I don't understand.\n")
        entry.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("Salt")

# Create chat area
chat_area = scrolledtext.ScrolledText(root, width=50, height=20)
chat_area.grid(column=0, row=0, padx=10, pady=10)

# Create input field
entry = tk.Entry(root, width=40)
entry.grid(column=0, row=1, padx=10, pady=10)

# Create send button
send_button = tk.Button(root, text="Chat", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Start GUI event loop
root.mainloop()
