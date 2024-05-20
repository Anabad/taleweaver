import os
from pathlib import Path

import questionary
import yaml
from story_teller import StoryTeller


def tell_story(tale_path: Path) -> None:
    story_teller = StoryTeller(tale_path)
    story_teller.tell()


def get_stories(tale_dir: Path) -> dict[str, Path]:
    tale_files = list(tale_dir.glob("*.yaml"))
    stories: dict[str, Path] = {}
    for tale_file in tale_files:
        with tale_file.open() as f:
            data = yaml.safe_load(f)
        stories[data["title"]] = tale_file
    return stories


def choose_story(tale_dir: Path) -> Path | None:
    stories = get_stories(tale_dir)
    choices = list(stories.keys()) + ["Quit"]
    while True:
        os.system("clear")
        choice = questionary.select("Choose a story:", choices=choices).ask()
        if choice == "Quit":
            return None
        tell_story(stories[choice])


if __name__ == "__main__":
    tale_dir = Path("tales")
    choose_story(tale_dir)
