numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def even_odd_check(num):
    """it devides the number by 2
    and if there is no remainder it dispays even if theres a remainder it displays odd"""
    return "even"if num % 2 == 0 else "odd"
"""using for loop to pass through the list and to display if its odd or even """
for n in numbers:
    print(f"{n} is {even_odd_check(n)}")