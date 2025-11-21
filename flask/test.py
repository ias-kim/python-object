from flask import Flask, Response

app = Flask(__name__)

@app.before_request
def prt_log():
    print("log")

# Path : /, Method: Get or Post
@app.route("/", methods=["GET", "POST"])
def home():
    return "hello flask", 200, {"GSC": "gsc"}

@app.route("/student/<int:id>", methods=["GET"])
def student(id):
    return f"Student ID: {id}"

@app.after_request
def prt_after(rsp: Response):
    print(rsp.headers.get('GSC'))
    return rsp

@app.teardown_request
def teardown(e:Exception):
    print(e)

if __name__ == "__main__":
    app.run(debug=True)
