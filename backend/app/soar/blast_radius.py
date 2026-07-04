import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class BlastRadiusAnalyzer:
    def calculate_blast_radius(self, host_id: str) -> Dict[str, Any]:
        """
        Uses Cypher (via NetworkX mock here) to find all downstream dependent services
        and users affected if host_id is isolated.
        Returns a score 0-100.
        """
        # Mock logic based on Feature #3 spec
        if "dc" in host_id.lower() or "db" in host_id.lower():
            score = 85.0
            services = ["svc-payroll", "svc-auth"]
            users = 2400
        else:
            score = 12.0
            services = []
            users = 1
            
        logger.info(f"Calculated blast radius for {host_id}: {score}")
        
        return {
            "score": score,
            "affected_services": services,
            "affected_users": users,
            "action": "ESCALATE" if score >= 50 else "AUTO_ISOLATE"
        }

blast_radius_analyzer = BlastRadiusAnalyzer()
