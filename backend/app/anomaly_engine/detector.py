import logging
import numpy as np
from pyod.models.iforest import IForest
from typing import List, Dict, Any
from app.models.schemas import TelemetryEvent

logger = logging.getLogger(__name__)

class AnomalyDetector:
    def __init__(self):
        self.model = IForest(contamination=0.05, random_state=42)
        self.is_fitted = False
        
    def extract_features(self, event: TelemetryEvent) -> np.ndarray:
        """
        Extract numerical features from TelemetryEvent for the Isolation Forest.
        Features: port, bytes_sent, bytes_received, protocol_encoded
        """
        port = float(event.port) if event.port else 0.0
        bytes_sent = float(event.bytes_sent) if event.bytes_sent else 0.0
        bytes_received = float(event.bytes_received) if event.bytes_received else 0.0
        
        # Simple encoding for protocol
        proto_map = {"tcp": 1.0, "udp": 2.0, "icmp": 3.0}
        protocol = proto_map.get(event.protocol.lower() if event.protocol else "", 0.0)
        
        return np.array([port, bytes_sent, bytes_received, protocol])
        
    def fit(self, events: List[TelemetryEvent]):
        logger.info(f"Training Isolation Forest on {len(events)} events...")
        X = np.vstack([self.extract_features(e) for e in events])
        self.model.fit(X)
        self.is_fitted = True
        logger.info("Training complete.")
        
    def predict(self, event: TelemetryEvent) -> Dict[str, Any]:
        if not self.is_fitted:
            # If not fitted, everything is normal or we just simulate
            return {"is_anomaly": False, "score": 0.0}
            
        X = self.extract_features(event).reshape(1, -1)
        pred = self.model.predict(X)[0]
        score = self.model.decision_function(X)[0]
        
        # Normalize score roughly between 0 and 1 for UI
        normalized_score = min(max(float(score) / 0.5, 0.0), 1.0)
        
        return {
            "is_anomaly": bool(pred == 1),
            "score": normalized_score,
            "raw_score": float(score)
        }

anomaly_detector = AnomalyDetector()
