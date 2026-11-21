"""Cronograma dos 16 dias, quizzes (questões reais do banco), vídeos e textos das provas."""


def Q(ref):
    exam, num = ref.split(":")
    return {"examId": exam, "qNum": int(num)}


def refs(*items):
    return [Q(x) for x in items]


# Vídeos conferidos pelo oEmbed do YouTube em 20/11/2026 (título e canal batem).
VIDEOS = {
    "variaveis": {"title": "Variáveis e tipos primitivos de dados", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "N91jAze53uA"},
    "while": {"title": "Estruturas de repetição: enquanto (while)", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "U5PnCt58Q68"},
    "vetores": {"title": "Vetores — Curso de Algoritmos #14", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "j9473xQ39vY"},
    "matrizes": {"title": "Matrizes — Curso de Algoritmos #15", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "hkE9WrjpAAk"},
    "semantica": {"title": "Semântica na HTML5 é importante", "channel": "Curso em Vídeo (HTML5 e CSS3)", "videoId": "HaSgt1hK2Fs"},
    "boxmodel": {"title": "Modelo de caixas (box model): primeiros passos", "channel": "Curso em Vídeo (HTML5 e CSS3)", "videoId": "3ZFYXkzXhqE"},
    "normalizacao": {"title": "Modelagem de dados: normalização e 1ª forma normal", "channel": "Bóson Treinamentos", "videoId": "eRaAMNjCFYw"},
    "mysql": {"title": "Curso MySQL #03 — Criando o primeiro banco de dados", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "m9YPlX0fcJk"},
    "scrum": {"title": "Scrum — Dicionário do Programador", "channel": "Código Fonte TV", "videoId": "3aCww_1RnL0"},
    "rgbcmyk": {"title": "RGB, CMYK, vetor e bitmap", "channel": "Curso de Design", "videoId": "wU6rwo-SeIw"},
    "binarios": {"title": "Números binários — Bases numéricas #02", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "eD56zn5kYfU"},
    "hexa": {"title": "Números octais e hexadecimais — Bases numéricas #03", "channel": "Curso em Vídeo (Gustavo Guanabara)", "videoId": "gIXiFhEA-Qw"},
    "figuras": {"title": "Passo a passo para entender as figuras de linguagem", "channel": "Professor Noslen", "videoId": "n0e75nRstcU"},
    "conjuntos": {"title": "Questões comentadas: conjuntos numéricos", "channel": "Professor Ferretto", "videoId": "Bq5XYZKXk-Q"},
    "ligacoes": {"title": "Ligações químicas: aprenda de uma vez por todas", "channel": "Brasil Escola", "videoId": "FDnxddw0P1g"},
}

