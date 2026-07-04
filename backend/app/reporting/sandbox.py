import logging
from typing import Dict, Any, List
from app.anomaly_engine.attack_path import attack_path_analyzer

logger = logging.getLogger(__name__)

class DigitalTwinSandbox:
    """
    Exposes a safe querying layer for SOC Analysts to ask "What If" questions
    against the mock NetworkX topology without affecting live SOAR configurations.
    """
    def simulate_compromise(self, node_id: str) -> Dict[str, Any]:
        """
        Simulates the blast radius and potential paths to crown jewels
        if a specific node is compromised.
        """
        logger.info(f"Sandbox Simulation: Compromise of {node_id}")
        
        blast = attack_path_analyzer.find_blast_radius(node_id, max_depth=4)
        if "error" in blast:
            return blast
            
        # Hardcoded crown jewels for simulation
        crown_jewels = ["srv-db-fin-01", "srv-dc-01"]
        paths = []
        
        for jewel in crown_jewels:
            if jewel == node_id:
                continue
            path = attack_path_analyzer.find_shortest_attack_path(node_id, jewel)
            if path["path_exists"]:
                paths.append({
                    "target": jewel,
                    "steps": path["steps"],
                    "route": path["path"]
                })
                
        return {
            "compromised_node": node_id,
            "blast_radius": blast,
            "critical_paths_exposed": paths,
            "simulation_result": "HIGH RISK" if paths else "MODERATE RISK"
        }

network_sandbox = DigitalTwinSandbox()
