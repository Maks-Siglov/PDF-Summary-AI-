"""This module contains the application run script."""

import logging

import uvicorn

from src.config.utils import read_config
from src.system.entry import prepare_app


config = read_config()
logging.info(config.model_dump_json(indent=4))
app = prepare_app(config)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.service_settings.host,
        port=config.service_settings.port,
    )
