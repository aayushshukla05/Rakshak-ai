import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SOCWorkloadOptimizer:
    """
    Analyzes SOC analyst workload to demonstrate ROI of autonomous capabilities.
    """
    def __init__(self):
        self.manual_time_per_incident_mins = 45.0
        self.autonomous_time_per_incident_mins = 2.0 # Just reviewing the action taken

    def calculate_roi(self, total_incidents: int, autonomous_resolution_rate: float) -> Dict[str, Any]:
        """
        Calculates time saved by autonomous SOAR.
        """
        autonomous_incidents = total_incidents * autonomous_resolution_rate
        manual_incidents = total_incidents - autonomous_incidents
        
        time_without_ai = total_incidents * self.manual_time_per_incident_mins
        time_with_ai = (manual_incidents * self.manual_time_per_incident_mins) + (autonomous_incidents * self.autonomous_time_per_incident_mins)
        
        hours_saved = (time_without_ai - time_with_ai) / 60.0
        
        return {
            "hours_saved_per_period": round(hours_saved, 2),
            "efficiency_gain_percent": round((hours_saved / (time_without_ai / 60.0)) * 100, 1) if time_without_ai > 0 else 0.0
        }

workload_optimizer = SOCWorkloadOptimizer()
