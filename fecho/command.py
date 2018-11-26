import click
from setuptools.command import alias


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def fecho(filename):
    """
    Command line interface in python using click
    Echoes the filename
    """
    click.echo(click.format_filename(filename))
