#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies=[]
movie1=input("Enter your movie name")
movies.append(movie1)
movie2=input("Enter your movie name")
movies.append(movie2)
movie3=input("Enter your movie name")
movies.append(movie3)
print(movies)

#WAP to check if the list contains palindrome
li=[1,2,3,2,1,4]
copyli=li.copy()
reversecopy= copyli.reverse()
if(li==copyli):
    print("List is Palindrome")
else:
    print("List is not Palindrome")

#WAP to count the number of "a" grade in the following tuple:
tuple=("c","d","a","a","b","b","a")
print(tuple.count("a"))

#Store the above values in list and sort them from "a" to "d"
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)

