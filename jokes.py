# Create a random joke generator using Python’s random module.
import random

# Create a list of jokes that include their punchlines
jokes = [
    {
        "setup": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "setup": "I told my wife she was drawing her eyebrows too high.",
        "punchline": "She looked surprised."
    },
    {
        "setup": "Why don’t skeletons fight each other?",
        "punchline": "They don’t have the guts."
    },
    {
        "setup": "What do you call cheese that isn't yours?",
        "punchline": "Nacho cheese."
    },
    {
        "setup": "Why did the bicycle fall over?",
        "punchline": "Because it was two-tired!"
    }
]

# Use the random module to display a random joke each time the code runs
random_joke = random.choice(jokes)
print(f"Joke: {random_joke['setup']}")
print(f"Punchline: {random_joke['punchline']}")
