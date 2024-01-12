from cria_index.core.tools.base import BaseTool
from cria_index.plugins.tools.arxiv import ArxivTool

def test_arxiv_tool():
    tool = ArxivTool()
    assert isinstance(tool, BaseTool)
    assert tool.class_name() == "ArxivTool"