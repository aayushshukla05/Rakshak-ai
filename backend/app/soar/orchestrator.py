import logging
from typing import Dict, Any, List
from app.soar.playbooks import playbooks

logger = logging.getLogger(__name__)

class SOAROrchestrator:
    """
    Simulates a LangGraph-style state machine for autonomous response.
    Based on threat intelligence context and risk scores, it automatically
    selects and executes playbooks.
    """
    def __init__(self):
        self.decision_history = []
        
    def evaluate_and_respond(self, threat_report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Takes a synthesized threat report from the RAG engine and
        decides on an automated response.
        """
        synthesis = threat_report.get("synthesis", "").lower()
        query = threat_report.get("query", "").lower()
        
        response_taken = None
        
        # Decision Logic (simulating an LLM Agent's output routing)
        if "brute force" in synthesis or "brute force" in query:
            # For brute force from an external entity, we route to honeypot
            response_taken = playbooks.route_to_honeypot(attacker_ip="192.168.1.100", context=threat_report)
            
        elif "exfiltration" in synthesis or "insider" in synthesis:
            # High risk internal threat requires immediate isolation
            response_taken = playbooks.isolate_host(host_id="srv-db-fin-01", context=threat_report)
            
        elif "critical" in str(threat_report.get("path_risk_level", "")).lower():
            # If gap analysis shows critical attack path, isolate the source
            response_taken = playbooks.isolate_host(host_id="ws-user-01", context=threat_report)
            
        else:
            response_taken = {
                "status": "pending",
                "action": "manual_review",
                "message": "Confidence too low for autonomous action. Sent to SOC analyst."
            }
            
        self.decision_history.append({
            "report": threat_report,
            "decision": response_taken
        })
        
        return response_taken

soar_orchestrator = SOAROrchestrator()
