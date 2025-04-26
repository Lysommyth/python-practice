def factorial_recursive(n):
    """Computes the factorial of a number using recursion.
     Handles negative inputs by returning an error message.
     """
    if n<0:  #theres no factorial for a negative number
        return "error no factorial for negatives"
    if n==0 or n==1:
        #use of a base case
        return 1
    #recursive case
    return n*factorial_recursive(n-1)

# Using a for loop to print factorials of numbers from 0 to 9

for i in range(10):
    print(f"Factorial of {i}: {factorial_recursive(i)}")