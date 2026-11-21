"""Flashcards, Verdade ou Fake e pares. Por enquanto, o conteúdo legado (agy) com áreas convertidas.
Será substituído pelo conteúdo revisado (etapa 5)."""
import json
from pathlib import Path

_L = json.loads((Path(__file__).parent / "legado.json").read_text(encoding="utf-8"))
_AREA = {"tpa_csharp": "tpa", "web_design": "web", "bd_aps_fi": "bd", "port_ing": "port", "ciencias_hum": "pesq", "exatas": "mat"}

FLASHCARDS = _L["flashcards"]
VF = [dict(v, area=_AREA.get(v["area"], v["area"])) for v in _L["vf"]]
PAIRS = _L["pairs"]
