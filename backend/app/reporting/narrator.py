import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class ThreatNarrator:
    """
    Synthesizes multiple individual anomalies and SOAR actions into a single
    coherent attack narrative timeline.
    """
    def __init__(self):
        self.active_campaigns = {}

    def ingest_event(self, timestamp: str, event_type: str, details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Takes an event (anomaly or SOAR action) and attaches it to an ongoing narrative.
        """
        # Simplistic grouping logic based on target or source IP/host
        target = details.get("target") or details.get("compromised_node") or details.get("host_id", "unknown")
        
        if target not in self.active_campaigns:
            self.active_campaigns[target] = {
                "campaign_id": f"campaign_{target}",
                "target": target,
                "timeline": [],
                "current_risk": "LOW"
            }
            
        campaign = self.active_campaigns[target]
        campaign["timeline"].append({
            "timestamp": timestamp,
            "type": event_type,
            "description": self._generate_description(event_type, details)
        })
        
        # Escalate risk if isolation occurs or critical vuln found
        if event_type == "soar_action" and details.get("action") == "isolate_host":
            campaign["current_risk"] = "CRITICAL"
            
        return campaign
        
    def _generate_description(self, event_type: str, details: Dict[str, Any]) -> str:
        if event_type == "anomaly":
            return f"Detected anomalous behavior: {', '.join(details.get('alarms', []))}."
        elif event_type == "soar_action":
            return f"Autonomous action taken: {details.get('action')}. {details.get('message', '')}"
        elif event_type == "intel_match":
            return f"Threat Intel correlated: {details.get('synthesis')}"
        return str(details)
        
    def get_narrative(self, target: str) -> Dict[str, Any]:
        return self.active_campaigns.get(target, {})

threat_narrator = ThreatNarrator()
