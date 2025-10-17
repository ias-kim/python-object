# Collection -> Abstract Data Type -> Implementaion Set
# Python -> list, tuple, dict, set

from optparse import Option
from typing import List
from typing_extensions import LiteralString

x: List = [1, 2, 3] # Legacy -> 예전 방식
x: list = [1, 2, 3]

def get_total_avg(x: int, y: int) -> tuple:
    sum = x + y
    avg = sum / 2
    return sum, avg

x_tuple: tuple = (1,2,3)
x_dic:dict = {1:2, 3:4}
x_range:range = range(2)

x_list:list[int] = [1, 2, 3]

# 조심해야 할 것
x_tuple_int: tuple[int, float, str, int] = (2, 3.0, "",3)

# 타입 딕서녀리
y:tuple[int, ...]
y = (1,2,3,4,5,5)
y = (1,4)

x_dic_str_float:dict[str, float] = {"k1": 2.0, "k2": 3.0}

x_set_bool:set[bool] = {True, False}

from typing import Sequence 
# Sequence -> Type hinting -> list, tuple, range
x_seq_int:Sequence[int] = [1, 2, 3]
x_seq_int = (1, 2, 3)
# x_seq_int = {1, 2, 3}
x_seq_int = (1, 2)

# Union -> 집합의 원소 중 하나이면 -> Ok, 모두 해당되지 않으면 에러
from typing import Union
# x_new: int | float -> 최신 버전
x: Union[int, float, bool]
x = 2
x = 3.0
x = False
# x = "2"
# Optional -> if else -> if [T] else None

from typing import Optional
x_op_int = Optional[int]

x_op_int = 3
x_op_int = None

from typing import Literal, Any, Callable
x_lit:Literal["man", "woman"]
x_lit = "man"
x_lit = "woman"

x: Any 
x = 1

# Callable -> 함수, 메서드 
def sum(x: float, y: float) -> float:
    return x + y

sum_2 = sum
sum_2(2, 3)
print(sum_2) # 5

def do_something(x: float, y: float, op:Callable[[float, float], float]):
    return op(x,y)

do_something(1, 2, sum) # 매개변수의 개수와 반환하는 자료형이 중요함.
