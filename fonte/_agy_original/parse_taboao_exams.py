# -*- coding: utf-8 -*-
"""
Parser e banco oficial das provas reais da Etec de Taboão da Serra (2ª Série M-Tec-PI DS)
+ Simulado Premonição Taboão 04/12/2026 (40 questões inéditas no molde exato da escola).
"""
import re
from pathlib import Path

TABOAO_DIR = Path("/home/galves/.gemini/antigravity-cli/brain/810bbede-d2b8-441a-bdef-d5e94d7dfe42/scratch/taboao")
LETTER_TO_IDX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def img_tag(fname: str, alt: str) -> str:
    return (
        f'<div class="q-fig"><img src="./img/{fname}" alt="{esc(alt)}" '
        f'loading="lazy" style="max-width:100%; height:auto; border-radius:10px; border:1px solid var(--border); background:#fff; padding:6px;"></div>'
    )

# ==================== 1. PROVA REAL TABOÃO 2026 (05/12/2025 — 40Q) ====================
# Gabarito verificado questão a questão (matematicamente, gramaticalmente e tecnicamente),
# pois o PDF GABARITO-2a-Serie-Mtec-PI-Desenvolvimento-de-Sistemas.pdf publicado no site da escola
# veio deslocado/trocado com outra turma (ex.: marcava Q38=C 'editor de texto' p/ tabela BD).
T26_ANSWERS = {
    1: "D", 2: "B", 3: "D", 4: "C", 5: "A", 6: "B", 7: "E", 8: "B", 9: "A", 10: "E",
    11: "D", 12: "D", 13: "D", 14: "E", 15: "B", 16: "E", 17: "A", 18: "C", 19: "A", 20: "A",
    21: "C", 22: "A", 23: "C", 24: "C", 25: "C", 26: "E", 27: "B", 28: "B", 29: "C", 30: "C",
    31: "B", 32: "C", 33: "D", 34: "C", 35: "A", 36: "B", 37: "E", 38: "A", 39: "B", 40: "C",
}

T26_EXPLAINS = {
    1: "(D) O texto afirma explicitamente que discursos pouco fundamentados circulam amplamente quando apelam a emoções, identidades grupais e confirmação de crenças já existentes.",
    2: "(B) Retomada direta do texto: propagam-se ao apelar a estratégias emocionais e identitárias.",
    3: "(D) O pronome demonstrativo 'esta' retoma claramente o referente mais próximo ('Maria'), eliminando a ambiguidade de 'ela'.",
    4: "(C) Adequação linguística significa escolher a variedade da língua mais apropriada aos interlocutores e à situação/finalidade comunicativa — sem rotular falas regionais como 'erradas'.",
    5: "(A) Present Perfect usa <code>have/has + particípio passado</code> para ações sem tempo definido no passado: <code>She has danced</code>.",
    6: "(B) Sujeito plural (<code>The students</code>) exige <code>haven't</code> + particípio passado regular <code>studied</code>.",
    7: "(E) Tema é o assunto/inspiração central da obra (ex.: natureza); colagem é técnica, e público-alvo/curadoria são gestão da exposição.",
    8: "(B) Colagem é uma técnica (meio/procedimento prático) para construir a composição visual.",
    9: "(A) Os 3 tipos clássicos de contração muscular são concêntrica (encurta), excêntrica (alonga controlando) e isométrica (tensão sem mudar o comprimento).",
    10: "(E) O aparelho locomotor (ossos, articulações e músculos) atua em conjunto permitindo locomoção e deslocamento dos membros.",
    11: "(D) Os dois triângulos isósceles são semelhantes (mesmo ângulo marcado na base): <code>x / 330 = 330 / 550 = 3/5 → x = 198 m</code>. Cercando as duas partes (contorno + divisória interna): <code>330 + 550 + 198 + 198 + 330 = 1606 m</code>.",
    12: "(D) Áreas: Quadrado <code>Q = 9×9 = 81 cm²</code>; Triângulo <code>T = (12×16)/2 = 96 cm²</code>; Retângulo <code>R = 15×7 = 105 cm²</code>. Menor = <strong>Q</strong>, maior = <strong>R</strong>.",
    13: "(D) Centro-Oeste (38,3%) + Sul (37,2%) = <code>75,5%</code> = <code>119,8 milhões t</code>. Total ≈ <code>119,8 / 0,755 ≈ 158,68 mi</code>. Sudeste (11,4%): <code>158,68 × 0,114 ≈ 18,1 milhões t</code>.",
    14: "(E) Saldos Jul–Nov: <code>+500 - 1600 + 50 + 2000 - 1800 = -850</code>. Taxa Set→Out na receita: <code>3500 / 1400 = 2,5</code>. Receita Dez = <code>2000 × 2,5 = 5000</code>; Despesa Dez = <code>3800</code> → Dez = <code>+1200</code>. Semestre = <code>-850 + 1200 = +R$ 350,00</code> (lucro).",
    15: "(B) 🔁 <strong>Questão repetida em Taboão!</strong> Pela lei geral dos gases (<code>p·V/T = cte</code>): em A temos <code>(p₀, V₀, 300 K)</code>. No ponto B temos pressão <code>p₀</code> e volume dobrado <code>2V₀</code> → temperatura máxima <code>T_B = 2 × 300 = 600 K</code>!",
    16: "(E) Lente convergente com <code>f = 5 cm</code> → <code>C = 2f = 10 cm</code>. O objeto P está a <code>p = 10 - 2,5 = 7,5 cm</code> (entre F e C). Pela equação de Gauss: <code>1/5 = 1/7,5 + 1/p' → p' = +15 cm</code> (Real). Aumento <code>A = -15/7,5 = -2</code> (Invertida e com o dobro da altura).",
    17: "(A) Niels Bohr propôs elétrons em camadas/níveis quantizados de energia que emitem luz (cores específicas) ao saltar de uma camada mais externa para uma interna.",
    18: "(C) Em <code>CO + 2NO → 2CO₂ + N₂</code>, o carbono passa de NOX <code>+2</code> (no CO) para <code>+4</code> (no CO₂) — logo o carbono <strong>oxida</strong> e o monóxido de carbono (CO) é o agente <strong>redutor</strong>.",
    19: "(A) I, II e IV estão corretas. A III é falsa porque os servos pagavam pesados tributos ao senhor feudal (corveia, talha, banalidades).",
    20: "(A) A ciência médica árabe (como Avicena) preservou e ampliou textos gregos, traduzidos ao latim e estudados nas universidades europeias medievais.",
    21: "(C) O teste molecular (PCR/DNA-HPV) identifica diretamente o material genético (DNA) do vírus HPV por amplificação molecular.",
    22: "(A) A clonagem por transferência nuclear exige material genético (DNA) preservado em células congeladas da espécie extinta.",
    23: "(C) Toda investigação científica começa definindo com clareza qual é o <strong>problema de pesquisa</strong> antes de coletar ou analisar dados.",
    24: "(C) Pesquisa <strong>qualitativa</strong> foca na compreensão aprofundada e subjetiva dos fenômenos; <strong>quantitativa</strong> foca em medições numéricas e estatísticas.",
    25: "(C) I, IV e V corretas! II é falsa porque URI = <em>Uniform</em> Resource Identifier (Uniforme, não Unilateral); III erra ao chamar DNS de 'lista de tele transferência' (DNS traduz nomes de domínio em IP).",
    26: "(E) Ordem exata: parágrafo <code>&lt;p&gt;</code>, linha horizontal <code>&lt;hr&gt;</code>, título <code>&lt;h2&gt;</code>, quebra/pular linha <code>&lt;br&gt;</code> e corpo <code>&lt;body&gt;</code>.",
    27: "(B) URI (<em>Uniform Resource Identifier</em>) é o identificador único de um recurso disponível na internet (URL e URN são tipos de URI).",
    28: "(B) No Diagrama de Classes UML, associações representam a relação estrutural entre classes indicando como seus objetos se conectam.",
    29: "(C) O Diagrama de Casos de Uso descreve as interações externas entre <strong>atores</strong> (usuários/sistemas) e as <strong>funcionalidades</strong> do sistema.",
    30: "(C) Em UX Design, <strong>usabilidade</strong> mede a facilidade, eficiência e satisfação com que o usuário aprende e interage com o produto.",
    31: "(B) *(Nota: na prova oficial de 05/12/2025 a banca repetiu acidentalmente o enunciado da Q28 na Q31 — resposta igualmente B!)*",
    32: "(C) 🔁 <strong>Questão repetida literalmente de 2024!</strong> No gabarito oficial da Etec de Taboão da Serra, CLI é marcada como <strong>Interface monotarefa por linha de comando</strong>.",
    33: "(D) 🔁 <strong>Mesmo número repetido de 2024!</strong> <code>187 ÷ 16 = 11</code> (resto <code>11</code>). Como em hexadecimal <code>10=A, 11=B</code>, temos <strong>BB</strong>!",
    34: "(C) Menor que 100 paga 5% (<code>* 0,05</code>); caso contrário (100 ou mais) paga 12% (<code>* 0,12</code>).",
    35: "(A) I e II são verdadeiras: <code>try/catch</code> captura letras/formato inválido, e ainda precisamos de um <code>if</code> para rejeitar números ≤ 0. III é falsa pois o enunciado pede para solicitar novamente, não encerrar.",
    36: "(B) Um <strong>breakpoint</strong> pausa a execução em uma linha marcada para o desenvolvedor inspecionar variáveis e o fluxo passo a passo em tempo real.",
    37: "(E) É a <strong>INCORRETA</strong>: várias linguagens (como C#, Java, JavaScript e Python) suportam matrizes irregulares (<em>jagged arrays</em>), onde cada linha pode ter quantidade diferente de colunas!",
    38: "(A) Uma <strong>tabela</strong> no banco de dados organiza dados de um mesmo assunto em linhas e colunas — como uma lista de alunos com matrícula, nome e notas.",
    39: "(B) Um <strong>registro</strong> (ou tupla) corresponde a <strong>uma linha completa</strong> da tabela contendo todos os campos de um item específico.",
    40: "(C) Procurar um contato específico na agenda equivale a fazer uma <strong>consulta (SELECT)</strong> no banco de dados.",
}

