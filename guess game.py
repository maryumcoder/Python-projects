import random

number = random.randint(1, 10)
guess = 0

print("1 se 10 ke beech number guess karo!")

while guess != number:
    guess = int(input("Tumhara guess: "))
    
    if guess < number:
        print("Zyada bada number likho")
    elif guess > number:
        print("Zyada chota number likho")
    else:
        print("Wah! Sahi pakde 🎯")
