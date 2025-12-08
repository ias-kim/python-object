from flask import Flask, jsonify, request, flash, get_flashed_messages
import os 

app = Flask(__name__)
app.secret_key = "test" # 세션 키 값

UPLOAD_PATH = "upload/" # ('/')마지막은 디렉토리
os.makedirs(UPLOAD_PATH, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    msg = get_flashed_messages()
    return jsonify(msg), 200

count = 1
@app.route("/myflash", methods=["GET"])
def myflash():
    global count

    flash(f"flash {count} th")
    
    count += 1

    return "flashed", 200
    # return redirect(url_for('bar')) bar로 이동 및 새롭게 요청
        # 302 -> path for bar view function, /bar

# @app.route("/bar", methods=["GET"])
# def bar():
#     return "welcome bar", 200

# @app.route("/upload", methods=["POST"])
# def upload():
#     file = request.files.get("file1", None)

#     file_name = file.filename
#     file_name = os.path.join(UPLOAD_PATH, file_name)

#     file.save(file_name)

#     return 'file_saved', 200


if __name__ == "__main__":
    app.run(debug=True) 