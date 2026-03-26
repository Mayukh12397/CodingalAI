import requests

def getRandomJoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code== 200:
        print(f"Full Json Response: {response.json()}")
        jokedata= response.json() 
        return f"{jokedata['setup']}-{jokedata['punchline']}"
    else:
        return "Failed to Retreive Joke"
def main():
    print("Welcome to our hilarious joke generator!")
    while True:
        userInput= input("Kindly Press enter to get a new joke, or type 'q/exit/esc' to quit.")
        if userInput in("q","exit","esc"):
            print("Bye! Hope to meet you again soon.")
            break 
        joke= getRandomJoke()
        print(joke)
if __name__== "__main__":
    main()
