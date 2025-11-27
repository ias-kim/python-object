from ipaddress import ip_address
from flask import Flask, request, make_response, jsonify

app = Flask(__name__, 
            static_folder="resources/",  # 정적인 파일 설정
            static_url_path="/contents")

# view function
@app.route("/", methods=["GET"])
def home():
    # 플라스크의 반환형은 HTTP Response이다.
    return jsonify({'name': 'ycjung', 'age': '50'})

@app.after_request
# 후처리 들어감.
def post_process(response):
    ### 
    return response

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)