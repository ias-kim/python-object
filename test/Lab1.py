class std_grades:
    count = 0

    def __init__(self, id, name, eng, kor, math):
        std_grades.count += 1

        self.id = id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
    
    def calc_total(self):
        self.total = self.eng + self.kor + self.math
        print(self.total)

    def calc_average(self):
        self.avg = self.total / 3
        print(self.avg)

s1 = std_grades("2025001", "kim", 90, 80, 85)
s2 = std_grades("2025002", "lee", 70, 75, 80)


# 합계 및 평균 계산
s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

# 결과
print(s1.id, s1.name, s1.total, s1.avg)
print(s2.id, s2.name, s2.total, s2.avg)

print("총 학생 수", std_grades.count)