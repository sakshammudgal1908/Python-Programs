a=input("enter the number")
a=int(a)                            #typecasting
if(a>10):
    print("number is greater than 10")
else:
    print("number is smaller than or equals to 10 ")


age=input("enter the age")
age=int(age)                        #typecasting
if(age>=18):
    print("person can caste their vote")
else:
    print("person can't caste their vote")


#nested if else
a=input("enter a number between 1-10")
a=int(a)
if(a<5):
    print("number is smaller then 5")
elif(a<10):
    print("number is less then 10")
else:
    print("number is out of range")


#and operator
a=int(input("enter the age"))
if(a>21 and a<60):
    print("u can work with us")
else:
    print("u can't work with us")

#or operator
a=int(input("enter the number"))
if(a>1 or a<18):
    print("he can go to school")
else:
    print("he can go to scollege")
