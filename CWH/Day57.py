#Object oriented programming
#class
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 1000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Ankit"
a.occupation = "Test Engineer"

print(a.name, a.occupation)

b = Person()
b.name = "Neetu"
b.occupation = "SDM"

a.info()
b.info()

c = Person
c.info




