from flask import Flask, jsonify, request, Response
import uuid
import time

app = Flask(__name__)

MESSAGES = []


def error(code: str, message: str, status: int) -> tuple[Response, int]:
    return jsonify({"error": code, "message": message}), status


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/messages", methods=["POST"])
def post_message():
    data = request.get_json(silent=True)

    if not data:
        return error("invalid_request", "Missing JSON body", 400)

    if "type" not in data or "content" not in data or "sender" not in data:
        return error("invalid_request", "Missing required fields", 400)

    message = {
        "id": str(uuid.uuid4()),
        "type": data["type"],
        "sender": data["sender"],
        "timestamp": int(time.time()),
        "content": data["content"],
    }

    MESSAGES.append(message)

    return jsonify({"id": message["id"], "timestamp": message["timestamp"]}), 201


@app.route("/messages", methods=["GET"])
def get_messages():
    since = request.args.get("since", type=int)
    if since is None:
        return jsonify(MESSAGES), 200

    filtered = [m for m in MESSAGES if m["timestamp"] > since]
    return jsonify(filtered), 200
