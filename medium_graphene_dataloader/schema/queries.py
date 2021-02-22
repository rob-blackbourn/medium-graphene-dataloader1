"""Queries"""

from typing import Any, Mapping

import aiomysql
import graphene
import graphql

from ..constants import AIOMYSQL_POOL_KEY

from .types import Customer, Product, Order

class Query(graphene.ObjectType):
    products = graphene.Field(graphene.List(Product))
    customers = graphene.Field(graphene.List(Customer))
    orders = graphene.Field(graphene.List(Order))

    @staticmethod
    async def resolve_products(
            _root: Mapping[str, Any],
            info: graphql.GraphQLResolveInfo
    ) -> Mapping[str, Any]:
        pool: aiomysql.Pool = info.context[AIOMYSQL_POOL_KEY]
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM example.product;")
                return await cur.fetchall()

    @staticmethod
    async def resolve_customers(
            _root: Mapping[str, Any],
            info: graphql.GraphQLResolveInfo
    ) -> Mapping[str, Any]:
        pool: aiomysql.Pool = info.context[AIOMYSQL_POOL_KEY]
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM example.customer;")
                return await cur.fetchall()

    @staticmethod
    async def resolve_orders(
            _root: Mapping[str, Any],
            info: graphql.GraphQLResolveInfo
    ) -> Mapping[str, Any]:
        pool: aiomysql.Pool = info.context[AIOMYSQL_POOL_KEY]
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM example.order;")
                return await cur.fetchall()
