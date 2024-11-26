print('Method 1')
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = 15  
print(fibonacci(n))


print('method 2')

def fibonacci(num):

    a, b = 0, 1

    for _ in range(num):
        print(a, end = ' ')
        a, b = b , a + b

num = int(input('Enter the number of fibonaaci : '))
fibonacci(num)