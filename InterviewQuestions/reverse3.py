def reverse_string(s):
    return s[::-1]
def main():
    user_input = input("Please enter the string only: ")
    reverse = reverse_string(user_input)
    print("Reverse word will be : ", reverse)

if __name__ == "__main__":
    main();