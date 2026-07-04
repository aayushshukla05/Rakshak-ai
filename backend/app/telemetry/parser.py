import pandas as pd
from datetime import datetime
import uuid
from typing import Dict, Any, List
from app.models.schemas import TelemetryEvent

class TelemetryParser:
    """
    Parses LANL (auth.txt) and UNSW-NB15 CSV data into the unified TelemetryEvent schema.
    """
    
    @staticmethod
    def parse_lanl_auth_row(row: Dict[str, Any]) -> TelemetryEvent:
        """
        Schema: time, user@domain, source_computer, destination_computer, auth_type, logon_type, auth_orientation, success/failure
        Example: 1, ANONYMOUS LOGON@C586, C1250, C586, NTLM, Network, LogOn, Success
        """
        # LANL time is an integer offset (seconds from an unknown epoch). We'll convert it to a relative datetime for simulation.
        # Here we just parse it back to a base datetime + offset.
        base_time = datetime(2026, 7, 1)
        try:
            offset_seconds = int(row.get('time', 0))
            ts = pd.to_timedelta(offset_seconds, unit='s') + base_time
        except ValueError:
            ts = base_time
            
        user = row.get('user@domain', '').split('@')[0] if '@' in row.get('user@domain', '') else row.get('user@domain')
        
        return TelemetryEvent(
            event_id=str(uuid.uuid4()),
            timestamp=ts,
            source_ip=row.get('source_computer', 'Unknown'),
            destination_ip=row.get('destination_computer', 'Unknown'),
            source_user=user,
            destination_host=row.get('destination_computer', 'Unknown'),
            auth_result=row.get('success/failure', 'Unknown'),
            protocol=row.get('auth_type', 'Unknown'),
            command=row.get('logon_type', 'Unknown'),
            dataset_label="Normal" if row.get('success/failure') == 'Success' else "AuthFailure" # placeholder
        )

    @staticmethod
    def parse_unsw_row(row: Dict[str, Any]) -> TelemetryEvent:
        """
        UNSW-NB15 Schema includes many network flow features.
        We map key ones: stime, srcip, dstip, sport, dsport, proto, sbytes, dbytes, attack_cat
        """
        try:
            ts = datetime.fromtimestamp(float(row.get('stime', 0)))
        except ValueError:
            ts = datetime.now()
            
        return TelemetryEvent(
            event_id=str(uuid.uuid4()),
            timestamp=ts,
            source_ip=str(row.get('srcip', '')),
            destination_ip=str(row.get('dstip', '')),
            port=int(row.get('dsport', 0)) if str(row.get('dsport', '0')).isdigit() else None,
            protocol=str(row.get('proto', '')),
            bytes_sent=int(row.get('sbytes', 0)),
            bytes_received=int(row.get('dbytes', 0)),
            dataset_label=str(row.get('attack_cat', 'Normal')).strip() or "Normal"
        )
