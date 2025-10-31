from typing import Sequence


class Bar:
    def __init__(self, data:Sequence[int | float]) -> None:
        self.data:Sequence = data

    def __iter__(self):
        return BarIterator(self.data)

class BarIterator:
    def __init__(self, data:Sequence[int | float]) -> None:
        self.data:Sequence = data
        self.index:int = 0

    def __next__(self) -> int:
        # self.data 리스트의 0번째 요소에서 마지막 까지 순회
        if (self.index < len(self.data)):
                value = self.data[self.index]
                self.index += 1
                return value
            
        raise StopIteration
    
obj = Bar([1, 2, 3, 4])

for v in obj: # -> instance of Bar 주소 
    print(v)


x = [10, 20, 30]

for _ in x:
    print(_)


foo = iter(x)
while True:
    try:
        next(foo)
    except StopIteration:
        break

print(len(obj)) # 참조의 객체 주소를 가르킴

obj2 = object()
print(obj2.__str__())

print(obj.__str__())

class Student:
    def __init__(self, id:int) -> None:
        self.id:int = id
        self.kor:int = 0
        self.eng:int = 0
        self.math:int = 0

    def __call__(self, kor:int, eng:int, math:int):
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def __str__(self) -> str:
        return f"kor: {self.kor}, math: {self.math}, eng: {self.eng}"

    def __eq__(self, value: "Student") -> bool:
        return self.id == value.id
    

std1 = Student(1)
std2 = Student(1)
std1(1, 1, 1) # -> 함수처럼 호출 
print(std1)
print(std1 == std2) # False

# Iteration : 순회

x = [_ for _ in range(10)]

