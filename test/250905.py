class Foo:
    univ = "YJU"
    dept = "GSC"

    # def __init__ (self, name):
    #     self.name = name
    
    def prt_info(self, age):
        self.age = age
        print(self.name, self.age)
    
    # 실제로는 new가 먼저 호출된 생성자가 실행된다.
    def __new__(cls): # cls -> 0xff
        cls.test = "KIRIN"
        print("cls")
        return super().__new__(cls)
    

new1 = Foo()
# new1.prt_info(20)

print(Foo.test)


# new2 = Foo('Lee')
# new2.prt_info(25)
