# Ex01   | Write a program that prints the numbers from 1 to 100
# n=0 
# while n <= 100:   print(n)          #AMiNE BELMILI
#   n += 1                      
# ***************MUNIR*******************
# for i in range(1,101,1): print(i)
# *****************************************************************

# Ex02   | Write a program that prints the numbers from 100 to 1
# for i in range(100,0,-1): print(i)


# EX03   | Write a program that prints the even numbers from 2 to 100
# for i in range(2,101,2): print(i)

# Ex04   | Write a program that prints the odd numbers from 1 to 100
# for i in range(1,101,2): print(i)

# Ex05   | Write a program that prints the multiples of 5 from 5 to 100
# for i in range(5,101,5): print(i)

# Ex06   | Write a program that prints the square of the numbers from 1 to 10
# for i in range(5,11): 
#     print(i**2)

# Ex07   | Write a program that calculates the sum of the numbers from 1 to 100
# sum=0
# for i in range(1,101):
#     sum +=1
# print(sum)

# Ex08   | Write a program that calculates the average of the numbers from 1 to 100
# sum=0
# for i in range(1,101): sum +=1
# print(int(sum/100))

# Ex09   | Write a program that calculates the factorial of a number
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# number=int(input("Enter a Positive integer: "))
# result=factorial(number)
# print("The factorial of ", number, "is ",result)

# Ex10   | Write a program that calculates the Fibonacci sequence
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(int(input("enter: "))))

# Ex11   | Write a program that checks if a number is prime
# def prime(n):
#     if n<=1:
#         return False
#     for i in range (2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# print(prime(20))

# Ex12   | Write a program that generates a random number between 1 and 100.
# import random
# print(random.choice(range(1,100)))

# Ex13   | Write a program that generates a list of random numbers between 1 and 100.
# list= []
# for n in range(1,101):list.append(n)
# print(list)

# Ex14   | Write a program that sorts a list of numbers in ascending order.
# list = [7,3,1,5,10]
# list.sort()
# print(list)

# Ex15   | Write a program that sorts a list of numbers in descending order.
# list = [7,3,1,5,10]
# list.sort(reverse=True)
# print(list)

# Ex16   | Write a program that finds the maximum number in a list.
# list = [7,3,1,5,10]
# list.sort()
# print(list[-1])

# Ex17   | Write a program that finds the minimum number in a list.
# list = [7,3,1,5,10]
# list.sort()
# print(list[0])

# Ex18   | Write a program that calculates the mean of a list of numbers. (حساب المتوسط)
# list = [7,3,1,5,10]
# s = sum(list)/len(list)
# print(s)

# Ex19   | Write a program that calculates the median of a list of numbers. (حساب الوسيط)
# list = [7,3,1,5,10,15]
# list.sort()
# l=len(list)
# if(l % 2 != 0):
#     print(list)
#     print("the median of a list of numbers is: ", list[int(l/2)])
# else:
#     print(list)
#     print("the median of a list of numbers is: ", list[int(l/2)], " and ", list[int(l/2)-1])
    
# Ex20   | 


# Ex21   | Write a program that converts a number from decimal to binary.
# d= int(input("Enter Number Decimal: "))
# b= ""
# while d > 0:
#     b= str(d%2) + b
#     d= d // 2
# print(b)

# Ex21   | Write a program that converts a number from binary to decimal XXX
# b=[*input("Enter Number Decimal: ")]
# f=0

# for x in b:
#     while f <= len(b):
#         print(x,f)
#         f +=1
#         if f == len(b)-1: break

# Ex27   | Write a program that reverses a string.
# st="hello"
# print(st[::-1])

# Ex28   | Write a program that finds the length of a string.
# txt="hello"
# print(len(txt))

# Ex29   | Write a program that finds the number of vowels in a string.
# list = ["a","b","c","d","e","f","i","g","k"]
# v = ["a","o","e","i","y","u"]
# for x in v:
#     if x in list:
#         print(list.index(x))
        
# Ex30   | Write a program that finds the number of consonants in a string
# list = ["a","b","c","d","e","f","i","g","k"]
# v = ["a","o","e","i","y","u"]
# for x in v:
#     if x in list:
#         list.remove(x)
# print(list)

# Ex31   | Write a program that finds the number of words in a string
text = "hello amine"
w=1
s= text.lstrip()
for x in text:
    if s == " ":
        w +=1
print(w)

# Ex31   |   Write a program that finds the number of characters in a string. 
# text = "hello"
# print (len(text))

# Write a program that finds the number of characters in a string