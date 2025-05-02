from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TubeAcessibilityInfo:
    title: str
    duration: str