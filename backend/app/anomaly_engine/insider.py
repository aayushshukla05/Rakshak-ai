import logging
import numpy as np
from sklearn.cluster import DBSCAN
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class InsiderThreatDetector:
    """
    Uses DBSCAN clustering to identify outlier users based on their
    behavioral feature vectors. Outliers are assigned higher risk scores.
    """
    def __init__(self, eps: float = 0.5, min_samples: int = 3):
        self.model = DBSCAN(eps=eps, min_samples=min_samples)
        self.is_fitted = False
        
    def extract_features(self, user_features: Dict[str, float]) -> np.ndarray:
        """
        Expects aggregated weekly features for a user.
        e.g. unique_hosts_accessed, total_bytes_sent, after_hours_ratio
        """
        # Normalization/scaling would ideally happen here based on population stats
        return np.array([
            float(user_features.get('unique_hosts_accessed', 0)),
            float(user_features.get('total_bytes_sent', 0)),
            float(user_features.get('after_hours_ratio', 0))
        ])

    def detect_outliers(self, users_data: Dict[str, Dict[str, float]]) -> Dict[str, float]:
        """
        Takes a dict of user_id -> feature_dict.
        Returns a dict of user_id -> risk_score (0.0 for normal, higher for outliers).
        """
        if len(users_data) < self.model.min_samples:
            logger.warning("Not enough users to run DBSCAN clustering. Need at least %d.", self.model.min_samples)
            return {uid: 0.0 for uid in users_data}

        user_ids = list(users_data.keys())
        X = np.vstack([self.extract_features(users_data[uid]) for uid in user_ids])
        
        # In a real pipeline, we'd scale X with StandardScaler here
        
        labels = self.model.fit_predict(X)
        
        # DBSCAN returns -1 for outliers
        risk_scores = {}
        for uid, label in zip(user_ids, labels):
            if label == -1:
                # Basic risk score assigned to outliers
                # Further logic could refine this based on distance to nearest cluster
                risk_scores[uid] = 0.8 
            else:
                risk_scores[uid] = 0.1 # Baseline normal risk
                
        self.is_fitted = True
        return risk_scores

insider_detector = InsiderThreatDetector()
