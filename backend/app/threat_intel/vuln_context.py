import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class VulnerabilityContextAnalyzer:
    """
    Enriches nodes in the topology with known vulnerabilities (CVEs)
    and performs a gap analysis against active threats.
    """
    def __init__(self):
        # Mock CVE database for the hosts
        self.cve_db = {
            "srv-vpn-01": [
                {"cve": "CVE-2023-46805", "cvss": 8.2, "description": "Authentication bypass"},
                {"cve": "CVE-2024-21887", "cvss": 9.1, "description": "Command injection"}
            ],
            "srv-dc-01": [
                {"cve": "CVE-2020-1472", "cvss": 10.0, "description": "Zerologon privilege escalation"}
            ]
        }

    def enrich_node(self, node_name: str) -> List[Dict[str, Any]]:
        """
        Returns known vulnerabilities for a given node.
        """
        return self.cve_db.get(node_name, [])

    def gap_analysis(self, attack_path: List[str]) -> Dict[str, Any]:
        """
        Analyzes an attack path for exploitable gaps (unpatched CVEs).
        """
        vulnerable_nodes = []
        max_cvss_on_path = 0.0
        
        for node in attack_path:
            cves = self.enrich_node(node)
            if cves:
                vulnerable_nodes.append({
                    "node": node,
                    "cves": cves
                })
                for cve in cves:
                    if cve["cvss"] > max_cvss_on_path:
                        max_cvss_on_path = cve["cvss"]
                        
        risk_level = "CRITICAL" if max_cvss_on_path >= 9.0 else "HIGH" if max_cvss_on_path >= 7.0 else "MEDIUM"
        
        return {
            "path_risk_level": risk_level,
            "max_cvss": max_cvss_on_path,
            "exploitable_nodes": vulnerable_nodes,
            "recommendation": f"Patch the {len(vulnerable_nodes)} vulnerable nodes in the attack path immediately to break the kill chain."
        }

vuln_analyzer = VulnerabilityContextAnalyzer()
