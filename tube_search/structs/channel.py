from dataclasses import dataclass
from typing import List

from .thumbnails import TubeThumbnailsInfo

@dataclass(frozen=True, slots=True)
class TubeChannelInfo:
    title: str
    id: str
    thumbnails: List[TubeThumbnailsInfo]
    url: str