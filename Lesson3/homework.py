
import re, random
from colorama import Fore,init
init(autoreset=True)

destinations= {"beaches": ["Puri", "Chennai", "Miami"],
              "mountains": ["Table Mountain", "Mt. Fuji", "Himalayas"],
            "cities": ["Rome", "London", "Barcelona"]}

jokes = [
        "Why don't aliens visit earth? Because they checked our reviews and saw we only have one star!",
        "Why do people like traveling by train? Because it's a great way to 'track' your progress!",
        "Why did the mountain go to the doctor? Because it had 'peak' condition issues!"
]


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)


    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()


        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()


def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location= normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days= input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: packing tips for {days} days in {location}:")
    print(Fore.GREEN + "-Pack versatile clothes")
    print(Fore.GREEN + "-Bring chargers and adapters")
    print(Fore.GREEN + "-Keep a track of weather forecast")
    print(Fore.GREEN + "-Ensure to secure international roaming for connectivity and safety!")


def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


def show_help():
    print(Fore.MAGENTA + "\n I can:")
    print(Fore.GREEN + "-suggest traveling locations(type 'recommendation')")
    print(Fore.GREEN + "-offer packing tips (type 'packing')")
    print(Fore.GREEN + "-crack a joke(type 'joke')")
    print(Fore.GREEN + "-type 'exit' or 'bye' to end")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")


    show_help()


    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)


        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe and fun travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")


if __name__ == "__main__": 
    chat()










