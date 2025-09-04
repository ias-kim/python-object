class A(object):
    # 생성자
    # 멤버속성 (Attribute)
    # 멤버메서드
    # 소멸자
    pass
class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Foo("hong", 12)

obj.university = "yju"

import types
def prt_unif (self, univ):
    self.univ = univ
obj.prt_univ = types.MethodType(prt_unif, obj)

print(obj.name)
print(obj.age)

del obj.name
print(obj.name)