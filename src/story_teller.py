import os
import sys
from pathlib import Path

import questionary
from story_graph import StoryGraph
from story_node import StoryNode


class StoryTeller:
    def __init__(self, tale_path: Path) -> None:
        self.story_graph = StoryGraph.from_yaml(tale_path)

    def tell(self) -> None:
        current_node = self.story_graph.get_node("start")
        while current_node:
            current_node = self.render_node(current_node)

    def render_node(self, node: StoryNode) -> str | None:
        os.system("clear")
        questionary.print(f"{node.title}\n", style="bold")
        questionary.print(node.text)
        if node.choices:
            next_node_choice = questionary.select(
                "", choices=list(node.choices.keys())
            ).ask()
            next_node = self.story_graph.get_node(node.choices[next_node_choice])
            return next_node
        else:
            choice = questionary.select(
                "What would you like to do",
                choices=["Start again", "Choose another story", "Quit"],
            ).ask()
            if choice == "Start again":
                return self.story_graph.get_node("start")
            elif choice == "Choose another story":
                return None
            else:
                sys.exit(0)
