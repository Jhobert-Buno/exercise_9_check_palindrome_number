# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

def palindrome (number):
    print('The given number is: ', number)
    original_number = str(number)

    reverse_number = original_number[::-1]
    if original_number == reverse_number:
        print("Yes. The number is a palindrome number")

    else:
        print("No. The number is not a palindrome number")

# given/example
print("Given:")
given_1 = 121
given_2 = 125

palindrome(given_1)
print('')
palindrome(given_2)

#ask user input
print('')
inputted_number = input("Input a number: ")
palindrome(inputted_number)