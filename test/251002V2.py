from functools import singledispatch, singledispatchmethod

# 매개변수 1개 -> 오버로딩 구현
# 지원 자료형은 int, float

@singledispatch
def bar(x):
    raise TypeError("unsupported Type")

@bar.register(float) # 타입힌팅
def _(x : float):
    print("float")

@bar.register(int) # 타입힌팅
def _(x : int):
    print("integer")


print(bar(2.0))
print(bar(2))
print(bar("@"))
