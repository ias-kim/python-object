from abc import ABC, abstractmethod

# 추상 클래스 정의 
class Bar(ABC):
    # 추상 메서드 정의
    @abstractmethod
    def instance_method(self):
        pass

    @classmethod
    @abstractmethod
    def class_method(cls):
        pass

    @staticmethod
    @abstractmethod
    def static_method():
        pass

    @property
    @abstractmethod
    def getter(self):
        pass


# 에러 발생 예시
# Bar는 추상 메서드(instance_method)를 구현하지 않았기에 
# obj1 = Bar() # TypeError

# 하위 클래스에서 추상 메서드 구현
class Foo(Bar):
    def instance_method(self):
        print("Invoked instance_method of Foo class")

    @classmethod
    def class_method(cls):
        print("invoked class_method")
    
    @staticmethod
    def static_method():
        print("invoked static_method")
    
    @property
    def getter(self):
        return "invoked getter method"
    

# 정상 인스턴스 생성 및 메서드 호출
obj2 = Foo()
obj2.instance_method() # 출력 -> 

obj2.static_method()
Foo.static_method()

obj2.class_method()
Foo.class_method()

print(obj2.getter)