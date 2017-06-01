import click

from leginx import Server


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command(help='Start service')
def start():
    server = Server()
    server.start()
