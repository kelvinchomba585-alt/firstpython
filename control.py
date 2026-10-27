# a python program that checks if someone is eligible to vote or not

age = int(input("Enter your age"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You cant vote.. Underage")

# pragram that check whether a number is old or even
num = int(input("Enter a number"))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is old")

# create a program that checks biggest in 3 numbers
num1, num2, num3 = map(int, input("Enter 3 numbers separated by spaces: ").split())
if num1 > num2 and num1 > num3:
    print("Num1 is biggest")
elif num2 > num1 and num2 > num3:
    print("Num2 is biggest")
elif num3 > num2 and num3 > num1:
    print("Num3 is biggest")
elif num3 == num2 and num3 > num1:
    print("Num3 and num2 are biggest")
elif num3 == num1 and num3 > num2:
    print("Num3 and num1 are biggest")  
elif num2 == num1 and num2 > num3:
    print("Num1 and num2 are biggest")
else:
    print("All numbers are equal")