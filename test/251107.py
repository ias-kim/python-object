
# from math import exp
# from typing import Any, Self



# class Bar:
#     def __init__(self) -> None:
#         self.name = "Bar"
    
#     # event -> 객체 멤버 변수에 값을 넣을 때
#     def __setattr__(self, name: str, value: Any) -> None:
#         # 재귀 함수 호출하다가 호출 끊음
#         # 부모의 object의 setattr를 호출해야한다.
#         object.__setattr__(self, name, value)
#         print(f"name: {name}, value: {value}") # 인스턴스 멤버 변수에 값을 넣는다.

#     def __getattribute__(self, name: str) -> Any:
#         try:
#             value = object.__getattribute__(self, name)
#             print(f"Get: {value}")
#             return value
#         except AttributeError:
#             print(f"Missing: {name}")

# obj = Bar()
# obj.tag = "hello"
# print(obj.tag)

# import random
# from collections import OrderedDict # 순차적으로 집어넣음

# class Module:
#     _parameters:OrderedDict # typechcker 확인용 (동적으로 확인)

#     def __init__(self, input:int, output:int) -> None:
#         object.__setattr__(self, "_parameters", OrderedDict())
#         self.weight = [ random.gauss(0, 1) for _ in range(input) ]
#         self.bias = [ random.gauss(0, 1) for _ in range(input) ]

#     def __setattr__(self, name: str, value: Any) -> None:
#         # name -> weight or bias -> ordereddic에 저장
#         # 이외는 그냥 저장
#         if name in ["weight", "bias"]:
#             self._parameter[name] = value
        
#         object.__setattr__(self, name, value)

#     def __getattribute__(self, name: str) -> Any:
#         if name in ["weight", "bias"]:
#             return self._parameters[name]
        
#         return self.name

#     def parameters(self):
#         yield from self._parameters.items()

# module = Module(3, 1)

# for w, b in module.parameters():
#     print(w, b)


from typing import Any, Self

class Bar:
    def __enter__(self) ->Self:
        print("Bar: DB CONNECTING")
        return self

    def div(self, x, y) -> float:
        return x / y

    # Exception의 약자  -> 비정상 종료될 시 해당 값이 출력
    def __exit__(self, exc_type, exc_value, traceback)->bool:
        print(f"exit: type [{exc_type}], val: [{exc_value}], trace: [{traceback}]")
        return True

with Bar() as obj:
    obj.div(2, 0)


# Bar: Enter
# ----
# Bar: Exit

from dataclasses import dataclass, field

# @dataclass
# class Student: # Data 저장용 클래스가 된다.
#     id: str = field(default=2) # 인스턴스 멤버 변수
#     name: str = field(compare = False, repr=False)
#     age: int # 인스턴스 멤버 변수

#     data:list = field(default_factory=[])

#     def __eq__(self, value: object) -> bool:
#         pass

#     # <= 숫자뿐만 아니라 문자열도 비교를 한다.
#     def __le__(self, value: "Student") -> bool:
#         return self.age <= value.age

# std1 = Student("123", "kim", 20)
# std2 = Student("123", "Lee", 10)

# print(std1 <= std2)
# print(std2.id, std2.name, std2.age)

# -------------

def decorator(func):
    def wrapper(msg: str):
        print("write log")
        func(msg)

    return wrapper

@decorator #decorator(test) # 소스코드를 해석할때 실행
def test(msg: str):
    print(msg)

test("hello")
print(test.__name__)