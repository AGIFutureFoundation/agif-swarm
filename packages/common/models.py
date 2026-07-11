"""Core data models for the swarm framework."""

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Entity(BaseModel):
    """Base entity model representing a company or organizational unit."""

    id: str = Field(default_factory=lambda: f"entity-{uuid4().hex[:8]}")
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: dict = Field(default_factory=dict)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "entity-abc12345",
                "name": "Company A",
                "description": "Subsidiary of AGI Future Foundation PBC",
            }
        }


class Company(Entity):
    """Represents a company within the PBC holding structure."""

    entity_type: str = "company"
    parent_id: Optional[str] = None  # Reference to parent/holding company
    registration_number: Optional[str] = None
    jurisdiction: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": "comp-a",
                "name": "Company A",
                "entity_type": "company",
                "parent_id": "pbc-holding",
                "jurisdiction": "US",
            }
        }


class SwarmConfig(BaseModel):
    """Configuration for the entire swarm orchestration platform."""

    organization_name: str
    organization_id: str
    companies: list[Company] = Field(default_factory=list)
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    database_url: str
    redis_url: str
    max_workers: int = 10
    memory_limit_gb: int = 100
    enable_metrics: bool = True
    log_level: str = "INFO"

    class Config:
        json_schema_extra = {
            "example": {
                "organization_name": "AGI Future Foundation PBC",
                "organization_id": "agif-pbc",
                "companies": [],
                "database_url": "postgresql://user:pass@localhost/agif_swarm",
                "redis_url": "redis://localhost:6379",
            }
        }
