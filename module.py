import math
a=math.sqrt(36)
print (a)


print("""Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.""")


#problem 2 : Print the table of 5
for i in range(1,11):
    print (f"{i} * 5 =" ,i * 5)



import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text ,what will you speak?")
engine.runAndWait()


marks=[]
f1=int(input("Enter the marks:"))
marks.append(f1)
f2=int(input("Enter the marks:"))
marks.append(f2)
f3=int(input("Enter the marks:"))
marks.append(f3)
f4=int(input("Enter the marks:"))
marks.append(f4)
f5=int(input("Enter the marks:"))
marks.append(f5)
f6=int(input("Enter the marks:"))
marks.append(f6)
f7=int(input("Enter the marks:"))
marks.append(f7)

marks.sort()
print(marks)
