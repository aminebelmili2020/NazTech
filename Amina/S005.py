import random

opt=["Rock","Paper","Scissors"]
S=0
                    #by:Amine Belmili
p=0
while p < 1:
    opt_U= str(input("Rock (r), Paper (p), Scissors (s)?.. "))
    opt_C= str(random.choice(opt))
    
    if opt_U == "r":
        print("You chose the Rock")
        if opt_C == "Paper":
            print("Computer Chose Paper")
            print("Loser")
            continue
        elif opt_C == "Scissors":
            print("Computer Chose Scissors")
            print("win")
            S += 1
            continue
        elif opt_C == "Rock":
            print("Computer Chose Rock")
            print("equal")
            continue

#**************************************************#by:Amine Belmili

    elif opt_U == "p":
        print("You chose the Paper")
        if opt_C == "Paper":
            print("Computer Chose Paper")
            print("equal")
            continue
        elif opt_C == "Scissors":
            print("Computer Chose Scissors")
            print("Loser")
            continue
        elif opt_C == "Rock":
            print("Computer Chose Rock")
            print("win")
            S += 1
            continue
    
#**************************************************#by:Amine Belmili

    elif opt_U == "s":
        print("You chose the Scissors")
        if opt_C == "Paper":
            print("Computer Chose Paper")
            print("win")
            S += 1
            continue
        elif opt_C == "Scissors":
            print("Computer Chose Scissors")
            print("equal")
            continue
        elif opt_C == "Rock":
            print("Computer Chose Rock")
            print("Loser")
            continue

#**************************************************#by:Amine Belmili
    
    else:
        break

print("Your Score is: " + str(S))

                        #by:Amine Belmili