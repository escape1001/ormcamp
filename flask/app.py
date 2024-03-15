# app.py
from flask import Flask, render_template

# Flask 인스턴스
app = Flask(__name__)


@app.route("/")  # URL
def index():
    return render_template(
        "index.html", title="Flask", message="Hello Flask!", data=[1, 2, 3, 4, 5]
    )


if __name__ == "__main__":
    app.run(debug=True)
    # host 직접 지정 app.run(host="127.0.0.1", port="8000", debug=True)