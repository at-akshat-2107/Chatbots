import tkinter as tk

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Rule-Based Chatbot")
        self.root.geometry("400x400")
        
        # Creating the chat history area
        self.chat_history = tk.Text(self.root, width=50, height=15, wrap=tk.WORD)
        self.chat_history.pack(pady=10)
        self.chat_history.config(state=tk.DISABLED)

        # Creating the input field to type the user message
        self.entry_field = tk.Entry(self.root, width=40)
        self.entry_field.pack(pady=10)

        # Creating the send button to trigger the function
        self.send_button = tk.Button(self.root, text="Send", width=10, command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        user_input = self.entry_field.get()
        
        if user_input:
            # Displaying user message in the chat history
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"User: {user_input}\n")
            self.chat_history.config(state=tk.DISABLED)
            
            # Simple rule-based chatbot response using if-else statements
            response = self.get_bot_response(user_input)
            
            # Displaying bot response in the chat history
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"Bot: {response}\n")
            self.chat_history.config(state=tk.DISABLED)
        
        # Clearing the input field
        self.entry_field.delete(0, tk.END)

    def get_bot_response(self, user_input):
        # Simple if-else rule-based responses
        if 'hello' in user_input.lower():
            return "Hello! How can I assist you today?"
        elif 'how are you' in user_input.lower():
            return "I'm doing great, thank you for asking!"
        elif 'bye' in user_input.lower():
            return "Goodbye! Have a great day!"
        elif 'your name' in user_input.lower():
            return "I am your friendly chatbot."
        else:
            return "Sorry, I didn't understand that. Can you rephrase?"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
