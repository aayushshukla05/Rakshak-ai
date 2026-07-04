import networkx as nx
import logging
from typing import List, Dict, Any
from app.database.neo4j_client import neo4j_client

logger = logging.getLogger(__name__)

class AttackPathAnalyzer:
    """
    Analyzes potential attack paths using NetworkX graph heuristics 
    (Fallback for GNN architecture).
    """
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def sync_from_database(self):
        """
        Pulls topology from Neo4j and loads it into NetworkX for fast
        heuristic path analysis.
        """
        if not neo4j_client.driver:
            logger.warning("Neo4j client not connected. Using empty graph.")
            return
            
        try:
            query = """
            MATCH (n)
            OPTIONAL MATCH (n)-[r]->(m)
            RETURN id(n) as source_id, labels(n) as source_labels, n.name as source_name,
                   type(r) as edge_type,
                   id(m) as target_id, labels(m) as target_labels, m.name as target_name
            """
            
            with neo4j_client.driver.session() as session:
                result = session.run(query)
                self.graph.clear()
                
                for record in result:
                    src_id = record["source_name"] or str(record["source_id"])
                    
                    if src_id not in self.graph:
                        self.graph.add_node(src_id, labels=record["source_labels"])
                        
                    tgt_id = record["target_name"] or (str(record["target_id"]) if record["target_id"] else None)
                    
                    if tgt_id:
                        if tgt_id not in self.graph:
                            self.graph.add_node(tgt_id, labels=record["target_labels"])
                        self.graph.add_edge(src_id, tgt_id, type=record["edge_type"])
                        
            logger.info(f"Synced NetworkX graph: {self.graph.number_of_nodes()} nodes, {self.graph.number_of_edges()} edges")
        except Exception as e:
            logger.error(f"Error syncing graph from Neo4j: {e}")
            
    def find_blast_radius(self, compromised_node_name: str, max_depth: int = 3) -> Dict[str, Any]:
        """
        Calculates the theoretical blast radius if a specific node is compromised,
        using BFS up to a certain depth.
        """
        if compromised_node_name not in self.graph:
            return {"error": "Node not found in topology graph."}
            
        reachable = nx.single_source_shortest_path_length(self.graph, compromised_node_name, cutoff=max_depth)
        
        # Calculate a theoretical risk score based on PageRank of compromised node
        try:
            pr = nx.pagerank(self.graph)
            node_centrality = pr.get(compromised_node_name, 0.0)
        except Exception:
            node_centrality = 0.0
            
        return {
            "compromised_node": compromised_node_name,
            "blast_radius_nodes": list(reachable.keys()),
            "impact_score": node_centrality * len(reachable),
            "depth_analyzed": max_depth
        }
        
    def find_shortest_attack_path(self, source_name: str, crown_jewel_name: str) -> Dict[str, Any]:
        """
        Finds the shortest path from a compromised host to a critical asset.
        """
        if source_name not in self.graph or crown_jewel_name not in self.graph:
            return {"error": "Source or Target node not found in graph."}
            
        try:
            path = nx.shortest_path(self.graph, source=source_name, target=crown_jewel_name)
            return {
                "path_exists": True,
                "path": path,
                "steps": len(path) - 1
            }
        except nx.NetworkXNoPath:
            return {
                "path_exists": False,
                "path": [],
                "steps": 0
            }

attack_path_analyzer = AttackPathAnalyzer()
