# app.py
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=("GET", "POST"))
def test():
    if request.method == "POST":
        # args 보기
        print(request.args)
        # form 보기
        print(request.form)
        # name 필드 보기
        print(request.form.get("name"))
        return "POST request"
    else:
        # args 보기
        print(request.args)
        # form 보기
        print(request.form)
        # name 필드 보기
        print(request.args.get("name"))
        return "GET request"


if __name__ == "__main__":
    app.run(debug=True)
