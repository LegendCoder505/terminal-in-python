import typer

app = typer.Typer()

@app.command()
def hello_name(name : str):
    typer.echo(f"Hello, {name}")

# Simple Math CLI First
@app.command()
def add(a : int, b : int):
    convertor = a + b
    typer.echo(f"Sum is {convertor}")

@app.command()
def sub(a : int, b : int):
    convertor = a - b
    typer.echo(f"Sum is {convertor}")

@app.command()
def div(a : int, b : int):
    convertor = a / b
    typer.echo(f"Sum is {convertor}")

@app.command()
def mul(a : int, b : int):
    convertor = a * b
    typer.echo(f"Sum is {convertor}")

if __name__ == "__main__":
    app()