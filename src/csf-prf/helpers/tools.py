import pathlib
import importlib


def get_ags_tools():
    parent = pathlib.Path(__file__).parents[1]
    ags_tools = parent / "ags_tools"

    tools = []
    for tool in ags_tools.glob('**/*.py'):
        tools.append(tool)
    return tools
