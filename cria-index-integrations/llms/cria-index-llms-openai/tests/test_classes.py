from cria_index.llms.openai import OpenAI
from cria_index.core.llms import LLM

def test_openai():
    llm = OpenAI()
    assert isinstance(llm, LLM)
    assert llm.class_name() == "OpenAI"