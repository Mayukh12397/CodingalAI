# In this project learn to access a particular endpoint
import requests

Api_Url= "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_facts():
    response= requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language=en')
    if response.status_code== 200:
        print(f"Full Json Response: {response.json()}")
        data= response.json()
        return f"{data["text"]}"
    else:
        return 'Failed to Fetch Data!'

def main():
    print("Welcome to facts generator!")
    while True:
        user_input= input("Please press enter to get a new interesting fact and q/esc to quit the program.")
        if user_input in("q","esc"):
            print("Goodbye! Hope to meet you again soon.")
            break
        facts= get_facts()
        print(facts)

if __name__== "__main__":
    main()
   
    
     
