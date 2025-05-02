from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TubeViewsInfo:
    view_count: str
    view_abbr_count: str