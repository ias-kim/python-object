from ipaddress import ip_address
from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_PATH = "upload/"
os.makedirs(UPLOAD_PATH, exist_ok=True)
# view function
@app.route("/", methods=["GET", "POST"])
def home():

    files = request.files.get("gsc")

    # 1) 
    file_name = files.filename # 유효성 검사

    import time 

    #file_name = secure_filename(file_name)  # path 저장 경로
    file_name = time.strftime("%Y%M%D") # 년 월 일 시간정보 
    # 또한 uuid 정보도 가능!
    file_name = os.path.join(UPLOAD_PATH, file_name)

    files.save(file_name) # 파일 이동

    # DB에 파일 정보 저장

    print(f"files: {files}, file_name: {file_name}")

    return "hello flask"

@app.after_request
# 후처리 들어감.
def post_process(response):
    ### 
    return response

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)