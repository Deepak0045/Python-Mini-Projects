# Method 1


num = int(input('Enter a number : '))

def factorial(n):
    if n < 0:
        return 'Not Valid'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f'The factorial of {num} is', factorial(num))

# although it handles negetive numbers but throws an error if input is string to resolve that issue we have method 2

# Method 2



def factorial(n):
    if n < 0:
        return 'Not Valid'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    try:
        num = int(input('Enter a number : '))
        break    # Exit loop if input is valid
    
    except ValueError:
        print('Invalid input, Enter an integer')


print(f'The factorial of {num} is', factorial(num))
