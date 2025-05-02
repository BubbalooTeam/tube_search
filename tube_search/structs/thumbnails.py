from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TubeThumbnailsInfo:
    url: str
    width: int
    height: int