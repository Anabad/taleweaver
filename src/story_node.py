from typing import Optional

from timer import Timer


class StoryNode:
    def __init__(
        self,
        short_name: str,
        title: str,
        text: str,
        choices: dict[str, str],
        timer: Optional[Timer],
    ) -> None:
        self.short_name: str = short_name
        self.title: str = title
        self.text: str = text
        self.choices: dict[str, str] = choices
        self.timer: Optional[Timer] = timer

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
