"""
1. 위치 인자
2. 키워드 인자
3. 기본값 인자
4. 가변 위치 인자
5. 가변 키워드 인자
"""
# 위치 전용 파라미터 예제
def positional_only(a, b, /): # '/' 앞에 오는 인자들을 '위치 전용'
    print(a, b)

positional_only(1, 2) # 정상 호출 (위치 인자로 전달)
#positional_only(a=1, b=2) # Error 
# -> '/' 때문에 a, b는 반드시 위치 인자로 넣어야 함
# -> 키워드 인자로 전달 불가

# 키워드 전용 파라미터 예제
def keyword_only(*, a, b): # '*' 뒤에 오는 인자들은 '키워드 전용'
    print(a, b)

keyword_only(a=10, b=10) # 정상 호출 (키워드 인자로 전달)
#keyword_only(10, 20) # Error
# -> '*' 뒤의 a, b는 반드시 키워드 인자로만 넣어야 함.
# -> 위치 인자로 전달 불가함.

# 기본값 인자
# 기본값을 가진 매개변수는 위치인자 뒤에 위치해야 한다
def setup_environment(os, version, language="Python"):
    # 잘못된 사용 예: setup_environment(language="Python", os, version)
    print(f"Operating System: {os}, Version: {version}, Prg. Language: {language}")

setup_environment("windows", "10")
setup_environment("linux", "18.04", "Java")

# 가변 위치 인자
# 함수는 가변 위치 인자 *ingredients를 받음
# *ingredients는 함수에 전달된 위치 기반의 인자들을 튜플로 취급하며, 이를 통해 함수는 임이의 수의 인자를 받을 수 있다.
def list_ingredients(*ingredients):
    print("Ingredients In your dish:")
    print(ingredients)
    # 전달된 모든 인자 (ingredients 튜플의 각 요소)에 대해 반복함
    for ingredient in ingredients:
        print(f"- {ingredient}")

list_ingredients("tomatoes", "cheese", "peppers")

# 가변 키워드 인자
def configure_setting(**settings):
    # 함수에 전달된 모든 키워드 인자에 대한 반복
    # settings.items()는 딕셔너리의 키(key)와 값(value) 쌍을 반복 가능한 형태로 제공
    for key, value in settings.items():
        # 각 설정의 키와 값을 출력, 출력 형식은 '키 is set to 값'
        print(f"{key} is set to {value}")

# configuer_settings 함수를 세 개의 키워드 인자와 호출
# - database='MYSQL', port=3306, timeout=30
# 이 인자들을 함수 내에서 settings 딕셔너리로 그룹화되어 처리
configure_setting(database='MYSQL', port=3306, timeout=30)