import os

import tomli
from dotenv import load_dotenv

from .base import ProjectAbout
from .config import Config

load_dotenv()


def _read_project_about(pyproject_file_path: str) -> ProjectAbout:
    """Reads project about info.

    Args:
        pyproject_file_path (str): The path to pyproject.toml.

    Returns:
        ProjectAbout: Service about.
    """
    with open(pyproject_file_path, "rb") as f:
        data = tomli.load(f)

    project_info = {
        "name": data["project"]["name"],
        "version": data["project"]["version"],
        "description": data["project"].get("description", ""),
    }

    return ProjectAbout(**project_info)


def read_config() -> Config:
    """Reads the service configuration.

    Returns:
        Config: Service configuration.
    """
    about = _read_project_about(os.environ.get("PYPROJECT_PATH", "pyproject.toml"))
    config = Config(version=about.version)
    if config.service_settings.name is None:
        config.service_settings.name = about.name
    if config.service_settings.description is None:
        config.service_settings.description = about.description
    return config
