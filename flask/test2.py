from ipaddress import ip_address
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# view function
@app.route("/", methods=["GET"])
def home():
    data = request.get_json(silent=True)
    required_keys = ["name", "age"]
    
    missing_keys = [key for key in required_keys if key not in data]
    print(missing_keys)

    # 이 네개의 틀은 백엔드 프레임워크에 공통적이다.
    print(request.args.get('page', default=1, type=int)) # 파라미터 정보를 갖고오는 것만 생각하면 된다.
    print(request.headers['content-type'])
    print(request.form.get("yju") or "Yeungjin")
    print(data)
    return "hello flask"

@app.after_request
# 후처리 들어감.
def post_process(response):
    ### 
    return response

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)