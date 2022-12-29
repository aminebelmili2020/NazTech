import random

Values = [1, 2, 3, 4, 5, 6]
print("Rolling The Dices...")
print("The Value Are: " + str(random.choice(Values)))
n=0
while n < 1:            #by:Amine Belmili
    ag= str(input("Roll the Dices Again?"))
    if ag=="":
        print("The Value Are: " + str(random.choice(Values)))
    else:
        n += 1