print(1 + 1)
print((1).__add__(1))

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
    
    # 기존에 있는 매직메서드 재정의
    def __add__(self, r_operand:"Vector"):
        x = self.x + r_operand.x
        y = self.y + r_operand.y
        return Vector(x, y)
        print(f"add_is invoked {r_operand}")

    
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2 # v1.__add__(v2)
v4 = v1 + v2 
print(v3.x, v3.y)

# x3 = v1.x + v2.x
# y3 = v1.y + v2.y

# v3 = Vector(x3, y3)