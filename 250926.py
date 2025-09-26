# Access modifier in Python
# -> convention

# naming of a variable
# public -> bar
# protected -> _bar
# private -> __bar (name mangling)

# Getter / Setteer => Method
class A:
    def __init__(self):
        self.__age = None # ._A__age

    # getter method
    @property
    def age(self):
        return f"나이는 : {self.__age}"
    
    # setter method
    @age.setter # age의 setter
    def age(self, age):
        if age < 0:
            raise TypeError('음수임')
        self.age = age

obj = A()
print(obj.age)
obj.age = -100