# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra


class Gentk(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    version: str


class TopBid(BaseModel):
    class Config:
        extra = Extra.forbid

    bidder: str
    price: str


class Auctions(BaseModel):
    class Config:
        extra = Extra.forbid

    bid_increment_table_id: str
    bid_time_increment: str
    ends_at: Optional[str]
    gentk: Gentk
    min_duration: str
    seller: str
    top_bid: TopBid


class AuctionsBidIncrement(BaseModel):
    class Config:
        extra = Extra.forbid

    current_bid: str
    increment: str


class CollectionOffers(BaseModel):
    class Config:
        extra = Extra.forbid

    amount: str
    buyer: str
    collection: str
    price: str


class GentkContracts(BaseModel):
    class Config:
        extra = Extra.forbid

    fa2: str
    views: str


class Gentk1(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    version: str


class Listings(BaseModel):
    class Config:
        extra = Extra.forbid

    gentk: Gentk1
    price: str
    seller: str


class Gentk2(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    version: str


class Offers(BaseModel):
    class Config:
        extra = Extra.forbid

    buyer: str
    gentk: Gentk2
    price: str


class FxhashV2Storage(BaseModel):
    class Config:
        extra = Extra.forbid

    admin: str
    auctions: Dict[str, Auctions]
    auctions_bid_increments: Dict[str, List[AuctionsBidIncrement]]
    auctions_count: str
    collection_offers: Dict[str, CollectionOffers]
    collection_offers_count: str
    entrypoints_enabled: Dict[str, bool]
    extended_storage: Dict[str, str]
    fees: str
    gentk_contracts: Dict[str, GentkContracts]
    listings: Dict[str, Listings]
    listings_count: str
    locked_eps: bool
    metadata: Dict[str, str]
    offers: Dict[str, Offers]
    offers_count: str
    paused: bool
    treasury: str
    big_map: Dict[str, str]
