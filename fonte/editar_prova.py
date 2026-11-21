"""Utilitário para revisar questões de um arquivo de prova.

Uso (em script): from editar_prova import Prova
    p = Prova("provas/2024-12_DS.md")
    p.cabecalho(28, "aps", "Modelo cascata")
    p.explicacao(28, "texto em Markdown")
    p.trocar(40, "texto antigo", "texto novo")   # troca dentro do bloco da questão
    p.salvar()
"""
import re
from pathlib import Path

HEAD_RE = re.compile(r"^## (\d+) \| ([a-z]+) \| ([^|\n]*?)(?: \| ([^\n]*))?$", re.M)


class Prova:
    def __init__(self, path):
        self.path = Path(path)
        self.text = self.path.read_text(encoding="utf-8")

    def _span(self, num):
        heads = list(HEAD_RE.finditer(self.text))
        for i, h in enumerate(heads):
            if int(h.group(1)) == num:
                end = heads[i + 1].start() if i + 1 < len(heads) else len(self.text)
                return h, end
        raise KeyError(f"Q{num} não encontrada em {self.path.name}")

    def cabecalho(self, num, area, tema, extra=None):
        h, _ = self._span(num)
        extra = h.group(4) if extra is None else extra
        new = f"## {num} | {area} | {tema}" + (f" | {extra}" if extra else "")
        self.text = self.text[:h.start()] + new + self.text[h.end():]

    def explicacao(self, num, md):
        h, end = self._span(num)
        block = self.text[h.end():end]
        m = re.search(r"^> Resposta: [A-E]\s*$", block, re.M)
        assert m, f"Q{num}: sem resposta"
        new_block = block[:m.end()] + "\n\n" + md.strip() + "\n\n"
        self.text = self.text[:h.end()] + new_block + self.text[end:]

    def resposta(self, num, letra):
        h, end = self._span(num)
        block = self.text[h.end():end]
        block = re.sub(r"^> Resposta: [A-E]", f"> Resposta: {letra}", block, count=1, flags=re.M)
        self.text = self.text[:h.end()] + block + self.text[end:]

    def trocar(self, num, antigo, novo):
        h, end = self._span(num)
        block = self.text[h.end():end]
        assert antigo in block, f"Q{num}: trecho não encontrado: {antigo[:60]!r}"
        block = block.replace(antigo, novo, 1)
        self.text = self.text[:h.end()] + block + self.text[end:]

    def salvar(self):
        self.path.write_text(self.text, encoding="utf-8")
