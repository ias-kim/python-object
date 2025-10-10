"""
파이썬 아규먼트 고오급 활용
"""

# 기본값 인자와 선택적 인자의 조합
def configure_device(model, capacity, color='black', warranty=None):
    # 기능: 디바이스의 설정을 출력
    # model과 capacity는 필수 인자
    # color는 기본값 'black'을 가진 선택적 인자
    # warranty는 기본값이 None인 선택적 인자로, 보증 정보가 필요할 때만 제공
    print(f"Model: {model}")
    print(f"Capacity: {capacity}GB")
    print(f"Color: {color}")

    if warranty:
        print(f"Warranty: {warranty} years")
    else:
        print("Warranty: Not specified")

# 예제 함수 호출
# 모델명과 용량은 필수로 제공되어야 하며, 색상과 보증은 선택적으로 제공
configure_device('Model X', 256)
configure_device('Model Y', 512, color='white', warranty=2)

# 가변 인자 조합
def initizalize_settings(*args, debug=False, **kwargs):
    # *args는 위치에 따라 전달된 모든 추가 인자를 튜플로 받음
    # debug는 키워드 인자, 기본값은 false, 디버그 모드의 활성화 여부를 지정
    # **kwargs는 키워드에 따라 전달된 모든 추가 인자를 딕셔너리로 받음

    print(f"Arguments: {args}, Debug Mode: {debug}, Keyword Arguments: {kwargs}")

# Initialize_settings 함수 호출
initizalize_settings(1, 2, 3, debug=True, configuration="Complete", user="admin")

# "*" 사용 인자 전달
def print_numbers(a, b, c):
    print(a, b, c)

numbers = [1, 2, 3]
print_numbers(*numbers) # 리스트를 풀어서 각 요소에 독립적인 인자로 함수에 전달