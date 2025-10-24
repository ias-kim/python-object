class A:
    def __init__(self):
        self.name = "Class A"
        print(self.name)

    @classmethod
    def prt_something(cls):
        print("Invoked prt_something")

class B(A):
    def __init__(self):
        super().__init__()
        self.age = 20

class C(B):
    def __init__(self):
        super().__init__()
        self.nick = "Class C"

        # 시작은 __ 로 하나 끝은 __를 붙이면 안됨.
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

class D(C):
    def print(self):
        print(self.public) # public
        print(self._protected) # protected
        print(self._C__private) # Error -> 네임 핸들링으로 접근 가능

obj = C()

print(obj.nick) # class C
print(obj.age) # error
print(obj.name)

print(obj.public)
print(obj._protected)
print(obj._C__private) # 네임 맹링으로 가능!

obj2 = D()
obj2.print()