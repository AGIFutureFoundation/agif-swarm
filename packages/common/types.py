"""Type definitions and enums for the swarm framework."""

from enum import Enum


class EntityType(str, Enum):
    """Types of entities in the swarm."""

    HOLDING_COMPANY = "holding_company"
    SUBSIDIARY = "subsidiary"
    DEPARTMENT = "department"
    TEAM = "team"


class AgentType(str, Enum):
    """Types of agents that can be deployed."""

    ORCHESTRATOR = "orchestrator"  # Master coordinator
    WORKER = "worker"  # Compute node
    MEMORY = "memory"  # Knowledge/memory service
    MESSENGER = "messenger"  # Communication broker
    MONITOR = "monitor"  # Health/metrics monitor
    GATEWAY = "gateway"  # External interface


class SwarmStatus(str, Enum):
    """Overall swarm health status."""

    INITIALIZING = "initializing"
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    SHUTTING_DOWN = "shutting_down"
    OFFLINE = "offline"


class TaskStatus(str, Enum):
    """Status of a task in the swarm."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"


class CompanyRole(str, Enum):
    """Roles companies can have within the PBC structure."""

    HOLDING_COMPANY = "holding_company"
    OPERATING_COMPANY = "operating_company"
    SERVICE_COMPANY = "service_company"
    INVESTMENT_COMPANY = "investment_company"
