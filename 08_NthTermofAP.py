# Nth term of AP from First Two Terms
# Given two integers a1 and a2, the first and second terms of an Arithmetic 
# Series respectively, the problem is to find the nth term of the series. 

# Input : a1 = 2,  a2 = 3,  n = 4
# Output : 5
# Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

# Input : a1 = 1, a2 = 3, n = 10
# Output : 19
# Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.

def AP():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))

    nth_term = int(input("Enter a nth term : "))

    print(f"{num1 + (nth_term - 1) * (num2 - num1)}")
    
def main():
    AP()

if __name__ == "__main__":
    main()