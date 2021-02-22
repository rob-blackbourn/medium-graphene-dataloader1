"""The Server"""

import asyncio
import logging
import logging.config
from typing import Any, Mapping, Optional

from bareasgi import Application
import hypercorn.asyncio
import hypercorn.config
import pkg_resources

from medium_graphene_dataloader.app import make_application


def start_server():
    """Start the server
    """
    app = make_application()

    http_config = hypercorn.config.Config()
    http_config.bind = ["0.0.0.0:9001"]

    asyncio.run(
        hypercorn.asyncio.serve(app, http_config)
    )

if __name__ == '__main__':
    start_server()