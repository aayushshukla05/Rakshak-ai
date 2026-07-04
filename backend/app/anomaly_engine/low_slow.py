import logging
import numpy as np
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class LowSlowDetector:
    """
    Implements CUSUM (Cumulative Sum) algorithm to detect low-and-slow
    behavioral shifts over time.
    """
    def __init__(self, threshold: float = 4.0, slack: float = 0.5):
        self.threshold = threshold
        self.slack = slack
        # Store state per user: {user_id: {"cusum": {"feature": S_t}, "baseline": {"feature": (mean, std)}}}
        self.state = {}

    def update_baseline(self, user_id: str, historical_features: List[Dict[str, float]]):
        """
        Calculates the baseline mean and standard deviation for a user's features
        based on their first N days (e.g., 7 days) of activity.
        """
        if not historical_features:
            return

        baseline = {}
        # Aggregate all feature keys
        keys = historical_features[0].keys()
        for key in keys:
            values = [day[key] for day in historical_features]
            mean = np.mean(values)
            std = np.std(values) if np.std(values) > 0 else 1.0 # Prevent div by zero
            baseline[key] = (mean, std)

        if user_id not in self.state:
            self.state[user_id] = {"cusum": {k: 0.0 for k in keys}, "baseline": baseline}
        else:
            self.state[user_id]["baseline"] = baseline

    def process_daily_features(self, user_id: str, daily_features: Dict[str, float]) -> Dict[str, Any]:
        """
        Processes a new day's worth of features. Returns an alert if CUSUM triggers
        on 2 or more features.
        """
        if user_id not in self.state or "baseline" not in self.state[user_id]:
            # No baseline yet, can't detect anomaly
            return {"is_anomaly": False, "reason": "No baseline established"}

        baseline = self.state[user_id]["baseline"]
        cusum_state = self.state[user_id]["cusum"]
        
        alarms_triggered = []

        for feature, value in daily_features.items():
            if feature not in baseline:
                continue
                
            mean, std = baseline[feature]
            # Normalize the value
            z_score = (value - mean) / std
            
            # CUSUM formula: S_t = max(0, S_{t-1} + (z_score - slack))
            new_cusum = max(0, cusum_state.get(feature, 0.0) + (z_score - self.slack))
            cusum_state[feature] = new_cusum
            
            if new_cusum > self.threshold:
                alarms_triggered.append(feature)
                # Reset CUSUM after alarm
                cusum_state[feature] = 0.0

        is_anomaly = len(alarms_triggered) >= 2

        return {
            "is_anomaly": is_anomaly,
            "alarms": alarms_triggered,
            "mitre_mapping": ["T1018", "T1083"] if is_anomaly else []
        }

low_slow_detector = LowSlowDetector()
