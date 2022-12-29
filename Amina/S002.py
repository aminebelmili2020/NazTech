
h= float(input("Enter your height in centimeters : "))
while h==0:
    print("Pleas Try Again, Not Enter Zero ")
    h= float(input("Enter your height in centimeters : "))
    if h != 0: 
        H= h/100
        break
w= float(input("Enter your weight in Kg: "))

BMI = w/(h*h)
print("your Body Mass Index is: " + str(BMI))

if BMI < 19:
    print("You are underweight")
elif BMI <= 24:
    print("normal weight")              #by:Amine Belmili
elif BMI < 30:
    print("stop eating chocolate")
elif BMI < 40:                      
    print("استمر ستشبه الفقمة قريبا")
else:
    print("أنت ديناصور يا صديقي، استمر وستلحق بهم قريبا بإدن الله")
