import logging
import click

_logger = logging.getLogger(__name__)

@click.group()
def cloudfront():
    pass

@click.option('--cert-arn', required=True, type=str)
@click.option('--id', required=True, type=str)
@cloudfront.command()
def update(cert_arn, id):
    click.echo(f'The subcommand cloudfront: {cert_arn}, {id}')
    _logger.info(f'The subcommand cloudfront: {cert_arn}, {id}')