#f string  -- String formatting
letter = "Hey i am {} and i am from {}"
Name = "Ankit"
Country = "India"
print(letter.format(Name,Country)) 
print(letter.format(Country,Name))

letter = "Hey i am {1} and i am from {0}"
print(letter.format(Country,Name))


#New method - using f string
print(f"Hey i am {Name} and i am from {Country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.0999))


prizee= 49.09999
txt1 = f"For only {prizee:.2f} dollars!"
print(txt1)

print(f"{2*30}")
print(type(f"{2*30}"))


print(f"Hey i am {{Name}} and i am from {{Country}}")