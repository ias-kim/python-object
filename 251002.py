from typing import Union
def bar(a, b, *args, c=299):
    print(a, b, args, c)


bar(1, 2, 3, 4, 5, 6)

# type hinting

x : int = 3 # -> 누구에게 타입을 알려주는 건가?

def sum(a: Union[int, float], b: Union[int, float]) -> float:
    return (a + b)

print(sum (1, 2))
print(sum(4.0, 2.0))
#print(sum("4"/"2"))

def bar(x: int):
    print("X")
def bar(y: float):
    print("Y")
def bar(z: str):
    print("Z")

bar(3)

if isinstance(x, int):
    print(f"X: {type(x)}")
elif isinstance(x, float):
    print(f"X: {type(x)}")
else:
    raise TypeError("unsupported type")