print("Hellow ! I am AI Bot. Can i get to know your name ? ")
name = input()
print(f"Nice to meet you {name}!")
print("How are you feeling Today ? (good/bad)")
mood = input().lower()
if mood == "good":
    print("That's great to hear! I'm glad you're feeling good.")
elif mood == "bad":
    print("I'm sorry to hear that. If you want to talk about it, I'm here to listen.")
else:
    print("I see ! Sometimes we have mixed feelings. It's okay to feel that way.")
print("It was a nice chatting with you!")