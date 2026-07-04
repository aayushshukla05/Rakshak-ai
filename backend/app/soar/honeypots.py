import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class HoneypotRegistry:
    def __init__(self):
        self.honey_tokens = ["backup_admin_2024", "svc_sql_admin"]
        
    def check_event(self, event: Dict[str, Any]) -> bool:
        """
        If a log event uses a honeypot credential, trigger instant P0 alert.
        """
        user = event.get("source_user", "")
        if user in self.honey_tokens:
            logger.warning(f"HONEYPOT TRIGGERED by user {user}!")
            return True
        return False

honeypot_registry = HoneypotRegistry()
