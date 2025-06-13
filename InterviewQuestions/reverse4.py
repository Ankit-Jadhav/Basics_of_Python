def reverse_string(s):
    return s[::-1]
def main():
    try: 
        user_input = input("Please enter the alphabate: ")
        
        if not user_input.isalpha():
            raise ValueError("please enter alphabate character")
        
        reverse = reverse_string(user_input)
        print(reverse)
        
    except ValueError as ve:
        print ("ValueError: ", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
        
if __name__ =="__main__":
    main()