import logging
from app.database.neo4j_client import neo4j_client

logger = logging.getLogger(__name__)

def seed_network_topology():
    """Seeds the initial network topology (hosts, users, services, zones) into Neo4j."""
    
    # Check if database already has nodes
    check_query = "MATCH (n) RETURN count(n) as count"
    result = neo4j_client.execute_query(check_query)
    if result and result[0]["count"] > 0:
        logger.info("Database is not empty. Skipping seed.")
        return

    logger.info("Seeding network topology into Neo4j...")
    
    seed_queries = [
        # Create Hosts
        "CREATE (:Host {id: 'srv-web-01', ip: '10.0.0.10', hostname: 'WebServer', type: 'server', os: 'Linux', zone: 'dmz', sensitivity: 'medium', cve_list: ['CVE-2023-38408'], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-vpn-01', ip: '10.0.0.20', hostname: 'VPNGateway', type: 'vpn_gateway', os: 'FortiOS', zone: 'dmz', sensitivity: 'high', cve_list: ['CVE-2024-21762'], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-dc-01', ip: '10.0.1.10', hostname: 'DomainController', type: 'server', os: 'Windows Server 2019', zone: 'internal', sensitivity: 'critical', cve_list: [], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-email-01', ip: '10.0.1.20', hostname: 'EmailServer', type: 'server', os: 'Linux', zone: 'internal', sensitivity: 'high', cve_list: [], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-db-fin-01', ip: '10.0.1.30', hostname: 'FinanceDB', type: 'server', os: 'Linux', zone: 'internal', sensitivity: 'critical', cve_list: [], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-hr-01', ip: '10.0.1.40', hostname: 'HRApp', type: 'server', os: 'Linux', zone: 'internal', sensitivity: 'medium', cve_list: [], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'srv-file-01', ip: '10.0.1.50', hostname: 'FileServer', type: 'server', os: 'Windows Server 2019', zone: 'internal', sensitivity: 'medium', cve_list: [], is_honeypot: true, status: 'active'})", # Contains honeypot share
        "CREATE (:Host {id: 'srv-scada-01', ip: '10.0.2.10', hostname: 'SCADAController', type: 'server', os: 'Windows', zone: 'ot', sensitivity: 'critical', cve_list: [], is_honeypot: false, status: 'active'})",
        
        # Workstations (just a few for mock)
        "CREATE (:Host {id: 'ws-user-01', ip: '10.0.3.15', hostname: 'WS-Rajesh', type: 'workstation', os: 'Windows 11', zone: 'internal', sensitivity: 'low', cve_list: [], is_honeypot: false, status: 'active'})",
        "CREATE (:Host {id: 'ws-admin-01', ip: '10.0.3.100', hostname: 'WS-Admin1', type: 'workstation', os: 'Windows 11', zone: 'internal', sensitivity: 'high', cve_list: [], is_honeypot: false, status: 'active'})",

        # Create Users
        "CREATE (:User {id: 'u-rajesh', username: 'rajesh.kumar', department: 'Finance', role: 'analyst', risk_score: 0.1, is_honeypot: false})",
        "CREATE (:User {id: 'u-admin1', username: 'sysadmin', department: 'IT', role: 'admin', risk_score: 0.05, is_honeypot: false})",
        "CREATE (:User {id: 'u-fake-admin', username: 'backup_admin', department: 'IT', role: 'admin', risk_score: 0.0, is_honeypot: true})",

        # Create Services
        "CREATE (:Service {id: 'svc-payroll', name: 'Payroll Processing', criticality: 'critical', active_users: 2400, financial_value: 42000000.0, sla_hours: 6})",
        "CREATE (:Service {id: 'svc-scada', name: 'Grid Control', criticality: 'critical', active_users: 10, financial_value: 100000000.0, sla_hours: 1})",

        # Create Relationships
        "MATCH (u:User {id: 'u-rajesh'}), (h:Host {id: 'ws-user-01'}) CREATE (u)-[:AUTHENTICATES_TO {last_login: '2026-07-04T08:00:00Z', frequency: 'daily'}]->(h)",
        "MATCH (h1:Host {id: 'ws-user-01'}), (h2:Host {id: 'srv-db-fin-01'}) CREATE (h1)-[:CONNECTS_TO {port: 1433, protocol: 'TCP', firewall_rule: 'allow', segmented: false}]->(h2)",
        "MATCH (h1:Host {id: 'srv-vpn-01'}), (h2:Host {id: 'srv-dc-01'}) CREATE (h1)-[:CONNECTS_TO {port: 443, protocol: 'TCP', firewall_rule: 'allow', segmented: false}]->(h2)",
        "MATCH (h:Host {id: 'srv-db-fin-01'}), (s:Service {id: 'svc-payroll'}) CREATE (h)-[:RUNS {port: 1433, process: 'mssql'}]->(s)",
        "MATCH (h:Host {id: 'srv-scada-01'}), (s:Service {id: 'svc-scada'}) CREATE (h)-[:RUNS {port: 502, process: 'modbus'}]->(s)",
        
        # More realistic connections for lateral movement
        "MATCH (h1:Host {id: 'srv-web-01'}), (h2:Host {id: 'srv-db-fin-01'}) CREATE (h1)-[:CONNECTS_TO {port: 1433, protocol: 'TCP', firewall_rule: 'allow', segmented: true}]->(h2)",
        "MATCH (h1:Host {id: 'srv-dc-01'}), (h2:Host {id: 'srv-file-01'}) CREATE (h1)-[:CONNECTS_TO {port: 445, protocol: 'TCP', firewall_rule: 'allow', segmented: false}]->(h2)",
    ]

    for query in seed_queries:
        neo4j_client.execute_query(query)
        
    logger.info("Successfully seeded network topology.")

if __name__ == "__main__":
    seed_network_topology()
