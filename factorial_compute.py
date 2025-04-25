
def factorial(n):
    """not accepting negative numbers"""
    if n < 0:
        return "error"
    result = 1
    """using the for loop statement"""
    for i in range(1, n + 1):
        result *= i
    return result

"""now testing if it displays """
for i in range(11):
    print(f"Factorial of {i}: {factorial(i)}")