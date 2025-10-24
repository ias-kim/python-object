from abc import ABC, abstractmethod

# 추상 클래스
# java -> abstract class {P}

# Bar-> 추상 클래스로 정의
class Bar(ABC):

    # 추상 인스턴스 메서드 정의
    @abstractmethod
    def instance_method(self):
        ...

class Foo(Bar):
    def instance_method(self):
        print("My class")

obj = Foo() # -> Error
obj.instance_method()