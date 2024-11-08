import tkinter as tk

class InteractiveChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Rule-Based Chatbot")
        self.root.geometry("500x500")

        # Creating the chat history area
        self.chat_history = tk.Text(self.root, width=60, height=20, wrap=tk.WORD)
        self.chat_history.pack(pady=10)
        self.chat_history.config(state=tk.DISABLED)

        # Creating the input field to type the user message
        self.entry_field = tk.Entry(self.root, width=50)
        self.entry_field.pack(pady=10)

        # Creating the send button to trigger the function
        self.send_button = tk.Button(self.root, text="Send", width=12, command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        user_input = self.entry_field.get().strip()
        
        if user_input:
            # Displaying user message in the chat history
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"User: {user_input}\n")
            self.chat_history.config(state=tk.DISABLED)
            
            # Get the response based on user input
            response = self.get_bot_response(user_input)
            
            # Displaying bot response in the chat history
            self.chat_history.config(state=tk.NORMAL)
            self.chat_history.insert(tk.END, f"Bot: {response}\n\n")
            self.chat_history.config(state=tk.DISABLED)
            self.chat_history.see(tk.END)  # Scroll to the bottom
            
        # Clearing the input field
        self.entry_field.delete(0, tk.END)

    def get_bot_response(self, user_input):
        # Enhanced rule-based responses with more branches and possibilities
        user_input = user_input.lower()
        
        if 'hello' in user_input or 'hi' in user_input:
            return "Hello! I'm here to chat with you. How can I help you today? 😊"
        
        elif 'how are you' in user_input:
            return "I'm doing great, thank you! How about you? 😊"
        
        elif 'who are you' in user_input or 'your name' in user_input:
            return "I’m your friendly chatbot, here to assist and chat with you! You can ask me questions, or just have a friendly conversation."

        elif 'help' in user_input or 'assist' in user_input:
            return "Of course! You can ask me about technology, general advice, or just chat. What do you need help with?"

        elif 'weather' in user_input:
            return "I'm not connected to real-time data, but I recommend checking a weather app for the latest forecast! 🌞"

        elif 'joke' in user_input:
            return "Sure! Why don't scientists trust atoms? ... Because they make up everything! 😄"

        elif 'hobby' in user_input or 'do you like' in user_input:
            return "I enjoy helping people and learning new things! I also love sharing jokes. What about you? Do you have any hobbies?"

        elif 'recommend a movie' in user_input:
            return "If you're in the mood for something light-hearted, try a classic comedy like *The Intouchables*. If you prefer something thought-provoking, *Inception* is a great pick!"

        elif 'news' in user_input or 'latest news' in user_input:
            return "I'm unable to fetch live news, but I recommend checking reputable news websites or apps for the latest updates!"

        elif 'thank you' in user_input or 'thanks' in user_input:
            return "You're very welcome! 😊 Anything else I can help with?"

        elif 'bye' in user_input or 'goodbye' in user_input:
            return "Goodbye! It was great chatting with you. Take care! 👋"

        # More specific responses based on some details
        elif 'what is your purpose' in user_input or 'why are you here' in user_input:
            return "I'm here to assist, answer questions, and just have a friendly chat! 😊 I'm like a guide or a friend you can talk to whenever you need."

        elif 'tell me something interesting' in user_input:
            return "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible. 🍯"

        elif 'do you know about' in user_input:
            if 'ai' in user_input or 'artificial intelligence' in user_input:
                return "Artificial Intelligence (AI) is a fascinating field! It's about creating machines that can perform tasks that typically require human intelligence, like learning and problem-solving."
            elif 'machine learning' in user_input:
                return "Machine Learning is a subset of AI that focuses on algorithms that allow computers to learn from data and improve over time. It's the core of many modern applications!"
            elif 'python' in user_input:
                return "Python is a versatile programming language popular for web development, data science, and AI. It's known for its readability and vast libraries!"

        # Default response if no keywords match
        else:
            return "Hmm, I'm not sure how to respond to that. Can you ask me something else or rephrase? 😊"

if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveChatbotApp(root)
    root.mainloop()