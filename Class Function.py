# Class Exercise

# Create a class called Person
# Add two attributes: name and age that can be set when the object is created.
# Create a method called introduce that prints a string in the format:
#
# Hi, My name is Joe and I am 12 years old.

class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

    def introduce(self):
        print(f"Hi, My name is {self.name} and I am {self.age} years old.")


person_1 = Person("Joe", 12)
person_1.introduce()
