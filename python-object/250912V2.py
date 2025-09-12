class Student:
    count = 0
    
    def __init__(self, student_id, name, eng, kor, math):
        Student.count += 1
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math

    def calc_total(self):
        self.sum = self.eng + self.kor + self.math
    
    def calc_average(self):
        self.avg = self.sum / 3.0


s1 = Student("2025001", "Kim", 90, 80, 85)
s2 = Student("2025002", "Lim", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

print(s1.student_id, s1.name, s1.sum, s1.avg)
print(s2.student_id, s2.name, s2.sum, s2.avg)

print("총 학생 수:", Student.count)