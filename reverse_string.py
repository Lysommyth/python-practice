def reverse_string(string):
    """Start with an empty string"""
    reverse_str = ''
    for char in string:
        reverse_str = char + reverse_str
    return reverse_str

if __name__ == '__main__':
    """our input"""
    original_string = input("enter string value")
    #Call the function
    reverse_output = reverse_string(original_string)
    print("Original string:", original_string)
    print("Reversed string:", reverse_output)