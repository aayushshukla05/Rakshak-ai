import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class ComplianceMapper:
    def get_compliance_requirements(self, incident_type: str, severity: str) -> List[Dict[str, Any]]:
        """
        Maps an incident type and severity to applicable Indian and international regulations
        like CERT-In reporting (within 6 hrs) and DPDPA notification.
        """
        requirements = []
        if severity.upper() in ["CRITICAL", "HIGH"]:
            requirements.append({
                "regulation": "CERT-In 2022 Directions",
                "action": "Report incident to CERT-In",
                "deadline": "Within 6 hours of noticing",
                "status": "pending"
            })
            requirements.append({
                "regulation": "DPDPA 2023",
                "action": "Data Fiduciary must notify Data Protection Board",
                "deadline": "ASAP",
                "status": "pending"
            })
        return requirements

compliance_mapper = ComplianceMapper()
