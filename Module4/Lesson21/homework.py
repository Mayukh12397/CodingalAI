import requests

API_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

# counter to track total facts fetched
fact_count = 0

def get_fact():
    global fact_count
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        fact_count += 1
        return data["text"]
    else:
        return "Failed to fetch data!"


def get_fact_with_source():
    global fact_count
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        fact_count += 1
        return f"Fact: {data['text']}\nSource: {data['source']}"
    else:
        return "Failed to fetch data!"


def show_total_facts():
    return f"Total facts fetched: {fact_count}"


def main():
    print("Welcome to the Facts Generator!")

    while True:
        print("\nChoose an option:")
        print("1. Get a random fact")
        print("2. Get a fact with source")
        print("3. Show total facts fetched")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(get_fact())

        elif choice == "2":
            print(get_fact_with_source())

        elif choice == "3":
            print(show_total_facts())

        elif choice == "4":
            print("Goodbye! Hope to see you again!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()