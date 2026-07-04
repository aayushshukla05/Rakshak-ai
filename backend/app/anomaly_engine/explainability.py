import shap
import numpy as np
import logging
from typing import Dict, Any, List
from app.anomaly_engine.detector import anomaly_detector
from app.models.schemas import TelemetryEvent

logger = logging.getLogger(__name__)

class AnomalyExplainer:
    def __init__(self):
        self.explainer = None
        self.feature_names = ["port", "bytes_sent", "bytes_received", "protocol"]
        
    def initialize(self, background_events: List[TelemetryEvent]):
        if not anomaly_detector.is_fitted:
            logger.warning("Cannot initialize SHAP explainer before detector is fitted.")
            return
            
        # Extract features for background dataset
        background_data = np.vstack([anomaly_detector.extract_features(e) for e in background_events])
        
        # We use TreeExplainer for Isolation Forest
        try:
            self.explainer = shap.TreeExplainer(anomaly_detector.model)
            logger.info("SHAP explainer initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize SHAP explainer: {e}")
            
    def explain(self, event: TelemetryEvent) -> Dict[str, Any]:
        if not self.explainer:
            return {"error": "Explainer not initialized"}
            
        features = anomaly_detector.extract_features(event).reshape(1, -1)
        
        try:
            shap_values = self.explainer.shap_values(features)
            # shap_values could be a list or array depending on the exact model
            if isinstance(shap_values, list):
                values = shap_values[1][0].tolist() # class 1
            else:
                values = shap_values[0].tolist()
                
            contributions = [
                {"feature": name, "value": float(val), "impact": float(shap_val)}
                for name, val, shap_val in zip(self.feature_names, features[0], values)
            ]
            
            # Sort by absolute impact
            contributions.sort(key=lambda x: abs(x["impact"]), reverse=True)
            
            return {
                "base_value": float(self.explainer.expected_value[1] if isinstance(self.explainer.expected_value, (list, np.ndarray)) else self.explainer.expected_value),
                "contributions": contributions
            }
        except Exception as e:
            logger.error(f"Failed to generate SHAP explanation: {e}")
            return {"error": str(e)}

anomaly_explainer = AnomalyExplainer()
