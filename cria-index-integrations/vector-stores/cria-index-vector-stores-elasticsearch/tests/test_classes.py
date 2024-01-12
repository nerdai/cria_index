from cria_index.core import VectorStore
from cria_index.vector_stores.elasticsearch import ElasticSearchVectorStore

def test_elasticsearch_vectorstore():
    vs = ElasticSearchVectorStore()
    assert isinstance(vs, VectorStore)
    assert vs.class_name() == "ElasticSearchVectorStore"