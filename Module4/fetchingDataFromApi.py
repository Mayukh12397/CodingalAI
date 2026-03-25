# Students will use the requests library to fetch data from public APIs (e.g., joke API, trivia API) and display the results in a user-friendly way.
import requests

def getRandomJoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code== 200:
        print(f"Full Json Response: {response.json()}") # Line 8 just shows the full response, actual joke is in line 10.
        jokedata= response.json() # Converting the data into something which is easier and readable for humans to interpret.(Parsing the Data). When we receive an API data, we can use the .json() method in python to comvert the response into a dictionary(data in curly bracket). This is known as Parsing.
        return f"{jokedata['setup']}-{jokedata['punchline']}"
    else:
        return "Failed to Retreive Joke"
def main():
    print("Welcome to random joke generator!")
    while True:
        userInput= input("Press enter to get a new joke, or type 'q/exit' to quit.")
        if userInput in("q","exit"):
            print("Goodbye!")
            break 
        joke= getRandomJoke()
        print(joke)
if __name__== "__main__":
    main()
# API is Application Programming Interface. This URL will call API of random joke and in response(when success), it will give a random joke.