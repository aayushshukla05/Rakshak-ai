import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SOCMetricsEngine:
    """
    Calculates SOC efficiency and workload metrics (MTTD, MTTR).
    """
    def __init__(self):
        # In memory storage for the mock
        self.incidents = []
        
    def record_incident(self, detection_time: float, resolution_time: float, autonomous: bool):
        self.incidents.append({
            "detection_time": detection_time,
            "resolution_time": resolution_time,
            "autonomous": autonomous
        })
        
    def calculate_metrics(self) -> Dict[str, Any]:
        """
        Returns average MTTD and MTTR, showing the delta between manual and autonomous responses.
        """
        if not self.incidents:
            return {"mttd": 0, "mttr": 0, "autonomous_resolution_rate": 0.0}
            
        total_mttd = 0
        total_mttr = 0
        autonomous_count = 0
        
        for inc in self.incidents:
            # Assuming times are relative to start of attack in seconds
            total_mttd += inc["detection_time"]
            total_mttr += inc["resolution_time"]
            if inc["autonomous"]:
                autonomous_count += 1
                
        count = len(self.incidents)
        return {
            "mttd_seconds": total_mttd / count,
            "mttr_seconds": total_mttr / count,
            "autonomous_resolution_rate": autonomous_count / count,
            "total_incidents": count
        }

soc_metrics = SOCMetricsEngine()
