# Name: Seth Pearson 
# Date: October 26, 2026

print("Hello, Ai.")

from datetime import datetime

current_hour = datetime.now().hour

if current_hour < 12:
    time_of_day = "morning"
elif current_hour < 17:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"


print(f"It is currently {time_of_day}.")
mood = input("How are you feeling today? ").lower()

if "happy" in mood or "good" in mood:
    print("That is great")
elif "bad" in mood or "down" in mood:
    print("I'm sorry you're feeling that way. I hope things get better.")
elif "tired" in mood or "sleepy" in mood:
    print("Remember to take get rest.")
elif "excited" in mood:
    print("That's wonderful hope you have a good rest of your day.")


# AI facts
print("\nHere are some AI facts:")
print("1.AI started in 1950.")
print("2.The Term AI is 70 years old.")
