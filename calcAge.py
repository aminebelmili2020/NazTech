import datetime

yearOfBirth= int(input("please Enter Year Of Bith: "))
year= int(datetime.datetime.now().strftime("%Y"))
print(year-yearOfBirth)