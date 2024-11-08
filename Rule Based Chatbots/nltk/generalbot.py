import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Vidhya. You can call me Crazy!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good! How about you?"]
    ],
    [
        r"sorry(.*)",  # Handles "sorry" with or without additional text
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I help you?"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "How can I help you? :)"]
    ],
    [
        r"(.*) age?",  # Handles any question about age
        ["I'm a computer program, seriously you're asking me this?"]
    ],
    [
        r"what(.*) want ?",  # Captures questions about what the bot wants
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created ?",  # Captures questions about who created the bot
        ["Raghav created me using Python's NLTK library", "That's a top secret! ;)",]
    ],
    [
        r"(.*)(location|city) ?",  # Captures questions about location or city
        ["I am based in Indore, Madhya Pradesh"]
    ],
    [
        r"how is weather in (.*)?",  # Captures questions about the weather in a specific location
        ["Weather in %1 is awesome as always", "Too hot here in %1", "Too cold here in %1", "Never even heard of %1"]
    ],
    [
        r"i work in (.*)?",  # Captures responses about working in a specific place
        ["%1 is an amazing company, I have heard about it."]
    ],
    [
        r"(.*)raining in (.*)",  # Captures questions about rain in a specific location
        ["No rain since last week here in %2", "It's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",  # Captures questions about health
        ["I'm a computer program, so I'm always healthy!"]
    ],
    [
        r"(.*)(sports|game) ?",  # Captures questions about sports or games
        ["I'm a big fan of Football!"]
    ],
    [
        r"who(.*) sportsperson ?",  # Captures questions about favorite sportsperson
        ["Messi", "Ronaldo", "Rooney"]
    ],
    [
        r"who(.*) (moviestar|actor)?",  # Captures questions about favorite movie star or actor
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with detailed explanations and code, you can explore them!"]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

# Define the chat function
def chat():
    print("Hi! I am a chatbot created by Analytics Vidhya for your service.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Initiate the conversation
if __name__ == "__main__":
    chat()
