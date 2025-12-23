import requests
from . import config
import click
import logging

logger = logging.getLogger(__name__)


def check_health():
    click.echo("Checking connection health ...")
    logger.info("Start health check")
    url = f"http://{config.HOST}:{config.PORT}/health"
    res = requests.get(url)
    if res.status_code == 200:
        logger.info("Health Check - Success")
        click.echo("Connection healthy.")
    else:
        logger.error("Health Check - Failure")
        click.echo("Something went wrong...")
