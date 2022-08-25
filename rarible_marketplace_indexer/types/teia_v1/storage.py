# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any
from typing import Dict
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra


class Swaps(BaseModel):
    class Config:
        extra = Extra.forbid

    issuer: str
    fa2: str
    objkt_id: str
    objkt_amount: str
    xtz_per_objkt: str
    royalties: str
    creator: str


class TeiaV1Storage(BaseModel):
    class Config:
        extra = Extra.forbid

    allowed_fa2s: Dict[str, Dict[str, Any]]
    collects_paused: bool
    counter: str
    fee: str
    fee_recipient: str
    manager: str
    metadata: Dict[str, str]
    proposed_manager: Optional[str]
    swaps: Dict[str, Swaps]
    swaps_paused: bool