def reverse_function(s):
    reverse_str = ''
    i = len(s) -1
    while i>=0:
        reverse_str += s[i]
        i -= 1
    return reverse_str
user_input = input("Enter a string")
print(reverse_function(user_input))
    