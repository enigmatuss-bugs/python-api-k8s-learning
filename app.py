import os
import socket
from flask import Flask, jsonify, request

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "local")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
API_KEY = os.getenv("API_KEY")


@app.get("/")
def home():
    return jsonify({
        "message": "Hello from Kubernetes!",
        "hostname": socket.gethostname(),
        "version": "3.0",
        "environment": APP_ENV,
        "log_level": LOG_LEVEL
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/protected")
def protected():
    if not API_KEY or request.headers.get("X-API-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Access granted!"})

@app.route("/version")
def version():
    return {
        "version": "2.0",
        "message": "Deployed automatically using GitHub Actions and Argo CD"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
