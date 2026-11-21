"""Exporta as provas já estruturadas pelo agy (dados_plataforma.js) para o formato de texto. Uso único."""
import json, re, subprocess, sys
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
raw = (BASE / "dados_plataforma.js").read_text(encoding="utf-8")
D = json.loads(raw[len("window.ETEC_DATA = "):].rstrip().rstrip(";"))
SPL = "SPLITMARKERX9Q"
def h2m(snips):
    joined = f"\n<p>{SPL}</p>\n".join(snips)
    out = subprocess.check_output(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"], input=joined, text=True)
    parts = re.split(rf"\n*{SPL}\n*", out)
    assert len(parts) == len(snips)
    return [p.strip() for p in parts]
GUESS = {
 "taboao2026": "port port port port ing ing arte arte edf edf mat mat mat mat fis fis qui qui hist hist bio bio pesq pesq web web web aps aps design aps fund fund tpa tpa tpa tpa bd bd bd",
 "taboao2025": "port port port ing hist hist mat mat mat mat bio bio fis fis pesq pesq qui qui edf arte tpa tpa tpa tpa tpa aps aps bd fund fund fund web web web web web bd bd aps bd",
}
META = {
 "taboao2026": ("2025-12_DS.md", "Prova Real Etec Taboão — 05/12/2025", "05/12/2025", "revisado"),
 "taboao2025": ("2024-12_DS.md", "Prova Real Etec Taboão — 06/12/2024", "06/12/2024", "oficial"),
 "mtec2022": ("2022-12_DS.md", "Prova Real Etec Taboão — 14/12/2022", "14/12/2022", "oficial"),
}
for eid, (fname, title, date, gab) in META.items():
    qs = D["exams"][eid]["questions"]
    snips = []
    for q in qs:
        snips.append(q["stemHtml"]); snips.extend(q["options"]); snips.append(q["explain"])
    md = h2m(snips)
    areas = GUESS.get(eid, " ".join(["port"] * len(qs))).split()
    out = [f"---\nid: {eid}\ntitulo: {title}\ndata: {date}\ncurso: DS\ngabarito: {gab}\n---\n"]
    k = 0
    for i, q in enumerate(qs):
        stem = md[k]; k += 1
        opts = [o.replace("\n", " ") for o in md[k:k+5]]; k += 5
        exp = md[k]; k += 1
        exp = re.sub(r"^\(([A-E])\)\s*", "", exp)
        out.append(f"## {q['num']} | {areas[i]} | {q.get('topic','')}\n{stem}\n\n" + "\n".join(f"{L}) {o}" for L, o in zip("ABCDE", opts)) + f"\n\n> Resposta: {'ABCDE'[q['answer']]}\n\n{exp}\n")
    (BASE / "fonte/provas" / fname).write_text("\n".join(out), encoding="utf-8")
    print(fname, len(qs))
