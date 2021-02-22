"""Data loaders"""

from typing import Any, List, Mapping

from aiodataloader import DataLoader
import aiomysql

class ProductDataLoader(DataLoader):

    def __init__(self, pool: aiomysql.Pool) -> None:
        super().__init__()
        self._pool = pool

    # pylint: disable=method-hidden
    async def batch_load_fn(
            self,
            keys: List[int]
    ) -> List[Mapping[str, Any]]:
        stmt = f"""
SELECT *
FROM example.product
WHERE product_id IN ({','.join(['%s'] * len(keys))})
"""
        async with self._pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(stmt, tuple(keys))
                rows = await cur.fetchall()
                rows_by_id = {
                    row['product_id']: row
                    for row in rows
                }
                return [
                    rows_by_id[key]
                    for key in keys
                ]

class CustomerDataLoader(DataLoader):

    def __init__(self, pool: aiomysql.Pool) -> None:
        super().__init__()
        self._pool = pool

    # pylint: disable=method-hidden
    async def batch_load_fn(
            self,
            keys: List[int]
    ) -> List[Mapping[str, Any]]:
        stmt = f"""
SELECT *
FROM example.customer
WHERE customer_id IN ({','.join(['%s'] * len(keys))})
"""
        async with self._pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(stmt, tuple(keys))
                rows = await cur.fetchall()
                rows_by_id = {
                    row['customer_id']: row
                    for row in rows
                }
                return [
                    rows_by_id[key]
                    for key in keys
                ]
