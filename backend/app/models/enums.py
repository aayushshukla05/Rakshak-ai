from enum import Enum

class SeverityLevel(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class AssetType(str, Enum):
    SERVER = "server"
    WORKSTATION = "workstation"
    FIREWALL = "firewall"
    VPN_GATEWAY = "vpn_gateway"
    ROUTER = "router"

class IncidentStatus(str, Enum):
    ACTIVE = "active"
    CONTAINED = "contained"
    RESOLVED = "resolved"

class ZoneType(str, Enum):
    DMZ = "dmz"
    INTERNAL = "internal"
    MANAGEMENT = "management"
    INTERNET = "internet"
    OT = "ot"

class PlaybookStatus(str, Enum):
    ACTIVE = "active"
    PROPOSED = "proposed"
    ARCHIVED = "archived"
