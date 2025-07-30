from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        option = request.form.get("option")
        requests.post("http://vote:5000/vote", json={"option": option})
        return redirect("/results")
    return render_template("index.html")

@app.route("/results")
def results():
    r = requests.get("http://results:5000/results")
    votes = r.json()
    return render_template("results.html", votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
