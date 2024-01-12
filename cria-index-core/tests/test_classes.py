from cria_index.core import LLM, VectorStore

def test_llm_class():
    llm = LLM()
    assert llm.class_name() == "LLM"


def test_vector_store_class():
    vs = VectorStore()
    assert vs.class_name() == "VectorStore"