# -*- coding: utf-8 -*-
import json
import re
import subprocess
import sys
from pathlib import Path

SCRATCH = Path("/home/galves/.gemini/antigravity-cli/brain/810bbede-d2b8-441a-bdef-d5e94d7dfe42/scratch")
BASE = Path("/home/galves/gabriel/projeto-henrique/estudo-etec-ds")
sys.path.insert(0, str(SCRATCH))

from build_exams_json import sim1_qs, sim2_qs, apo_qs
from parse_fat_pdfs import build_all_fat
from parse_mtec_2022 import build_mtec_2022
from parse_taboao_exams import build_taboao_2026, build_taboao_2025, build_sim_taboao_2027
from taboao_lessons_1_8 import TABOAO_LESSONS_1_8
from taboao_lessons_9_16 import TABOAO_LESSONS_9_16
from taboao_phase2_content import PHASE2_DATA
from taboao_cards_vf import (
    TABOAO_AREAS,
    classify_taboao_area,
    TABOAO_FLASHCARDS,
    TABOAO_PAIRS,
    TABOAO_VF,
)
from mtec_content import PORTUGOL_SINTAXE_MD


TECH_AREAS = {"tpa_csharp", "web_design", "bd_aps_fi"}


TABOAO_COLA_BOLSO_HTML = """
<div class="callout callout-note">
  <strong>⚡ COLA DE BOLSO DE 1 PÁGINA — ETEC TABOÃO DA SERRA (04/12 &amp; 08/12)</strong><br>
  Revise estes 15 blocos de ouro antes da <strong>1ª Fase (04/12 — corte 20/40)</strong> e da <strong>2ª Fase (08/12 — Prática + Entrevista)</strong>!
</div>
<div class="table-wrap"><table class="q-table">
  <thead><tr><th>Matéria (1º Ano Taboão)</th><th>Verdade Oficial (Marque sem medo)</th><th>Pegadinha Clássica (Fuja disso!)</th></tr></thead>
  <tbody>
    <tr><td><strong>Fundamentos (Hex &amp; CLI)</strong></td><td><strong>187 (dec) = BB (hex)</strong> (<code>187 ÷ 16 = 11</code>, resto <code>11</code>; <code>10=A, 11=B... 15=F</code>).<br><strong>CLI:</strong> Interface por linha de comando (texto).<br><strong>Multiusuário:</strong> vários usuários com permissões próprias.</td><td>Achar que <code>11</code> em Hex é <code>A</code> (<code>10=A</code>, <code>11=B</code>!) ou confundir CLI com janela gráfica (GUI).</td></tr>
    <tr><td><strong>TPA (C# — Laços &amp; Matriz)</strong></td><td><strong><code>do-while</code>:</strong> executa pelo menos <strong>1 vez</strong> garantida.<br><strong><code>while</code>:</strong> testa antes (pode rodar 0 vezes).<br><strong>Matriz C#:</strong> <code>int[,]</code> → <code>matriz[linha, coluna]</code> começando do <strong>0</strong>!<br><strong><code>%</code>:</strong> resto da divisão (<code>i % 2 == 0</code> = par).</td><td>Começar vetor/matriz no índice 1; confundir <code>=</code> (guarda) com <code>==</code> (compara); achar que <code>%</code> é porcentagem!</td></tr>
    <tr><td><strong>TPA (Debug &amp; Erros C#)</strong></td><td><strong>Breakpoint:</strong> pausa a execução em uma linha para inspecionar variáveis e achar bugs.<br><strong><code>try / catch</code>:</strong> captura erro (ex.: digitar letra no lugar de número) sem travar.<br><strong>Erro de sintaxe:</strong> falta <code>;</code> ou <code>}</code> → compilador recusa compilar!</td><td>Achar que o compilador corrige falta de <code>;</code> sozinho ou que <em>breakpoint</em> apaga código!</td></tr>
    <tr><td><strong>Web I (HTML5 &amp; Internet)</strong></td><td><code>&lt;p&gt;</code> parágrafo | <code>&lt;hr&gt;</code> linha horizontal | <code>&lt;h2&gt;</code> subtítulo | <code>&lt;br&gt;</code> quebra de linha | <code>&lt;body&gt;</code> conteúdo visível.<br><code>&lt;img alt="..."&gt;</code> = texto alternativo + acessibilidade.<br><code>&lt;script src="app.js"&gt;&lt;/script&gt;</code> = liga JS externo.<br><strong>URI:</strong> identifica recurso de forma única na Web.</td><td>Usar <code>&lt;link&gt;</code> para puxar JS (<code>&lt;link&gt;</code> é para CSS!); mandar senha por <code>GET</code> (use <strong><code>POST</code></strong>!).</td></tr>
    <tr><td><strong>Web I (CSS3, Flexbox &amp; JS)</strong></td><td><strong>Box Model:</strong> <code>padding</code> (interno) vs <code>margin</code> (externo).<br><strong>Flexbox:</strong> <code>display: flex; justify-content: center; align-items: center;</code>.<br><strong>Responsivo:</strong> <code>@media (max-width: 600px)</code>.<br><strong>JS Primitivos:</strong> <code>String, Number, Boolean, Undefined, Null</code>.</td><td>Inverter <code>padding</code> com <code>margin</code>; achar que <code>Array</code> ou <code>Object</code> são tipos primitivos!</td></tr>
    <tr><td><strong>Banco de Dados I</strong></td><td><strong>Tabela</strong> = conjunto de dados | <strong>Registro</strong> = 1 linha individual | <strong>Campo</strong> = coluna.<br><strong>PK:</strong> única e <code>NOT NULL</code> | <strong>FK:</strong> vai sempre no lado <strong><code>N</code></strong> (em <code>N:N</code> cria 3ª tabela!).<br><strong>Normalização:</strong> elimina redundâncias/anomalias (<strong>1FN</strong> = valores atômicos).<br><strong>SQL:</strong> DDL (<code>CREATE/ALTER/DROP</code>), DML (<code>INSERT/UPDATE/DELETE</code>), DQL (<code>SELECT</code>).</td><td>Pôr dois telefones na mesma célula (quebra 1FN!); inverter DDL com DML!</td></tr>
    <tr><td><strong>APS (Requisitos &amp; UML)</strong></td><td><strong>RF:</strong> O QUE faz | <strong>RNF:</strong> COMO se comporta (velocidade/segurança).<br><strong>Ágeis:</strong> Scrum, XP, Kanban.<br><strong>Casos de Uso:</strong> interação atores × funcionalidades.<br><strong>Diagrama de Classes:</strong> associações = relacionamentos entre classes.</td><td>Chamar <em>Cascata</em> de método ágil ou confundir Casos de Uso com Diagrama de Classes!</td></tr>
    <tr><td><strong>Design Digital &amp; UX</strong></td><td><strong>Usabilidade:</strong> facilidade, eficiência e satisfação de uso.<br><strong>RGB</strong> (telas/luz) vs <strong>CMYK</strong> (impressão/tinta).<br><strong>Vetor</strong> (<code>SVG, PDF</code> — não pixela, ideal p/ logo) vs <strong>Bitmap</strong> (<code>JPEG, PNG</code>).</td><td>Achar que usabilidade é só "deixar bonito" ou chamar JPEG/PNG de vetor!</td></tr>
    <tr><td><strong>Português &amp; Inglês</strong></td><td><strong>Adequação:</strong> varia com contexto/público | <strong>Conativa:</strong> imperativo (propaganda).<br><strong>Present Perfect:</strong> <code>have/has + Particípio</code> (<code>She has finished</code>).<br><strong>Phrasal Verbs:</strong> <code>give up</code> (desistir), <code>find out</code> (descobrir), <code>look for</code> (procurar).</td><td>Usar <code>has</code> com plural (<em>They has</em> = erro!) ou traduzir <code>actually</code> como "atualmente"!</td></tr>
    <tr><td><strong>Pesquisa, Arte &amp; Ed. Física</strong></td><td><strong>Quantitativa</strong> (números/gráficos) vs <strong>Qualitativa</strong> (opiniões/sentidos).<br><strong>SWOT:</strong> Interno (S/W) vs Externo (O/T).<br><strong>Arte:</strong> Tema (ideia/assunto) vs Técnica (como faz: aquarela, grafite).<br><strong>Ed. Física:</strong> Isométrica (prancha parada); Invasão (futebol/basquete/handebol — vôlei NÃO!).</td><td>Confundir Tema com Técnica ou colocar Vôlei como esporte de invasão!</td></tr>
    <tr><td><strong>Matemática Taboão</strong></td><td><strong>Venn:</strong> <code>(A + B) - (Total - Nenhum) = Interseção</code>.<br><strong>Log:</strong> <code>log_a(mᵏ · nᵖ) = k·log_a(m) + p·log_a(n)</code>.<br><strong>PA:</strong> <code>aₙ = a₁ + (n-1)·r</code> | <strong>Pitágoras:</strong> 3-4-5 (30-40-50, 330-440-550).<br><strong>Inequação:</strong> dividir por negativo <strong>inverte o sinal</strong>!</td><td>Esquecer de virar o sinal na inequação ou começar número de 3 dígitos com <code>0</code>!</td></tr>
    <tr><td><strong>Física, Química &amp; História</strong></td><td><strong>Gases:</strong> <code>T</code> (Kelvin) proporcional a <code>p × V</code> (dobrou V c/ p igual → dobrou T!).<br><strong>Lente lupa (entre F e O):</strong> Virtual, Direita e Maior.<br><strong>Química:</strong> Bohr (elétron retorna e emite luz); Exotérmica (libera calor); Metal conduz sólido.<br><strong>História:</strong> Idade Média (Clero, Nobreza, Servos); Atenas excluía mulheres/escravos/estrangeiros; Renascimento = Antropocentrismo/Razão.</td><td>Usar Celsius em vez de Kelvin nos gases ou achar que Atenas incluía mulheres na democracia!</td></tr>
  </tbody>
</table></div>
"""


