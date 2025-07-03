#find the greatest of 4 numbers
"""
a1 = int(input("Enter the number a1:"))
a2 = int(input("Enter the number a2:"))
a3 = int(input("Enter the number a3:"))
a4 = int(input("Enter the number a4:"))

#find the greatest of the 4 numbers
if (a1 > a2 and a2 > a3 and a3 > a4):
    print("greatest number is ",a1)

elif (a2 > a1 and a2 > a3 and a2 > a4):
    print("greatest number is ",a2)

elif (a3 > a1 and a3 > a2 and a3 > a4):
    print("greatest number is ",a3)

elif (a4 > a2 and a4 > a3 and a4 > a1):
    print("greatest number is ",a4)


#find the students who have passed with minimum 40% and individually scored 33% individually in each subject

marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))

#find the percentage of all 3 subjects
total_percentage=((marks1 + marks2 + marks3)/300) *100

if (total_percentage > 40 and marks1>33 and marks2 > 33 and marks3 > 33):
    print("You have passed ",total_percentage)

else:
    print("You have failed,please try again next year",total_percentage)


post = input("Enter the post: ")

if ("harry" in post.lower()):
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")
 
 
 #find the name in the list   
l=['Harry','Happy','Lovely','Barbie']
name = input("Enter your name ")

if (name in l):
    print("Your name is in the list ", name)

else:
    print("Your name is not in the list ", name)
  

#find whether the message is spam or not
a1='Make a lot of money'
a2='buy now'
a3='subscribe this'
a4='click this'

message=input("Enter your message ")

if ((a1 in message) or (a2 in message) or (a3 in message) or (a4 in message)):
    print("This message is spam")

else:
   print("This message is not spam")
 
 #to check the length of username
username = input("Enter username ")

if (len(username)<10):
    print("Username is less than 10 characters")

else:
    print("All is well")

#in used in python
l=['Harry','Shubham','Divya','Vidya']

name = input("Enter your name :")

if (name in l):
    print("Your name is in the list")
else:
   print("Your name is not in the list") 
   
#write program to find the grade of student

marks=int(input("Enter your marks "))

if (marks<= 100 and marks >=90):
    grade="Ex"
elif (marks< 90 and marks >=80):
    grade="A"
elif (marks< 80 and marks >=70):
    grade="B"
elif (marks< 70 and marks >=60):
    grade="C"
elif (marks< 60 and marks >=50):
    grade="D"
else:
    grade="F"  
print("Your grade is ",grade) 

#while loops 
i= 1
while i<6:
    print(i)
    i = i + 1
"""

#while loops in list
l=[1,3,'Night owl','Papita',3.14,False,'Prita']

i = 0
while (i< len(l)):
    print(l[i])
    i= i + 1