DIAS = [
    {"day": 1, "date": "Sáb 21/11", "phase": 1, "weight": "Diagnóstico",
     "title": "Diagnóstico: a prova real de Taboão (05/12/2025)",
     "intro": "Faça a prova real de dezembro/2025 sem consulta, entenda as regras do edital e mande o diagnóstico para recalibrar o plano.",
     "practice": "vf", "tag": "",
     "examTask": {"examId": "taboao2026", "label": "Fazer a prova real de 05/12/2025 (diagnóstico)"},
     "quiz": refs("taboao2023:8", "taboao2021:14", "taboao2021:13", "taboao2023:2", "taboao2021:18",
                  "irma2025inf:35", "taboao2023:16", "mtec2022:3")},
    {"day": 2, "date": "Dom 22/11", "phase": 1, "weight": "Máxima",
     "title": "Programação I: algoritmo, variáveis, operadores e if/else em C#",
     "intro": "Do zero: o que é um algoritmo, fluxograma, variáveis e tipos, operadores (incluindo % e &&), tabela verdade, if/else e teste de mesa — escrevendo C# de verdade.",
     "practice": "lab_tipos", "tag": "01_TPA_CSharp",
     "videos": [("variaveis", 65, 345, "Como uma variável guarda um valor na memória e quais são os tipos básicos.")],
     "quiz": refs("taboao2021:36", "taboao2021:38", "irma2025ipi:11", "irma2024ipi:36", "irma2024ipi:38",
                  "irma2025ipi:13", "irma2025ipi:14", "taboao2026:34")},
    {"day": 3, "date": "Seg 23/11", "phase": 1, "weight": "Máxima",
     "title": "Programação II: laços, vetores, matrizes, exceções e depuração",
     "intro": "for, while e do/while com teste de mesa; vetores e matrizes int[,]; try/catch, breakpoint, compilador e erros — o que mais cai no bloco técnico.",
     "practice": "lab02", "tag": "01_TPA_CSharp",
     "videos": [("while", 150, 510, "A ideia do laço 'enquanto' e por que ele pode rodar zero vezes."),
                ("vetores", 120, 460, "Vetor como uma fileira de caixinhas numeradas a partir de zero."),
                ("matrizes", 105, 495, "Matriz como uma tabela de linhas e colunas.")],
     "quiz": refs("taboao2021:39", "irma2025ipi:12", "taboao2023:36", "taboao2023:35", "taboao2023:34",
                  "taboao2026:35", "taboao2026:36", "taboao2026:37", "irma2024ipi:37", "taboao2023:33")},
    {"day": 4, "date": "Ter 24/11", "phase": 1, "weight": "Alta",
     "title": "Web I: como a internet funciona e HTML do zero",
     "intro": "Cliente e servidor, WWW, URL e URI, DNS, IP, TCP e HTTP; a estrutura de uma página e as tags que caem (p, hr, br, h1–h6, listas, img alt, links, tabelas e formulários GET/POST).",
     "practice": "lab01", "tag": "02_Web_Design",
     "videos": [("semantica", 180, 570, "Por que usar tags com significado (header, main, footer).")],
     "quiz": refs("taboao2026:25", "taboao2026:26", "taboao2026:27", "irma2025ipi:20", "irma2025ipi:21",
                  "mtec2022:38", "mtec2022:39", "mtec2022:40", "taboao2023:30", "irma2025inf:16")},
    {"day": 5, "date": "Qua 25/11", "phase": 1, "weight": "Alta",
     "title": "Web II: CSS (seletores, box model, Flexbox, responsivo) e JavaScript",
     "intro": "Como o CSS escolhe e estiliza elementos, padding × margin, centralizar com Flexbox, viewport e @media; JavaScript básico e tipos de aplicativo (web, nativo, híbrido).",
     "practice": "lab04", "tag": "02_Web_Design",
     "videos": [("boxmodel", 120, 510, "As camadas da caixa: conteúdo, padding, borda e margem.")],
     "quiz": refs("irma2025ipi:22", "irma2024ipi:39", "irma2024ipi:40", "novas:3", "novas:4", "novas:5",
                  "novas:6", "novas:7", "novas:8", "novas:10")},
    {"day": 6, "date": "Qui 26/11", "phase": 1, "weight": "Alta",
     "title": "Banco de Dados I: tabelas, chaves, DER, normalização e SQL",
     "intro": "Tabela, registro e campo; chave primária e estrangeira; cardinalidade; DER e os modelos conceitual, lógico e físico; dicionário de dados; normalização; SQL básico.",
     "practice": "lab03", "tag": "03_BD_APS_FI",
     "videos": [("normalizacao", 60, 450, "Por que normalizar e o que é a 1ª forma normal."),
                ("mysql", 180, 540, "Criando um banco e uma tabela em SQL.")],
     "quiz": refs("taboao2021:37", "mtec2022:32", "taboao2023:31", "taboao2023:32", "taboao2026:38",
                  "taboao2026:39", "taboao2026:40", "irma2025inf:37", "irma2025inf:38", "irma2025inf:39")},
    {"day": 7, "date": "Sex 27/11", "phase": 1, "weight": "Alta",
     "title": "Análise de Sistemas e Design: requisitos, ágil, UML e UX",
     "intro": "Ciclo de vida, cascata × ágil (Scrum, XP, Kanban), requisitos funcionais e não funcionais, casos de uso e diagrama de classes; usabilidade, cores e formatos de imagem.",
     "practice": "lab04", "tag": "03_BD_APS_FI",
     "videos": [("scrum", 120, 480, "Como funciona o Scrum (sprints, papéis e reuniões)."),
                ("rgbcmyk", 15, 215, "RGB × CMYK e vetor × bitmap.")],
     "quiz": refs("taboao2021:35", "taboao2021:40", "mtec2022:31", "irma2024ipi:32", "irma2024ipi:33",
                  "taboao2026:28", "taboao2026:29", "taboao2026:30", "irma2025ipi:23", "taboao2021:31")},
    {"day": 8, "date": "Sáb 28/11", "phase": 1, "weight": "Alta",
     "title": "Fundamentos da Informática: bases numéricas, hardware, SO e segurança",
     "intro": "Binário, octal e hexadecimal (o 187 = BB), hardware × software, RAM, ROM, BIOS, sistema operacional, CLI × GUI, comandos do CMD, software livre e segurança.",
     "practice": "lab_bin", "tag": "03_BD_APS_FI",
     "examTask": {"examId": "prev_tec_a", "label": "Depois da aula, fazer o Simulado de Previsão Técnico A (20 questões, 50 min)"},
     "videos": [("binarios", 120, 480, "Como contar em binário."), ("hexa", 150, 510, "Octal e hexadecimal.")],
     "quiz": refs("taboao2021:32", "taboao2021:34", "mtec2022:36", "taboao2026:32", "taboao2026:33",
                  "irma2024ipi:29", "irma2024ipi:30", "irma2025inf:10", "irma2025inf:17", "irma2024ipi:31")},
    {"day": 9, "date": "Dom 29/11", "phase": 1, "weight": "Simulado",
     "title": "Simulado: a prova real de Taboão de 06/12/2024",
     "intro": "Quatro horas, sem consulta, do jeito do dia 04/12. Depois, a correção guiada: o que errar vai para o Caderno de Erros.",
     "practice": "pairs", "tag": "",
     "examTask": {"examId": "taboao2025", "label": "Fazer a prova real de 06/12/2024 (simulado)"},
     "quiz": refs("taboao2023:15", "taboao2023:26", "taboao2023:27", "taboao2023:10", "taboao2023:24",
                  "taboao2023:21", "taboao2023:20", "taboao2023:28")},
    {"day": 10, "date": "Seg 30/11", "phase": 1, "weight": "Média",
     "title": "Linguagens: Português, Inglês e Arte",
     "intro": "Interpretação, referência de pronomes, adequação, figuras de linguagem, tipos textuais, Trovadorismo e Barroco; Present Perfect, phrasal verbs e falsos cognatos; tema, técnica e materialidade.",
     "practice": "vf", "tag": "04_Port_Ingles",
     "videos": [("figuras", 90, 420, "Metáfora, antítese, paradoxo, hipérbole, eufemismo, ironia.")],
     "quiz": refs("taboao2026:3", "taboao2026:4", "taboao2025:1", "taboao2025:3", "irma2025inf:3",
                  "irma2025ipi:2", "taboao2026:5", "taboao2021:22", "taboao2026:7", "irma2025inf:22")},
    {"day": 11, "date": "Ter 01/12", "phase": 1, "weight": "Média",
     "title": "Matemática: os moldes que se repetem",
     "intro": "Conjuntos e Venn, PA, porcentagem e gráficos, áreas e o triângulo 3-4-5, contagem, função afim e do 2º grau, estatística — e as duas questões com defeito que sempre voltam.",
     "practice": "lab_mtec", "tag": "06_Exatas",
     "videos": [("conjuntos", 30, 360, "Conjuntos numéricos com questões comentadas.")],
     "quiz": refs("taboao2021:10", "taboao2021:14", "taboao2025:10", "mtec2022:21", "mtec2022:23",
                  "taboao2023:28", "taboao2026:12", "taboao2026:14", "irma2025inf:8", "irma2025inf:9")},
    {"day": 12, "date": "Qua 02/12", "phase": 1, "weight": "Média",
     "title": "Ciências da Natureza: Física, Química e Biologia",
     "examTask": {"examId": "prev_tec_b", "label": "Antes da aula, fazer o Simulado de Previsão Técnico B (20 questões, 50 min) — a parte técnica é onde você mais ganha pontos"},
     "intro": "Gases, movimento, força, lentes, calor; modelos atômicos, ligações, reações, oxirredução e massa molar; biotecnologia, doenças, ecologia e meio ambiente.",
     "practice": "lab_mtec", "tag": "06_Exatas",
     "videos": [("ligacoes", 45, 360, "Ligação iônica, covalente e metálica.")],
     "quiz": refs("taboao2021:18", "taboao2025:13", "taboao2026:16", "irma2025inf:5", "mtec2022:18",
                  "taboao2026:18", "irma2025inf:27", "taboao2025:11", "taboao2023:21", "taboao2026:21")},
    {"day": 13, "date": "Qui 03/12", "phase": 1, "weight": "Véspera",
     "title": "Humanas, Pesquisa, Ed. Física — e a véspera da prova",
     "intro": "Pré-história, Grécia, Idade Média e Renascimento, ética e moral; método científico, pesquisa qualitativa × quantitativa, empreendedorismo e SWOT; contração muscular e esportes. E o checklist para amanhã.",
     "practice": "vf", "tag": "05_Hum_Aprof",
     "quiz": refs("taboao2026:19", "taboao2025:5", "mtec2022:27", "irma2025ipi:33", "taboao2026:23",
                  "taboao2026:24", "mtec2022:29", "taboao2026:9", "taboao2026:10", "taboao2025:19")},
    {"day": 14, "date": "Sáb 05/12", "phase": 2, "weight": "2ª fase",
     "title": "Laboratório 1: uma página completa em HTML e CSS",
     "intro": "No computador, do zero: estrutura, textos, lista, imagem com alt, tabela, formulário e CSS com Flexbox. Sem copiar e colar.",
     "practice": "phase2", "tag": "02_Web_Design",
     "videos": [("boxmodel", 120, 480, "Revisão rápida de padding, borda e margem.")],
     "quiz": refs("taboao2025:34", "taboao2025:36", "taboao2025:32", "taboao2025:35", "irma2024ipi:39",
                  "taboao2026:26", "mtec2022:38", "irma2025ipi:22")},
    {"day": 15, "date": "Dom 06/12", "phase": 2, "weight": "2ª fase",
     "title": "Laboratório 2: programas em C# no console",
     "intro": "Escrever, compilar e consertar programas pequenos: ler dados, decidir com if, repetir com for/while, somar um vetor, tratar entrada errada.",
     "practice": "phase2", "tag": "01_TPA_CSharp",
     "videos": [("vetores", 120, 460, "Revisão de vetores para o programa das notas.")],
     "quiz": refs("taboao2025:21", "taboao2025:22", "taboao2025:23", "taboao2025:25", "taboao2023:36",
                  "irma2025ipi:14", "taboao2026:35", "taboao2023:35")},
    {"day": 16, "date": "Seg 07/12", "phase": 2, "weight": "2ª fase",
     "title": "Laboratório 3: modelar um banco e escrever SQL — e ensaiar a entrevista",
     "intro": "Do enunciado ao DER, do DER às tabelas com chave primária e estrangeira, e as consultas SQL. Depois, as perguntas da entrevista em voz alta.",
     "practice": "phase2", "tag": "03_BD_APS_FI",
     "videos": [("mysql", 180, 510, "Revisão de CREATE TABLE com PRIMARY KEY.")],
     "quiz": refs("taboao2025:38", "taboao2025:39", "taboao2025:40", "irma2025inf:39", "taboao2023:31",
                  "taboao2021:37", "taboao2026:38", "irma2025inf:40")},
]

