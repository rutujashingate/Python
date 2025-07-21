#WAP to input user’s first name & print its length.
name= str(input("Enter your name"))
print(len(name))

#WAP to find the occurrence of ‘$’ in a String.
str="I have 30$ left out of 50$ which means I spent 20$"
print(str.count("$"))

# Grade students based on marks
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade =“D”
marks=int(input("Enter your marks"))
if(marks >= 90):
    print("Grade=A")
elif(90 > marks >= 80):
    print("Grade=B")
elif(80 > marks >= 70):
    print("Grade=c")
else:
    print("Grade=D")

#WAP o check if the number is odd or even
num= int(input("enter your number"))
if(num%2 == 0):
    print("the number is even")
else:
    print("the number is odd")

#WAP to find the greatest of 4 numbers entered by the user.
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("enter number 3:"))
d=int(input("enter number 4:"))

if(a>b and a>c and a>d):
    print("A is greater")
elif(b>c and b>a and b>d):
    print("B is greater")
elif(c>d):
    print("C is greater")
else:
    print("D is Greater")

#WAP to check if the number is Multiple of 7

num= int(input("Enter your number"))

if(num%7==0):
    print("Num is multiple of 7")
else:
    print("Not a multiple of 7")

