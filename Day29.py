#Docstring and PEP8
#Doctstring - String literals

#Doctstring is different that comments.. we can print this but comments are ignored
#docstring put under tripple single qoute and position of this must be right after the defination of function

def square(n):
    '''Takes in a number n, returns te square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#below will not work -- check
def square(n):
    print(n)
    '''Takes in a number n, returns te square of n'''
    print(n**2)
square(5)
print(square.__doc__)


#PEP 8 -- guidelines to provide best practice python code
#Python enhancement proposals


#ZEN of python
