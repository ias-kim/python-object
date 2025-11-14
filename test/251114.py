# from textwrap import wrap
# from turtle import up


# def is_login(func):
#     # func 매개변수를 캡처하므로 클로저 func
#     def wrapper(msg: str, key = 20): # wrapper 함수에 오는 매개변수가 존재해야함.
#         print("before")
#         func(msg) # msg
#         print(f"after: {key}")

#     return wrapper

# @is_login # do_something = is_login(do_something)
# def do_something(msg:str):
#     print(f"do something: {msg}")

# do_something("h1")
# do_something("h2")


# # 함수의 매개변수 덮어 쒸움!
# #-----------------------
# def test():
#     print("test")

# def bar(x, y):
#     print(f"bar: {x, y}")

# test = bar

# test(2, 3)
# #-----------------------

# def f_a(func):
#     def wrapper():
#         print(f"f_A{func}")
#         func()
#     return wrapper

# def f_b(func):
#     def wrapper():
#         print(f"f_B{func}")
#         func()
#     return wrapper

# @f_a
# @f_b
# def bar1():
#     print("bar")

# bar1()

# 체이닝 메서드의 틀들
from functools import wraps
from textwrap import wrap


def strip(func):
    def wrapper(msg: str):
        return func(msg.strip())
    return wrapper

def upper(func):
    def wrapper(msg: str):
        return func(msg.upper())
    return wrapper

@upper
@strip
def prt_something1(msg: str):
    print(f"prt: {msg}")

@strip
def prt_something2(msg: str):
    print(f"prt: {msg}")

@upper
def prt_something3(msg: str):
    print(f"prt: {msg}")

msg = "     test "
msg = msg.strip().upper()

if msg == "TEST":
    print('true')
else:
    print('false')

prt_something1("hello")
prt_something2("    hi")
prt_something3("ffff")





def upper2(func):
    @wraps(func) # 기존 함수를 데코레이터 함수에서 본연의 함수로 덧쒸어진다.
    def wrapper(msg: str):
        return func(msg.upper())
    return wrapper

@upper2 # 자동으로 dom 트리를 만들어 데코레이터를 사용했지만 bar는 덮어쒸여서 bar가 감쳐지며 wrapper함수로 쌓여져있다.
def bar(msg: str):
    return f"bar {msg}"

print(bar("hello"))

print(bar.__name__)

def test(func):
    def wrapper():
        func()
    
    # 실질적인 wraps 동작
    wrapper.__name__ = func.__name__
    return wrapper

@test
def bar3():
    ...
print(bar3.__name__)

# flask 예씨
def test2(path):
    def factory(func):
        # 내부적으로 구현 route_map['path'] = func
        def wrapper(func):
            func()
        return wrapper
    return factory

@test2(1) # test(1) -> factory()(bar) 또 다른 wrapper함수를 또 함수를 집어넣는다.
def bar4():
    ...

bar4()