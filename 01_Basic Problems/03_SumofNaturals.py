# Program of Sum of n natural numbers

# Given a positive integer n, find the sum of the first n natural numbers.

"""
Input : 3
Output : 6
Explanation : 1 + 2 + 3 = 6
"""

def sum():
    num = int(input("Enter a number : "))

    sum = 0
    i = 1

    while i<=num:
        sum = sum + i
        i = i + 1
    print(f"Sum of {num} natural numbers are : {sum}")

def main():
    sum()

if __name__ == "__main__":
    main()

# Second Approach

# Formula : (n*(n+1)) / 2

def sumofnumbers():
    n = int(input("Enter a number : "))

    sum = (n*(n+1)) // 2
    print(f"Sum of {n} natural numbers are : {sum}")

def main():
    sumofnumbers()

if __name__ == "__main__":
    main()
