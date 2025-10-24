class Bar:
    # 멤버 변수(속성) -> 1. 인스턴스 멤버변수. 2. 클래스 멤버변수
    # 클래스 멤버 변수
    # 실무 -> 여기
    def __init__(self):
        # 초기화 작업
        # 인스턴스 멤버 변수 : 실무 -> 생성자
        pass

    def __del__(self):
        # 객체 소멸 전 자원 정리
        pass
    
    
    # 멤버메서드 -> 1. 클래스 메서드 2. 인스턴스 메서드
    # 인스턴스 멤버 메서드
    def instance_method(self):
        pass

    # 클래스 멤버 메서드
    @classmethod
    def class_method(cls):
        pass

    # 메서드 -> 멤버 메서드 (인스턴스, 클래스), 스태틱(static) 메서드
    # Static method
    @staticmethod
    def static_method():
        pass


obj = Bar()

