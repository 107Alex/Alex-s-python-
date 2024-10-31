# first drafting 
import random

def main():
    init_chances = 7
    L = set_lower_bnd()
    U = set_Upper_bnd()
    randomNum = generate_random_no(str(L), str(U))
    display_initial_No_of_guesses(init_chances)
    start_guessing(init_chances, randomNum)

def set_lower_bnd():
    set_low = input("Enter Lower bound: ")
    return set_low

def set_Upper_bnd():
    set_high = input("Enter Upper Bound: ")
    return set_high

def display_initial_No_of_guesses(init_chances):
    Fstring = f"""
        You've only {init_chances} to guess the integer!
                """
    print(Fstring)

def generate_random_no(lower, upper):
    r = random.randint(int(lower), int(upper))
    return r

def provide_input():
    gussing_No = input("Guess a number:")
    return gussing_No

def compare_random_guessingNo(gussing_No, randomNum, count):
    if gussing_No != randomNum:
        if gussing_No > randomNum:
            print("you guessed too high")
        elif gussing_No < randomNum:
                print("you guess too low")
        return False
    else:
        fstring = f"Congratulation you did it in {count} try"
        print(fstring)
        return True

def validate_chances(count,init_chances):
    if count >= init_chances:
        print("Game Over!!")
        return False
    else:
        return True
    
def start_guessing(init_chances, randomNum):
    count = 1
    life = True
    guess_right = False
    while life == True:
        while guess_right == False and life == True:
            gussing_No = int(provide_input())
            guess_right = compare_random_guessingNo(gussing_No, randomNum, count)
            life = validate_chances(count, init_chances)
            count += 1
        
            
        
    

main()