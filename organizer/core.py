
from pathlib import Path
import shutil
import logging

from organizer.exceptions import SourceFolderError, FileOperationError

logger = logging.getLogger(__name__)


def organize_files(source, target, categories, dry_run=False):
    """Organize files according to configured extensions."""
    source = Path(source)
    target = Path(target)

    if not source.exists() or not source.is_dir():
        raise SourceFolderError(f"Invalid source folder: {source}")

    if source.resolve() == target.resolve():
        raise SourceFolderError("Source and target cannot be the same.")

    moved = 0
    skipped = 0

    for file_path in source.iterdir():
        if not file_path.is_file():
            continue

        category = "Others"

        for name, extensions in categories.items():
            if file_path.suffix.lower() in extensions:
                category = name
                break

        destination = target / category / file_path.name

        if destination.exists():
            logger.warning("Skipped: %s", file_path.name)
            skipped += 1
            continue

        if dry_run:
            logger.info("[DRY RUN] %s -> %s", file_path.name, category)
            continue

        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))
            logger.info("Moved: %s", file_path.name)
            moved += 1
        except OSError as error:
            raise FileOperationError(
                f"Failed to move {file_path.name}: {error}"
            ) from error

    logger.info("Summary | Moved: %s | Skipped: %s", moved, skipped)
    return moved, skipped
