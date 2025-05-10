#String Methods
# Strings are immutable
a = "Ankit"
a = "harry"
print(a)
#we can overwrite the variable in python
c = "Aniket"
print(len(c))
print(c.upper())    #New String
print(c.lower()) 

d = "Harry !!!!!!!!" 
print(d.rstrip("!"))  # Strip only traling part
# rstrip removes any trailing character
e = "!!!!Harry !!!!!"
print(e.rstrip("!"))


# replace
f = "Harry potter Harry"
print(f.replace("Harry","Potter"))

#Split: The split() method splits the given string at the specified instance and returns the separated strings as list items.
g = " harry %%% Porterr"
print(g.split(" "))

# capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

h = '''capitalize() :
the capitalize() method turns Only the first cHaracter of the string to uppercase and the rest other characters of the string are turned to LowerCASE. 
the string has no eFFect if the first character is already uppercase. '''
print(h.capitalize())

i = "Introduction of python"
print(len(i))
print(i.center(44))

#count
print(f.count("Harry"))

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)


#endswith() --- Return boolean value
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str = "Welcome to the console !!!!!"
print(str.endswith("!"))

#We can even also check for a value in-between the string by providing start and end index positions.
print(str.endswith("to", 4, 10))   #end index should be plus one only -- ends with "to"

#find() : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
#As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

str1= "He's name is Dan. He is an honest man. 0"
print(str1.find("is"))
print(str1.find("Hii"))

#index()
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
#print(str1.index("dan")) -- Will give error
print(str1.index("Dan"))


#isalnum() :
#The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

print(str1.isalnum())  # Contains special character
str3 = "AnkitJadhav"
print(str3.isalnum())
str4 = "AnkitJ3010"
print(str4.isalnum())

#isalpha() :The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

print(str3.isalpha())
print(str4.isalpha())

#islower() :The islower() method returns True if all the characters in the string are lower case, else it returns False.

print(str1.islower())
print(str2.islower())
print(str3.islower())
print(str4.islower())

str5 = "asodjsdjosj3010"
print(str5.islower())

#isprintable() :The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str6 = "asodjs\ndjosj3010"
print(str6.isprintable())
print(str1.isprintable())

#startswith()
str7 = "Python is a Interpreted Language" 
print(str7.startswith("Python"))

#isspace() :The isspace() method returns True only and only if the string contains white spaces, else returns False.
str8 = "     "    #Spacebar
print("str8:" ,str8.isspace())
str9 = "            "   #Tab
print(str9.isspace())

#istitle() :The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
print(str7.istitle())
str10= "Python Is A Interpreted Language 01"
print(str10.istitle())


#isupper() :The isupper() method returns True if all the characters in the string are upper case, else it returns False.

str11 = "WORLD HEALTH ORGANIZATION" 
print(str11.isupper())


#swapcase() :The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(str11.swapcase())
print(str7.swapcase())

#title() :The title() method capitalizes each letter of the word within the string.
print(str7.title())












