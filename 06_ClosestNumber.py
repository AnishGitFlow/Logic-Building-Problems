# Find Closest to n and Divisible by m

# Given two integers n and m (m != 0). Find the number closest to n 
# and divisible by m. If there is more than one such number, then 
# output the one having maximum absolute value.

# Input : n = 13, m = 4
# Output : 12

# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.

def closestnum():
    n = int(input("Enter a number: "))
    m = int(input("Enter a divisor: "))

    # Find the closest number to n that is divisible by m
    closest = n - (n % m)
    if (n % m) > (m / 2):
        closest += m

    # If there are two closest numbers, choose the one with maximum absolute value
    if abs(n - closest) == abs(n - (closest - m)):
        closest = closest if abs(closest) > abs(closest - m) else closest - m

    print(closest)

closestnum()