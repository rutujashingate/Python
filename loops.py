#WAP to print numbers from 1 to 100 using while loop
i=1
while i<=100:
    print(i)
    i+=1
    
#Numbers from 100 to 1 using while loop
i=100
while i>=1:
    print(i)
    i-=1

#Print multiplication table of number n
n=int(input("enter your number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#Print the elements of following list using loop
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i< len(nums):
    print(nums[i])
    i+=1

#Search for a number x in this tuple using while loop
num=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("Enter your number"))
i=0
while i<len(num):
    if(num[i]==x):
        print("Found at index:",i)
    i+=1

#Print the elements in the follwoing list using For Loop
num=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
for val in num:
    print(val)

#Search for number x in the tuple using for loop
num=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("enter your number"))
i=0
for val in num:
    if(val==x):
        print("Found at indx", i)
    i+=1
    
#Print numbers from 1 to 100 using for & range
for i in range(1,101):
    print(i)    

#Print numbers from 100 to 1 using for & range
for i in range(100,0,-1):
    print(i)

#Print multiplication table of number n
n=int(input("enter your number"))

for i in range(1,11):
    print(n*i)

#WAP to find the sum of first n numbers. (using while)
n=int(input("enter your number:"))
i=1
sum=0
while i<=n:
    sum=i+sum
    i+=1
print(sum)

#WAP to find factorial of first n numbers.(using for loop)
n=int(input("enter your number"))
mul=1

for i in range(1,n+1):
    mul=i*mul
    i+=1
print(mul)    
    
