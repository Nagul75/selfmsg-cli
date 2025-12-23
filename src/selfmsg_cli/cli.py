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


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet")
def test(count: int, name: str):
    logger.info("start test")
    """Print Hello, <name> <count> times"""
    client.test()
    for x in range(count):
        click.echo(f"Hello, {name}!")

    logger.info("end test")
