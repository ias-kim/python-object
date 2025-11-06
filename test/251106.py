
# 클래스 밑에 타입지정을 알려주는 것
from itertools import count
from mimetypes import init
from typing import Any, ClassVar

# 학생 정보: 이름, ID, 나이

class Student:
    name: str
    id: str
    age: int

    def __init__(self, name: str, id: str, age: int) -> None:
        
        self.name:str = name
        self.id:str = id
        self.age:int = age

obj = Student("kim", "1234", 12)

class MyDataset:
    def __init__(self, feature:list, label:list) -> None:
        self.feature:list = feature
        self.label:list = label

    # 사용자용 출력
    def __str__(self):
        return f"Dataset:\nfeature: {self.feature}\
            \nlabel: {self.label}"
    
    # 디버깅용 출력
    def __repr__(self):
        return "For log, debug and Dog"
    
    def __getitem__(self, index) -> tuple:
        return self.feature[index], self.label[index]
    
    def __setitem__(self, index: int, value: tuple[list, list]) -> None:
        self.feature[index] = value[0]
        self.label[index] = value[1]

    def __len__(self):
        return len(self.feature)
dataset = MyDataset([1, 2, 3], [10, 20, 30])

print(dataset[0]) # get -> 0번째 샘플의 값 (feature, labels)

dataset[2] = ([5], [50])

class MyData:
    def __init__(self, data:list) -> None:
        self.data:list = data

    def __iter__(self):
        DataIterator(self.data)


class DataIterator:
    def __init__(self, data) -> None:
        self.index = 0
        self.data = data

    def __next__(self) -> int:
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        
        raise StopIteration


class Mydata1:
    def __init__(self, feature:list, label: list) -> None:
        self.feature: list = feature
        self.label: list = label
    
    def __iter__(self):
        for x, y in zip(self.feature, self.label):
            yield x, y

data = Mydata1([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])

for x, y in data:
    print(f"x, y: {x}, {y}")



# for x in data:
#     print(x)

def my_range(num: int):
    count: int = 0

    while(count < num):
        yield count
        count+=1

for x in my_range(5):
    print(x)



