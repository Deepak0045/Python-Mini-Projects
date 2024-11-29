# Get input from the user
user_input = input('Enter a word: ')

# Reverse the user input
is_palindrome = user_input[::-1]

# Check if the original input is the same as the reversed string
if user_input == is_palindrome:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