T26_IMAGES = {
    11: ("t26_p4_i1.png", "Figura do terreno dividido em dois triângulos (330m, 550m, x)"),
    13: ("t26_p5_i1.jpg", "Gráfico de setores da safra nacional de cereais por região (ENEM 2019)"),
    14: ("t26_p6_i1.png", "Gráfico de barras de Receita e Despesa de Julho a Novembro (ENEM 2020)"),
    15: ("t26_p6_i2.png", "Diagrama p x V do ciclo termodinâmico A-B-C-D"),
    16: ("t26_p7_i1.png", "Esquema óptico de lente convergente com objeto P, F=5cm e C-P=2,5cm"),
}

T26_AREAS = {
    **{q: "port_ing" for q in range(1, 7)},
    **{q: "ciencias_hum" for q in [7, 8, 9, 10, 19, 20, 21, 22, 23, 24]},
    **{q: "exatas" for q in [11, 12, 13, 14, 15, 16, 17, 18]},
    **{q: "web_design" for q in [25, 26, 27, 30]},
    **{q: "bd_aps_fi" for q in [28, 29, 31, 32, 33, 38, 39, 40]},
    **{q: "tpa_csharp" for q in [34, 35, 36, 37]},
}

def build_taboao_2026():
    raw = (TABOAO_DIR / "prova_2026.txt").read_text(encoding="utf-8")
    # Cut from Texto-base para questões 1 e 2
    start = raw.find("Texto-base para questões 1 e 2")
    body = raw[start:]
    # Clean page numbers and form feeds
    body = re.sub(r"\n\s*\d{1,2}\s*\n+\x0c", "\n", body)
    body = body.replace("\x0c", "\n")

    # Extract shared text for Q1 and Q2
    m_shared = re.match(r'(Texto-base para questões 1 e 2\s*"[\s\S]*?")\s*\n1\.', body)
    shared_1_2 = m_shared.group(1).strip() if m_shared else ""
    body_q = body[body.find("\n1.") + 1:]

    # Split sequentially 1. .. 40.
    questions = []
    pos = 0
    for qnum in range(1, 41):
        pat_cur = re.compile(rf'(?m)^{qnum}\.\s+')
        m_cur = pat_cur.search(body_q, pos)
        if not m_cur:
            raise ValueError(f"Taboao 2026 missing Q{qnum}")
        q_start = m_cur.end()
        if qnum < 40:
            pat_next = re.compile(rf'(?m)^{qnum+1}\.\s+')
            m_next = pat_next.search(body_q, q_start)
            if not m_next:
                raise ValueError(f"Taboao 2026 missing next Q{qnum+1}")
            chunk = body_q[q_start:m_next.start()].strip()
            pos = m_next.start()
        else:
            chunk = body_q[q_start:].strip()

        # Split options A) .. E)
        opt_matches = list(re.finditer(r'(?m)^([A-E])\)\s*', chunk))
        if len(opt_matches) != 5:
            raise ValueError(f"Taboao 2026 Q{qnum} options count={len(opt_matches)}")
        stem_txt = chunk[:opt_matches[0].start()].strip()
        opts = []
        for i, om in enumerate(opt_matches):
            o_end = opt_matches[i+1].start() if i < 4 else len(chunk)
            otxt = re.sub(r'\s+', ' ', chunk[om.end():o_end]).strip()
            if qnum == 26 and i == 4 and otxt.endswith("<body"):
                otxt = otxt + ">"
            opts.append(esc(otxt))

        # Format stem
        stem_clean = re.sub(r'terre-\s*no', 'terreno', stem_txt)
        parts_html = []
        if qnum in (1, 2) and shared_1_2:
            shared_clean = re.sub(r"\s+", " ", shared_1_2)
            parts_html.append(f'<blockquote class="q-quote">{esc(shared_clean)}</blockquote>')
        # Preserve line breaks for numbered items / bullets in stem
        lines = [ln.strip() for ln in stem_clean.splitlines() if ln.strip() and not re.fullmatch(r'\d{1,2}', ln.strip())]
        # Group lines smartly
        para = []
        for ln in lines:
            if re.match(r'^([I|V]+\.|[•\-]|\d\s*–|Equação\s+\d)', ln):
                if para:
                    parts_html.append(f'<p>{esc(" ".join(para))}</p>')
                    para = []
                parts_html.append(f'<p style="margin:4px 0 4px 10px;">{esc(ln)}</p>')
            else:
                para.append(ln)
        if para:
            parts_html.append(f'<p>{esc(" ".join(para))}</p>')
        if qnum in T26_IMAGES:
            fname, alt = T26_IMAGES[qnum]
            parts_html.append(img_tag(fname, alt))

        questions.append({
            "num": qnum,
            "stemHtml": "\n".join(parts_html),
            "options": opts,
            "answer": LETTER_TO_IDX[T26_ANSWERS[qnum]],
            "explain": T26_EXPLAINS[qnum],
            "area": T26_AREAS[qnum],
            "isTech": qnum >= 25,
        })
    assert len(questions) == 40
    return questions