EXAM_META = {
    "taboao2026": {"group": "primary", "recommended": True,
                   "title": "Prova Real Etec Taboão — 05/12/2025 (a mais recente)",
                   "badge": "⭐ Diagnóstico • 40 questões",
                   "desc": "A prova mais recente de Taboão, com as figuras originais. O gabarito publicado pela Etec é de outra versão do caderno e não confere; usamos um gabarito revisado questão por questão."},
    "taboao2025": {"group": "primary",
                   "title": "Prova Real Etec Taboão — 06/12/2024",
                   "badge": "Simulado do Dia 9 • 40 questões",
                   "desc": "Prova real com gabarito oficial (conferido): código C#, Flexbox, box model, hexadecimal, CLI, requisitos e Base Comum. Guarde para o simulado de domingo, 29/11."},
    "taboao2023": {"group": "extra",
                   "title": "Prova Real Etec Taboão — dezembro/2023",
                   "badge": "Taboão • 40 questões",
                   "desc": "Prova de dez/2023 (o cabeçalho do PDF diz 2018 por engano). Tem C#, banco de dados e muita Base Comum que se repete. O gabarito oficial erra a questão 3."},
    "mtec2022": {"group": "extra",
                 "title": "Prova Real Etec Taboão — 14/12/2022",
                 "badge": "Taboão • 40 questões",
                 "desc": "Prova de 2022: mais literatura e menos programação que as recentes. O gabarito oficial erra as questões 13 e 27 (explicado em cada uma)."},
    "taboao2021": {"group": "extra",
                   "title": "Prova Real Etec Taboão — 30/11/2021",
                   "badge": "Taboão • 40 questões",
                   "desc": "Prova de 2021 (2ª série de Informática integrado). Várias questões dela voltaram em 2023 e 2024. O gabarito oficial tem 5 erros, explicados em cada questão."},
    "irma2024ipi": {"group": "bank", "title": "Taboão — Informática para Internet, 06/12/2024", "badge": "Banco", "desc": ""},
    "irma2025inf": {"group": "bank", "title": "Taboão — Informática, 05/12/2025", "badge": "Banco", "desc": ""},
    "irma2025ipi": {"group": "bank", "title": "Taboão — Informática para Internet, 05/12/2025", "badge": "Banco", "desc": ""},
    "prev_tec_a": {"group": "primary", "minutes": 50, "cutoff": 10, "target": 15,
                   "title": "Simulado de Previsão — Técnico A (20 questões)",
                   "badge": "🎯 Previsão • só parte técnica • 50 min",
                   "desc": "Questões inéditas montadas sobre o que mais se repete nas provas de Taboão: hexadecimal, CLI, binário, tags, laços, matriz com índices trocados, exceções, chaves, requisitos e UML. Fazer no Dia 8."},
    "prev_tec_b": {"group": "primary", "minutes": 50, "cutoff": 10, "target": 15,
                   "title": "Simulado de Previsão — Técnico B (20 questões)",
                   "badge": "🎯 Previsão • só parte técnica • 50 min",
                   "desc": "Os temas técnicos do 1º ano com mais chance de cair a seguir: breakpoint, compilador, vetores, fluxograma, tabela verdade, CSS, JavaScript, normalização, DER, SQL, cascata, classes, cores e software livre. Fazer no Dia 12."},
    "prev_completo": {"group": "primary", "minutes": 240, "cutoff": 20, "target": 24,
                      "title": "Simulado de Previsão — Completo (40 questões)",
                      "badge": "🎯 Previsão • formato real (20 Base Comum + 20 técnicas)",
                      "desc": "Uma prova inteira no formato de Taboão, com variações das questões que mais se repetem. Treino extra: faça em partes (modo treino) se não tiver 4 horas."},
    "novas": {"group": "bank", "title": "Questões inéditas no estilo de Taboão", "badge": "Banco", "desc": ""},
}

