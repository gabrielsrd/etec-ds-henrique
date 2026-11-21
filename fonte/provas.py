"""Leitura das provas no formato de texto da pasta fonte/provas/.

Formato de cada arquivo (um por prova):

    ---
    id: taboao2026
    titulo: Prova Real Etec Taboão — 05/12/2025
    ...outros campos chave: valor...
    ---

    ## 1 | port | Interpretação de texto | rep=2024
    Enunciado em Markdown (pode ter imagem: ![](./img/arquivo.png)).

    A) alternativa
    B) alternativa
    C) alternativa
    D) alternativa
    E) alternativa

    > Resposta: D

    Explicação em Markdown, até o próximo "## ".

O cabeçalho da questão é: número | área | tema | opções extras separadas por espaço
(rep=... lista provas em que a questão se repete; tec força parte técnica).
"""
import re
import subprocess
from pathlib import Path

from md import convert_alerts

AREAS = [
    # parte técnica (1ª série do Plano 612)
    {"id": "tpa", "title": "Lógica e Programação (TPA)", "short": "Programação", "tech": True, "recommendedDay": 2},
    {"id": "web", "title": "Programação Web I (HTML, CSS, internet)", "short": "Web", "tech": True, "recommendedDay": 4},
    {"id": "bd", "title": "Banco de Dados I", "short": "Banco de Dados", "tech": True, "recommendedDay": 6},
    {"id": "aps", "title": "Análise e Projeto de Sistemas (requisitos, UML, ágil)", "short": "APS/UML", "tech": True, "recommendedDay": 7},
    {"id": "design", "title": "Design Digital e UX", "short": "Design/UX", "tech": True, "recommendedDay": 7},
    {"id": "fund", "title": "Fundamentos da Informática (bases numéricas, SO, hardware)", "short": "Fundamentos", "tech": True, "recommendedDay": 8},
    # base comum
    {"id": "port", "title": "Português", "short": "Português", "tech": False, "recommendedDay": 10},
    {"id": "ing", "title": "Inglês", "short": "Inglês", "tech": False, "recommendedDay": 10},
    {"id": "pesq", "title": "Investigação Científica e Empreendedorismo", "short": "Pesquisa/Empreend.", "tech": False, "recommendedDay": 13},
    {"id": "arte", "title": "Arte", "short": "Arte", "tech": False, "recommendedDay": 10},
    {"id": "edf", "title": "Educação Física", "short": "Ed. Física", "tech": False, "recommendedDay": 13},
    {"id": "mat", "title": "Matemática", "short": "Matemática", "tech": False, "recommendedDay": 11},
    {"id": "fis", "title": "Física", "short": "Física", "tech": False, "recommendedDay": 12},
    {"id": "qui", "title": "Química", "short": "Química", "tech": False, "recommendedDay": 12},
    {"id": "bio", "title": "Biologia e Ecologia", "short": "Biologia", "tech": False, "recommendedDay": 12},
    {"id": "hist", "title": "História, Geografia e Filosofia", "short": "Humanas", "tech": False, "recommendedDay": 13},
]
AREA_IDS = {a["id"] for a in AREAS}
TECH_IDS = {a["id"] for a in AREAS if a["tech"]}

HEAD_RE = re.compile(r"^## (\d+) \| ([a-z]+) \| ([^|\n]*?)(?: \| ([^\n]*))?$", re.M)
OPT_RE = re.compile(r"^([A-E])\) ?(.*)$")
ANS_RE = re.compile(r"^> Resposta: ([A-E])\s*$", re.M)
SPLIT = "SPLITMARKERX9Q"


def md_batch(snippets):
    """Converte vários trechos Markdown em HTML com uma única chamada ao pandoc."""
    if not snippets:
        return []
    joined = f"\n\n{SPLIT}\n\n".join(convert_alerts(s) for s in snippets)
    html = subprocess.check_output(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"], input=joined, text=True)
    parts = re.split(rf"<p>{SPLIT}</p>\n?", html)
    assert len(parts) == len(snippets), (len(parts), len(snippets))
    out = []
    for p in parts:
        p = p.strip()
        p = p.replace("<table>", '<div class="table-wrap"><table class="q-table">').replace("</table>", "</table></div>")
        out.append(p)
    return out


def unwrap_p(html):
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        return html[3:-4]
    return html


def parse_exam_file(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, f"{path}: falta cabeçalho ---"
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    body = text[m.end():]
    heads = list(HEAD_RE.finditer(body))
    questions = []
    for i, h in enumerate(heads):
        block = body[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(body)].strip("\n")
        num, area, tema, extra = int(h.group(1)), h.group(2), h.group(3).strip(), (h.group(4) or "").strip()
        assert area in AREA_IDS, f"{path.name} Q{num}: área inválida {area}"
        am = ANS_RE.search(block)
        assert am, f"{path.name} Q{num}: falta '> Resposta: X'"
        before, explain = block[:am.start()], block[am.end():].strip()
        lines = before.rstrip().split("\n")
        opts = {}
        stem_lines = []
        for ln in lines:
            om = OPT_RE.match(ln)
            if om and (om.group(1) not in opts) and (not opts and om.group(1) == "A" or opts):
                opts[om.group(1)] = om.group(2).strip()
            elif opts:
                # continuação de alternativa longa
                last = list(opts)[-1]
                if ln.strip():
                    opts[last] += " " + ln.strip()
            else:
                stem_lines.append(ln)
        assert list(opts) in (list("ABCDE"), list("ABCD")), f"{path.name} Q{num}: alternativas {list(opts)}"
        assert explain, f"{path.name} Q{num}: falta explicação"
        flags = dict(kv.split("=", 1) if "=" in kv else (kv, "1") for kv in extra.split()) if extra else {}
        questions.append({
            "num": num, "area": area, "topic": tema,
            "stem_md": "\n".join(stem_lines).strip(), "options_md": [opts[k] for k in "ABCDE" if k in opts],
            "answer": "ABCDE".index(am.group(1)), "explain_md": explain, "_n": len(opts),
            "repeats": [x for x in flags.get("rep", "").split(",") if x],
            "isTech": area in TECH_IDS or "tec" in flags,
        })
    nums = [q["num"] for q in questions]
    if meta.get("completa", "sim") == "sim":
        assert nums == list(range(1, len(nums) + 1)), f"{path.name}: numeração {nums}"
    else:
        assert nums == sorted(set(nums)), f"{path.name}: numeração {nums}"
    # Converte tudo em lote
    snippets = []
    for q in questions:
        snippets.append(q["stem_md"])
        snippets.extend(q["options_md"])
        snippets.append(q["explain_md"])
    html = md_batch(snippets)
    k = 0
    for q in questions:
        q["stemHtml"] = html[k]; k += 1
        n = q.pop("_n")
        q["options"] = [unwrap_p(x) for x in html[k:k + n]]; k += n
        q["explain"] = html[k]; k += 1
        for f in ("stem_md", "options_md", "explain_md"):
            del q[f]
    return meta, questions
