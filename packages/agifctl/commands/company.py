"""Company management commands."""

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Manage companies in the swarm")
console = Console()


@app.command()
def create(
    name: str = typer.Option(..., "--name", "-n", help="Company name"),
    entity_id: str = typer.Option(..., "--entity-id", "-e", help="Company entity ID"),
    parent_id: Optional[str] = typer.Option(None, "--parent-id", "-p", help="Parent company ID"),
):
    """Create a new company in the swarm."""
    console.print(f"[green]✓[/green] Creating company: [bold]{name}[/bold]")
    console.print(f"  Entity ID: {entity_id}")
    if parent_id:
        console.print(f"  Parent: {parent_id}")
    console.print("[bold green]Company created successfully![/bold green]")


@app.command()
def list():
    """List all companies in the swarm."""
    table = Table(title="Companies in Swarm")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Parent", style="yellow")
    table.add_column("Status", style="green")

    # Placeholder data
    table.add_row("comp-a", "Company A", "pbc-holding", "healthy")
    table.add_row("comp-b", "Company B", "pbc-holding", "healthy")
    table.add_row("comp-c", "Company C", "pbc-holding", "degraded")

    console.print(table)


@app.command()
def show(entity_id: str = typer.Argument(..., help="Company entity ID")):
    """Show details of a company."""
    console.print(f"[bold]Company: {entity_id}[/bold]")
    console.print("Name: Company A")
    console.print("Status: [green]healthy[/green]")
    console.print("Agents: 5")
    console.print("Created: 2024-01-15 10:30:00")