PRIMARY = ["taboao2026", "taboao2025", "repetidas", "prev_tec_a", "prev_tec_b", "prev_completo"]
EXTRA = ["taboao2023", "mtec2022", "taboao2021"]

# Repetições que a comparação automática não pega (alternativas embaralhadas) e
# ocorrências em provas irmãs que não entraram no banco por serem cópias idênticas.
MANUAL_GROUPS = [
    [("mtec2022", 1), ("taboao2023", 1)],                       # Barroco: cultismo × conceptismo
    [("mtec2022", 2), ("taboao2023", 4)],                       # variação linguística
    [("taboao2021", 1), ("mtec2022", 3), ("taboao2023", 3)],    # tipos textuais
    [("taboao2021", 3), ("mtec2022", 4)],                       # paradoxo
    [("taboao2023", 9), ("irma2025ipi", 38)],                   # músculo estriado esquelético
]
EXTRA_OCCURRENCES = {
    ("taboao2023", 8): ["dez/2024 (Inf. p/ Internet) Q13"],                                  # contração muscular
    ("taboao2026", 10): ["dez/2024 (Inf. p/ Internet) Q14", "dez/2025 (Inf. p/ Internet) Q37"],  # aparelho locomotor
    ("taboao2026", 7): ["dez/2025 (Inf. p/ Internet) Q31"],                                   # tema em processos criativos
    ("irma2025inf", 2): ["dez/2025 (Inf. p/ Internet) Q4"],                                   # classes de palavras
    ("irma2025inf", 4): ["dez/2025 (Inf. p/ Internet) Q3"],                                   # acentuação
    ("irma2025inf", 8): ["dez/2025 (Inf. p/ Internet) Q10"],                                  # função afim
    ("irma2025inf", 10): ["dez/2025 (Inf. p/ Internet) Q9"],                                  # 86 em várias bases
}
