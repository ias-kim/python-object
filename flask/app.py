from flask import Flask, request

# Flask 클래스의 객체 생성
# __name__: 현재 실행 프로그램의 경로 정보를 먼저 인자값으로 전달
app = Flask(__name__) # 실행할 때에 현재 파일의 route라고 적시

# Routing -> view function
@app.route('/', methods=["GET"])

def home():
    # response
    print(f"Path: {request.path}") # http request가 올때 생성이 되며, 해당 정보가 요청이 당함.
    print(f"Method: {request.method}") # 그 헤더에 대한 정보 Response 클래스 객체를 남길 수 있다.
    
    upload_file_name = None

    print(request.headers.get('gsc'))

    file_obj = request.files.get("file_1")
    if file_obj:
        upload_file_name = file_obj.filename

    return {
        "method": request.method,
        "param": request.args,
        "json": request.get_json(silent=True),
        "files": upload_file_name,
        "forms": request.form
    }

print(app.url_map)

# Flask 실행
if __name__ == "__main__":
    # 디버그 : 콘솔에 디버깅 정보 출력
    app.run(debug=True)
    # run -> 개발용 web server + WSGI server + flask 객체 바인딩 -> WSGI server