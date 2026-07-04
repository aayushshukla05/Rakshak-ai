from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.models.enums import SeverityLevel, IncidentStatus

class TelemetryEvent(BaseModel):
    event_id: str
    timestamp: datetime
    source_ip: str
    destination_ip: str
    source_user: Optional[str] = None
    destination_host: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    bytes_sent: Optional[int] = 0
    bytes_received: Optional[int] = 0
    command: Optional[str] = None
    auth_result: Optional[str] = None
    dataset_label: Optional[str] = None
    mitre_technique: Optional[str] = None

class Incident(BaseModel):
    id: str
    status: IncidentStatus
    severity: SeverityLevel
    detected_at: datetime
    contained_at: Optional[datetime] = None
    playbook_used: Optional[str] = None
    narrative: Optional[str] = None
    mitre_techniques: List[str] = []