def convert_alerts(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r'^>\s*\[!(WARNING|CAUTION|NOTE|TIP|IMPORTANT)\]\s*(.*)$', lines[i])
        if m:
            kind = m.group(1).lower()
            block = [m.group(2)] if m.group(2).strip() else []
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                block.append(re.sub(r'^>\s?', '', lines[i]))
                i += 1
            out.append(f'<div class="callout callout-{kind}">\n\n' + "\n".join(block) + "\n\n</div>\n")
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def md_to_html(md_text: str) -> str:
    clean_md = convert_alerts(md_text)
    clean_md = clean_md.replace("$\\rightarrow$", "→").replace("$\\leftrightarrow$", "↔")
    html = subprocess.check_output(
        ["pandoc", "-f", "gfm", "-t", "html5"],
        input=clean_md,
        text=True,
    )
    html = html.replace("<table>", '<div class="table-wrap"><table class="q-table">')
    html = html.replace("</table>", "</table></div>")
    return html


def main():
    tab26 = build_taboao_2026()
    tab25 = build_taboao_2025()
    sim27 = build_sim_taboao_2027()
    mtec22 = build_mtec_2022()
    ds25, info25, ds19 = build_all_fat()

    # Ordem prioritária: primeiro as 4 provas 40Q padrão Taboão da Serra; depois as 6 provas extras FAT (preservando IDs antigos!)
    primary_exam_ids = ["taboao2026", "taboao2025", "sim_taboao2027"]
    extra_exam_ids = ["mtec2022", "ds2025", "info2025", "ds2019", "apostas", "sim1", "sim2"]

    exams = {
        "taboao2026": {
            "id": "taboao2026",
            "group": "primary",
            "recommended": True,
            "title": "Prova Real Etec Taboão da Serra — 2ª Série M-Tec DS (05/12/2025)",
            "badge": "⭐ DIAGNÓSTICO OFICIAL • 40 Questões",
            "desc": "A prova oficial MAIS RECENTE da Etec de Taboão da Serra (1º Sem/2026), com as 5 figuras reais, gabarito 100% revisado e comentários passo a passo. Comece por ela!",
            "minutes": 240,
            "cutoff": 20,
            "target": 25,
            "questions": tab26,
        },
        "taboao2025": {
            "id": "taboao2025",
            "group": "primary",
            "title": "Prova Real Etec Taboão da Serra — 2ª Série M-Tec DS (06/12/2024)",
            "badge": "Taboão Oficial • 40 Questões",
            "desc": "Prova oficial de Taboão da Serra (1º Sem/2025) com gabarito oficial: códigos C# reais (int[,], for %), Flexbox, Box Model, Hex 187=BB, CLI, Requisitos e Base Comum.",
            "minutes": 240,
            "cutoff": 20,
            "target": 25,
            "questions": tab25,
        },
        "sim_taboao2027": {
            "id": "sim_taboao2027",
            "group": "primary",
            "title": "Simulado Inédito Premonição — Taboão da Serra (04/12/2026)",
            "badge": "🎯 PREMONIÇÃO 2027 • 40 Questões",
            "desc": "40 questões inéditas construídas no molde exato das provas de Taboão da Serra (Base Comum do 1º ano + 18 questões técnicas de C#, Web I, BD I, APS, UX e Fundamentos).",
            "minutes": 240,
            "cutoff": 20,
            "target": 25,
            "questions": sim27,
        },
        "mtec2022": {
            "id": "mtec2022",
            "group": "extra",
            "title": "Prova Extra M-Tec 2022 (outra Etec — NÃO é o padrão de Taboão)",
            "badge": "Treino Extra • 40 Questões",
            "desc": "Prova de 2022 de outra unidade, com literatura e temas que Taboão NÃO cobra. Mantida só para preservar o histórico — prefira as provas de Taboão.",
            "minutes": 240,
            "cutoff": 20,
            "target": 25,
            "questions": mtec22,
        },
        "ds2025": {
            "id": "ds2025",
            "group": "extra",
            "title": "Prova Extra Fundação FAT — DS Modular (1º SEM/2025)",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "Prova técnica modular da Fundação FAT — ótima como treino extra de SQL, Design, HTML/CSS e Lógica (lembrando que Taboão usa formato M-Tec 40Q).",
            "minutes": 180,
            "cutoff": 15,
            "target": 20,
            "questions": ds25,
        },
        "info2025": {
            "id": "info2025",
            "group": "extra",
            "title": "Prova Extra FAT — Info para Internet (1º SEM/2025)",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "Treino extra técnico com Binário, DOM, CSS, UML, Requisitos e Banco de Dados.",
            "minutes": 180,
            "cutoff": 15,
            "target": 20,
            "questions": info25,
        },
        "ds2019": {
            "id": "ds2019",
            "group": "extra",
            "title": "Prova Extra Histórica FAT — DS (1º SEM/2019)",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "Treino extra com Tabela Verdade, Algoritmos, Cascata, Scrum, Git e CSS3.",
            "minutes": 180,
            "cutoff": 15,
            "target": 20,
            "questions": ds19,
        },
        "apostas": {
            "id": "apostas",
            "group": "extra",
            "title": "Simulado Extra — 30 Apostas Técnicas FAT",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "30 questões técnicas extras focadas em algoritmos, SQL, modelagem e web.",
            "minutes": 120,
            "cutoff": 15,
            "target": 20,
            "questions": apo_qs,
        },
        "sim1": {
            "id": "sim1",
            "group": "extra",
            "title": "Simulado Extra Técnico #1 — Núcleo Principal",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "Simulado técnico complementar de 30 questões.",
            "minutes": 120,
            "cutoff": 15,
            "target": 20,
            "questions": sim1_qs,
        },
        "sim2": {
            "id": "sim2",
            "group": "extra",
            "title": "Simulado Extra Técnico #2 — Tópicos Irmãos",
            "badge": "Treino Técnico Extra • 30 Questões",
            "desc": "Simulado técnico complementar cobrindo tópicos extras do 1º módulo.",
            "minutes": 120,
            "cutoff": 15,
            "target": 20,
            "questions": sim2_qs,
        },
    }

    # Classifica area + isTech em todas as 340 questões (preservando os rótulos precisos das 3 provas Taboão!)
    valid_areas = {a["id"] for a in TABOAO_AREAS}
    for exam_id, ex in exams.items():
        for q in ex["questions"]:
            if not q.get("area") or q["area"] not in valid_areas:
                q["area"] = classify_taboao_area(exam_id, q["num"])
            assert q["area"] in valid_areas, f"Invalid area {q['area']} for {exam_id} Q{q['num']}"
            if "isTech" not in q:
                q["isTech"] = q["area"] in TECH_AREAS

    # Renderiza as 16 aulas (21/11 -> 07/12) + guia de sintaxe
    lessons_md = {**TABOAO_LESSONS_1_8, **TABOAO_LESSONS_9_16}
    assert set(lessons_md.keys()) == set(range(1, 17)), f"Expected 16 lessons, got {sorted(lessons_md.keys())}"
    lessons_html = {d: md_to_html(lessons_md[d]) for d in range(1, 17)}
    portugol_sintaxe_html = md_to_html(PORTUGOL_SINTAXE_MD)

    # Atualiza o Guia Teórico completo em Markdown (usado também para gerar o PDF da Apostila!)
    guia_header = (
        "# Guia Definitivo — Etec de Taboão da Serra (2ª Série M-Tec-PI Desenvolvimento de Sistemas)\n\n"
        "**Calendário Oficial:** 1ª Fase Escrita em **04/12/2026** (40 questões • corte 20/40) • "
        "Resultado em **07/12/2026** • 2ª Fase Prática em Laboratório + Entrevista em **08/12/2026** (13h00–15h30).\n\n"
        "Este manual foi 100% construído por engenharia reversa das provas reais e do Plano de Curso 612 da Etec de Taboão da Serra.\n\n---\n\n"
    )
    (BASE / "apostila/01_guia_teorico_fundacao_fat.md").write_text(
        guia_header
        + "\n\n---\n\n".join(lessons_md[d] for d in range(1, 17))
        + "\n\n---\n\n"
        + PORTUGOL_SINTAXE_MD
        + "\n",
        encoding="utf-8",
    )

    apostilaSections = [
        {"id": "cola", "title": "⚡ Cola de Bolso Taboão (1 Página • 04/12 & 08/12)", "html": TABOAO_COLA_BOLSO_HTML},
        {"id": "dia1", "title": "🎯 Dia 1 (21/11) • Raio-X Taboão, Regras 20/40 & 3 Passadas", "html": lessons_html[1]},
        {"id": "tpa", "title": "💻 Dias 2–3 (22–23/11) • TPA em C#: Lógica, if/else, Laços, Vetores, int[,], Debug & try/catch", "html": lessons_html[2] + "<hr>" + lessons_html[3]},
        {"id": "web", "title": "🌐 Dias 4–5 (24–25/11) • Programação Web I: HTML5, Formulários, URI, CSS3, Box Model, Flexbox & JS", "html": lessons_html[4] + "<hr>" + lessons_html[5]},
        {"id": "bd", "title": "🗄️ Dia 6 (26/11) • Banco de Dados I: Tabelas, PK/FK, DER, Normalização 1FN–3FN & SQL", "html": lessons_html[6]},
        {"id": "aps_ux", "title": "📐 Dia 7 (27/11) • APS (Requisitos, Ágil, UML) + Design Digital & UX", "html": lessons_html[7]},
        {"id": "fund", "title": "⚙️ Dia 8 (28/11) • Fundamentos: Hexadecimal 187=BB, Binário, CLI, Hardware & SO", "html": lessons_html[8]},
        {"id": "base_ling", "title": "📚 Dias 9–10 (29–30/11) • Português, Inglês, Pesquisa Científica, Empreendedorismo, Arte & Ed. Física", "html": lessons_html[9] + "<hr>" + lessons_html[10]},
        {"id": "base_exatas", "title": "📐 Dias 11–12 (01–02/12) • Matemática Taboão + Física, Química & História (Alvos Certos)", "html": lessons_html[11] + "<hr>" + lessons_html[12]},
        {"id": "vespera", "title": "🏁 Dia 13 (03/12) • Revisão 15 Pontos de Ouro & Checklist 04/12", "html": lessons_html[13]},
        {"id": "fase2_sprint", "title": "🛠️ Dias 14–16 (05–07/12) • Sprint 2ª Fase: Lab Web I, Lab C# Console, Lab BD I & Entrevista", "html": lessons_html[14] + "<hr>" + lessons_html[15] + "<hr>" + lessons_html[16]},
        {"id": "portugol_sintaxe", "title": "🗣️ Guia Extra: Como Ler Qualquer Código do Zero (Portugol ↔ C# / JS)", "html": portugol_sintaxe_html},
    ]

    chapters = [
        {
            "day": 1,
            "dateLabel": "Sáb 21/11",
            "phase": 1,
            "title": "Diagnóstico Oficial Taboão (05/12/2025) & Estratégia 20/40",
            "weight": "Essencial",
            "storyIntro": "Comece pelo Diagnóstico Real de Taboão da Serra, entenda as regras do Edital (20/40 + 2ª Fase em 08/12) e aprenda a Estratégia das 3 Passadas.",
            "lessonHtml": lessons_html[1],
            "practiceType": "lab_tipos",
            "practiceTag": "03_BD_APS_FI",
            "videoClips": [
                {
                    "title": "Variáveis e Tipos Primitivos de Dados",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "N91jAze53uA",
                    "startSec": 65,
                    "endSec": 345,
                    "tip": "Foco: como funcionam variáveis na memória e os tipos básicos antes do diagnóstico.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 32},
                {"examId": "taboao2026", "qNum": 33},
                {"examId": "taboao2026", "qNum": 38},
                {"examId": "taboao2026", "qNum": 39},
                {"examId": "taboao2026", "qNum": 40},
                {"examId": "sim_taboao2027", "qNum": 23},
                {"examId": "sim_taboao2027", "qNum": 32},
                {"examId": "sim_taboao2027", "qNum": 38},
            ],
        },
        {
            "day": 2,
            "dateLabel": "Dom 22/11",
            "phase": 1,
            "title": "TPA I: Lógica, Fluxograma, Tabela Verdade e if/else em C#",
            "weight": "Máxima",
            "storyIntro": "A matéria com maior carga horária do 1º ano (120 aulas!): domine tipos em C#, operadores && / || / %, if/else e erros de sintaxe.",
            "lessonHtml": lessons_html[2],
            "practiceType": "lab_tipos",
            "practiceTag": "01_TPA_CSharp",
            "videoClips": [
                {
                    "title": "Variáveis e Tipos Primitivos de Dados",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "N91jAze53uA",
                    "startSec": 65,
                    "endSec": 345,
                    "tip": "Foco: diferença entre inteiro (int), real (double), texto (string) e lógico (bool).",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 34},
                {"examId": "taboao2025", "qNum": 24},
                {"examId": "sim_taboao2027", "qNum": 35},
                {"examId": "ds2019", "qNum": 1},
                {"examId": "ds2019", "qNum": 2},
                {"examId": "ds2025", "qNum": 8},
                {"examId": "info2025", "qNum": 19},
                {"examId": "info2025", "qNum": 20},
            ],
        },
        {
            "day": 3,
            "dateLabel": "Seg 23/11",
            "phase": 1,
            "title": "TPA II: Laços (while/do/for), Vetores, Matrizes int[,] & Debug C#",
            "weight": "Máxima",
            "storyIntro": "Resolva teste de mesa em C# com %, leia matrizes int[,], diferencie while vs do-while e domine breakpoints e try/catch.",
            "lessonHtml": lessons_html[3],
            "practiceType": "lab02",
            "practiceTag": "01_TPA_CSharp",
            "videoClips": [
                {
                    "title": "Estruturas de Repetição 1: Enquanto (While)",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "U5PnCt58Q68",
                    "startSec": 150,
                    "endSec": 510,
                    "tip": "Foco: como acompanhar o valor das variáveis passo a passo (Teste de Mesa).",
                },
                {
                    "title": "Matrizes — Curso de Algoritmos #15",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "hkE9WrjpAAk",
                    "startSec": 105,
                    "endSec": 495,
                    "tip": "Foco: navegação por [linha, coluna] em matrizes (igual à Q22 de Taboão 2025!).",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 35},
                {"examId": "taboao2026", "qNum": 36},
                {"examId": "taboao2026", "qNum": 37},
                {"examId": "taboao2025", "qNum": 21},
                {"examId": "taboao2025", "qNum": 22},
                {"examId": "taboao2025", "qNum": 23},
                {"examId": "taboao2025", "qNum": 25},
                {"examId": "sim_taboao2027", "qNum": 36},
                {"examId": "sim_taboao2027", "qNum": 37},
            ],
        },
        {
            "day": 4,
            "dateLabel": "Ter 24/11",
            "phase": 1,
            "title": "Programação Web I (Pt. 1): HTML5, Formulários & Internet (WWW/URI/DNS)",
            "weight": "Máxima",
            "storyIntro": "Domine todas as tags que caíram em Taboão (<p>, <hr>, <h2>, <br>, <body>, <img alt>, <script src>), formulários POST e URI/HTTP.",
            "lessonHtml": lessons_html[4],
            "practiceType": "lab01",
            "practiceTag": "02_Web_Design",
            "videoClips": [
                {
                    "title": "Semântica na HTML5 é Importante",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "HaSgt1hK2Fs",
                    "startSec": 180,
                    "endSec": 570,
                    "tip": "Foco: tags semânticas (<header>, <main>, <footer>) vs <div> genérica.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 25},
                {"examId": "taboao2026", "qNum": 26},
                {"examId": "taboao2026", "qNum": 27},
                {"examId": "taboao2025", "qNum": 32},
                {"examId": "taboao2025", "qNum": 35},
                {"examId": "sim_taboao2027", "qNum": 23},
                {"examId": "sim_taboao2027", "qNum": 24},
                {"examId": "sim_taboao2027", "qNum": 26},
            ],
        },
        {
            "day": 5,
            "dateLabel": "Qua 25/11",
            "phase": 1,
            "title": "Programação Web I (Pt. 2): CSS3, Box Model, Flexbox, @media & JS",
            "weight": "Máxima",
            "storyIntro": "Centralize qualquer bloco com Flexbox, separe padding de margin no Box Model, entenda @media e acerte tipos primitivos em JS.",
            "lessonHtml": lessons_html[5],
            "practiceType": "lab01",
            "practiceTag": "02_Web_Design",
            "videoClips": [
                {
                    "title": "Modelo de Caixas (Box Model): Primeiros Passos",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "3ZFYXkzXhqE",
                    "startSec": 120,
                    "endSec": 510,
                    "tip": "Foco: diferença visual entre content, padding (interno), border e margin (externo).",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2025", "qNum": 33},
                {"examId": "taboao2025", "qNum": 34},
                {"examId": "taboao2025", "qNum": 36},
                {"examId": "sim_taboao2027", "qNum": 25},
                {"examId": "ds2019", "qNum": 16},
                {"examId": "ds2019", "qNum": 17},
                {"examId": "ds2019", "qNum": 19},
                {"examId": "taboao2025", "qNum": 32},
            ],
        },
        {
            "day": 6,
            "dateLabel": "Qui 26/11",
            "phase": 1,
            "title": "Banco de Dados I: Tabelas, PK/FK, DER, Normalização & SQL",
            "weight": "Máxima",
            "storyIntro": "Garanta as 3–4 questões de BD I na escrita e já domine PK/FK, DER, 1FN–3FN e SQL (DDL/DML/DQL) para a prática de 08/12!",
            "lessonHtml": lessons_html[6],
            "practiceType": "lab03",
            "practiceTag": "03_BD_APS_FI",
            "videoClips": [
                {
                    "title": "Modelagem de Dados: Normalização e 1ª Forma Normal (1FN)",
                    "channel": "Bóson Treinamentos",
                    "videoId": "eRaAMNjCFYw",
                    "startSec": 60,
                    "endSec": 450,
                    "tip": "Foco: por que normalizar bancos de dados (eliminar redundância e anomalias).",
                },
                {
                    "title": "Criando o Primeiro Banco de Dados SQL (DDL)",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "m9YPlX0fcJk",
                    "startSec": 180,
                    "endSec": 540,
                    "tip": "Foco: CREATE TABLE e tipos de dados básicos para a 2ª Fase.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 38},
                {"examId": "taboao2026", "qNum": 39},
                {"examId": "taboao2026", "qNum": 40},
                {"examId": "taboao2025", "qNum": 37},
                {"examId": "taboao2025", "qNum": 38},
                {"examId": "taboao2025", "qNum": 39},
                {"examId": "taboao2025", "qNum": 40},
                {"examId": "sim_taboao2027", "qNum": 38},
                {"examId": "sim_taboao2027", "qNum": 39},
                {"examId": "sim_taboao2027", "qNum": 40},
            ],
        },
        {
            "day": 7,
            "dateLabel": "Sex 27/11",
            "phase": 1,
            "title": "APS (Requisitos, Ágil, UML) + Design Digital & UX",
            "weight": "Alta",
            "storyIntro": "Acerte em cheio Requisitos Funcionais vs Não Funcionais, Scrum/XP/Kanban, Diagramas UML (Casos de Uso e Classes), Usabilidade, RGB/CMYK e Vetor!",
            "lessonHtml": lessons_html[7],
            "practiceType": "lab04",
            "practiceTag": "02_Web_Design",
            "videoClips": [
                {
                    "title": "Scrum // Dicionário do Programador",
                    "channel": "Código Fonte TV",
                    "videoId": "3aCww_1RnL0",
                    "startSec": 120,
                    "endSec": 480,
                    "tip": "Foco: visão clara de Metodologias Ágeis (Scrum, Sprints, PO, Scrum Master).",
                },
                {
                    "title": "RGB vs. CMYK e Vetor vs. Bitmap no Design",
                    "channel": "Curso de Design Digital",
                    "videoId": "wU6rwo-SeIw",
                    "startSec": 15,
                    "endSec": 215,
                    "tip": "Foco: diferença visual direta entre RGB vs CMYK e Vetor SVG vs Bitmap.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 28},
                {"examId": "taboao2026", "qNum": 29},
                {"examId": "taboao2026", "qNum": 30},
                {"examId": "taboao2025", "qNum": 26},
                {"examId": "taboao2025", "qNum": 27},
                {"examId": "taboao2025", "qNum": 28},
                {"examId": "sim_taboao2027", "qNum": 27},
                {"examId": "sim_taboao2027", "qNum": 28},
                {"examId": "sim_taboao2027", "qNum": 30},
                {"examId": "sim_taboao2027", "qNum": 31},
            ],
        },
        {
            "day": 8,
            "dateLabel": "Sáb 28/11",
            "phase": 1,
            "title": "Fundamentos da Informática: Hex 187=BB, Binário, CLI, Hardware & SO",
            "weight": "Máxima",
            "storyIntro": "Os 2 pontos mais repetidos da história de Taboão (Hexadecimal e CLI!), além de Binário, RAM vs SSD, Sistemas Multiusuário e Software Livre.",
            "lessonHtml": lessons_html[8],
            "practiceType": "lab_bin",
            "practiceTag": "03_BD_APS_FI",
            "videoClips": [
                {
                    "title": "Números Binários — Bases Numéricas #02",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "eD56zn5kYfU",
                    "startSec": 120,
                    "endSec": 480,
                    "tip": "Foco: conversão rápida Decimal ↔ Binário usando potências de 2.",
                },
                {
                    "title": "Números Octais e Hexadecimais — Bases Numéricas #03",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "gIXiFhEA-Qw",
                    "startSec": 150,
                    "endSec": 510,
                    "tip": "Foco: conversão Decimal → Hexadecimal (0–9 e A–F) que repetiu 2 anos seguidos em Taboão!",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 32},
                {"examId": "taboao2026", "qNum": 33},
                {"examId": "taboao2025", "qNum": 29},
                {"examId": "taboao2025", "qNum": 30},
                {"examId": "taboao2025", "qNum": 31},
                {"examId": "sim_taboao2027", "qNum": 32},
                {"examId": "sim_taboao2027", "qNum": 33},
                {"examId": "sim_taboao2027", "qNum": 34},
            ],
        },
        {
            "day": 9,
            "dateLabel": "Dom 29/11",
            "phase": 1,
            "title": "Base Comum I: Português Prático & Inglês (Present Perfect / Phrasal Verbs)",
            "weight": "Alta",
            "storyIntro": "Foque no Português que realmente cai em Taboão (interpretação, referenciação, adequação, função conativa) e garanta os 2 pontos de Inglês!",
            "lessonHtml": lessons_html[9],
            "practiceType": "pairs",
            "practiceTag": "04_Port_Ingles",
            "videoClips": [
                {
                    "title": "Passo a Passo para Entender as Figuras de Linguagem",
                    "channel": "Professor Noslen",
                    "videoId": "n0e75nRstcU",
                    "startSec": 90,
                    "endSec": 420,
                    "tip": "Foco: revisão leve de Metáfora, Antítese e Paradoxo sem decoreba pesada.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 1},
                {"examId": "taboao2026", "qNum": 3},
                {"examId": "taboao2026", "qNum": 4},
                {"examId": "taboao2026", "qNum": 5},
                {"examId": "taboao2026", "qNum": 6},
                {"examId": "taboao2025", "qNum": 1},
                {"examId": "taboao2025", "qNum": 3},
                {"examId": "taboao2025", "qNum": 4},
                {"examId": "sim_taboao2027", "qNum": 5},
                {"examId": "sim_taboao2027", "qNum": 6},
            ],
        },
        {
            "day": 10,
            "dateLabel": "Seg 30/11",
            "phase": 1,
            "title": "Aprofundamento (Pesquisa & Empreendedorismo) + Arte & Ed. Física",
            "weight": "Alta",
            "storyIntro": "Pegue 6+ pontos fáceis em Pesquisa Quali/Quanti, Método Científico, SWOT, Tema vs Técnica (Arte), Contração Muscular e Esportes de Invasão!",
            "lessonHtml": lessons_html[10],
            "practiceType": "vf",
            "practiceTag": "05_Hum_Aprof",
            "videoClips": [
                {
                    "title": "Git // Dicionário do Programador (Bônus Revisão Espaçada)",
                    "channel": "Código Fonte TV",
                    "videoId": "za5KWZ5pRag",
                    "startSec": 70,
                    "endSec": 360,
                    "tip": "Foco: revisão rápida de versionamento enquanto fixa os conceitos de pesquisa e projetos.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 7},
                {"examId": "taboao2026", "qNum": 8},
                {"examId": "taboao2026", "qNum": 9},
                {"examId": "taboao2026", "qNum": 10},
                {"examId": "taboao2026", "qNum": 23},
                {"examId": "taboao2026", "qNum": 24},
                {"examId": "taboao2025", "qNum": 15},
                {"examId": "taboao2025", "qNum": 16},
                {"examId": "taboao2025", "qNum": 19},
                {"examId": "sim_taboao2027", "qNum": 22},
            ],
        },
        {
            "day": 11,
            "dateLabel": "Ter 01/12",
            "phase": 1,
            "title": "Base Comum II: Matemática de Taboão (Os 7 Moldes que Caem!)",
            "weight": "Alta",
            "storyIntro": "Sem sofrimento: domine só os 7 moldes que realmente caem em Taboão — Gráficos, Venn, Logaritmo por propriedades, PA, Inequação e Áreas/3-4-5!",
            "lessonHtml": lessons_html[11],
            "practiceType": "lab_mtec",
            "practiceTag": "06_Exatas",
            "videoClips": [
                {
                    "title": "Conjuntos Numéricos: Naturais, Inteiros, Racionais e Irracionais",
                    "channel": "Professor Ferretto",
                    "videoId": "Bq5XYZKXk-Q",
                    "startSec": 30,
                    "endSec": 360,
                    "tip": "Foco: conjuntos numéricos e leitura de diagramas sem cair em pegadinhas.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 11},
                {"examId": "taboao2026", "qNum": 12},
                {"examId": "taboao2026", "qNum": 13},
                {"examId": "taboao2026", "qNum": 14},
                {"examId": "taboao2025", "qNum": 7},
                {"examId": "taboao2025", "qNum": 8},
                {"examId": "taboao2025", "qNum": 9},
                {"examId": "taboao2025", "qNum": 10},
                {"examId": "sim_taboao2027", "qNum": 12},
                {"examId": "sim_taboao2027", "qNum": 14},
            ],
        },
        {
            "day": 12,
            "dateLabel": "Qua 02/12",
            "phase": 1,
            "title": "Base Comum III: Física, Química & História (Alvos Diretos de Taboão)",
            "weight": "Alta",
            "storyIntro": "Gases p×V (repetiu 2x!), Lente lupa, Bohr (cores dos fogos), Reações Exotérmicas, Condutividade, Idade Média, Atenas e Renascimento.",
            "lessonHtml": lessons_html[12],
            "practiceType": "cards",
            "practiceTag": "06_Exatas",
            "videoClips": [
                {
                    "title": "Ligações Químicas: Iônica, Covalente e Metálica",
                    "channel": "Brasil Escola",
                    "videoId": "FDnxddw0P1g",
                    "startSec": 45,
                    "endSec": 360,
                    "tip": "Foco: por que Metal conduz sólido e Iônico só conduz líquido/dissolvido.",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 15},
                {"examId": "taboao2026", "qNum": 16},
                {"examId": "taboao2026", "qNum": 17},
                {"examId": "taboao2026", "qNum": 19},
                {"examId": "taboao2026", "qNum": 20},
                {"examId": "taboao2025", "qNum": 5},
                {"examId": "taboao2025", "qNum": 6},
                {"examId": "taboao2025", "qNum": 17},
                {"examId": "taboao2025", "qNum": 18},
                {"examId": "sim_taboao2027", "qNum": 15},
            ],
        },
        {
            "day": 13,
            "dateLabel": "Qui 03/12",
            "phase": 1,
            "title": "Véspera 04/12: Simulado Final, 15 Pontos de Ouro & Checklist",
            "weight": "Essencial",
            "storyIntro": "Revise a Cola de Bolso de 1 página, faça seu teste final misto e prepare RG, caneta e sono tranquilo para detonar amanhã (04/12)!",
            "lessonHtml": lessons_html[13],
            "practiceType": "vf",
            "practiceTag": "REVIEW",
            "videoClips": [
                {
                    "title": "Revisão Turbo 3 min: Normalização 1FN",
                    "channel": "Bóson Treinamentos",
                    "videoId": "eRaAMNjCFYw",
                    "startSec": 90,
                    "endSec": 270,
                    "tip": "Foco: revisão relâmpago de Banco de Dados sem cansar a mente.",
                },
                {
                    "title": "Revisão Turbo 2 min: RGB vs CMYK e Vetor vs Bitmap",
                    "channel": "Curso de Design Digital",
                    "videoId": "wU6rwo-SeIw",
                    "startSec": 20,
                    "endSec": 150,
                    "tip": "Foco: revisão relâmpago de Design Digital para a véspera.",
                },
            ],
            "challengeRefs": [
                {"examId": "sim_taboao2027", "qNum": 5},
                {"examId": "sim_taboao2027", "qNum": 11},
                {"examId": "sim_taboao2027", "qNum": 15},
                {"examId": "sim_taboao2027", "qNum": 23},
                {"examId": "sim_taboao2027", "qNum": 25},
                {"examId": "sim_taboao2027", "qNum": 29},
                {"examId": "sim_taboao2027", "qNum": 32},
                {"examId": "sim_taboao2027", "qNum": 35},
                {"examId": "sim_taboao2027", "qNum": 36},
                {"examId": "sim_taboao2027", "qNum": 39},
            ],
        },
        {
            "day": 14,
            "dateLabel": "Sáb 05/12",
            "phase": 2,
            "title": "Sprint 2ª Fase #1: Laboratório Prático Web I (HTML5 + CSS3 + Flexbox)",
            "weight": "2ª Fase 08/12",
            "storyIntro": "Mão na massa no VS Code! Monte do zero uma página completa HTML5 semântica + formulário POST + Flexbox + @media na aba 2ª Fase.",
            "lessonHtml": lessons_html[14],
            "practiceType": "phase2",
            "practiceTag": "02_Web_Design",
            "videoClips": [
                {
                    "title": "Modelo de Caixas (Box Model) na Prática",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "3ZFYXkzXhqE",
                    "startSec": 120,
                    "endSec": 480,
                    "tip": "Foco: revisar padding, border e margin antes de codar seu style.css no VS Code!",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 26},
                {"examId": "taboao2025", "qNum": 32},
                {"examId": "taboao2025", "qNum": 34},
                {"examId": "taboao2025", "qNum": 35},
                {"examId": "taboao2025", "qNum": 36},
                {"examId": "sim_taboao2027", "qNum": 23},
                {"examId": "sim_taboao2027", "qNum": 24},
                {"examId": "sim_taboao2027", "qNum": 25},
            ],
        },
        {
            "day": 15,
            "dateLabel": "Dom 06/12",
            "phase": 2,
            "title": "Sprint 2ª Fase #2: Laboratório Prático C# Console (3 Programas + Debug)",
            "weight": "2ª Fase 08/12",
            "storyIntro": "Digite e rode 3 programas reais em C# (if/else + try/catch, for com %, vetor de notas) no Visual Studio ou dotnetfiddle.net!",
            "lessonHtml": lessons_html[15],
            "practiceType": "phase2",
            "practiceTag": "01_TPA_CSharp",
            "videoClips": [
                {
                    "title": "Vetores — Curso de Algoritmos #14",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "j9473xQ39vY",
                    "startSec": 120,
                    "endSec": 460,
                    "tip": "Foco: lógica de percorrer vetores com laço for para codar o Programa B em C#!",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 34},
                {"examId": "taboao2026", "qNum": 35},
                {"examId": "taboao2026", "qNum": 36},
                {"examId": "taboao2026", "qNum": 37},
                {"examId": "taboao2025", "qNum": 22},
                {"examId": "taboao2025", "qNum": 23},
                {"examId": "sim_taboao2027", "qNum": 35},
                {"examId": "sim_taboao2027", "qNum": 37},
            ],
        },
        {
            "day": 16,
            "dateLabel": "Seg 07/12",
            "phase": 2,
            "title": "Sprint 2ª Fase #3: Lab BD I (DER + SQL) & Simulação da Entrevista (08/12)",
            "weight": "2ª Fase 08/12",
            "storyIntro": "Modele Biblioteca (Aluno × Livro → Empréstimo N:N) com PK/FK e SQL, e ensaie em voz alta as 8 perguntas reais da Entrevista Individual!",
            "lessonHtml": lessons_html[16],
            "practiceType": "phase2",
            "practiceTag": "03_BD_APS_FI",
            "videoClips": [
                {
                    "title": "Criando Tabelas SQL (DDL) na Prática",
                    "channel": "Curso em Vídeo • Gustavo Guanabara",
                    "videoId": "m9YPlX0fcJk",
                    "startSec": 180,
                    "endSec": 510,
                    "tip": "Foco: sintaxe CREATE TABLE com PRIMARY KEY para o laboratório de amanhã!",
                },
            ],
            "challengeRefs": [
                {"examId": "taboao2026", "qNum": 28},
                {"examId": "taboao2026", "qNum": 29},
                {"examId": "taboao2026", "qNum": 38},
                {"examId": "taboao2025", "qNum": 26},
                {"examId": "taboao2025", "qNum": 37},
                {"examId": "taboao2025", "qNum": 39},
                {"examId": "sim_taboao2027", "qNum": 38},
                {"examId": "sim_taboao2027", "qNum": 39},
                {"examId": "sim_taboao2027", "qNum": 40},
            ],
        },
    ]

    # Normaliza flashcards (tuplas -> dicts) e VF statements para o formato exato esperado pelo front-end
    flashcards_norm = [
        {"front": x[0], "back": x[1], "tag": x[2]} if isinstance(x, (tuple, list)) else x
        for x in TABOAO_FLASHCARDS
    ]
    area_title_map = {a["id"]: a["title"] for a in TABOAO_AREAS}
    vf_norm = []
    for v in TABOAO_VF:
        is_true = bool(v.get("isTrue") if "isTrue" in v else v.get("truth"))
        vf_norm.append({
            "id": v["id"],
            "area": v["area"],
            "topic": v.get("topic") or area_title_map.get(v["area"], "Taboão M-Tec"),
            "text": v.get("text") or v.get("stmt", ""),
            "isTrue": is_true,
            "verdictTitle": v.get("verdictTitle") or ("✅ VERDADE OFICIAL!" if is_true else "🚨 FAKE DA BANCA!"),
            "explain": v.get("explain") or v.get("why", ""),
        })

    # Validações rigorosas
    assert len(vf_norm) >= 50, f"Expected >= 50 VF items, got {len(vf_norm)}"
    for vf in vf_norm:
        assert vf["area"] in valid_areas, f"Invalid VF area: {vf}"
        assert len(vf["text"]) > 10 and len(vf["explain"]) > 10, f"Incomplete VF item: {vf}"
    for fc in flashcards_norm:
        assert fc["front"] and fc["back"] and fc["tag"], f"Incomplete flashcard: {fc}"
    assert len(chapters) == 16, f"Expected 16 chapters, got {len(chapters)}"
    for ch in chapters:
        l_len = len(ch["lessonHtml"])
        q_cnt = len(ch["challengeRefs"])
        clips = ch.get("videoClips", [])
        assert l_len >= 4000, f"Day {ch['day']} lessonHtml too short: {l_len} chars"
        assert len(clips) >= 1, f"Day {ch['day']} missing videoClips"
        for vc in clips:
            assert len(vc["videoId"]) == 11, f"Invalid videoId in Day {ch['day']}: {vc['videoId']}"
            assert 0 <= vc["startSec"] < vc["endSec"], f"Invalid start/end in Day {ch['day']}: {vc}"
        assert 8 <= q_cnt <= 10, f"Day {ch['day']} challengeRefs must be 8..10, got {q_cnt}"
        for ref in ch["challengeRefs"]:
            ex = exams[ref["examId"]]
            found = [q for q in ex["questions"] if q["num"] == ref["qNum"]]
            assert len(found) == 1, f"Broken challengeRef in Day {ch['day']}: {ref}"
        # Check no raw LaTeX $$ or broken tags
        assert "$$" not in ch["lessonHtml"], f"Raw LaTeX $$ in Day {ch['day']}"
        print(f"  Day {ch['day']:02d} ({ch['dateLabel']}, F{ch['phase']}): lesson={l_len} chars | clips={len(clips)} | quiz={q_cnt} Qs | practice={ch['practiceType']}")

    data = {
        "platformVersion": "taboao_mtec_2027_v3",
        "schoolName": "Etec de Taboão da Serra — 2ª Série M-Tec-PI (DS)",
        "examDateIso": "2026-12-04",
        "phase2DateIso": "2026-12-08",
        "defaultStartIso": "2026-11-21",
        "primaryExamIds": primary_exam_ids,
        "extraExamIds": extra_exam_ids,
        "areas": TABOAO_AREAS,
        "vfStatements": vf_norm,
        "flashcards": flashcards_norm,
        "pairs": TABOAO_PAIRS,
        "phase2": PHASE2_DATA,
        "exams": exams,
        "apostilaSections": apostilaSections,
        "chapters": chapters,
    }

    out_js = BASE / "dados_plataforma.js"
    out_js.write_text("window.ETEC_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    total_q = sum(len(ex["questions"]) for ex in exams.values())
    print(f"\nWrote {out_js} ({out_js.stat().st_size} bytes)")
    print(f"Stats: {len(chapters)} chapters | {len(exams)} exams ({total_q} questions) | {len(TABOAO_FLASHCARDS)} flashcards | {len(TABOAO_VF)} VF items | {len(PHASE2_DATA['labs'])} phase2 labs | {len(PHASE2_DATA['interview'])} interview Qs")


if __name__ == "__main__":
    main()
