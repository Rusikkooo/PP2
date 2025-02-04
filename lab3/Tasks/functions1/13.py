import random
def game():
    print("Hello! What is your name?")
    x = input()
    cnt = 0 
    r = random.randint(1,20) 
    print(f"Well, {x} ,I am thinking of a number between 1 and 20.")
    while True:
        print("Take a guess.")
        number = int(input())
        if r > number:
            print("Your guess is too low.")
            cnt+=1
        if r < number:
            print("Your guess is too high.")
            cnt+=1
        if r == number :
            cnt+=1
            print(f"Good job, {x} You guessed my number in {cnt} guesses!")
            break
game()