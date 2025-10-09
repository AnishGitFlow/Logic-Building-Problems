# Swap Two Numbers

# Given two numbers a and b, the task is to swap them.

# Input : a = 2, b = 3
# Output : a = 3, b = 2

def SwapNum():
    a,b = 2,3
    temp = a
    a = b
    b = temp
    print("a =", a, " b =", b)

def main():
    SwapNum()

if __name__ == "__main__":
    main()

# Second Approach

def SwapNum():
    a,b = 2,3
    a,b = b,a
    print("a =", a, " b =", b)

def main():
    SwapNum()

if __name__ == "__main__":
    main()