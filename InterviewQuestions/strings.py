#✅ Que1: Shift all zeroes or any char to the end
s = "a0b0cd0e"
non_zeroes= [x for x in s if x != '0']
zeros = [ x for x in s if x == '0']
print(zeros)
print(non_zeroes)
print(''.join(zeros+non_zeroes))

#✅ Que2: Rotate string right from a character
s = "pythonrocks"
#rotate from r
index = s.index('r')

#Que3: Calculate index of every char in string
s = "Ankit Jadhav"
for index,char in enumerate(s):
    print(index , char)

#Que 4 : Frequnecy of every character using Counter
from collections import Counter
s = "Programming Test"
frequency = Counter(s)
print(frequency)
a = { char : count for char , count in frequency.items() if count > 1}
print(a)

#Que 5 : Frequnecy of every character using enumerate
s = "Programming Test"
count_dict = {}

for i, char in enumerate(s):
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)

duplicates = {char: count for char, count in count_dict.items() if count > 1}
print(duplicates)

#Que 6 :  Count duplicate characters using a basic for loop
s = "Programming Test"
count_dict = {}

for char in s:
    if char in count_dict:
        count_dict[char] +=1
    else:
        count_dict[char] = 1 
print(count_dict)

duplicates = {}
for char in count_dict:
    if count_dict[char] > 1:
        duplicates[char] = count_dict[char]
print(duplicates)

#Que 7 : String reverse without space change but char change.
name = "Ankit Jadhav Test"

# Step 1: Store positions of spaces
space_indices = [i for i, char in enumerate(name) if char == ' ']

# Step 2: Remove spaces and reverse the characters
chars = [char for char in name if char != " "]
reversed_chars = chars[::-1]  # reversed copy

# ✅ Step 3: Insert spaces in reverse order
for i in space_indices:
    reversed_chars.insert(i, " ")

# Step 4: Join the result
result = "".join(reversed_chars)
print(result)

#Que 8 : reverse the words in descending order
name = "Ankit Jadhav Test"
words = name.split()
reverse_word = words[::-1]
result = " ".join(reverse_word)
print(result)


#Que 9 : reverse string fully
name = "Ankit Jadhav Test"
print(name[::-1])

#Que10 : Unique and duplicate characters
s = "aabccd"
unique , duplicate = [] , []

for x in s:
    if x not in unique and x not in duplicate:
        unique.append(x)
    elif x in unique:
        unique.remove(x)
        duplicate.append(x)
print(unique , duplicate)

#Que11: Remove any char with use of index
s = "Ankit Jadhav"
index = 5
print(s[:index] + s[index+1:])

#Que12 : remove any char with use of letter - first char
n = "Ankit Jadhav"
char_remove = "a"
result = n.replace("a", "",1)
print(result)

#Que13: Remove all occurence of any letter
n = "Ankit Jadhav"
char_remove = "a"
result = n.replace("a", "")
print(result)

#Que14 : Remove multiple or specific characters using a loop
n = "Ankit Jadhav"
char_remove = ["A" , "J"]
result = [x for x in n if x not in char_remove]
print("".join(result))

#Que15 :  Unique, duplicates, and frequency
from collections import Counter
s = "aabccddee"
counter1 = Counter(s)
print(dict(counter1))
print([ key1 for key1,index1 in counter1.items() if index1 == 1])
print([ key1 for key1, index1 in counter1.items() if index1 > 1])

#Que16. Built in functions and methods

#Que17: Use of count()
s = "aabccddee"
print(s.count('a'))

#Que18: Index of all occurrences
s = "abracadabra"
char = 'a'
indices = [i for i, ch in enumerate(s) if ch == char]
print(indices)

#Que19:  Insert character at specific position
s = "hello"
s = s[:2] + "Z" + s[2:]
print(s)  # heZllo

#Que20: Swap of first and last digit
s = "python"
s = s[-1] + s[1:-1] + s[0]
print(s)

#Que21: Palindrome
s = "aba"
print("Palindrome" if s == s[::-1] else "False")

#Que23: Replace vowels with dollar in sentence
str = "Ankit Jadhav"
vowels = "aeiouAEIOU"
result = " "

for x in str:
    if x in vowels:
        result = result + "$"
    else : 
        result = result + x
print(result)
         

#Que24: Replace consonet with dollar
str = "Ankit Jadhav"
vowels = "aeiouAEIOU"
result = " "

for x in str:
    if x not in vowels:
        result = result + "$"
    else : 
        result = result + x
print(result)
         
#Que25: Anagram - they contain the same characters with the same frequency, but possibly in a different order.
str1 = "listen"
str2 = "Slient"
str3 = "ABC"

#using sorting 
x = ["Anagram" if sorted(str1.lower()) == sorted(str2.lower()) else "Not an Anagram"]
print(x)

# using Counter
from collections import Counter
y = ["Anagram" if Counter(str1.lower()) == Counter(str2.lower()) else "Not an Anagram"]
print(y)

#Que26 : pop() equivalent in string - -String is immutable
s = "banana"
print(s[:-1])           # Remove last char
print(s[:4] + s[5:])    # Remove index 4 char


