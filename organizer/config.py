
from pathlib import Path
import yaml

from organizer.exceptions import ConfigError


def load_config(config_path="config.yaml"):
    """Load application configuration from YAML."""
    path = Path(config_path)

    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
    except yaml.YAMLError as error:
        raise ConfigError(f"Invalid YAML configuration: {error}") from error

    if not isinstance(config, dict):
        raise ConfigError("Configuration must be a YAML dictionary.")

    return config
