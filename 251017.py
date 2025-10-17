
value_1: int = 2
value_2: float = 2.0
# 매개변수와 반환값에 타입 힌트 지정
def add(x: int, y: float) -> float:
    return x + y

class Bar:
    def __init__(self, arg: str) -> None:
        self._name: str = arg
    
    @property
    def name(self) -> str:
        return f"Class name : {self._name}"

# Callable(param...) -> return type
def sum(x: int, y: int) -> int:
    return x + y

class Foo:
    # 생성자에는 반환형이 없으므로 None 반환
    def __init__(self, x: int, y: str) -> None:
        self.x: int = x
        self.y: str = y

def something(a: int, b: int, c:None = None) -> None:
    ...

