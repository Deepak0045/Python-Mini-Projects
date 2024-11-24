print('Method 1: Using a function to check if a single number is prime.')

def is_prime(number):
    if number <= 1:          # Numbers less than or equal to 1 are not prime
        return False
    
    for i in range(2, number):  # Check divisors from 2 to number - 1
        if number % i == 0:
            return False
        
    return True

num = int(input('Enter a number : '))

if is_prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')


print('')


print('Method 2: Checking all prime numbers from 2 to n.')

n = int(input('Enter a number : '))

for i in range(2, n + 1):

    for j in range(2, i):

        if i % j == 0:
            print(i, 'Is Not a prime number')
            break
    
    else:
        print(i, 'Is a prime number')