from flask import Flask, request, jsonify
import psycopg2, os
import requests

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"]
    )

@app.route("/vote", methods=["POST"])
def cast_vote():
    option = request.json.get("option")
    if option not in ["Option A", "Option B"]:
        return jsonify({"error": "Invalid option"}), 400
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO votes (option) VALUES (%s);", (option,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"Vote recorded for {option}."})

@app.route("/votes", methods=["GET"])
def get_votes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT option, COUNT(*) FROM votes GROUP BY option;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({r[0]: r[1] for r in rows})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
