print('Method 1')

def reverse_string(word):
    return word[::-1]

user_input = input('Enter a word : ')
print(f'The reversed string is : ', reverse_string(user_input))

print('')

print('Method 2')

def reverse(word):
    return word[::-1]

while True:
    user_input = input('Enter a word : ')
    if user_input.replace(" ", "").isalpha():       # Allows alphabetic characters and spaces
        print(f'The reversed string is : ', reverse(user_input))
        break
    else:
        print("Invalid input. Please enter letters only (no numbers or special characters).")