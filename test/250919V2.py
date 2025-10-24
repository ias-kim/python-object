class A(object):
    name = "A"

    def __init__(self):
        self.age = 20


class B(A):
    name = "B"

    def __init__(self):
        self.age = 100
        super().__init__()


# print(A.name) # A
# print(B.name) # B

obj = B()
print(obj.age) # 리어 사이어먼트 