# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra


class RaribleExchangeLegacyDataStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    owner: str
    owner_candidate: Optional[str]
    user: List[str]
    fill: Dict[str, Optional[str]]
    metadata: Dict[str, str]