# ==================== 2. PROVA REAL TABOÃO 2025 (06/12/2024 — 40Q) ====================
T25_ANSWERS = {
    1: "C", 2: "D", 3: "D", 4: "C", 5: "B", 6: "B", 7: "A", 8: "E", 9: "C", 10: "B",
    11: "E", 12: "C", 13: "A", 14: "C", 15: "C", 16: "C", 17: "C", 18: "A", 19: "D", 20: "D",
    21: "A", 22: "E", 23: "C", 24: "D", 25: "B", 26: "A", 27: "A", 28: "C", 29: "D", 30: "B",
    31: "A", 32: "E", 33: "A", 34: "C", 35: "A", 36: "B", 37: "D", 38: "C", 39: "B", 40: "D",
}

T25_EXPLAINS = {
    1: "(C) 'Os alunos' está no plural, então ambos os adjetivos devem concordar no plural: 'ansiosos e <strong>atentos</strong>'.",
    2: "(D) O trecho clássico de João Cabral de Melo Neto denuncia a miséria, fome ('sangue com pouca tinta') e desumanização dos retirantes.",
    3: "(D) Verbo no imperativo ('Compre já!') voltado a convencer o receptor caracteriza a função <strong>conativa (apelativa)</strong>.",
    4: "(C) <code>save up</code> = economizar / poupar energia.",
    5: "(B) A democracia ateniense era direta, porém restrita: só homens adultos, livres e filhos de atenienses votavam (excluía mulheres, escravos e estrangeiros).",
    6: "(B) O Renascimento resgatou a cultura greco-romana valorizando o antropocentrismo, a razão humana e a ciência.",
    7: "(A) 🔁 <strong>Repetiu de 2021!</strong> <code>(1-x)/(1+x) &gt; -1</code> → <code>(1-x)/(1+x) + 1 &gt; 0</code> → <code>2/(1+x) &gt; 0</code> → <code>1+x &gt; 0</code> (obs.: gabarito oficial da prova marcou A).",
    8: "(E) 🔁 <strong>Repetiu de 2021!</strong> Diagrama de Venn: só 1ª = <code>92-35=57</code>; só 2ª = <code>80-35=45</code>; ambas = <code>35</code>; nenhuma = <code>33</code>. Total = <code>57 + 45 + 35 + 33 = 170</code> funcionários!",
    9: "(C) 🔁 <strong>Repetiu de 2021!</strong> Na questão original de logaritmo (<code>log_a m = 11</code>, <code>log_a n = 6</code>), pela propriedade <code>log(m^k · n^p) = k·log m + p·log n</code> (gabarito oficial C = 45, vindo de <code>3×11 + 2×6 = 45</code>).",
    10: "(B) 🔁 <strong>Repetiu de 2021!</strong> Progressão Aritmética (PA): <code>a₁ = 40</code>, razão <code>r = 10</code>, <code>aₙ = 520</code>. Fórmula: <code>520 = 40 + (n-1)·10 → 480 = 10(n-1) → n-1 = 48 → n = 49 meses</code>!",
    11: "(E) Na biorremediação, microrganismos metabolizam (quebram quimicamente) o contaminante transformando-o em substâncias menos tóxicas ou atóxicas.",
    12: "(C) Leguminosas fazem associação com bactérias fixadoras de nitrogênio no solo, reduzindo a necessidade de <strong>fertilizantes</strong> químicos.",
    13: "(A) MRUV partindo do repouso (<code>v₀=0, a=2, t=3</code>): <code>v = 0 + 2×3 = 6,0 m/s</code> e <code>ΔS = (a·t²)/2 = (2×9)/2 = 9,0 m</code>!",
    14: "(C) Desaceleração: <code>a = Δv/Δt = 40/20 = 2 m/s²</code>. Segunda Lei de Newton: <code>F = m·a = 5 × 2 = 10 N</code>!",
    15: "(C) Ordem oficial do método científico: Observação → Hipótese → Experimento → Análise de Dados → Conclusão.",
    16: "(C) Resiliência permite persistir após falhas; criatividade permite reformular soluções inovadoras.",
    17: "(C) Toda combustão (queima) libera calor para o ambiente, portanto é uma reação <strong>exotérmica</strong>.",
    18: "(A) Sódio (Na) e Césio (Cs) pertencem à Família 1A (Metais Alcalinos): reagem vigorosamente com água produzindo gás hidrogênio (H₂) e base.",
    19: "(D) É a <strong>INCORRETA</strong>: badminton, voleibol, beisebol e bocha NÃO são esportes de invasão (são de rede/parede, campo/taco ou precisão).",
    20: "(D) Os traços em preto e branco do grafite de Speto remetem diretamente à <strong>xilogravura nordestina</strong> (literatura de cordel).",
    21: "(A) Em C# (assim como C, Java e JS), o operador lógico <strong>E</strong> (ambas verdadeiras) é <strong><code>&amp;&amp;</code></strong>.",
    22: "(E) Atenção ao índice invertido <code>matriz[j, i]</code>! Para <code>i=0</code> imprime <code>[0,0]=1</code> e <code>[1,0]=3</code> → linha <code>1 3</code>. Quebra linha. Para <code>i=1</code> imprime <code>[0,1]=2</code> e <code>[1,1]=4</code> → linha <code>2 4</code>!",
    23: "(C) Usuário digita <code>10</code>. Entra em <code>while(10 &lt;= 10)</code>: testa <code>10 % 5 == 0 &amp;&amp; 10 != 0</code> → Verdadeiro → imprime <strong><code>10</code></strong>! Depois <code>numero++</code> vira 11 e sai.",
    24: "(D) Na linguagem compilada (como C# no Visual Studio), erros de sintaxe (como faltar <code>;</code>) impedem a compilação e o compilador/IDE destaca a linha do erro.",
    25: "(B) O laço <code>do/while</code> é pós-teste: executa o bloco <strong>pelo menos uma vez</strong> antes de checar a condição no final.",
    26: "(A) 🔁 <strong>Repetiu de 2022!</strong> Requisitos funcionais definem o que o sistema <strong>deve fazer</strong>, ou seja, suas <strong>funções</strong> e informações.",
    27: "(A) <strong>XP, SCRUM e KANBAN</strong> são exclusivamente metodologias/frameworks ágeis.",
    28: "(C) Característica clássica do Modelo em Cascata: divisão em <strong>etapas</strong> predeterminadas executadas de forma <strong>sequencial</strong>.",
    29: "(D) 🔁 <strong>Repetiu idêntica em 2025!</strong> <code>187 ÷ 16 = 11</code> (B) resto <code>11</code> (B) → <strong>BB</strong>!",
    30: "(B) 🔁 <strong>Repetiu idêntica em 2025!</strong> Gabarito oficial de Taboão: <strong>Interface monotarefa por linha de comando</strong>.",
    31: "(A) Sistema multiusuário permite vários usuários utilizando aplicações diversificadas simultaneamente no mesmo servidor/sistema.",
    32: "(E) O atributo <code>alt</code> na tag <code>&lt;img&gt;</code> define o texto alternativo exibido caso a imagem não carregue (e lido por leitores de tela para acessibilidade).",
    33: "(A) Em JavaScript, <strong>Número (<code>number</code>)</strong>, string, boolean, undefined, null, symbol e bigint são tipos primitivos.",
    34: "(C) CSS Box Model descreve como todo elemento é calculado como uma caixa composta por conteúdo, preenchimento (<code>padding</code>), borda (<code>border</code>) e margem (<code>margin</code>).",
    35: '(A) Para importar um arquivo JS externo no HTML usa-se <code>&lt;script src="arquivo.js"&gt;&lt;/script&gt;</code>.',
    36: "(B) Para centralizar horizontal e verticalmente com CSS Flexbox: <code>display: flex; justify-content: center; align-items: center;</code>.",
    37: "(D) Gabarito oficial da prova (D) — princípios gerais da normalização técnica (ABNT/ISO): voluntariedade, representatividade, transparência, paridade, simplificação e consenso.",
    38: "(C) <strong>Chave Primária (Primary Key)</strong> impede registros duplicados na tabela; <strong>Chave Estrangeira (Foreign Key)</strong> é a PK da tabela pai que migra para a tabela filha.",
    39: "(B) O <strong>Diagrama Entidade-Relacionamento (DER)</strong> ilustra como entidades (pessoas, objetos, conceitos) se relacionam dentro de um sistema.",
    40: "(D) 🔁 <strong>Repetiu de 2022!</strong> Dicionário de dados é uma coleção de <strong>nomes, atributos</strong> e definições sobre elementos de <strong>dados</strong>.",
}

