import click

@click.group()
def cli():
    """A simple cli"""
    pass

@cli.command()
@click.argument("name")
def hello(name : str):
    click.echo(f"Hello, {name}")

@cli.command()
@click.argument("a", type = int)
@click.argument("b", type = int)
def add(a:int, b:int):
    convertor = a + b
    click.echo(f"Sum is {convertor}")

@cli.command()
@click.argument("a", type = int)
@click.argument("b", type = int)
def sub(a:int, b:int):
    convertor = a - b
    click.echo(f"Sum is {convertor}")
@cli.command()
@click.argument("a", type = int)
@click.argument("b", type = int)
def mul(a:int, b:int):
    convertor = a * b
    click.echo(f"Sum is {convertor}")
@cli.command()
@click.argument("a", type = int)
@click.argument("b", type = int)
def div(a:int, b:int):
    convertor = a / b
    click.echo(f"Sum is {convertor}")

if __name__ == "__main__":
    cli()