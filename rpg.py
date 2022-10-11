name = input("Type your character name:  ")
print("Welcome", name, "to your adventure!")



def pathing():
    answer = input("You are on a dirt road, the road ends into a T-split. 2 ways too go, do you take left or right?: ").lower()

        #left
    if answer == "left":
        answer = input("You arrive at a river, do you swim through it or walk around? Type either swim or walk: ")
        
        
        if answer == "swim":
            print("You tried to swim across the river and got eaten by a crocodile")
        elif answer == "walk":
            print("You decided to look for a way around and after a long search you found a crossing")
            answer = input("It's nearing nightfall do you cross and setup camp or camp on this side. Cross or camp: ")
            
            if answer == "cross":
                print("While setting up a fire you notice some strange noises")
            elif answer == "camp":
                print("You setup camp and start a fire")
                
            
        #right
    elif answer == "right":
        print()

    else:
        print("Not a valid option. Try again!")
    