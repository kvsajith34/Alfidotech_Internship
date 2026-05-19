from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Alfido Tech DevOps Internship</h1><p>Flask app is running in Docker!</p>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "flask-app"})

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "alfidodb"),
            user=os.getenv("DB_USER", "alfido"),
            password=os.getenv("DB_PASSWORD", "alfido123")
        )
        conn.close()
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"database": "error", "detail": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
