class Student:
    school = "YJU" # 클래스 속성

    def __init__(instance_ref, name): # 인스턴스 참조 변수
        instance_ref.name = name # 인스턴스 속성
    
    # 1. 인스턴스 메서드
    def introduce(instance_ref):
        print(f"안녕하세요, 저는 {instance_ref.name}입니다.")

    # 2. 클래스 메서드
    @classmethod
    def get_school(class_ref): # 클래스 참조 변수
        print(f"학교: {class_ref.school}")
    
    # 3. 정적 메서드
    @staticmethod
    def add(a, b):
        print("합", a + b)

s1 = Student("kim")

# 인스턴스 메서드 -> 인스턴스 참조 변ㅅ ㅜ사용
s1.introduce()
# 클래스 메서드 -> 클래스 참조 변수 사용
Student.get_school() 
# 정적 메서드 -> 독립 유틸리티 함수
Student.add(3, 5)