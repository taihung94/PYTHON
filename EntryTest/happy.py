def HappyNumbers(num):
    def sum_of_squares(n):
        return sum(int(digit) ** 2 for digit in str(n))

    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    
    return num == 1

# Test the function with the provided examples
print(HappyNumbers(1))    # Expected output: true
print(HappyNumbers(101))  # Expected output: false
