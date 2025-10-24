# 가변 인자를 이용한 오버로딩 흉내
def add(*args): # 튜플로 묶어 받음
    return sum(args) # 받은 모든 인자의 합을 반환

# 호출 예시
print(add(1)) 
print(add(1, 2))
print(add(1, 2, 3))

# 타입 분기를 이용한 오버로딩 흉내내기
def to_str(x):
    # isinstance()로 런타임 시점에 타입을 확인
    if isinstance(x, int):
        return f"int: {x}"
    elif isinstance(x, float):
        return f"float: {x}"
    elif isinstance(x, str):
        return f"str:{x}"
    
    # 정의하지 않은 타입이 들어오면 예외 발생
    raise TypeError("unsupported type")

# 호출 예시
print(to_str(1))
print(to_str(2.0))
print(to_str("3"))
# print(to_str(add))

# singledispatch 활용
from functools import singledispatch
# 기본 함수 정의 (Dispatcher 객체로 교체)
# @sigledispatch : 첫 번째 인자의 타입에 따라 다른 구현을 선택하도록 만듬
@singledispatch
def prt(x):
    # 기본 구현 (fallback): 지원되지 않는 타입이면 에러 발생
    raise TypeError(f"unsupported type {type(x)}")

# int 타입이 들어왔을 때 실행되는 구현 등록
@prt.register(int)
def _(x: int) -> str:
    return f"int {x}"

# float 타입이 들어왔을 때 실행되는 구현 등록
@prt.register(float)
def _(x: float) -> str:
    return f"float {x}"

# 호출 예시
print(prt(2.0)) # float 타입 
print(prt(3)) # int 타입

# 오버로드 활용
from typing import overload, Union

# 타입 힌트용 오버로드 선언 (런타임에는 함수 정의 안 됨) --
@overload
def prt(x: int) -> str:
    # 타입체커에게 알려줌: 인자로 int를 주면 str을 반환
    pass

# 실제 구현부 (런타임에서 호출되는 유일한 함수)
def prt(x: Union[int, float]) -> str:
    # 실제 동작: int/float에 따라 문자열을 반환
    if isinstance(x, int):
        return f"int: {x}"
    elif isinstance(x, float):
        return f"float: {x}"
    
    # int, float 이외 타입이 들어오면 런타임 오류 발생
    raise TypeError("unsupported type")
# 호출 예시
print(prt(10))
print(prt(3.14))
print(prt("abc"))
