#Code for the Python section of the app: 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    start = None
    destination = None

    if request.method == "POST":
        start = request.form["start"]
        destination = request.form["destination"]

    return render_template("index.html", start=start, destination=destination)

if __name__ == "__main__":
    app.run(debug=True)
