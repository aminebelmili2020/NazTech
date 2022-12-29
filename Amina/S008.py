email = str(input("Enter e-mail: "))
a = email.index("@")            
print("Your user name is '{}' and your domain is '{}'".format(email[:a],email[a+1:]))
