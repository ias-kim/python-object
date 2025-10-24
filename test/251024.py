# def test():
#     ...

# # bar 변수에 test 함수 주소값을 할당
# bar = test

# def run(my_func):
#     my_func()

# test 함수를 run 함수에 매개변수의 인자값 할당.

# run(test)
from typing import Callable, TypedDict

def test(x: int, y: float, z: str) -> str:
    return f"{x}, {y}, {z}"

# my_func -> argument - > 3개, 반환형은 문자열이여야 함.
# my_func은 함수형 object 주소가 들어 온다.
# Callable 함수의 주소가 되며, 매개변수의 주소가 반환형

def run(my_func: Callable[[int, float, str], str], a: int, b: float, c: str) -> None:
    print(my_func(a, b, c))


# run(test(1, 2.0, 'f'), 1, 2.0, 'a')

# 타입딕셔너리 -> 스키마 정의 -> dictionary -> JSON
class Student(TypedDict):
    id: int
    name: str
    gpa: float
std1: Student = {"id": 2, "name": "kim", "gpa": 4.2}

from typing import NamedTuple

class User(NamedTuple):
    name: str
    age: int
    gender: str

u1 = User("ycjung", 2, "M")

def create_user(name: str, age:int, gender:str) -> User:
    return User(name, age, gender)

name, age, gender = create_user("ycjung", 2, "M")