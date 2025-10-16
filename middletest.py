class Student:
    # 클래스 멤버 변수
    __id_count = 0

    # 인스턴스 멤버 변수
    def __init__(self, name, id, gender):
        Student.__id_count += 1
        self.name = name
        self.id = Student.__id_count
        self.gender = gender

    # 인스턴스 메서드
    def set_score(self, korean, math, eng):
        self.korean = korean
        self.math = math
        self.eng = eng
        self.total = korean + math + eng
        self.avg = self.total / 3.0

    def get_total_avg(self):
        return self.total, self.avg

    # 클래스 메서드
    @classmethod
    def get_id_count(cls): 
        return Student.__id_count
    
    # 정적 메서드
    @staticmethod
    def get_avg(arg1, arg2, arg3):
        sum = arg1 + arg2 + arg3
        return sum / 3.0

# 객체 생성
s1 = Student("Alice", 0, "F")
s2 = Student("Bob", 0, "M")

# 점수 입력
s1.set_score(90, 85, 92)
s2.set_score(75, 80, 78)

# 총점과 평균 출력
print(s1.get_total_avg()) # (267, 89.0)
print(s2.get_total_avg()) # (233, 77.67)

# 클래스 메서드 호출 (현재 생성된 객체 수)
print(Student.get_id_count()) #2

# 정적 메서드 호출 (별도의 객체 없이 평균 계산)
print(Student.get_avg(100, 90, 80)) # 90.0