T25_AREAS = {
    **{q: "port_ing" for q in [1, 2, 3, 4]},
    **{q: "ciencias_hum" for q in [5, 6, 11, 12, 15, 16, 19, 20]},
    **{q: "exatas" for q in [7, 8, 9, 10, 13, 14, 17, 18]},
    **{q: "tpa_csharp" for q in [21, 22, 23, 24, 25]},
    **{q: "bd_aps_fi" for q in [26, 27, 28, 29, 30, 31, 37, 38, 39, 40]},
    **{q: "web_design" for q in [32, 33, 34, 35, 36]},
}

def build_taboao_2025():
    raw = (TABOAO_DIR / "prova_2025.txt").read_text(encoding="utf-8")
    start = raw.find("Questão 1:")
    end = raw.find("\nGABARITO\n")
    body = raw[start:end].replace("\x0c", "\n")

    questions = []
    pos = 0
    for qnum in range(1, 41):
        pat_cur = re.compile(rf'(?m)^Questão\s+{qnum}:\s*')
        m_cur = pat_cur.search(body, pos)
        if not m_cur:
            raise ValueError(f"Taboao 2025 missing Q{qnum}")
        q_start = m_cur.end()
        if qnum < 40:
            pat_next = re.compile(rf'(?m)^Questão\s+{qnum+1}:\s*')
            m_next = pat_next.search(body, q_start)
            if not m_next:
                raise ValueError(f"Taboao 2025 missing next Q{qnum+1}")
            chunk = body[q_start:m_next.start()].strip()
            pos = m_next.start()
        else:
            chunk = body[q_start:].strip()

        # Fix Q7 fraction line that appeared before Questão 7 in PDF extraction
        if qnum == 7:
            chunk = chunk.replace("1+𝑥 > - 1", "(1 - x) / (1 + x) > -1")
        if qnum == 6:
            chunk = re.sub(r'\n1−𝑥\s*$', '', chunk)

        opt_matches = list(re.finditer(r'(?m)^([a-e])\)\s*', chunk))
        if len(opt_matches) != 5:
            raise ValueError(f"Taboao 2025 Q{qnum} options count={len(opt_matches)}")
        stem_txt = chunk[:opt_matches[0].start()].strip()
        opts = []
        for i, om in enumerate(opt_matches):
            o_end = opt_matches[i+1].start() if i < 4 else len(chunk)
            otxt = chunk[om.end():o_end].strip()
            if qnum == 36:
                otxt_clean = re.sub(r'\n+', ' ', otxt)
                otxt_clean = re.sub(r'\s+', ' ', otxt_clean)
                opts.append(f'<code>{esc(otxt_clean)}</code>')
            else:
                otxt_clean = re.sub(r'\s+', ' ', otxt).strip()
                opts.append(esc(otxt_clean))

        parts_html = []
        if qnum == 20:
            parts_html.append(img_tag("t25_p8_i1.jpg", "TEXTO I — SPETO. Grafite. Museu Afro Brasil, 2009."))
        if qnum == 22:
            parts_html.append('<p>Dado o código abaixo em C#, o que será exibido no console?</p>')
            parts_html.append('<pre class="q-code">int[,] matriz = { { 1, 2 }, { 3, 4 } };\nfor (int i = 0; i &lt; 2; i++) {\n    for (int j = 0; j &lt; 2; j++) {\n        Console.Write(matriz[j, i] + " ");\n    }\n    Console.WriteLine();\n}</pre>')
        elif qnum == 23:
            parts_html.append('<p>Analise o código em C# abaixo e responda:</p>')
            parts_html.append('<pre class="q-code">class Program\n{\n    public static void Main(string[] args)\n    {\n        int numero;\n        Console.Write("Digite um número: ");\n        numero = int.Parse(Console.ReadLine());\n        while (numero &lt;= 10) {\n            if (numero % 5 == 0 &amp;&amp; numero != 0) {\n                Console.WriteLine(numero);\n            }\n            numero++;\n        }\n    }\n}</pre>')
            parts_html.append('<p><strong>Dado que o usuário insira o valor 10, qual será a saída esperada?</strong></p>')
        else:
            lines = [ln.strip() for ln in stem_txt.splitlines() if ln.strip()]
            parts_html.append(f'<p>{esc(" ".join(lines))}</p>')

        questions.append({
            "num": qnum,
            "stemHtml": "\n".join(parts_html),
            "options": opts,
            "answer": LETTER_TO_IDX[T25_ANSWERS[qnum]],
            "explain": T25_EXPLAINS[qnum],
            "area": T25_AREAS[qnum],
            "isTech": qnum >= 21,
        })
    assert len(questions) == 40
    return questions


