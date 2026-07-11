"""Common utilities and types for the AGI Future Foundation Swarm."""

__version__ = "0.1.0"

from .models import Company, Entity, SwarmConfig
from .types import AgentType, EntityType, SwarmStatus

__all__ = [
    "Company",
    "Entity",
    "SwarmConfig",
    "AgentType",
    "EntityType",
    "SwarmStatus",
]
