from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

TEMPLATE = """
<h2>Vote for your favorite option</h2>
<form method="post">
  <input type="radio" name="option" value="Option A"> Option A<br>
  <input type="radio" name="option" value="Option B"> Option B<br><br>
  <input type="submit" value="Vote">
</form>
<a href="/results">See Results</a>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        option = request.form.get("option")
        requests.post("http://vote:5000/vote", json={"option": option})
        return redirect("/results")
    return render_template_string(TEMPLATE)

@app.route("/results")
def results():
    r = requests.get("http://results:5000/results")
    votes = r.json()
    return render_template_string(
        "<h2>Results</h2>" +
        "".join(f"<p>{opt}: {count}</p>" for opt, count in votes.items()) +
        '<a href="/">Back to Vote</a>'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
