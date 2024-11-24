# A simple Python program to calculate the factorial of a given number:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is", factorial(num))

#  This Program has some minor flaws 

# 1) The code does not handle cases where the user inputs a negative number.

# 2) If the user enters a non-integer or invalid input (like a string or float), the program will throw an error