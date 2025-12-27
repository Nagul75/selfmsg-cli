import logging
from . import client
import click

LOG_FILE = "selfmsg-cli.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Self Messaging CLI"""
    logger.info("CLI started")


@cli.command()
def check():
    """Check server connection health"""
    logger.info("Connection health check started")
    client.check_health()
    logger.info("Connection health check finished")


@cli.command()
@click.option("--content", required=True, help="Message to be sent.")
def send_message(content: str):
    """Send Message"""
    logger.info("Send Message process started")
    client.send_message(content=content)
    logger.info("Send Message process finished")
