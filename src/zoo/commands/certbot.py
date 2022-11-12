import logging
import subprocess as sp
import click

_logger = logging.getLogger(__name__)

@click.group()
def certbot():
    pass


@click.option('-d', '--domain', required=True, type=str)
@click.option('--test/--no-test', default=False)
@certbot.command()
def create(domain, test):
    # process = sp.Popen(['echo', f'More output {domain}, {test}'],
    #                  stdout=sp.PIPE, 
    #                  stderr=sp.PIPE)
    process = sp.Popen('/usr/bin/true',
                     stdout=sp.PIPE, 
                     stderr=sp.PIPE)

    stdout, stderr = process.communicate()
    returnCode = process.poll()
    click.echo(f'The subcommand cert: {domain}, {test}, {stdout}, {stderr}, {returnCode}')
    _logger.info(f'The subcommand cert: {domain}, {test}, {stdout}, {stderr}, {returnCode}')
