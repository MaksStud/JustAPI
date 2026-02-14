import typer
from commands.server import server_app

app = typer.Typer()
app.add_typer(server_app, name="")


if __name__ == "__main__":
    app()
