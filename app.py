from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def uploadPhotos():
    #### colocar aqui o amazon s3 
    return 


if __name__ == "__main__":
    app.run(debug=True)