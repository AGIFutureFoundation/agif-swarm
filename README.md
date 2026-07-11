# AGI Future Foundation PBC - Corporate Swarm

A distributed, multi-company orchestration platform designed to coordinate AI agents across the AGI Future Foundation ecosystem.

## Vision

The AGI Future Foundation operates as a network of interconnected companies (entities). The corporate swarm framework enables:

- **Multi-Entity Management**: Coordinate operations across multiple subsidiary companies
- **Distributed Agents**: Deploy autonomous agents that work across organizational boundaries
- **Shared Intelligence**: Leverage collective memory and knowledge across the swarm
- **Scalable Operations**: From single server to global infrastructure

## Architecture

```
PBC Holding Company
├── Company A (Subsidiary)
├── Company B (Subsidiary)
└── Company C (Subsidiary)
      ↓
   Swarm Agents
      ├── Orchestrator (Master)
      ├── Workers (Compute)
      ├── Memory Layer (Knowledge)
      └── Messaging (Communication)
```

## Quick Start

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Node.js 18+ (for dashboard)

### Installation

```bash
git clone https://github.com/AGIFutureFoundation/agif-swarm.git
cd agif-swarm

pip install -e packages/agifctl

agifctl init --org "AGI Future Foundation"

docker-compose -f deployments/docker-compose.yml up
```

### CLI Commands

```bash
# Manage companies
agifctl company create --name "Company A" --entity-id "comp-a"
agifctl company list

# Deploy agents
agifctl agent deploy --company comp-a --agent-type orchestrator

# Monitor swarm health
agifctl swarm status
agifctl swarm health
```

## Project Structure

### `/apps`
- **api**: FastAPI backend serving the orchestration layer
- **dashboard**: React/Next.js web UI for swarm management
- **orchestrator**: NemoClaw-based master coordinator
- **worker**: Distributed compute nodes

### `/packages`
- **agifctl**: Command-line interface for swarm management
- **agents**: Agent framework and implementations
- **memory**: Distributed memory/knowledge layer
- **messaging**: Event-driven communication system
- **common**: Shared utilities and types

### `/deployments`
- **docker-compose.yml**: Local development stack
- **helm/**: Kubernetes Helm charts
- **kubernetes/**: Kubernetes manifests

### `/docs`
Comprehensive documentation, APIs, and guides

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black . && isort .

# Type checking
mypy .

# Lint
ruff check .
```

## Configuration

Create a `.env` file in the root:

```env
# Core
ENV=development
LOG_LEVEL=INFO

# API
API_HOST=0.0.0.0
API_PORT=8000

# Database
DATABASE_URL=postgresql://user:pass@localhost/agif_swarm

# Redis (Memory Layer)
REDIS_URL=redis://localhost:6379

# Companies (PBC Structure)
COMPANIES=[
  {"id": "comp-a", "name": "Company A", "type": "subsidiary"},
  {"id": "comp-b", "name": "Company B", "type": "subsidiary"},
  {"id": "comp-c", "name": "Company C", "type": "subsidiary"}
]
```

## Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Quick Start Guide](docs/QUICK_START.md)
- [Company Management](docs/company-management.md)
- [Agent Development](docs/agent-development.md)
- [Memory System](docs/memory-system.md)
- [Deployment Guide](docs/deployment.md)
- [API Reference](docs/api.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Apache 2.0 - See [LICENSE](LICENSE)

## Support

- **Issues**: [GitHub Issues](https://github.com/AGIFutureFoundation/agif-swarm/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AGIFutureFoundation/agif-swarm/discussions)
- **Email**: support@agifoundation.org
