import logging
from typing import Dict, Any, List
from app.database.vector_store import vector_store

logger = logging.getLogger(__name__)

class ThreatCorrelationEngine:
    """
    RAG Pipeline that correlates raw anomalies with Threat Intelligence
    from MITRE ATT&CK and CERT-In.
    """
    def __init__(self):
        # In a real environment, we would also initialize an LLM client here
        # e.g., self.llm_client = GeminiClient(...)
        pass
        
    def correlate_anomaly(self, anomaly_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Takes an anomaly detection result, queries the vector store,
        and generates a correlated threat report.
        """
        # Create a search query based on the anomaly features
        alarms = anomaly_data.get("alarms", [])
        if not alarms and "feature" in anomaly_data:
            alarms = [anomaly_data["feature"]]
            
        search_query = f"Anomaly detected involving: {', '.join(alarms)}."
        if anomaly_data.get("bytes_sent", 0) > 1000000:
            search_query += " High data transfer volume."
            
        # Retrieve context from Vector Store
        retrieved_docs = vector_store.search(search_query, n_results=2)
        
        contexts = []
        if retrieved_docs["documents"] and len(retrieved_docs["documents"]) > 0:
            # Flatten the nested list
            flat_docs = retrieved_docs["documents"][0]
            flat_metas = retrieved_docs["metadatas"][0]
            
            for doc, meta in zip(flat_docs, flat_metas):
                contexts.append({
                    "content": doc,
                    "source": meta.get("source", "unknown"),
                    "technique": meta.get("technique_id", "N/A")
                })
                
        # Simulate LLM synthesis
        synthesis = "Based on the telemetry, this behavior aligns with "
        if contexts:
            synthesis += f"{contexts[0]['source'].upper()} intel regarding {contexts[0]['technique']}."
        else:
            synthesis += "an unknown threat vector."
            
        return {
            "query": search_query,
            "retrieved_context": contexts,
            "synthesis": synthesis,
            "recommended_action": "Isolate the host and rotate valid accounts immediately." if contexts else "Investigate host behavior for further context."
        }

threat_correlator = ThreatCorrelationEngine()
