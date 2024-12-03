def is_armstrong(number):
    # Convert the number to a string to extract digits
    digits = str(number)
    power = len(digits)  # Number of digits
    total = sum(int(digit) ** power for digit in digits)  # Sum of powered digits
    return total == number  # Check if the number is equal to the sum

# Test the function
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
