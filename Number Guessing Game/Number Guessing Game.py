import random

def guss(answer, num):

    if num == answer:
        return False
    if num > answer:
        print("Try Again! You guessed TOO HIGH")
        return True
    if num < answer:
        print("Try Again! You guessed too small")
        return True
    
    return
    

def play():

    print("Welcome To The Number Guessing Game!!")
    print("Please Enter a Range to Start -> ")

    try:
        Lower = int(input("\nEnter the Lower Bound of the Range : "))
        Upper = int(input("Enter the Upper Bound of the Range : "))

    except ValueError:
        print("Enter a Valid Range")
        print("Lets Try it Again...")
        play()

    # Generating a Random Number from the given range
    Random_number = random.randrange(Lower, Upper)

    print("\nAlright! Now Try Guessing The Number ->")
    
    attempts = 0
    answer = True

    while answer:

        attempts += 1

        # Helping Hand
        if attempts >= 10:
            print("\nLooks like you are having a hard time guessing the number ")
            print("Do you Need a hint (-_-)")

            choice = input("\nEnter y or n -> ")

            if choice.lower() == 'y':
                print("Lets narrow down your search area, ")
                mid = (Upper + Lower) // 2
                if mid > Random_number:
                    print("Your Number is Greater than", mid)
                if mid < Random_number:
                    print("Your Number is Less than", mid)
                if mid == Random_number:
                    print("Your Number is around", mid)
                    
            if choice.lower() == 'n':
                print("Thats the spirit bro -> KEEP GOING (*-*)")


        num = int(input("\nGuss the Number -> "))

        if num not in range(Lower, Upper):
            print(f"Error InputOutOfRange, Enter a number that is in the Given Range({Lower}, {Upper})...")
            continue
        
        answer = guss(Random_number, num)

    print("\nCongratulations!! You Have Guessed The Number Correctly")
    print(f"Total Number of Guesses = {attempts}")

def ask():
   
    ans = input("Enter y or n -> ")

    if ans.lower() == 'y':
        play()
    if ans.lower() == 'n':
        print("Are you Sure?")
        print("It is a Fun game Though, I think you should gave it a try")
        ask()
    if ans.lower() != 'y' and ans.lower() != 'n':
        print("pls play it sincerely\n")
        ask()
    
    
print("wanna play a game?")
ask()

        




