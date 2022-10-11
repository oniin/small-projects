import random

top_range = input("Type a number:  ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()
    
    
rand = random.randrange(0, top_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess:  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == rand:
        print("You got it!")
        break
    elif user_guess > rand:
        print("You are above the number")
    else:
        print("you are below the number")
        
print("You got it in", guesses, "guesses")