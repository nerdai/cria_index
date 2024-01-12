from cria_index.llms.huggingface import HuggingFaceLLM
from cria_index.core.llms import LLM

def test_huggingfacellm():
    hf_llm = HuggingFaceLLM()
    assert isinstance(hf_llm, LLM)
    assert hf_llm.class_name() == "HuggingFaceLLM"