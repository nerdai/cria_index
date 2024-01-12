from cria_index.core.llama_packs.base import BasePack
from cria_index.plugins.packs.rag_evaluator import RagEvaluatorPack

def test_resumescreener_pack():
    pack = RagEvaluatorPack()
    assert isinstance(pack, BasePack)
    assert pack.class_name() == "RagEvaluatorPack"