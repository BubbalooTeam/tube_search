from dataclasses import dataclass
from typing import List

from tube_search.structs import TubeAccessibilityInfo, TubeChannelInfo, TubeViewsInfo, TubeThumbnailsInfo

@dataclass(frozen=True, slots=True)
class TubeVideoInfo:
    videoID: str
    videoTitle: str
    videoDuration: str
    publishedTime: str
    videoViewCount: TubeViewsInfo
    thumbnails: List[TubeThumbnailsInfo]
    descriptionSnippet: str
    channel: TubeChannelInfo
    accessibility: TubeAccessibilityInfo
    url: str
    shelfTitle: str