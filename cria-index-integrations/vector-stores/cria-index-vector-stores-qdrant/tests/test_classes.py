from cria_index.core import VectorStore
from cria_index.vector_stores.qdrant import QdrantVectorStore

def test_elasticsearch_vectorstore():
    vs = QdrantVectorStore()
    assert isinstance(vs, VectorStore)
    assert vs.class_name() == "QdrantVectorStore"