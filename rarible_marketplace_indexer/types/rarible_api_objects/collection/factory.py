import os
import uuid
from datetime import datetime
from typing import Optional, Dict
from uuid import uuid5

from rarible_marketplace_indexer.models import Collection
from rarible_marketplace_indexer.types.rarible_api_objects.collection.collection import RaribleApiCollection


class RaribleApiCollectionFactory:
    @staticmethod
    def build(event: Collection, meta: Optional[Dict]) -> RaribleApiCollection:
        event_id = uuid5(namespace=uuid.NAMESPACE_OID, name=str(datetime.timestamp(datetime.now())))
        name = None
        symbol = None
        if meta is not None:
            if 'name' in meta:
                name = meta['name']
            if 'symbol' in meta:
                symbol = meta['symbol']
        return RaribleApiCollection(
            id=event_id,
            network=os.getenv("NETWORK"),
            event_id=str(event_id),
            collection={
                "id": event.__dict__.get("id"),
                "owner": event.__dict__.get("owner"),
                "name": name,
                "minters": event.__dict__.get("minters"),
                "standard": event.__dict__.get("standard"),
                "symbol": symbol
            }
        )
