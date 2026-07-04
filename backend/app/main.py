from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.telemetry.replayer import telemetry_replayer

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Rakshak.AI - Cyber Resilience Platform for CNI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Rakshak.AI API"}

@app.websocket("/api/v1/telemetry/stream")
async def websocket_telemetry_endpoint(websocket: WebSocket):
    await telemetry_replayer.connect(websocket)
    try:
        while True:
            # Keep connection alive and listen for client messages if needed
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        telemetry_replayer.disconnect(websocket)

@app.post("/api/v1/telemetry/replay/start")
def start_replay(dataset: str = "lanl", speed_factor: float = 100.0):
    return telemetry_replayer.start_replay(dataset, speed_factor)

@app.post("/api/v1/telemetry/replay/stop")
def stop_replay():
    return telemetry_replayer.stop_replay()

@app.get("/api/v1/telemetry/replay/status")
def replay_status():
    return telemetry_replayer.status()

from app.soar.orchestrator import soar_orchestrator
from pydantic import BaseModel
from typing import Dict, Any

class ThreatReport(BaseModel):
    synthesis: str
    query: str = ""
    path_risk_level: str = "LOW"
    
@app.post("/api/v1/soar/respond")
def trigger_soar_response(report: ThreatReport):
    decision = soar_orchestrator.evaluate_and_respond(report.dict())
    return {"decision": decision}
    
@app.get("/api/v1/soar/history")
def get_soar_history():
    return {"history": soar_orchestrator.decision_history}
