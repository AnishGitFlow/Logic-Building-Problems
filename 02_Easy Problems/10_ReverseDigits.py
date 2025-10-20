# Write a program to reverse digits of a number

# Given an Integer n, find the reverse of its digits.

# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.

def reverse():
    num = str(input("Enter a number : "))
    rev = int(num[::-1])
    print(rev)
    
reverse()
