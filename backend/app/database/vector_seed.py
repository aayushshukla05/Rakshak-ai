import logging
from app.database.vector_store import vector_store

logger = logging.getLogger(__name__)

def seed_threat_intelligence():
    """
    Seeds the TF-IDF in-memory store with basic MITRE ATT&CK and CERT-In 
    threat intelligence reports for RAG correlation.
    """
    logger.info("Seeding threat intelligence vector store...")
    
    docs = [
        "Adversaries may use Valid Accounts to log into a service specifically designed to accept remote connections, such as telnet, SSH, and VNC. (T1078.003)",
        "Lateral Movement via Windows Management Instrumentation (WMI). Adversaries may abuse WMI to execute malicious commands and payloads on remote systems. (T1047)",
        "Data Exfiltration over Alternative Protocol. Attackers exfiltrate data from the target network over DNS or ICMP. (T1048)",
        "CERT-In Advisory: Threat actors observed performing low-and-slow brute force attacks against financial VPN gateways outside of standard business hours.",
        "CERT-In Warning: Insider threat actors using administrative privileges to dump database tables and exfiltrate over encrypted tunnels (SSH)."
    ]
    
    metadatas = [
        {"source": "mitre", "technique_id": "T1078.003", "tactic": "Initial Access"},
        {"source": "mitre", "technique_id": "T1047", "tactic": "Execution"},
        {"source": "mitre", "technique_id": "T1048", "tactic": "Exfiltration"},
        {"source": "cert-in", "advisory_id": "CI-2024-001", "type": "brute_force"},
        {"source": "cert-in", "advisory_id": "CI-2024-002", "type": "insider_threat"}
    ]
    
    ids = [f"intel_{i}" for i in range(len(docs))]
    
    vector_store.initialize()
    vector_store.add_documents(ids=ids, documents=docs, metadatas=metadatas)
    
if __name__ == "__main__":
    seed_threat_intelligence()
