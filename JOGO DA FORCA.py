import random
import math

print("Guess the word. Choose a letter.")

word_list = ["camel", "koala", "zebra", "toy", "lion", "fish"]
canswer = 0
lives = 5
wanswer = 0

cword = word_list[random.randint(len(word_list) - 1)]
slots = []

for slot in range(len(cword)):
    slots.append("_")

print(slots)
while canswer < len(cword) and lives >= 1:
    pletter = input("Choose a letter on the alphabet: ")
    wanswer = 0
    for i in range(len(cword)):
        if cword[i] == pletter:
            slots[i] = pletter
            canswer = canswer + 1
            wanswer = wanswer - canswer
        else:
            wanswer = wanswer + 1
            print(i)
            print(wanswer)
            if i == (len(cword) - 1):
                if wanswer >= (len(cword) - canswer):
                    print("WRONG!!!")
                    lives = lives - 1
                    print(f"YOU LOST 1 LIFE. NOW YOU ONLY HAVE {lives} lives.")
                    print("DONT DIE!!!")
    for display in range(len(slots)):
        print(slots[display])
if canswer == len(cword):
    print("Congratulations, you pass the game!")
else:
    print("YOU DIED.")