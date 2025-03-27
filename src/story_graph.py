from pathlib import Path

import yaml
from story_node import StoryNode
from timer import Timer


class StoryGraph:
    def __init__(self, graph: dict[str, StoryNode]):
        self.graph: dict[str, StoryNode] = graph

    @staticmethod
    def from_yaml(yaml_file_path: Path):
        with yaml_file_path.open() as f:
            data = yaml.safe_load(f)

        graph: dict[str, StoryNode] = {}
        for node_name, node in data["nodes"].items():
            timer = Timer(**node["timer"]) if "timer" in node else None
            graph[node_name] = StoryNode(
                node_name,
                node["title"],
                node["text"],
                node["choices"],
                timer,
            )

        return StoryGraph(graph)

    def get_node(self, node_name: str) -> StoryNode:
        return self.graph[node_name]
