import logging
import click

_logger = logging.getLogger(__name__)

@click.group()
def acm():
    """
    Group function
    """
    # pylint: disable=W0107
    pass

@click.option('-k', '--key-file', required=True, type=str)
@click.option('-c', '--cert-file', required=True, type=str)
@click.option('-a', '--ca-file', required=True, type=str)
@acm.command()
def upload(key_file, cert_file, ca_file):
    """
    An example function
    """
    click.echo(f'The subcommand acm: {key_file}, {cert_file}, {ca_file}')


@click.option('--arn', required=True, type=str)
@acm.command()
def delete(arn):
    """
    An example function
    """
    click.echo(f'Delete cert: {arn}')
    _logger.debug('Delete cert debug message...')
    _logger.info(f'Delete cert {arn}')
