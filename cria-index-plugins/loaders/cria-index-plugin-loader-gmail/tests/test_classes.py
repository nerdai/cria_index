from cria_index.core.readers.base import BaseLoader
from cria_index.plugins.loaders.gmail import GmailLoader

def test_notion_loader():
    loader = GmailLoader()
    assert isinstance(loader, BaseLoader)
    assert loader.class_name() == "GmailLoader"