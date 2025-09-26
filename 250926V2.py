# def prt(positional, variable positional, keyword, variable keywords):

# / : 위치기반 매개변수 전용 -> 앞까지의 모든 매개변수는 위치기반 인자값으로 할당되어야 한다.
from typing import Union

# 타이핑 적용
def calculate(x : Union[int, float], y : Union[int, float], /, op = "+"):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    else:
        print("error")

#가변 기반 위치 -> 튜플로 받을 수 있음.
def prt(a, *arg): 
    print(a, arg)

def prt1(**arg):
    for key, value in arg.items():
        print(f"{key}, {value}")

# 가변 위치 매개변수 뒤에는 일반적인 위치기반 매개변수는 올 수 없다. 
def prt2(a, *b, c = 10, d = 20, **kwargs): # 키워드 매개변수가 와야된다.
    print(a, b, c, d, kwargs)


calculate(2, 4)
calculate(10, 20, "-")
calculate(1, 1, 'f')

prt(1) # (1)
prt(1, 2) # (1, 2)
prt(1, 2, 3) # (1, 2, 3)


prt1(a = 2) # 1
prt1(d = 3, test = 'ddd') # 1, (2)


prt2(1, 2, 3, 4, 5, op=200, d=100) 
# 위치 기반 -> 키워드 -> 가변들이 따로 붙는다!
# 위치 키워드 동일하면 고정 가변으로 구성이됨
# 이를 잘 조합하면 함수가 잘 동작하게 만들 수 있음.