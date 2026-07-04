import asyncio
import pandas as pd
import logging
from typing import Optional, List
from fastapi import WebSocket
from app.telemetry.parser import TelemetryParser
import json

logger = logging.getLogger(__name__)

class TelemetryReplayer:
    def __init__(self):
        self.is_running = False
        self.speed_factor = 100.0
        self.dataset = "lanl" # or "unsw"
        self.connected_clients: List[WebSocket] = []
        self._current_task: Optional[asyncio.Task] = None

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connected_clients.append(websocket)
        logger.info(f"Client connected to telemetry stream. Total clients: {len(self.connected_clients)}")

    def disconnect(self, websocket: WebSocket):
        self.connected_clients.remove(websocket)
        logger.info(f"Client disconnected. Total clients: {len(self.connected_clients)}")

    async def broadcast(self, message: dict):
        for connection in self.connected_clients:
            try:
                await connection.send_text(json.dumps(message))
            except Exception as e:
                logger.error(f"Failed to send to client: {e}")
                self.disconnect(connection)

    async def _replay_loop(self):
        logger.info(f"Starting replay for {self.dataset} at {self.speed_factor}x speed")
        try:
            # Note: In a real environment, we'd load the full CSV here.
            # For demonstration, we'll simulate events if the CSV isn't found.
            # Ideally load from data/lanl/auth_sample.csv
            
            # Simulated dummy loop
            while self.is_running:
                event = {
                    "event_id": "dummy-uuid",
                    "timestamp": "2026-07-04T08:00:00Z",
                    "source_ip": "10.0.3.15",
                    "destination_ip": "10.0.1.30",
                    "source_user": "rajesh.kumar",
                    "destination_host": "FinanceDB",
                    "auth_result": "Success"
                }
                await self.broadcast(event)
                await asyncio.sleep(1.0 / self.speed_factor)
                
        except Exception as e:
            logger.error(f"Replay loop error: {e}")
        finally:
            self.is_running = False
            logger.info("Replay loop stopped")

    def start_replay(self, dataset: str = "lanl", speed_factor: float = 100.0):
        if self.is_running:
            logger.warning("Replay is already running")
            return {"status": "already_running"}
            
        self.dataset = dataset
        self.speed_factor = speed_factor
        self.is_running = True
        self._current_task = asyncio.create_task(self._replay_loop())
        return {"status": "started", "dataset": dataset, "speed": speed_factor}

    def stop_replay(self):
        self.is_running = False
        if self._current_task:
            self._current_task.cancel()
        return {"status": "stopped"}
        
    def status(self):
        return {
            "is_running": self.is_running,
            "dataset": self.dataset,
            "speed_factor": self.speed_factor,
            "connected_clients": len(self.connected_clients)
        }

telemetry_replayer = TelemetryReplayer()
