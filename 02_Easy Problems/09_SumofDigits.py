# Sum of Digits of a Number

# Given a number n, find the sum of its digits.

# Input: n = 687
# Output: 21

def SumDigit():
    num = input("Enter your number : ")

    sum = 0
    for ch in num:
        sum += int(ch)

    print(sum)

def main():
    SumDigit()

if __name__ == "__main__":
    main()
    