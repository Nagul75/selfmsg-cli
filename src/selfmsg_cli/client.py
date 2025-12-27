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


def send_message(content: str):
    click.echo("Sending message ...")
    logger.info("Making POST request /messages")
    url = f"http://{config.HOST}:{config.PORT}/messages"
    body = {"type": "text", "sender": "cli", "content": content}
    res = requests.post(url, json=body)
    if res.status_code == 201:
        logger.info("POST request /messages successful")
        click.echo("Message sent")
        click.echo(res.json())
    else:
        logger.info("POST request /messages failed")
        click.echo("Error sending message")
        click.echo(res.json())
