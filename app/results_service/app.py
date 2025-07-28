from flask import Flask, jsonify
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

@app.route("/results")
def results():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT option, COUNT(*) FROM votes GROUP BY option;")
    result = {opt: count for opt, count in cur.fetchall()}
    cur.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
