"""The GraphQL schema"""

from typing import Any, Mapping

from aiodataloader import DataLoader
import graphene
import graphql

from ..constants import (
    CUSTOMER_DATALOADER_KEY,
    PRODUCT_DATALOADER_KEY
)

class Product(graphene.ObjectType):
    """The product type"""
    product_id = graphene.ID(required=True)
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)

class Customer(graphene.ObjectType):
    """The customer type"""
    customer_id = graphene.ID(required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)

class Order(graphene.ObjectType):
    """The order type"""
    order_id = graphene.ID(required=True)
    customer = graphene.Field(Customer, required=True)
    product = graphene.Field(Product, required=True)
    cost = graphene.Decimal(required=True)

    @staticmethod
    async def resolve_product(
            root: Mapping[str, Any],
            info: graphql.GraphQLResolveInfo
    ) -> Mapping[str, Any]:
        data_loader: DataLoader = info.context[PRODUCT_DATALOADER_KEY]
        return await data_loader.load(root['product_id'])

    @staticmethod
    async def resolve_customer(
            root: Mapping[str, Any],
            info: graphql.GraphQLResolveInfo
    ) -> Mapping[str, Any]:
        data_loader: DataLoader = info.context[CUSTOMER_DATALOADER_KEY]
        return await data_loader.load(root['customer_id'])
