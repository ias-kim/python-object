from tkinter import NO
from typing import Any, NoReturn

class Bar:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


x: int | float = 1 # int or float -> W

from typing import Union
y: Union[int, float] = 1

# collection -> expression, type of the elements in a collection
# list, tuple, set, dict

x:list[int] = [1, 2, 3, 4]
y: tuple[int, str, int] = (1, "f", 3)
b: dict[str, int] = {"A": 2}  # json 디코딩해서 키, 밸류 값

from typing import Optional, TypeVar, Generic, Literal
z:Optional[int] = 2

T = TypeVar("T") # 임의의 타입 변수

class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item
    
    def get(self) -> T:
        return self.item
    
int_box = Box[int](2)
str_box = Box[str]("hello")

print(int_box.get())
print(str_box.get())

def add_user(name: Optional[str])-> str | None:
    if name is None:
        raise ValueError("Name Must be values")
    
    return name[0]


# 깂의 자료형과 밸류까지
def move(direction:Literal["forward", "backward", "left", "right"]) -> None: # 리터럴 상수 -> 이름있는 상수
    ...


# 일급시민 세가지 조건
def test():
    pass

a = test # 값 저장

a() # 값 읽기

def run(func):
    return func # 값 반환

run(test)
