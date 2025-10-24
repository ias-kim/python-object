# class Bar:
#     # instance method
#     def i_method(self):
#         self.iValue = 20
#     # class method
#     @classmethod
#     def c_method(cls):
#         cls.cValue = 30

#     #static method
#     @staticmethod
#     def s_method(): # 주소가 없음.
#         print("s_method")

# obj = Bar()
# obj.s_method()
# Bar.s_method()
# del obj.iValue
# del obj.cValue
# del Bar.i_method

# Bar.cValue = 1000

class Foo:

    # Constructor
    def __init__(self, id):
        self.id = id
        # Add instance member variables
        print(f"Constructor is object {self.id} invoked")
    
    def __del__(self):
        print(f"Destructor is object {self.id} invoked")
    
    
obj1 = Foo(1)
obj2 = Foo(2)
del obj1

print("Program is terminated")
del obj2