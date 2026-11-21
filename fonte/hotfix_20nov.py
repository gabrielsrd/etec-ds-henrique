"""Correção rápida de 20/11 sobre o dados_plataforma.js publicado pelo agy (commit 8453438).
Substituída depois pelo build completo (fonte/build.py)."""
import json
import re
from pathlib import Path

from md import md_to_html

BASE = Path(__file__).resolve().parent.parent
js_path = BASE / "dados_plataforma.js"
raw = js_path.read_text(encoding="utf-8")
prefix = "window.ETEC_DATA = "
assert raw.startswith(prefix)
D = json.loads(raw[len(prefix):].rstrip().rstrip(";"))

# 1. Dia 1 reescrito com fatos verificados
dia1 = md_to_html((BASE / "fonte/aulas/dia_01.md").read_text(encoding="utf-8"))
ch1 = D["chapters"][0]
ch1["title"] = "Diagnóstico: a prova real de Taboão (05/12/2025)"
ch1["storyIntro"] = "Faça a prova real de dezembro/2025 sem consulta, entenda as regras do edital e mande o diagnóstico para recalibrar o plano."
ch1["lessonHtml"] = dia1
for sec in D["apostilaSections"]:
    if sec["id"] == "dia1":
        sec["title"] = "🎯 Dia 1 (21/11) • Regras do edital, números reais e diagnóstico"
        sec["html"] = dia1

# 2. Regras da 2ª fase: o edital M-Tec nº 02/2026 não usa menções MB/B/R/I
D["phase2"]["introAlert"] = (
    "<strong>Por que esta aba vale a sua vaga:</strong> nos últimos 4 anos, as 9 pessoas que passaram da prova escrita "
    "não foram aprovadas na avaliação prática. A Etec não publica o motivo, mas a prática avalia as matérias técnicas do "
    "1º ano. Chegar no dia <strong>08/12</strong> sabendo montar uma página HTML+CSS, escrever um programa simples e modelar "
    "uma tabela é o que te coloca na frente."
)

replacements = [
    ("Nos últimos 3 anos, <strong>0 de 7 candidatos passaram na prova prática</strong>. Por quê? Porque nunca abriram o VS Code nem escreveram 30 linhas de HTML/CSS/C# de verdade!",
     "Nos últimos 4 anos, <strong>nenhum dos 9 candidatos que passaram da escrita foi aprovado na prática</strong>. A prática avalia o que se faz no computador — e é isso que você vai treinar agora."),
    ("pronto para tirar <strong>B ou MB</strong>!", "pronto para mostrar que sabe fazer!"),
]
for ch in D["chapters"]:
    for a, b in replacements:
        ch["lessonHtml"] = ch["lessonHtml"].replace(a, b)
for sec in D["apostilaSections"]:
    for a, b in replacements:
        sec["html"] = sec["html"].replace(a, b)
    sec["html"] = sec["html"].replace("No Plano 612 de Taboão da Serra, TPA tem 120 aulas (mais do que qualquer outra matéria técnica!) e usa a linguagem",
                                      "No Plano 612 de Taboão da Serra, TPA tem 120 aulas (mais do que qualquer outra matéria técnica!). As provas de Taboão usam a linguagem")
for ch in D["chapters"]:
    ch["lessonHtml"] = ch["lessonHtml"].replace(
        "No Plano 612 de Taboão da Serra, TPA tem 120 aulas (mais do que qualquer outra matéria técnica!) e usa a linguagem",
        "No Plano 612 de Taboão da Serra, TPA tem 120 aulas (mais do que qualquer outra matéria técnica!). As provas de Taboão usam a linguagem")

# 3. Rótulos de provas
ex = D["exams"]
ex["taboao2026"]["title"] = "Prova Real Etec Taboão — 05/12/2025 (a mais recente)"
ex["taboao2026"]["desc"] = ("Prova real mais recente de Taboão, com as figuras originais. O gabarito publicado pela Etec não confere "
                            "com este caderno (é de outra versão), então usamos um gabarito revisado questão por questão. Comece por ela!")
ex["taboao2025"]["title"] = "Prova Real Etec Taboão — 06/12/2024"
ex["taboao2025"]["desc"] = "Prova real de Taboão com gabarito oficial: código C#, Flexbox, Box Model, hexadecimal, CLI, requisitos e Base Comum."
ex["mtec2022"]["title"] = "Prova Real Etec Taboão — 14/12/2022 (formato antigo)"
ex["mtec2022"]["badge"] = "Taboão • 40 Questões"
ex["mtec2022"]["desc"] = ("Prova real de Taboão de 2022. É mais antiga e cobra mais literatura do que as provas recentes — "
                          "use depois das de 2025 e 2024.")
D["primaryExamIds"] = ["taboao2026", "taboao2025", "sim_taboao2027", "mtec2022"]
D["extraExamIds"] = [x for x in D["extraExamIds"] if x != "mtec2022"]
ex["mtec2022"]["group"] = "primary"

js_path.write_text(prefix + json.dumps(D, ensure_ascii=False) + ";\n", encoding="utf-8")

# Verificações
txt = json.dumps(D, ensure_ascii=False)
for bad in ["0 de 7", "B ou MB", "R (Regular)", "NÃO tem no 1º ano: Biologia"]:
    left = txt.count(bad)
    print(f"{bad!r}: {left} ocorrências restantes")
print("Dia 1:", len(re.sub(r"<[^>]+>", "", dia1)), "caracteres de texto")
