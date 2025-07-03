"""#multiplication table number using for loop
n= int(input("Enter the number "))

for i in range(1,11):
    print(f"{n} X {i} =",n * i)

#write a program to greet people with the names starting from S in the list
l=['Ramesh','Suresh','Sameer','Raju','Ajay','Savita']

for name in l:
    if (name.startswith('S')):
        print(f"Hello {name}"  )

#multiplication table number using while loop

n= int(input("Enter the number "))
i=1
while (i< 11):
    print(f"{n} X {i} = {n*i}")
    i= i+1
    

#to find the prime num
n = int(input("Enter the number :"))

for i in range(2,n):
    if (n%i == 0):
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")


#sum of natural numbers using while loop
n = int(input("Enter the number :"))
sum = 0
i=1
while (i<= n):
    sum = sum + i
    i=i+1

print("The sum of natural numbers are ",sum)
   
#factorial of number
#5!=5*4*3*2*1
n = int(input("Enter the number :"))
product = 1
for i in range(1,n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

#print the pattern
n = int(input("Enter the number:"))

for i in range(1,n+1):
    print(" " * (n-i),end='')
    print("*" * (2*i-1),end='')
    print( )
 """
"""Write a program to print the following star pattern:
*
**
*** for n = 3
""" 
"""  
n = int(input("Enter the number:"))

for i in range(1,n+1):
    # print("* " * n, end='' )
    print("*"*i, end='')
    print()

Write a program to print the following star pattern.
* * *
* * for n = 3
* * *  
m = int(input("Enter the number:"))

for i in range(1,m+1):
    if (i==1 or i==m):
        print('*'*m,end='')
    else:
        print("*",end='')
        print(" "*(m-2),end='')
        print("*",end='')
    print()
""" 
# Write a program to print multiplication table of n using for loops in reversed order
n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)} ")