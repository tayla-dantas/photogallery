from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import base64, json, BotoApi

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", images=BotoApi.awsDownload())

@app.route("/store",  methods = ['POST'] )
def store():
    json_data = request.json
    base64String = json_data["img"]
    image = base64String.replace("data:image/jpeg;base64,", "")
    BotoApi.awsUpload(image)
    return "JSON value sent: " + image

@app.route("/retrieve")
def retrieve():
    jsonString = json.dumps(BotoApi.awsDownload())
    return jsonString


if __name__ == "__main__":
    app.run(debug=True)