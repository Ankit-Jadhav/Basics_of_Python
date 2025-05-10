# write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.
# Your program should ask whether you want to code or decode.


#Python slicing trick used to reverse a string.
#example : word[::-1] 
# word[start:stop:step]
# start: where the slice starts (default is 0)
# stop: where the slice ends (default is the end of the string)
# step: how many characters to skip

# word[::-1]   ---> start and stop are left empty → use the whole string and step = -1 → move backwards


word = "hello"
reverse_word = word[::-1]
print(reverse_word)

#using list way
word = "AnkitSingh"
char_list = list(word)
print(char_list)

char_list.reverse()
print(char_list)

print(''.join(char_list))


'''''.join(...)

This means: join all items in the list using an empty string as separator.

'' is an empty string → so the characters are joined directly, without spaces or any symbols.'''

#in single line same code

Sentence = "Ankit Jadhav"
print(''.join(reversed(list(Sentence))))


# to remove the space
no_space = Sentence.replace(" ","")
print(no_space)



#secret code language.

import random
import string 

def random_chars(n=3):
    return ''.join(random.choices(string.ascii_letters, k = n))


def code_word(username):
    if len(username)>=3:
        return random_chars() + username[1:] + username[0] + random_chars()
    else:
        return username[::-1]
    
def decode_word(username):
    if len(username)<3:
        return username[::-1]
    else: 
        trimmed = username[3:-3]
        return trimmed[-1] + trimmed[:-1]

def main():
    action = input("Code or decode? ").strip().lower()
    msg = input("Enter a message: ").split()

    if action in ("code","decode"):
        func = code_word if action == "code" else decode_word
        print("Result: ", ' '.join(func(w) for w in msg))
    else:
        print("Invalid Option.")


main()

