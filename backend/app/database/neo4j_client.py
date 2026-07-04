import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from app.config import settings

logger = logging.getLogger(__name__)

class Neo4jClient:
    def __init__(self, uri, user, password):
        self._driver = None
        try:
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
            logger.info("Connected to Neo4j database")
        except Exception as e:
            logger.error(f"Failed to create Neo4j driver: {e}")

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def execute_query(self, query, parameters=None, db=None):
        if not self._driver:
            logger.error("Driver not initialized")
            return []
            
        assert self._driver is not None
        
        try:
            with self._driver.session(database=db) as session:
                result = session.run(query, parameters)
                return [record for record in result]
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return []
            
    def run_write_transaction(self, transaction_func, *args, **kwargs):
        if not self._driver:
            logger.error("Driver not initialized")
            return None
            
        with self._driver.session() as session:
            try:
                result = session.execute_write(transaction_func, *args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Transaction failed: {e}")
                return None

# Singleton instance
neo4j_client = Neo4jClient(
    uri=settings.NEO4J_URI,
    user=settings.NEO4J_USER,
    password=settings.NEO4J_PASSWORD
)
