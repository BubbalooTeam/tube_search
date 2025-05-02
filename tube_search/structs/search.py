from dataclasses import dataclass
from typing import List

from tube_search.structs import TubeAcessibilityInfo, TubeChannelInfo, TubeViewsInfo, TubeThumbnailsInfo

@dataclass(frozen=True, slots=True)
class TubeSearchInfo:
    videoID: str
    videoTitle: str
    videoDuration: str
    publishedTime: str
    videoViewCount: TubeViewsInfo
    thumbnails: List[TubeThumbnailsInfo]
    descriptionSnippet: str
    channel: TubeChannelInfo
    acessibility: TubeAcessibilityInfo
    url: str
    shelfTitle: bool