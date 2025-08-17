# Using For loop

def Multiplication(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

def main():
    Multiplication(5)

if __name__ == "__main__":
    main()

# Using while loop

def Multiplication(n):
    i = 0
    while i < 10:
        i += 1
        print(f"{n} * {i} = {n*i}")

def main():
    Multiplication(5)

if __name__ == "__main__":
    main()