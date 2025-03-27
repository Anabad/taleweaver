import asyncio
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

    async def ask_timed_question(self, node: StoryNode) -> StoryNode:
        if node.timer is None:
            raise ValueError("Node has no timer")
        question_task = asyncio.get_event_loop().create_task(self.ask_question(node))
        asyncio.get_event_loop().create_task(self.render_timer(node.timer.duration))

        try:
            next_node_choice = await asyncio.wait_for(
                question_task, node.timer.duration
            )
            next_node = self.story_graph.get_node(node.choices[next_node_choice])
            # async with asyncio.timeout(node.timer):  # type: ignore
            #     next_node_choice = await question_task
        except asyncio.TimeoutError:
            questionary.print("Time's up!", style="bold red")
            await asyncio.sleep(1)
            next_node = self.story_graph.get_node(node.timer.timeout_node)

        return next_node

    async def render_timer(self, duration: int) -> None:
        for i in range(duration, 0, -1):
            questionary.print(f"Time left: {i} seconds", style="bold", end="\r")
            await asyncio.sleep(1)

    async def ask_question(self, node: StoryNode) -> str:
        return await questionary.select(
            "",
            choices=list(node.choices.keys()),
            qmark="🕒",
        ).ask_async(patch_stdout=True)

    def render_node(self, node: StoryNode) -> str | None:
        os.system("clear")
        questionary.print(f"{node.title}\n", style="bold")
        questionary.print(node.text)
        if node.choices:
            if node.timer is None:
                next_node_choice = questionary.select(
                    "", choices=list(node.choices.keys()), qmark="📖"
                ).ask()
                next_node = self.story_graph.get_node(node.choices[next_node_choice])
            else:
                next_node = asyncio.run(self.ask_timed_question(node))

            return next_node
        else:
            choice = questionary.select(
                "What would you like to do?",
                choices=["Start again", "Choose another story", "Quit"],
            ).ask()
            if choice == "Start again":
                return self.story_graph.get_node("start")
            elif choice == "Choose another story":
                return None
            else:
                sys.exit(0)

        if node.timer is None:
            return self.render_standard_node(node)
        else:
            return self.render_timed_node(node)
