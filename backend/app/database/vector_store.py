import logging
from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

logger = logging.getLogger(__name__)

class VectorStore:
    """
    In-memory TF-IDF based vector store for Threat Intelligence correlation.
    (Mocking ChromaDB to avoid heavy C++ compilation dependencies on macOS Python 3.13)
    """
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.documents = []
        self.metadatas = []
        self.ids = []
        self.tfidf_matrix = None
        
    def initialize(self, collection_name: str = "threat_intel"):
        logger.info(f"Initialized In-Memory TF-IDF Store, collection: {collection_name}")

    def add_documents(self, ids: List[str], documents: List[str], metadatas: List[Dict[str, Any]]):
        self.ids.extend(ids)
        self.documents.extend(documents)
        self.metadatas.extend(metadatas)
        
        # Re-fit the vectorizer
        if self.documents:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        logger.info(f"Added {len(ids)} documents. Total: {len(self.documents)}")

    def search(self, query_text: str, n_results: int = 3, filter_dict: Dict[str, Any] = None) -> Dict[str, Any]:
        if not self.documents or self.tfidf_matrix is None:
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
            
        query_vec = self.vectorizer.transform([query_text])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        
        # Get top N indices
        top_indices = np.argsort(similarities)[::-1][:n_results]
        
        # We wrap in lists to mimic chromadb's output format: [[doc1, doc2]]
        return {
            "documents": [[self.documents[i] for i in top_indices]],
            "metadatas": [[self.metadatas[i] for i in top_indices]],
            "distances": [[1.0 - similarities[i] for i in top_indices]] # Convert similarity to distance
        }

vector_store = VectorStore()

