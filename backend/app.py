from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/response")
def response():
    return render_template("response.html")


if __name__ == "__main__":
    app.run(debug=True)