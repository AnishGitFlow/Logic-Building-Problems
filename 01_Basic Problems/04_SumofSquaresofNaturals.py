# Program for Sum of squares of first n natural numbers

# Given a positive integer n, we have to find the sum of squares of first n natural numbers

"""
Input : 2
Output : 5
Explanation : 1^2+2^2 = 5
"""

def sumofsquares():
    num = int(input("Enter a number : "))

    sum = 0
    i = 1

    while i<=num:
        sum = sum + (i**2)
        i = i + 1
    print(f"The sum of squares of first {num} numbers is : {sum}")

def main():
    sumofsquares()

if __name__ == "__main__":
    main()

# Second Approach

def squarenaturals():
    n = int(input("Enter a number : "))

    sum = (n*(n+1)*(2*n+1)) / 6
    print(f"The sum of squares of first {n} numbers is : {sum}")

def main():
    sumofsquares()

if __name__ == "__main__":
    main()