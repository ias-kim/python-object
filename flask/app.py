from flask import Flask

# Flask 클래스의 객체 생성
# __name__: 현재 실행 프로그램의 경로 정보를 먼저 인자값으로 전달
app = Flask(__name__) # 실행할 때에 현재 파일의 route라고 적시

# Routing -> view function
@app.route('/')

def home():
    # response
    return "hello flask", 200, {"X-Param": "gsc"}

print(app.url_map)

# Flask 실행
if __name__ == "__main__":
    # 디버그 : 콘솔에 디버깅 정보 출력
    app.run(debug=True)
    # run -> 개발용 web server + WSGI server + flask 객체 바인딩 -> WSGI server