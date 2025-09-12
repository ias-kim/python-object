class Foo:
    # class member attributes(variables)
    count = 0

    # Instance member variables
    def __init__ (self, name):
        self.name = name
        Foo.count += 1
    
    # class method
    @classmethod
    def class_method(cls, age):
        cls.age = age

    # instane method
    def instance_method(self, age):
        self.age = age

    # static method
    @staticmethod
    def static_method():
        pass


obj = Foo("Foo instance")
obj.class_method(30)
obj.instance_method(100)
print(obj.age, Foo.age)


# print(obj.name)
# print(Foo.count)