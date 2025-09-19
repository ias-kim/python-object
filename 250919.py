class A:
    def __init__(self):
        print("a")
    def prt(self):
        print("AA")
class B(A):
    def __init__(self):
        print("동시에 초기화")
    # def __init__(self):
        # super().__init__()
        # print("B")

class C(A):
    # def __init__(self):
    #     print("C")
    #     super().__init__()
    def prt(self):
        print("CC")
class D(B, C):
    def __init__(self):
        print("D만 초기화 됩니다!")
    def prt(self):
        print("D - prt")
        super().prt()
    # def __init__(self):
    #     print("D")
    #     super().__init__()


obj = D()
obj.prt()