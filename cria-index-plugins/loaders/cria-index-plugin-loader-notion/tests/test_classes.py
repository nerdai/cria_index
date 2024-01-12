from cria_index.core.readers.base import BaseLoader
from cria_index.plugins.loaders.notion import NotionLoader

def test_notion_loader():
    loader = NotionLoader()
    assert isinstance(loader, BaseLoader)
    assert loader.class_name() == "NotionLoader"