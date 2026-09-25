import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Project</title>
        </head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>DevOps Project</h1>
            <p>This is a basic Flask app for deployment.</p>
            <p>Health check endpoint: /health</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

