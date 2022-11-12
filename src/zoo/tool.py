from zoo import __version__

__author__ = "Marcin Witowski"
__copyright__ = "Marcin Witowski"
__license__ = "MIT"

import os
import logging
import sys
import click
from zoo.commands.acm import acm
from zoo.commands.route53 import route53
from zoo.commands.cloudfront import cloudfront
from zoo.commands.certbot import certbot

_logger = logging.getLogger(__name__)

def soap():
    print("soap")

def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )

@click.group()
@click.option('--loglevel', type=click.Choice(['INFO', 'DEBUG'], case_sensitive=False), default="INFO")
def cli(loglevel):
    setup_logging(loglevel)
    _logger.debug("Starting crazy calculations...")
    _logger.info("Script starting here")

cli.add_command(acm)
cli.add_command(route53)
cli.add_command(cloudfront)
cli.add_command(certbot)

if __name__ == '__main__':
    cli()
