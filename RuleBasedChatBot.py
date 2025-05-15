import re, random
from colorama import Fore, init
init(autoreset=True)

destinations = {
    "India": ["Delhi", "Mumbai", "Bangalore"],
    "USA": ["New York", "Los Angeles", "Chicago"],
    "UK": ["London", "Manchester", "Birmingham"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "beaches":["Bali", "Maldives", "Hawaii"],
    "mountains":["Himalayas", "Rockies", "Andes"]
}
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and now it won't stop sending me beach wallpapers.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the bicycle fall over? Because it was two-tired!"
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def get_destination_recommendation():
    print(Fore.CYAN + "TravelBot : India, USA, UK, Australia, Canada, beaches, mountains")
    preference = input(Fore.YELLOW + "What type of destination are you looking for? (e.g., beaches, mountains, city) : ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot : How about visiting {suggestions}?")
        print(Fore.CYAN + "TravelBot : Do you Like it ? (yes/no)")
        answer = input(Fore.YELLOW + "Your answer : ")
        if answer == "yes":
            print(Fore.GREEN + "TravelBot : Great! Enjoy your trip!")
            packing_tips()
        elif answer == "no":
            print(Fore.RED + "TravelBot : No problem! Let's try again.")
            get_destination_recommendation()
        else:
            print(Fore.RED + "TravelBot : I didn't understand that. Please answer with 'yes' or 'no'.")
    else:
        print(Fore.RED + "TravelBot : I'm sorry, I don't have recommendations for that type of destination.")
    show_help()
def show_help():
    print(Fore.CYAN + "TravelBot : I can help you with travel recommendations, jokes, and more!")
    print(Fore.CYAN + "TravelBot : If you wanna ask for travel spots (say 'recommendation').")
    print(Fore.CYAN + "TravelBot : If you wanna ask for jokes (say 'joke').")
    print(Fore.CYAN + "TravelBot : If you want to exit, just type 'exit'.")
    print(Fore.CYAN + "TravelBot : If you need help, type 'help'.")
def tell_joke():
    print(Fore.CYAN + "TravelBot : Here's a joke for you:")
    print(Fore.GREEN + random.choice(jokes))
def packing_tips():
    print(Fore.CYAN + "TravelBot : Where to ? :")
    location = normalize_input(input(Fore.YELLOW + "Your answer : "))
    print(Fore.CYAN + "TravelBot : What is the duration of your trip ? (days) :")
    days = input(Fore.YELLOW + "Your answer : ")
    print(Fore.GREEN + f"TravelBot : Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Clothes: Pack according to the weather.")
    print(Fore.GREEN + "- Toiletries: Don't forget your essentials.")
    print(Fore.GREEN + "- Electronics: Chargers, power banks, etc.")
    print(Fore.GREEN + "- Travel documents: Passport, tickets, etc.")
def chat():
    print(Fore.CYAN + "TravelBot : Hello! I'm your travel assistant")
    name = input(Fore.YELLOW + "What is your name? : ")
    print(Fore.GREEN + f"TravelBot : Nice to meet you, {name}!")
    show_help()

    while True:
        user_input=input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        if user_input == "exit":
            print(Fore.GREEN + "TravelBot : Goodbye! Have a great day!")
            break
        elif user_input == "recommendation":
            get_destination_recommendation()
        elif user_input == "joke":
            tell_joke()
        elif user_input == "packing tips":
            packing_tips()
        elif user_input == "help":
            show_help()
        else:
            print(Fore.RED + "TravelBot : I didn't understand that. Please type 'help' for assistance.")
if __name__ == "__main__":
    chat()