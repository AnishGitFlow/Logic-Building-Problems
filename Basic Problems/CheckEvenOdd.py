def CheckEvenOdd(n):
    
    rem = n % 2
    if rem == 0:
        return True
    else:
        return False
    
def main():
    print(CheckEvenOdd(8))
    print(CheckEvenOdd(45))

if __name__ == "__main__":
    main()