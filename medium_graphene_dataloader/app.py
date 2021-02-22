"""The application
"""

import logging

import aiomysql
from bareasgi import Application
from bareasgi_cors import CORSMiddleware
from bareasgi_graphql_next.graphene import add_graphene
from baretypes import (
    Scope,
    Info,
    Message
)

from .constants import (
    AIOMYSQL_POOL_KEY,
    CUSTOMER_DATALOADER_KEY,
    PRODUCT_DATALOADER_KEY
)
from .data_loaders import (
    ProductDataLoader,
    CustomerDataLoader
)
from .schema import SCHEMA

LOGGER = logging.getLogger(__name__)



async def _on_startup(_scope: Scope, info: Info, _request: Message) -> None:
    pool = await aiomysql.create_pool(
        host='localhost',
        port=3306,
        user='rob',
        password='makeitfunky',
        db='example'
    )
    info[AIOMYSQL_POOL_KEY] = pool
    info[CUSTOMER_DATALOADER_KEY] = CustomerDataLoader(pool)
    info[PRODUCT_DATALOADER_KEY] = ProductDataLoader(pool)


async def _on_shutdown(_scope: Scope, info: Info, _request: Message) -> None:
    pool: aiomysql.Pool = info[AIOMYSQL_POOL_KEY]
    pool.close()
    await pool.wait_closed()


def make_application() -> Application:

    app = Application(
        info={},
        middlewares=[CORSMiddleware()],
        startup_handlers=[_on_startup],
        shutdown_handlers=[_on_shutdown]
    )

    add_graphene(app, SCHEMA)

    return app
