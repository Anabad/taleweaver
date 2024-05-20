from story_graph import StoryGraph


def test_story_graph_from_yaml(tmp_path):
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(
        """
        nodes:
          start:
            title: Start
            text: This is the start.
            choices:
              Go to the middle.: middle
              Go to the end.: end
          middle:
            title: Middle
            text: This is the middle.
            choices:
              Go to the end.: end
          end:
            title: End
            text: This is the end.
            choices: {}
        """
    )

    graph = StoryGraph.from_yaml(yaml_file)
    assert len(graph.graph) == 3
    assert graph.graph["start"].title == "Start"
    assert graph.graph["middle"].text == "This is the middle."
    assert graph.graph["end"].choices == {}
