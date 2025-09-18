# class Parent:
#     def prt_name(self):
#         print(self.name)

# class Child(Parent):
#     def __init__(self):
#         self.name = "child"

# # 돌아가지면 이렇게 절대 쓰면 안됨!
# obj = Child()
# obj.prt_name()

class Bar:
    def __init__(self):
        self.name = "YC_jung"
    
    def prt_info(self):
        print(self.name, self.age)
    
class Foo(Bar):
    def __init__(self):
        self.name = "child" # 위치를 바꿔가면서 메모리 주소 그려보기
        super().__init__() # super -> Bar의 클래스 오브젝트의 주소

obj = Foo()
obj.prt_info() # 하나의 공간에서 덮어버림

print(Foo.__base__)