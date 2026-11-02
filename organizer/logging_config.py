
import logging


def setup_logging(level="INFO", verbose=False):
    """Configure application logging."""
    log_level = logging.DEBUG if verbose else getattr(
        logging, str(level).upper(), logging.INFO
    )

    logging.basicConfig(
        level=log_level,
        format="%(levelname)s: %(message)s"
    )
