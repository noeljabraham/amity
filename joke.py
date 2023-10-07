import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke_data = response.json()
    return joke_data["setup"], joke_data["punchline"]

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        input("Press Enter to get a random joke...")
        setup, punchline = get_joke()
        print("\nHere's a joke for you:")
        print(f"Setup: {setup}")
        print(f"Punchline: {punchline}\n")

        another = input("Want another joke? (yes/no): ")
        if another.lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
