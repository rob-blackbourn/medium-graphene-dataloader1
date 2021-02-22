"""Schema"""

import graphene

from .queries import Query

SCHEMA = graphene.Schema(query=Query)

__all__ = [
    'SCHEMA'
]
