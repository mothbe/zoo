import logging
import click

_logger = logging.getLogger(__name__)

@click.group()
def route53():
    pass


@click.option('-d', '--domain', required=True, type=str)
@click.option('-t', '--txt', required=True, type=str)
@route53.command()
def add(domain, txt):
    click.echo(f'The subcommand add: '
    f'domain {domain}, txt: {txt}')


@click.option('-d', '--domain', required=True, type=str)
@route53.command()
def delete(domain):
    click.echo('The subcommand route53: delete')
    _logger.info('The subcommand route53: delete')