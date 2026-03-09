# pip install pandas textblob colorama

import pandas as pd
from textblob import TextBlob
import random, time
from colorama import Fore, init

init(autoreset=True)

# Load dataset
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print("Dataset file not found.")
    raise SystemExit

# Clean genre list
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

# Loading dots animation
def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Sentiment label
def senti(p):
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

# Show movie details
def show_movies(movies, name):
    print(Fore.GREEN + f"\n🎬 Movie Recommendations for {name}:\n")

    for i, (_, r) in enumerate(movies.iterrows(), 1):
        print(Fore.CYAN + f"Movie {i}")
        print(Fore.YELLOW + f"Title   : {r['Series_Title']}")
        print(f"Genre   : {r['Genre']}")
        print(f"Year    : {r['Released_Year']}")
        print(f"Rating  : {r['IMDB_Rating']}")
        print(f"Overview: {r['Overview']}\n")
        print("-"*50)

# AI Recommendation
def ai_recommend(genre=None, mood=None, rating=None, n=5):
    data = df

    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]

    if rating:
        data = data[data["IMDB_Rating"] >= rating]

    if data.empty:
        return None

    data = data.sample(frac=1)

    results = []
    for _, row in data.iterrows():
        overview = row["Overview"]
        polarity = TextBlob(str(overview)).sentiment.polarity

        if mood:
            if polarity >= 0:
                results.append(row)
        else:
            results.append(row)

        if len(results) == n:
            break

    if not results:
        return None

    return pd.DataFrame(results)

# Random Recommendation
def random_recommend(n=5):
    return df.sample(n)

# Genre selection
def get_genre():
    print(Fore.GREEN + "Available Genres:")
    for i, g in enumerate(genres, 1):
        print(f"{i}. {g}")

    while True:
        choice = input(Fore.YELLOW + "Enter genre number or name: ").strip()

        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(genres):
                return genres[num-1]

        choice = choice.title()
        if choice in genres:
            return choice

        print(Fore.RED + "Invalid genre. Try again.")

# Rating input
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip': ")

        if x.lower() == "skip":
            return None

        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            else:
                print("Rating out of range.")
        except:
            print("Invalid input.")

# Main Program
print(Fore.BLUE + "🎥 Welcome to the Movie Recommendation System 🎥\n")

name = input(Fore.YELLOW + "Enter your name: ")
print(Fore.GREEN + f"\nHello {name}! Let's find a movie for you.\n")

# User chooses recommendation type
while True:
    print(Fore.BLUE + "Choose Recommendation Type:")
    print("1. AI Based Recommendation")
    print("2. Random Recommendation")

    choice = input(Fore.YELLOW + "Enter choice (1 or 2): ")

    # AI recommendation
    if choice == "1":

        genre = get_genre()

        mood = input(Fore.YELLOW + "How are you feeling today? ")

        print(Fore.BLUE + "Analyzing mood", end="")
        dots()

        polarity = TextBlob(mood).sentiment.polarity
        print(Fore.GREEN + f"\nMood polarity: {polarity:.2f} ({senti(polarity)})")

        rating = get_rating()

        print(Fore.BLUE + "\nFinding AI recommendations", end="")
        dots()

        recs = ai_recommend(genre, mood, rating)

        if recs is None:
            print(Fore.RED + "\nNo suitable movies found.")
        else:
            show_movies(recs, name)

        break

    # Random recommendation
    elif choice == "2":

        print(Fore.BLUE + "\nSelecting random movies", end="")
        dots()

        recs = random_recommend()

        show_movies(recs, name)

        break

    else:
        print(Fore.RED + "Invalid choice. Try again.")

# Loop for more recommendations
while True:
    again = input(Fore.YELLOW + "\nDo you want more recommendations? (yes/no): ").lower()

    if again == "no":
        print(Fore.GREEN + "\nEnjoy your movie! 🍿🎬")
        break

    elif again == "yes":
        recs = random_recommend()
        show_movies(recs, name)

    else:
        print("Invalid input.")