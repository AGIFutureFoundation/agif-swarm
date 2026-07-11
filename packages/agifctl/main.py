"""Main CLI entry point for agifctl."""

import typer
from rich.console import Console

from . import commands

app = typer.Typer(
    help="AGI Future Foundation Swarm Management CLI",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()

# Register command groups
app.add_typer(commands.company.app, name="company", help="Manage companies in the swarm")
app.add_typer(commands.agent.app, name="agent", help="Deploy and manage agents")
app.add_typer(commands.swarm.app, name="swarm", help="Monitor and control the swarm")


@app.callback()
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
):
    """AGI Future Foundation Swarm CLI."""
    if verbose:
        console.print("[bold cyan]Verbose mode enabled[/bold cyan]")


if __name__ == "__main__":
    app()
