from cria_index.core.llama_packs.base import BasePack
from cria_index.plugins.packs.resume_screener import ResumeScreenerPack

def test_resumescreener_pack():
    pack = ResumeScreenerPack()
    assert isinstance(pack, BasePack)
    assert pack.class_name() == "ResumeScreenerPack"