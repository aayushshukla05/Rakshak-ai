import collections
import logging
from typing import List, Dict, Any
from app.models.schemas import TelemetryEvent

logger = logging.getLogger(__name__)

class TelemetryBuffer:
    """
    Maintains a sliding window of recent telemetry events for 
    behavioral feature extraction and low-and-slow detection.
    """
    def __init__(self, window_size: int = 10000):
        self.window_size = window_size
        self.buffer = collections.deque(maxlen=window_size)
        
    def add_event(self, event: TelemetryEvent):
        self.buffer.append(event)
        
    def get_recent_events(self) -> List[TelemetryEvent]:
        return list(self.buffer)
        
    def extract_features_for_user(self, user_id: str) -> Dict[str, Any]:
        """
        Extracts behavioral features for a specific user from the buffer.
        """
        user_events = [e for e in self.buffer if e.source_user == user_id]
        
        if not user_events:
            return {
                "unique_hosts_accessed": 0,
                "total_bytes_sent": 0,
                "auth_failures": 0
            }
            
        unique_hosts = len(set(e.destination_host for e in user_events if e.destination_host))
        total_bytes = sum(e.bytes_sent for e in user_events if e.bytes_sent)
        auth_failures = sum(1 for e in user_events if e.auth_result and e.auth_result.lower() != 'success')
        
        return {
            "unique_hosts_accessed": unique_hosts,
            "total_bytes_sent": total_bytes,
            "auth_failures": auth_failures
        }

telemetry_buffer = TelemetryBuffer()
