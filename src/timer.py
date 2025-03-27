from dataclasses import dataclass


@dataclass
class Timer:
    duration: int
    timeout_node: str
