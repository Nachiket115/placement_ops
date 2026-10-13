from pathlib import Path
from datetime import datetime
import uuid
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
FRONTEND = Path(__file__).resolve().parents[1] / "frontend"

def _read_csv(name):
    return pd.read_csv(DATA / name).fillna("")

def create_app():
    app = Flask(__name__, static_folder=str(FRONTEND), static_url_path="")

    @app.get("/")
    def home():
        return send_from_directory(FRONTEND, "index.html")

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    @app.get("/api/interviews")
    def interviews():
        rows = _read_csv("interviews.csv").to_dict(orient="records")
        return jsonify(rows)

    @app.get("/api/interviews/<interview_id>")
    def interview_detail(interview_id):
        interviews = _read_csv("interviews.csv")
        row = interviews[interviews["interview_id"] == interview_id]
        if row.empty:
            return jsonify({"error": "interview not found"}), 404
        events = _read_csv("interview_events.csv")
        actions = _read_csv("operations_actions.csv")
        return jsonify({
            "interview": row.iloc[0].to_dict(),
            "events": events[events["interview_id"] == interview_id].to_dict(orient="records"),
            "actions": actions[actions["interview_id"] == interview_id].to_dict(orient="records"),
        })

    @app.get("/api/actions")
    def actions():
        return jsonify(_read_csv("operations_actions.csv").to_dict(orient="records"))

    @app.post("/api/actions")
    def create_action():
        payload = request.get_json(force=True) or {}
        if not payload.get("interview_id") or not payload.get("action_type"):
            return jsonify({"error": "interview_id and action_type are required"}), 400
        path = DATA / "operations_actions.csv"
        actions = _read_csv("operations_actions.csv")
        new_row = {
            "action_id": f"ACT-{uuid.uuid4().hex[:8]}",
            "interview_id": payload["interview_id"],
            "action_type": payload["action_type"],
            "action_time": datetime.now().isoformat(timespec="minutes"),
            "performed_by": payload.get("performed_by", "student_demo"),
            "reason": payload.get("reason", ""),
            "notes": payload.get("notes", ""),
        }
        actions = pd.concat([actions, pd.DataFrame([new_row])], ignore_index=True)
        actions.to_csv(path, index=False)
        return jsonify({"status": "recorded", "action": new_row}), 201

    return app
