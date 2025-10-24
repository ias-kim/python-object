# 추상화 (abstract) -> oop
# 미완성 + 강제 구현

from abc import ABC, abstractmethod

# ABC -> Abstrac Class
class Bar(ABC):

    @classmethod
    @abstractmethod
    def cls(cls):
        ...

    # instance
    @abstractmethod
    def test(self):
        ...

    @property
    @abstractmethod
    def prp(self):
        ...

    prp.setter
    @abstractmethod
    def _(self, value):
        ...

class Foo(Bar):

    @classmethod
    def cls(cls):
        ...

    # instance
    def test(self):
        ...
    
    @property
    def prp(self): 
        print("A")


class A:
    # 반드시 자식 클래스에서 구현되기를 바란다.
    def test(self):
        raise NotImplementedError

class B(A):
    ...

obj = A()
obj.test()

def sum(a : int | float, b : int | float) -> int | float:
    return a + b

print(sum(1, 1)) # 2
print(sum(1, 1.0)) # 2.0
print(sum(3, "1")) # Error