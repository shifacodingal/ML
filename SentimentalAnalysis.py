import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN} Welcome to Sentiental Analysis! {Style.RESET_ALL}")
print(f"{Fore.YELLOW} This program will analyze the sentiment of a given text. {Style.RESET_ALL}")
print(f"{Fore.GREEN} Please enter the text you want to analyze: {Style.RESET_ALL}")
Conversation_history = []
print(f"Type{Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN} or {Fore.YELLOW}'exit'{Fore.CYAN} to perform respective actions.")
while True:
    user_input = input(f"{Fore.MAGENTA} You: {Style.RESET_ALL}")
    if user_input.lower() == "exit":
        print(f"{Fore.RED} Exiting the program. Goodbye! {Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        Conversation_history.clear()
        print(f"{Fore.GREEN} Conversation history has been reset. {Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not Conversation_history:
            print(f"{Fore.YELLOW} No conversation history available. {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation history: {Style.RESET_ALL}")
            for i, message in enumerate(Conversation_history, 1):
                print(f"{Fore.MAGENTA} {i}. {message} {Style.RESET_ALL}")
    else:
        Conversation_history.append(user_input)
        analysis = TextBlob(user_input)
        if analysis.sentiment.polarity > 0:
            print(f"{Fore.GREEN} Positive sentiment detected! {Style.RESET_ALL}")
        elif analysis.sentiment.polarity < 0:
            print(f"{Fore.RED} Negative sentiment detected! {Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW} Neutral sentiment detected! {Style.RESET_ALL}")


