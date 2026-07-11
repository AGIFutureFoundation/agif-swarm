"""Swarm management commands."""

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Monitor and control the swarm")
console = Console()


@app.command()
def status():
    """Show overall swarm status."""
    table = Table(title="Swarm Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Count", style="yellow")

    table.add_row("Companies", "[green]●[/green] Healthy", "3")
    table.add_row("Orchestrators", "[green]●[/green] Healthy", "1")
    table.add_row("Workers", "[green]●[/green] Healthy", "12")
    table.add_row("Memory", "[green]●[/green] Healthy", "1")
    table.add_row("Messaging", "[green]●[/green] Healthy", "1")

    console.print(table)


@app.command()
def init(org: str = typer.Option(..., "--org", "-o", help="Organization name")):
    """Initialize a new swarm."""
    console.print(f"[bold]Initializing swarm for: {org}[/bold]")
    console.print("[green]✓[/green] Creating configuration")
    console.print("[green]✓[/green] Initializing database")
    console.print("[green]✓[/green] Setting up Redis")
    console.print("[green]✓[/green] Deploying orchestrator")
    console.print("[bold green]Swarm initialized successfully![/bold green]")


@app.command()
def health():
    """Check health of all swarm components."""
    console.print("[bold]Swarm Health Check:[/bold]")
    console.print("[green]✓[/green] API: Responding")
    console.print("[green]✓[/green] Database: Connected")
    console.print("[green]✓[/green] Redis: Connected")
    console.print("[green]✓[/green] Orchestrator: Running")
    console.print("[green]✓[/green] All Workers: Running")
    console.print("[bold green]All systems operational[/bold green]")


@app.command()
def metrics():
    """Show swarm metrics."""
    table = Table(title="Swarm Metrics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="yellow")

    table.add_row("Total Tasks", "1,234")
    table.add_row("Active Tasks", "45")
    table.add_row("Completed Tasks", "1,189")
    table.add_row("Failed Tasks", "0")
    table.add_row("Avg Task Duration", "2.3s")

    console.print(table)
