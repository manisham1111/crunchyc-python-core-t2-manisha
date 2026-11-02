
import argparse
import logging

from organizer.config import load_config
from organizer.core import organize_files
from organizer.logging_config import setup_logging
from organizer.exceptions import OrganizerError

logger = logging.getLogger(__name__)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Smart Downloads Folder Organizer"
    )

    parser.add_argument(
        "--source",
        help="Source folder containing files"
    )
    parser.add_argument(
        "--target",
        help="Destination folder for organized files"
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Configuration file path (default: config.yaml)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview file movements without moving files"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable detailed debug logging"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        config = load_config(args.config)

        setup_logging(
            level=config.get("log_level", "INFO"),
            verbose=args.verbose
        )

        source = args.source or config.get("source_folder")
        target = args.target or config.get("target_folder")
        categories = config.get("categories", {})

        if not source or not target:
            parser.error("Source and target folders are required.")

        organize_files(
            source,
            target,
            categories,
            dry_run=args.dry_run or config.get("dry_run", False)
        )

    except OrganizerError as error:
        logger.error("%s", error)
        return 1

    return 0
