from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", sub_num="01")

if __name__ == "__main__":
    app.run()
