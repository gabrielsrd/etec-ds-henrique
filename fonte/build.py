"""Gera dados_plataforma.js a partir de fonte/ (provas, aulas, dias, cards, 2ª fase).

Uso: python3 fonte/build.py
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

FONTE = Path(__file__).resolve().parent
BASE = FONTE.parent
sys.path.insert(0, str(FONTE))

from md import md_to_html  # noqa: E402
from provas import AREAS, AREA_IDS, parse_exam_file  # noqa: E402
from dias import DIAS, EXAM_META, PRIMARY, EXTRA, VIDEOS, MANUAL_GROUPS, EXTRA_OCCURRENCES  # noqa: E402
from cards import FLASHCARDS, VF, PAIRS  # noqa: E402
from fase2 import PHASE2  # noqa: E402

OLD_JS = BASE / "dados_plataforma.js"
LEGADO = json.loads((FONTE / "legado.json").read_text(encoding="utf-8"))


def load_old():
    raw = OLD_JS.read_text(encoding="utf-8")
    return json.loads(raw[len("window.ETEC_DATA = "):].rstrip().rstrip(";"))


def norm(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = unicodedata.normalize("NFKD", t.lower())
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def build_exams():
    exams = {}
    for f in sorted((FONTE / "provas").glob("*.md")):
        meta, qs = parse_exam_file(f)
        eid = meta["id"]
        em = EXAM_META[eid]
        exams[eid] = {
            "id": eid,
            "group": em["group"],
            "recommended": em.get("recommended", False),
            "title": em["title"],
            "badge": em["badge"],
            "desc": em["desc"],
            "date": meta.get("data", ""),
            "minutes": em.get("minutes", 240),
            "cutoff": em.get("cutoff", 20),
            "target": em.get("target", 24),
            "questions": qs,
        }
    # Simulados inéditos (fonte/simulados/*.md usam o mesmo formato)
    for f in sorted((FONTE / "simulados").glob("*.md")):
        meta, qs = parse_exam_file(f)
        eid = meta["id"]
        em = EXAM_META[eid]
        exams[eid] = {"id": eid, "group": em["group"], "recommended": False, "title": em["title"], "badge": em["badge"],
                      "desc": em["desc"], "date": meta.get("data", ""), "minutes": em.get("minutes", 240),
                      "cutoff": em.get("cutoff", 20), "target": em.get("target", 24), "questions": qs}
    return exams


REAL_ORDER = ["taboao2021", "mtec2022", "taboao2023", "irma2024ipi", "taboao2025", "irma2025inf", "irma2025ipi", "taboao2026"]
LABEL = {"taboao2021": "2021", "mtec2022": "2022", "taboao2023": "dez/2023", "irma2024ipi": "dez/2024 (Inf. p/ Internet)",
         "taboao2025": "dez/2024", "irma2025inf": "dez/2025 (Informática)", "irma2025ipi": "dez/2025 (Inf. p/ Internet)",
         "taboao2026": "dez/2025"}


def find_repeats(exams):
    """Agrupa questões repetidas entre provas reais diferentes (mesmo enunciado e mesmas alternativas)."""
    items = []
    for eid in REAL_ORDER:
        for q in exams[eid]["questions"]:
            items.append((eid, q, norm(q["stemHtml"]), sorted(norm(o) for o in q["options"])))
    parent = list(range(len(items)))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            e1, q1, s1, o1 = items[i]
            e2, q2, s2, o2 = items[j]
            if e1 == e2:
                continue
            rs = difflib.SequenceMatcher(None, s1, s2).ratio()
            if rs < 0.72:
                continue
            ro = difflib.SequenceMatcher(None, " ".join(o1), " ".join(o2)).ratio()
            if rs > 0.9 and ro > 0.6 or rs > 0.72 and ro > 0.85:
                parent[root(i)] = root(j)
    idx = {(it[0], it[1]["num"]): k for k, it in enumerate(items)}
    for grp in MANUAL_GROUPS:
        ks = [idx[x] for x in grp]
        for k in ks[1:]:
            parent[root(k)] = root(ks[0])
    groups = {}
    for i in range(len(items)):
        groups.setdefault(root(i), []).append(i)
    reps = []
    for g in groups.values():
        exs = sorted({items[i][0] for i in g}, key=REAL_ORDER.index)
        extra = sum(len(EXTRA_OCCURRENCES.get((items[i][0], items[i][1]["num"]), [])) for i in g)
        if len(exs) + extra < 2:
            continue
        reps.append([items[i] for i in sorted(g, key=lambda k: REAL_ORDER.index(items[k][0]))])
    return reps


def build_repeat_exam(exams, reps):
    qs = []
    def vezes_de(g):
        return len(g) + sum(len(EXTRA_OCCURRENCES.get((e, qq["num"]), [])) for e, qq, _, _ in g)
    for n, grp in enumerate(sorted(reps, key=lambda g: -vezes_de(g)), start=1):
        eid, q, _, _ = grp[-1]  # versão mais recente
        extras = [x for e, qq, _, _ in grp for x in EXTRA_OCCURRENCES.get((e, qq["num"]), [])]
        onde = ", ".join([f"{LABEL[e]} (Q{qq['num']})" for e, qq, _, _ in grp] + extras)
        vezes = len(grp) + len(extras)
        for e, qq, _, _ in grp:
            qq.setdefault("repeatsIn", [])
            qq["repeatsIn"] = [f"{LABEL[x]} Q{y['num']}" for x, y, _, _ in grp if not (x == e and y['num'] == qq['num'])]
        nq = dict(q)
        nq["num"] = n
        nq["source"] = f"{exams[eid]['title']} — questão {q['num']}"
        nq["explain"] = (f'<div class="callout callout-important"><p><strong>🔁 Caiu {vezes} vezes:</strong> {onde}.</p></div>'
                         + q["explain"])
        qs.append(nq)
    return {
        "id": "repetidas", "group": "primary", "recommended": False,
        "title": "Treino das Repetidas — questões que a Etec já repetiu",
        "badge": f"🔁 {len(qs)} questões • caíram 2 ou mais vezes",
        "desc": ("Questões que apareceram em duas ou mais provas de Taboão, quase sempre com o mesmo enunciado e as mesmas "
                 "alternativas. São as apostas mais seguras para 04/12: refaça até acertar todas."),
        "date": "", "minutes": 60, "cutoff": max(1, len(qs) // 2), "target": len(qs), "questions": qs,
    }


def lesson_html(day, old=None):
    md_path = FONTE / "aulas" / f"dia_{day:02d}.md"
    if md_path.exists():
        return md_to_html(md_path.read_text(encoding="utf-8")), True
    leg = {c["day"]: c["lessonHtml"] for c in LEGADO["chapters"]}
    mapa = {9: [], 10: [9], 13: [10, 13]}
    origem = mapa.get(day, [day])
    if not origem:
        return "<p>Hoje o estudo é a prova: abra a aba Provas e faça a prova indicada no topo deste dia.</p>", False
    return "<hr>".join(leg[d] for d in origem), False


def main():
    old = load_old()
    exams = build_exams()
    reps = find_repeats(exams)
    exams["repetidas"] = build_repeat_exam(exams, reps)

    chapters = []
    novas = []
    for d in DIAS:
        html, nova = lesson_html(d["day"], old)
        if nova:
            novas.append(d["day"])
        refs = d["quiz"]
        for r in refs:
            ex = exams[r["examId"]]
            assert any(q["num"] == r["qNum"] for q in ex["questions"]), f"Dia {d['day']}: ref inválida {r}"
            if d["day"] in range(2, 9):
                assert r["examId"] != "taboao2025", f"Dia {d['day']} usa dez/2024 antes do simulado do Dia 9: {r}"
        clips = [dict(VIDEOS[v[0]], startSec=v[1], endSec=v[2], tip=v[3]) for v in d.get("videos", [])]
        chapters.append({
            "day": d["day"], "dateLabel": d["date"], "phase": d["phase"], "title": d["title"], "weight": d["weight"],
            "storyIntro": d["intro"], "lessonHtml": html, "practiceType": d["practice"], "practiceTag": d.get("tag", ""),
            "videoClips": clips, "challengeRefs": refs, "examTask": d.get("examTask"),
        })

    for v in VF:
        assert v["area"] in AREA_IDS, v
    mapa = md_to_html((FONTE / "aulas" / "mapa_da_prova.md").read_text(encoding="utf-8"))
    apostila = [{"id": "mapa", "title": "📊 Como a Etec de Taboão monta a prova (padrões, pegadinhas e chute)", "html": mapa}] + [{"id": f"dia{c['day']}", "title": f"Dia {c['day']} ({c['dateLabel']}) • {c['title']}", "html": c["lessonHtml"]}
                for c in chapters]

    data = {
        "platformVersion": "taboao_mtec_2027_v4",
        "schoolName": "Etec de Taboão da Serra — 2ª Série M-Tec-PI (DS)",
        "examDateIso": "2026-12-04",
        "phase2DateIso": "2026-12-08",
        "defaultStartIso": "2026-11-21",
        "primaryExamIds": PRIMARY,
        "extraExamIds": EXTRA,
        "areas": AREAS,
        "vfStatements": VF,
        "cardsVersion": "cards_v2_20261121",
        "flashcards": FLASHCARDS,
        "pairs": PAIRS,
        "phase2": PHASE2,
        "exams": exams,
        "apostilaSections": apostila,
        "chapters": chapters,
    }
    for eid in PRIMARY + EXTRA:
        assert eid in exams, f"prova {eid} listada mas não existe"
    OLD_JS.write_text("window.ETEC_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")

    total_q = sum(len(e["questions"]) for e in exams.values())
    print(f"provas: {len(exams)} ({total_q} questões) | repetidas: {len(reps)} grupos | aulas novas: {novas}")
    for c in chapters:
        txt = len(re.sub(r"<[^>]+>", "", c["lessonHtml"]))
        print(f"  Dia {c['day']:02d} {c['dateLabel']:10} {txt:6} chars | quiz {len(c['challengeRefs'])} | {c['title']}")


if __name__ == "__main__":
    main()