#Que26: Print string as dict (char-frequency)
s = "Ankit Jadhav"
print(s.lower())
s=s.replace(" ", "")
print(s)
from collections import Counter
print(s[0])
dict1 = (dict(Counter(s)))
print(dict1)
print(dict1.items())
print(dict1.keys())
print(dict1.values())

#Que27: index of char
s = "Ankit Jadhav"
print(s.index('a'))

#Que28: Descending sort -- replace, lower , sort , rever , join
s = "Ankit Jadhav"
s = (s.replace(" ", "")).lower()
print("".join(sorted(s, reverse = True)))

#Que29 :Given two strings, check if they contain the same characters, regardless of order and frequency.
s1 = set("aabb1cc")
s2 = set("abc1abc")
print("Match" if s1 == s2 else "Mismatch")

#Que30 : Use of Break 
s = "ab c d"
for ch in s:
    if ch == " ":
        print("Space found, stopping...")
        break
    print(ch)

#Que31: use of pass
s = "ab c d"
for ch in s:
    if ch == " ":
        pass
    print(ch)

#Que32: use of Conitnue
s = "ab c d"
for ch in s:
    if ch == " ":
        continue
    print(ch)

#Que33 : try - except
s = "abc"
try:
    int(s)  #error
except ValueError:
    print("Cannot convert string to int")

#Que34 : == vs is
a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True (cached string)

#Que35 : Swap two characters in a string
str = "Ankit"
s = str
print(s[-1] + s[1:-1] + s[0])

#OR
str = "Ankit"
s = list(str)
s[0],s[-1] =s[-1],s[0]
print("".join(s))

#Que36: Remove duplicates
s = "banana"
print("".join(sorted(set(s))))

#Que37: 2nd & 3rd largest char
s = "abcdeabcde"
str = sorted(set(s))
print(str)
print(str[-2], str[-3])

#Que38: String comprehension
s = [str(x) for x in range(1,5)]
print("".join(s))

#Que39: Table of 2 as string
s = [str(2*x) for x in range(1,11)]
print(",".join(s))

#Que40: Ternary
s = "abc"
result = "Alpha" if s.isalpha() else "Non-Alpha"
print(result)

#Que41: Convert string to upper case  using lambda ,map
s = "jcfhsifhsifsojfo"
result = list(map(lambda x : x.upper(), s))
print("".join(result))

#Que42 : Remove all "a" characters from a string
s = "jcfhsiadadadadadadfhsifsojfo"
result = list(filter(lambda x: x != "a",s))
print("".join(result))

#Que43: Remove vowels : 
s = "jcfhsiadadadadadadfhsifsojfo"
vowels = "aeiouAEIOU"
result = list(filter(lambda x: x not in vowels,s))
print("".join(result))

#Que44:print only alpha
s = "jcfhsi$%^&*()snsc24828402adadadadadadfhsifsojfo"
result = list(filter(str.isalpha, s))
print("".join(result))

#Que45: Sum ,min and maxof digits from string
s = "jcfhsi$%^&*()snsc24828402adadadadadadfhsifsojfo"
result = [int(x) for x in s if x.isdigit()]
print(sum(result))
print(min(result))
print(max(result))

#Que46: Replace by using value
s = "hello"
s = s.replace("e", "a")
print(s)  # hallo

#Que47: separate int, alpha , special, vowels, consonent
s = "jcfhsi$%^&*()snsc24828402adadadadadadfhsifsojfo"
vowels = "aeiouAEIOU"
vowel_chars = []
consonent = []
digits = []
special = []

for x in s:
    if x.isalpha():
        if x in vowels:
            vowel_chars.append(x)
        else:
            consonent.append(x)
    elif x.isdigit():
        digits.append(x)
    
    else:
        special.append(x)


print("".join(vowel_chars))
print("".join(consonent))
print("".join(digits))
print("".join(special))


#Que48 :  Shift vowels left, consonants right
s = "abcdef"
vowels = "aeiou"
left = [x for x in s if x in vowels]
right = [x for x in s if x not in vowels]
print("".join(left + right))  # aecbdf


#Que48 : isalpha, isdigit, isalnum
s = "abc123"
print(s.isalpha())   # False
print(s.isdigit())   # False
print(s.isalnum())   # True


#Que49 : compare two strings, union, difference
s1 = "abc"
s2 = "bcdskfs"

set1 = set(s1)
set2 = set(s2)

print("Intersection (&):", set1 & set2)       # {'b', 'c'}
print("Union (|):", set1 | set2)              # all unique chars
print("Difference (-):", set1 - set2)         # in s1 but not s2 → {'a'}
print("Symmetric Diff (^):", set1 ^ set2)     # in either but not both

#Que50: Compare same characters
s1, s2 = "abc", "cab"
print(set(s1) == set(s2))  # True

#Que51:  Count even/odd digits in string
s = "abc12345"
digits = [int(ch) for ch in s if ch.isdigit()]
even = len([x for x in digits if x % 2 == 0])
odd = len([x for x in digits if x % 2 != 0])
print("Even:", even, "Odd:", odd)

#Que52: Check same letters
s1 = "listen"
s2 = "silent"
print(set(s1) == set(s2))  # True


#Que53: Prime check from digits

#Que54: Fibonacci (as string output)