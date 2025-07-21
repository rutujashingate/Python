#Store the following word meanings in python dictionary: table:"a piece of furniture","list of facts & figures" cat:"a small animal"
dict={
    "table": ("a piece of furniture","list of facts & figures"),
    "cat":"a small animal"
    }

print(dict)

#You are given a list of subjects for students. Assume one classroom is required for 1subject. How many classrooms are needed by all students.”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
dict={}

marks1=int(input("Enter youd marks for physics"))
dict.update({"physics":marks1})

marks1=int(input("Enter youd marks for maths"))
dict.update({"maths":marks1})

marks1=int(input("Enter youd marks for chem"))
dict.update({"chem":marks1})

print(dict)

# Initialize an empty dictionary
marks_dict = {}

# Take input for each subject and add to dictionary
subject1 = input("Enter name of subject 1: ")
marks1 = float(input(f"Enter marks for {subject1}: "))
marks_dict[subject1] = marks1

subject2 = input("Enter name of subject 2: ")
marks2 = float(input(f"Enter marks for {subject2}: "))
marks_dict[subject2] = marks2

subject3 = input("Enter name of subject 3: ")
marks3 = float(input(f"Enter marks for {subject3}: "))
marks_dict[subject3] = marks3

#Print the dictionary
print("\nMarks Dictionary:")
print(marks_dict)

#Figure out a way to store 9 & 9.0 as separate values in the set.(Can use built in data types)
set={9,"9.0"}
print(set)
set2={("float",9.0),("int",9)}
print(set2)

