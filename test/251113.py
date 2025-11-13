from typing import Any, Self

# python -> function -> first-class citizen

# nested function (중첩 함수)
def out_func():
    name = "out_fun"
    def in_func(id: int): # nested function
        print(f"in _ func: id -> {id} at {name}")

    return in_func

def test(func):
    def wrapper():
        print("before login")
        func()
        print("after login")
    return wrapper

@test # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출함.
# bar = test(bar) 재정희함
def bar():
    print("bar")

bar()
bar()
# bar()
# test()