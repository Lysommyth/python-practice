def sum_of_digits(n):
    """Computes the sum of digits in a number using modulus and integer division.
    This helps extract each digit one by one and adds them to a total.
    """
    total = 0
    while n > 0:
        # Extract the last digit and add to total
        total += n % 10
        # Remove the last digit
        n //= 10
    return total  # Return total after all digits processed

# I will use a for loop to compute digit sums of numbers from 23 to 29
for number in range(23, 30):  # range goes up to 29 inclusive
    result = sum_of_digits(number)
    print(f"Sum of digits of {number} is {result}")
