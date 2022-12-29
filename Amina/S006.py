from random import choice
                            #Amine Belmili
def genePass(n):
    password = ''
    letters= '0123456789abcdefjhigklmnopqurstvwxyz'
    for i in range(n):
        password += choice(letters) 
    return password

print(genePass(int(input("Enter The Lenght Password: "))))