"""Conteúdo da aba 2ª fase. Por enquanto, o legado (já sem as menções MB/B/R/I). Será reescrito (etapa 6)."""
import json
from pathlib import Path

PHASE2 = json.loads((Path(__file__).parent / "legado.json").read_text(encoding="utf-8"))["phase2"]
