# Check Even or Odd

# Given a number n, check whether it is even or odd. 
# Return true for even and false for odd

"""
Input = 15
Output = False
Explanation = 15 % 2 = 1, so 15 is odd

"""

def even_odd():
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

def main():
    even_odd()

if __name__ == "__main__":
    main()