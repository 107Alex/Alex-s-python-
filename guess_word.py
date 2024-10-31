import random

words = ["apple", "boy", "cat", "dog", "english"]

def generate_ramdom_word():
    ramdom_w = random.choice(words)
    return ramdom_w

def store_name():
    playerName = input("What is your name? ")
    print(f"hi {playerName}, Good luck.....")

def input_guessing():
    guessing = input("What is your guess? ")
    return guessing

def greetings():
    fString = f"Hello ....."
    print(fString)

def validate_guessing_word(R_W, guessing):
    if R_W == guessing:
        print("Contgrastes you are correct")
        return True
    else: 
        print("Try again")
        return False

def main():
    greetings()
    store_name()
    R_W = generate_ramdom_word()
    valid = False
    while valid == False:
        guessing = input_guessing()
        valid = validate_guessing_word(R_W, guessing)

main()


    