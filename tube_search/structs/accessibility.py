from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TubeAccessibilityInfo:
    title: str
    duration: str