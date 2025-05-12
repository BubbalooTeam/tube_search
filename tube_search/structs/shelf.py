from dataclasses import dataclass
from typing import List

@dataclass(frozen=True, slots=True)
class TubeShelfInfo:
    title: str