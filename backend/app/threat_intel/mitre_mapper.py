import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class MitreMapper:
    """
    Maps observed anomalies to MITRE ATT&CK tactics and techniques using heuristic rules.
    """
    def __init__(self):
        # A simple ruleset linking anomaly types to MITRE techniques
        self.rules = {
            "high_data_transfer": {
                "tactic": "Exfiltration",
                "technique": "T1048",
                "name": "Exfiltration Over Alternative Protocol"
            },
            "unusual_auth_failures": {
                "tactic": "Credential Access",
                "technique": "T1110",
                "name": "Brute Force"
            },
            "lateral_movement_scan": {
                "tactic": "Lateral Movement",
                "technique": "T1021",
                "name": "Remote Services"
            },
            "after_hours_db_access": {
                "tactic": "Collection",
                "technique": "T1560",
                "name": "Archive Collected Data"
            }
        }

    def map_anomalies(self, anomaly_labels: List[str]) -> List[Dict[str, str]]:
        """
        Takes a list of anomaly string labels and returns MITRE mapping dicts.
        """
        mappings = []
        for label in anomaly_labels:
            if label in self.rules:
                mappings.append(self.rules[label])
            else:
                # Default unknown mapping
                mappings.append({
                    "tactic": "Unknown",
                    "technique": "T0000",
                    "name": "Uncategorized Anomaly"
                })
        return mappings

mitre_mapper = MitreMapper()