# ==================== 3. SIMULADO PREMONIÇÃO TABOÃO 04/12/2026 (40Q INÉDITAS) ====================
def build_sim_taboao_2027():
    raw_qs = [
        # --- PORTUGUÊS (Q1–Q4) ---
        (1, "port_ing", False,
         '<blockquote class="q-quote">"Com a inteligência artificial generativa, produzir textos verossímeis tornou-se instantâneo. Por isso, a escola do século XXI precisa ensinar menos a copiar respostas prontas e mais a checar fontes, formular perguntas críticas e verificar a coerência dos dados."</blockquote><p>Segundo o texto, diante da popularização da IA generativa, o papel central da escola passa a ser:</p>',
         ["proibir o uso de computadores em sala para evitar erros.", "desenvolver senso crítico, checagem de fontes e análise de coerência.", "substituir a leitura pela memorização mecânica de resumos.", "limitar o ensino de ciências humanas em favor da digitação.", "aceitar automaticamente qualquer texto bem escrito como verdadeiro."],
         1, "O texto destaca explicitamente checar fontes, formular perguntas críticas e verificar a coerência dos dados."),

        (2, "port_ing", False,
         '<p>Assinale a alternativa em que o emprego da referenciação pronominal <strong>elimina</strong> ambiguidade:</p>',
         ["Lucas avisou Pedro que ele tirou nota máxima no laboratório.", "Lucas encontrou Pedro e disse que sua mochila caiu.", "Lucas informou a Pedro que este havia passado para a segunda fase.", "Lucas falou com Pedro porque ele esqueceu o código.", "O professor orientou o aluno em sua sala de aula."],
         2, "O pronome 'este' retoma de forma precisa o referente mais próximo ('Pedro'), evitando a dupla interpretação de 'ele' ou 'sua'."),

        (3, "port_ing", False,
         '<p>Em relação à <strong>variação e adequação linguística</strong>, assinale a afirmação correta:</p>',
         ["Gírias usadas por programadores ou gamers provam empobrecimento do português.", "A norma culta é obrigatória até em conversas informais entre amigos no WhatsApp.", "Uma mesma pessoa adapta seu nível de formalidade conforme o contexto e o interlocutor.", "A variação diatópica refere-se exclusivamente às mudanças históricas ao longo dos séculos.", "Existe apenas uma forma correta de falar português no Brasil inteiro."],
         2, "Adequação linguística (variação diafásica/situacional) significa ajustar a linguagem ao contexto e ao interlocutor. (Diatópica = região; Diacrônica = tempo)."),

        (4, "port_ing", False,
         '<p>Leia o anúncio: <em>"Inscreva-se hoje mesmo na Etec e transforme seu futuro na tecnologia!"</em> A função da linguagem predominante e o tipo textual principal são, respectivamente:</p>',
         ["Poética e Descrição.", "Referencial e Narração.", "Metalinguística e Exposição.", "Conativa (apelativa) e Injunção.", "Fática e Dissertação científica."],
         3, "Verbos no imperativo ('Inscreva-se', 'transforme') voltados a convencer o leitor a agir caracterizam a função conativa e o tipo injuntivo."),

        # --- INGLÊS (Q5–Q6) ---
        (5, "port_ing", False,
         '<p>Choose the grammatically correct sentence in the <strong>Present Perfect</strong>:</p>',
         ["Henrique have finished the HTML project.", "Henrique has finished the HTML project.", "Henrique has finish the HTML project.", "Henrique did finished the HTML project.", "Henrique is finished the HTML project yesterday."],
         1, "Present Perfect para 3ª pessoa do singular (He/Henrique) usa <code>has + particípio passado</code>: <code>has finished</code>."),

        (6, "port_ing", False,
         '<p>Complete the sentence with the appropriate phrasal verb: <em>"Don\'t ______ learning programming; practice every day and you will pass!"</em></p>',
         ["give up", "turn off", "run out", "put on", "look after"],
         0, "<code>give up</code> significa 'desistir' (<em>Don't give up</em> = Não desista!)."),

        # --- ARTE & EDUCAÇÃO FÍSICA (Q7–Q10) ---
        (7, "ciencias_hum", False,
         '<p>Em processos criativos na Arte, qual opção representa corretamente uma <strong>técnica artística</strong> (e não um tema)?</p>',
         ["A desigualdade social nas metrópoles.", "A preservação das florestas brasileiras.", "A xilogravura aplicada em ilustrações de cordel.", "A reflexão filosófica sobre a passagem do tempo.", "A solidão na era das redes sociais."],
         2, "Xilogravura é uma <strong>técnica</strong> (modo de fazer); os demais itens são temas/assuntos de inspiração."),

        (8, "ciencias_hum", False,
         '<p>Qual é a função principal do <strong>tema</strong> em um processo criativo artístico?</p>',
         ["Definir o preço final de venda da obra.", "Servir como ideia central ou assunto gerador que orienta a criação.", "Substituir o uso de qualquer material físico.", "Determinar apenas o tamanho da moldura.", "Impedir interpretações do público."],
         1, "O tema é a ideia central / assunto gerador que dá unidade e sentido ao processo criativo."),

        (9, "ciencias_hum", False,
         '<p>Quando uma pessoa segura uma prancha abdominal parada, mantendo os músculos contraídos e tensos <strong>sem encurtar nem alongar</strong> as fibras musculares, ocorre uma contração do tipo:</p>',
         ["Concêntrica.", "Excêntrica.", "Isométrica.", "Isquêmica.", "Aeróbica passiva."],
         2, "Na contração <strong>isométrica</strong> há tensão muscular sem alteração do comprimento do músculo (sem movimento articular)."),

        (10, "ciencias_hum", False,
         '<p>Assinale a alternativa que apresenta <strong>APENAS esportes de invasão</strong>:</p>',
         ["Futsal, basquetebol, handebol e rúgbi.", "Voleibol, tênis, futsal e natação.", "Basquetebol, xadrez, atletismo e bocha.", "Badminton, futebol, beisebol e golfe.", "Handebol, judô, tênis de mesa e surfe."],
         0, "Esportes de invasão têm duas equipes disputando território para levar o objeto à meta adversária (futsal, basquete, handebol, rúgbi, futebol)."),

        # --- MATEMÁTICA (Q11–Q14) ---
        (11, "exatas", False,
         '<p>Em uma escola técnica, 60 alunos estudam C#, 45 estudam HTML/CSS, 20 estudam ambos e 15 não estudam nenhum dos dois. Quantos alunos participaram da pesquisa?</p>',
         ["85 alunos", "100 alunos", "110 alunos", "120 alunos", "140 alunos"],
         1, "Diagrama de Venn: só C# = <code>60-20 = 40</code>; só HTML = <code>45-20 = 25</code>; ambos = <code>20</code>; nenhum = <code>15</code>. Total = <code>40 + 25 + 20 + 15 = 100</code> alunos!"),

        (12, "exatas", False,
         '<p>Dados <code>log<sub>a</sub> m = 8</code> e <code>log<sub>a</sub> n = 5</code>, qual é o valor de <code>log<sub>a</sub>(m² · n³)</code>?</p>',
         ["21", "26", "31", "40", "64"],
         2, "Propriedades dos logaritmos: <code>log(m² · n³) = 2·log m + 3·log n = 2(8) + 3(5) = 16 + 15 = 31</code>!"),

        (13, "exatas", False,
         '<p>Um estudante junta dinheiro para comprar um SSD: no 1º mês guarda R$ 30,00; no 2º mês R$ 45,00; no 3º mês R$ 60,00, aumentando sempre R$ 15,00 por mês. Em qual mês o depósito mensal será exatamente R$ 210,00?</p>',
         ["10º mês", "11º mês", "12º mês", "13º mês", "15º mês"],
         3, "Progressão Aritmética (<code>a₁ = 30, r = 15, aₙ = 210</code>): <code>210 = 30 + (n - 1)·15 → 180 = 15(n - 1) → n - 1 = 12 → n = 13º mês</code>!"),

        (14, "exatas", False,
         '<p>Um terreno é composto por um retângulo de <code>20 m × 15 m</code> unido a um triângulo retângulo de catetos <code>12 m</code> e <code>16 m</code>. Qual é a área total do terreno?</p>',
         ["348 m²", "396 m²", "420 m²", "492 m²", "540 m²"],
         1, "Retângulo = <code>20 × 15 = 300 m²</code>. Triângulo = <code>(12 × 16) / 2 = 96 m²</code>. Soma total = <code>300 + 96 = 396 m²</code>!"),

        # --- FÍSICA & QUÍMICA (Q15–Q18) ---
        (15, "exatas", False,
         '<p>Um gás ideal parte do estado inicial A com <code>T = 300 K</code>, pressão <code>p₀</code> e volume <code>V₀</code>. Ele passa por uma expansão <strong>isobárica</strong> (pressão constante) até o estado B com volume <code>3V₀</code>. Qual é a temperatura do gás no estado B?</p>',
         ["100 K", "300 K", "600 K", "900 K", "1200 K"],
         3, "Pela lei geral dos gases (<code>p·V/T = cte</code>) com pressão constante: <code>V₀ / 300 = 3V₀ / T_B → T_B = 3 × 300 = 900 K</code>!"),

        (16, "exatas", False,
         '<p>Um carro parte do repouso (<code>v₀ = 0</code>) em linha reta com aceleração constante <code>a = 3,0 m/s²</code>. Após <code>4,0 segundos</code>, sua velocidade e a distância percorrida serão, respectivamente:</p>',
         ["12 m/s e 24 m", "12 m/s e 48 m", "7 m/s e 16 m", "16 m/s e 24 m", "9 m/s e 18 m"],
         0, "MRUV: <code>v = v₀ + a·t = 0 + 3×4 = 12 m/s</code> e <code>ΔS = (a·t²)/2 = (3 × 16)/2 = 24 m</code>!"),

        (17, "exatas", False,
         '<p>Em laboratório, a substância <strong>X</strong> conduz eletricidade no estado sólido; <strong>Y</strong> não conduz sólida, mas conduz dissolvida em água; e <strong>Z</strong> não conduz nem sólida nem líquida. X, Y e Z apresentam, respectivamente, ligações:</p>',
         ["Iônica, Metálica e Covalente.", "Metálica, Iônica e Covalente.", "Covalente, Iônica e Metálica.", "Metálica, Covalente e Iônica.", "Iônica, Covalente e Metálica."],
         1, "Metal conduz sólido (mar de elétrons); Iônico só conduz fundido/aquoso (íons livres); Molecular/Covalente não conduz."),

        (18, "exatas", False,
         '<p>Sobre modelos atômicos e reações químicas, assinale a alternativa correta:</p>',
         ["No modelo de Dalton, os elétrons saltam entre camadas emitindo luz colorida.", "Toda combustão absorve calor do ambiente, sendo endotérmica.", "No modelo de Bohr, as cores emitidas resultam de transições eletrônicas entre camadas quantizadas.", "A Lei de Lavoisier afirma que átomos são destruídos durante reações químicas.", "Metais alcalinos (Família 1A) são gases nobres inertes."],
         2, "Bohr explicou os espectros de cores por saltos de elétrons entre níveis de energia. Combustão é exotérmica e Lavoisier garante conservação da massa."),

        # --- HISTÓRIA, INVESTIGAÇÃO CIENTÍFICA & EMPREENDEDORISMO (Q19–Q22) ---
        (19, "ciencias_hum", False,
         '<p>Sobre o <strong>Feudalismo</strong> na Idade Média europeia, assinale a alternativa correta:</p>',
         ["A sociedade era totalmente móvel, permitindo a servos comprarem títulos de nobreza facilmente.", "A economia era fortemente urbana, industrial e baseada em alta circulação monetária.", "A sociedade estamental dividia-se em clero, nobreza e servos, sustentada pelo trabalho camponês.", "Os servos não pagavam tributos nem trabalhavam nas terras do senhor feudal.", "O poder político era 100% centralizado em um único imperador absoluto."],
         2, "O Feudalismo caracterizou-se pela sociedade estamental (clero, nobreza e servos), economia agrária de subsistência com pouco uso de moedas e poder descentralizado."),

        (20, "ciencias_hum", False,
         '<p>O <strong>Renascimento Cultural</strong> (sécs. XIV–XVI) marcou a transição da Idade Média para a Idade Moderna ao:</p>',
         ["rejeitar completamente a herança greco-romana e a observação da natureza.", "valorizar o antropocentrismo, a razão humana e o desenvolvimento científico.", "reforçar exclusivamente o teocentrismo medieval sem espaço para a ciência.", "proibir o uso da matemática nas artes e na astronomia.", "acabar com a imprensa e com as universidades europeias."],
         1, "O Renascimento resgatou clássicos greco-romanos, promovendo antropocentrismo, racionalismo e ciência."),

        (21, "ciencias_hum", False,
         '<p>Em um projeto escolar, uma equipe aplica um questionário fechado a 200 alunos para gerar gráficos percentuais, enquanto outra equipe faz entrevistas abertas detalhadas com 8 alunos para compreender suas motivações subjetivas. Essas abordagens são, respectivamente:</p>',
         ["Qualitativa e Quantitativa.", "Quantitativa e Qualitativa.", "Ambas puramente qualitativas.", "Experimental e Hipotética.", "Bibliográfica e Estática."],
         1, "Números, porcentagens e estatísticas = <strong>Quantitativa</strong>; compreensão profunda e subjetiva = <strong>Qualitativa</strong>."),

        (22, "ciencias_hum", False,
         '<p>Na <strong>Análise SWOT (FOFA)</strong> aplicada a uma startup de tecnologia, uma equipe muito experiente em C# e o lançamento de um concorrente gigante no mercado classificam-se, respectivamente, como:</p>',
         ["Oportunidade e Fraqueza.", "Força (ambiente interno) e Ameaça (ambiente externo).", "Ameaça e Força.", "Fraqueza e Oportunidade.", "Fator externo e Fator interno."],
         1, "Equipe experiente = <strong>Força</strong> (interno, positivo). Concorrente gigante = <strong>Ameaça</strong> (externo, negativo)."),

        # --- PROGRAMAÇÃO WEB I (Q23–Q26) ---
        (23, "web_design", True,
         '<p>Assinale a alternativa que apresenta, respectivamente, as tags HTML5 para <strong>quebra de linha</strong>, <strong>linha horizontal</strong>, <strong>lista ordenada</strong> e <strong>importação de JavaScript externo</strong>:</p>',
         ["&lt;hr&gt;, &lt;br&gt;, &lt;ul&gt;, &lt;js src=&quot;app.js&quot;&gt;", "&lt;br&gt;, &lt;hr&gt;, &lt;ol&gt;, &lt;script src=&quot;app.js&quot;&gt;&lt;/script&gt;", "&lt;p&gt;, &lt;hr&gt;, &lt;ol&gt;, &lt;script href=&quot;app.js&quot;&gt;", "&lt;br&gt;, &lt;line&gt;, &lt;li&gt;, &lt;link src=&quot;app.js&quot;&gt;", "&lt;break&gt;, &lt;hr&gt;, &lt;ol&gt;, &lt;script file=&quot;app.js&quot;&gt;"],
         1, "<code>&lt;br&gt;</code> = quebra de linha; <code>&lt;hr&gt;</code> = linha horizontal; <code>&lt;ol&gt;</code> = lista ordenada; <code>&lt;script src=&quot;...&quot;&gt;&lt;/script&gt;</code> importa JS externo!"),

        (24, "web_design", True,
         '<p>Em um formulário HTML5 de login contendo campo de senha e imagem de logotipo, qual combinação segue as boas práticas?</p>',
         ["Usar method=&quot;GET&quot; para esconder a senha na URL e omitir alt na imagem.", "Usar method=&quot;POST&quot;, input type=&quot;password&quot; e atributo alt na tag &lt;img&gt;.", "Usar &lt;table&gt; no lugar de &lt;form&gt; e type=&quot;number&quot; para a senha.", "Colocar todo o formulário dentro da tag &lt;head&gt; para ficar visível.", "Usar &lt;tr&gt; para cada campo de texto e &lt;td&gt; para criar linhas."],
         1, "Senhas exigem <code>method=&quot;POST&quot;</code> (escondidas no corpo HTTP) + <code>type=&quot;password&quot;</code>; <code>alt</code> fornece texto alternativo acessível para a imagem."),

        (25, "web_design", True,
         '<p>Sobre <strong>CSS Box Model</strong> e <strong>Flexbox</strong>, assinale a alternativa correta:</p>',
         ["margin é o espaço interno entre o texto e a borda; padding é o espaço externo.", "Para centralizar um item horizontal e verticalmente com Flexbox usa-se display: flex; justify-content: center; align-items: center;.", "Media Queries (@media) servem para criar tabelas no banco de dados.", "O Box Model só se aplica à tag &lt;table&gt;.", "display: block centraliza automaticamente itens na vertical."],
         1, "<code>display: flex; justify-content: center; align-items: center;</code> é o padrão de ouro do Flexbox para centralizar! (E lembre: padding = interno, margin = externo)."),

        (26, "web_design", True,
         '<p>Sobre conceitos básicos da Web (WWW, URI, DNS e HTTP), analise:<br>I. <strong>URI</strong> identifica de forma única um recurso na internet.<br>II. <strong>DNS</strong> traduz nomes de domínio (ex.: etects.cps.sp.gov.br) em endereços IP.<br>III. <strong>HTTP</strong> é um protocolo da camada de aplicação usado na comunicação cliente-servidor web.</p>',
         ["Apenas I está correta.", "Apenas II e III estão corretas.", "Apenas I e III estão corretas.", "Todas (I, II e III) estão corretas.", "Nenhuma está correta."],
         3, "Todas as três definições oficiais estão 100% corretas!"),

        # --- ANÁLISE E PROJETO DE SISTEMAS — APS (Q27–Q29) ---
        (27, "bd_aps_fi", True,
         '<p>No <strong>Diagrama de Casos de Uso</strong> e no <strong>Diagrama de Classes</strong> da UML, suas funções principais são, respectivamente:</p>',
         ["Representar tabelas SQL; descrever cabos de rede.", "Descrever interações entre atores e funcionalidades do sistema; representar classes, atributos, métodos e associações estruturais.", "Desenhar telas coloridas; criar arquivos CSS.", "Listar senhas de usuários; configurar roteadores.", "Executar código C#; compilar páginas HTML."],
         1, "Casos de Uso = atores + funcionalidades vistas de fora; Diagrama de Classes = estrutura interna de classes e suas associações."),

        (28, "bd_aps_fi", True,
         '<p>Assinale a alternativa que apresenta <strong>somente metodologias/frameworks ágeis</strong> e a característica correta do <strong>Modelo em Cascata</strong>:</p>',
         ["Scrum, XP e Kanban; Cascata divide o projeto em etapas sequenciais.", "UML, DER e Cascata; Cascata não possui documentação.", "HTML, CSS e Scrum; Cascata permite voltar fases sem custo.", "MySQL, Kanban e Dicionário de Dados; Cascata entrega semanalmente.", "Photoshop, XP e GIMP; Cascata dispensa requisitos."],
         0, "Ágeis = Scrum, XP, Kanban. Cascata = etapas predeterminadas executadas de forma sequencial."),

        (29, "bd_aps_fi", True,
         '<p>Um cliente solicita: <em>"O sistema deve emitir boletim em PDF e responder a cada consulta em menos de 2 segundos."</em> Essas exigências são, respectivamente:</p>',
         ["Dois Requisitos Não Funcionais.", "Requisito Não Funcional e Requisito Funcional.", "Requisito Funcional (o que faz) e Requisito Não Funcional (desempenho/como se comporta).", "Dois Requisitos Funcionais.", "Apenas critérios de hardware."],
         2, "Emitir boletim = ação/função (<strong>RF</strong>); responder em < 2s = qualidade/desempenho (<strong>RNF</strong>)."),

        # --- DESIGN DIGITAL & UX (Q30–Q31) ---
        (30, "web_design", True,
         '<p>Em <strong>UX Design</strong>, quando um aplicativo organiza rótulos próximos aos seus campos e permite que novos usuários completem o cadastro rapidamente sem erros, dizemos que ele tem boa:</p>',
         ["Rasterização.", "Usabilidade (com apoio da Lei da Proximidade da Gestalt).", "Compilação estática.", "Fragmentação de disco.", "Tipografia Script."],
         1, "Usabilidade = facilidade de aprender e interagir com eficiência; rótulo colado ao campo aplica a Lei da Proximidade da Gestalt."),

        (31, "web_design", True,
         '<p>Para criar o logotipo oficial de uma escola que será usado tanto em um ícone pequeno de aplicativo quanto em uma faixa de 3 metros <strong>sem pixelar</strong>, e definir as cores para a <strong>impressão gráfica</strong> da faixa, o designer deve usar respectivamente:</p>',
         ["Bitmap (.JPEG) e RGB.", "Vetor (.SVG) e CMYK.", "Bitmap (.PNG) e Hexadecimal.", "Vetor (.JPEG) e RGB.", "Bitmap (.BMP) e CMYK."],
         1, "Logotipo sem pixelar no zoom = <strong>Vetor (.SVG)</strong>; impressão gráfica em papel/lona = <strong>CMYK</strong> (tinta)!"),

        # --- FUNDAMENTOS DA INFORMÁTICA (Q32–Q34) ---
        (32, "bd_aps_fi", True,
         '<p>Calcule: qual número em <strong>Hexadecimal</strong> corresponde ao número decimal <code>219</code>? <em>(Dica: divida por 16 e lembre: A=10, B=11, C=12, D=13, E=14, F=15)</em></p>',
         ["BB", "C9", "DB", "EA", "FA"],
         2, "<code>219 ÷ 16 = 13</code> (pois <code>13 × 16 = 208</code>), com resto <code>219 - 208 = 11</code>. Como <code>13 = D</code> e <code>11 = B</code>, resulta em <strong>DB</strong>!"),

        (33, "bd_aps_fi", True,
         '<p>Sobre <strong>Interface CLI</strong> e <strong>Sistemas Multiusuário</strong> nos Fundamentos da Informática (padrão Etec Taboão), assinale a correta:</p>',
         ["CLI é uma interface gráfica com janelas e ícones clicáveis.", "CLI caracteriza-se como interface por linha de comando (monotarefa clássica), e um sistema multiusuário permite vários usuários utilizando aplicações no mesmo servidor/sistema.", "Um sistema operacional não interage com o hardware.", "Software Livre nunca permite alterar o código-fonte.", "Memória RAM mantém todos os dados salvos permanentemente ao desligar da tomada."],
         1, "CLI = Command Line Interface (linha de comando); sistema multiusuário atende múltiplos usuários simultâneos."),

        (34, "bd_aps_fi", True,
         '<p>Qual é a principal vantagem técnica de um <strong>SSD</strong> em comparação com um <strong>HDD</strong> tradicional?</p>',
         ["O SSD possui discos magnéticos giratórios mais pesados.", "O SSD usa memória flash sem partes móveis, sendo muito mais rápido e resistente a impactos.", "O SSD é volátil e apaga os arquivos ao reiniciar o computador.", "O SSD substitui totalmente o processador (CPU).", "O SSD funciona apenas no sistema operacional Linux."],
         1, "SSD usa chips Flash NAND sem peças mecânicas girando → muito mais rápido, silencioso e resistente a quedas!"),

        # --- TÉCNICAS DE PROGRAMAÇÃO E ALGORITMOS — TPA / C# (Q35–Q37) ---
        (35, "tpa_csharp", True,
         '<p>Analise o código em <strong>C#</strong> abaixo. Se o usuário digitar <code>8</code>, o que será impresso no console?</p><pre class="q-code">int n = int.Parse(Console.ReadLine());\nint soma = 0;\nwhile (n &lt;= 10) {\n    if (n % 2 == 0) {\n        soma = soma + n;\n    }\n    n++;\n}\nConsole.WriteLine(soma);</pre>',
         ["8", "10", "18", "27", "Erro de compilação"],
         2, "Teste de mesa: <code>n=8</code> (par → soma=8); <code>n=9</code> (ímpar → pula); <code>n=10</code> (par → soma=8+10=<strong>18</strong>); <code>n=11</code> sai do laço! Imprime <strong>18</strong>."),

        (36, "tpa_csharp", True,
         '<p>Qual será a saída no console do código em <strong>C#</strong> abaixo?</p><pre class="q-code">int[,] m = { { 2, 5 }, { 7, 9 } };\nConsole.WriteLine(m[1, 0] + m[0, 1]);</pre>',
         ["7", "11", "12", "14", "16"],
         2, "Em C# os índices começam em 0 (<code>[linha, coluna]</code>): <code>m[1, 0] = 7</code> (linha 1, col 0) e <code>m[0, 1] = 5</code> (linha 0, col 1). Soma = <code>7 + 5 = 12</code>!"),

        (37, "tpa_csharp", True,
         '<p>Sobre <strong>depuração (debugging)</strong> e <strong>tratamento de exceções</strong> em C#, assinale a alternativa correta:</p>',
         ["Um breakpoint apaga automaticamente as linhas com erro do código.", "O laço do/while nunca executa se a condição inicial já for falsa.", "Breakpoints pausam a execução em pontos marcados para inspecionar variáveis, e blocos try/catch capturam erros em tempo de execução (como digitar letras em int.Parse).", "Faltar ponto e vírgula (;) no final da linha em C# é ignorado pelo compilador.", "O operador lógico E em C# é representado por ||."],
         2, "Breakpoint pausa para inspecionar variáveis; <code>try/catch</code> evita travamento em entradas inválidas. (Em C#: <code>;</code> é obrigatório, <code>&amp;&amp;</code> é E, e <code>do/while</code> roda ao menos 1 vez!)."),

        # --- BANCO DE DADOS I (Q38–Q40) ---
        (38, "bd_aps_fi", True,
         '<p>Na modelagem relacional de um banco de dados escolar, o conceito de <strong>Tabela</strong>, <strong>Registro (Tupla)</strong> e <strong>Chave Primária (PK)</strong> correspondem, respectivamente, a:</p>',
         ["Um cabo de rede; uma senha; um comentário.", "Conjunto organizado de linhas e colunas sobre uma entidade; uma linha completa de dados; coluna única que impede registros duplicados.", "Uma coluna isolada; o nome do SGBD; um campo opcional vazio.", "Um programa editor; uma foto; uma chave que sempre repete.", "Um relatório PDF; um botão HTML; uma tag CSS."],
         1, "Tabela = grade da entidade; Registro = 1 linha completa; Chave Primária (PK) = identificador único não nulo que impede duplicatas."),

        (39, "bd_aps_fi", True,
         '<p>Em um sistema com as tabelas <code>TURMA(id_turma PK, nome)</code> e <code>ALUNO(id_aluno PK, nome, id_turma FK)</code>, a coluna <code>id_turma</code> dentro de <code>ALUNO</code> é uma:</p>',
         ["Chave Primária da tabela ALUNO que permite duplicar alunos.", "Chave Estrangeira (Foreign Key) que migrou da tabela pai (TURMA) para ligar o aluno à sua turma.", "Variável booleana de C#.", "Violação direta da 1ª Forma Normal.", "Tag semântica de HTML5."],
         1, "A <strong>Chave Estrangeira (FK)</strong> é a PK da tabela pai (<code>TURMA</code>) que migra para a tabela filha (<code>ALUNO</code>, lado N) criando o vínculo relacional."),

        (40, "bd_aps_fi", True,
         '<p>Qual artefato de Banco de Dados I ilustra graficamente <strong>entidades e seus relacionamentos</strong>, e qual documento cataloga <strong>nomes, tipos, atributos e definições</strong> dos dados do sistema?</p>',
         ["CSS Box Model e Breakpoint.", "Diagrama Entidade-Relacionamento (DER) e Dicionário de Dados.", "Fluxograma e CLI.", "Protocolo HTTP e URI.", "Flexbox e Normalização."],
         1, "DER = desenho conceitual de Entidades e Relacionamentos; Dicionário de Dados = catálogo de nomes, atributos e definições dos elementos de dados!"),
    ]
    out = []
    for num, area, is_tech, stem, opts, ans, exp in raw_qs:
        out.append({
            "num": num,
            "stemHtml": stem,
            "options": opts,
            "answer": ans,
            "explain": exp,
            "area": area,
            "isTech": is_tech,
        })
    assert len(out) == 40
    return out

if __name__ == "__main__":
    q26 = build_taboao_2026()
    q25 = build_taboao_2025()
    q27 = build_sim_taboao_2027()
    print(f"OK! taboao2026={len(q26)}Q | taboao2025={len(q25)}Q | sim_taboao2027={len(q27)}Q")
