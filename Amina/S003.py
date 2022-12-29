S = 0
Q1 = 0
while Q1 <= 3:
    Answer= str(input("which bear lives at the North pole? ").lower())
    if Answer == "polar bear":
        print("Correct :) ")
        S += 1
        break
    else:
        print("Sorry Wrong Answer," "is Not \"" + Answer + "\" ,try again " )
        if Q1==2:
            print("The Correct answer is Polar Bear")
            break
        else:
            Q1 += 1
Q2 = 0
while Q2 <= 3:
    Answer= str(input("Which is the fastest land animal?").lower())
    if Answer == "cheetah":
        print("Correct :) ")
        S += 1
        break
    else:
        print("Sorry Wrong Answer," "is Not \"" + Answer + "\" ,try again " )
        if Q2==2:
            print("The Correct answer is Cheetah")
            break
        else:
            Q2 += 1
Q3 = 0      
while Q3 <= 3:
    Answer= str(input("Which is the larget animal?").lower())
    if Answer == "blue whale":
        print("Correct :) ")
        S += 1
        break                           
    else:
        print("Sorry Wrong Answer," "is Not \"" + Answer + "\" ,try again " )
        if Q3==2:
            print("The Correct answer is Blue Whale")
            break
        else:
            Q3 += 1
print("Your Score is: " + str(S))