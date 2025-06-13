def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

user_input = input("Please enter the string")
print(reverse_string(user_input))
