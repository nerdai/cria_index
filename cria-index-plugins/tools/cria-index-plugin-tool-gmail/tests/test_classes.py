from cria_index.core.tools.base import BaseTool
from cria_index.plugins.tools.gmail import GmailTool

def test_arxiv_tool():
    tool = GmailTool()
    assert isinstance(tool, BaseTool)
    assert tool.class_name() == "GmailTool"