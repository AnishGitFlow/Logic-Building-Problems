# Method 1

def SumOfNaturals(n):

    Sum = 0
    X = 1

    while X <= n:
        Sum = Sum + X
        X = X + 1
    return Sum
    
def main():
    print(SumOfNaturals(10))

if __name__ == "__main__":
    main()


# Method 2
def findsum(n):
    return n * (n + 1) // 2

def main():
    print(findsum(5))

if __name__ == "__main__":
    main()