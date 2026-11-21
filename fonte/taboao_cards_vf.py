# -*- coding: utf-8 -*-
"""
Áreas do Radar, Flashcards calibrados (~100), Pares Relâmpago e Verdade ou Fake (~56)
100% orientados ao Edital nº 02, Matriz 612 e Provas Reais da Etec de Taboão da Serra (2ª Série M-Tec DS).
"""

TABOAO_AREAS = [
    {"id": "tpa_csharp", "title": "Lógica, Algoritmos & C# (TPA)", "recommendedDay": 2},
    {"id": "web_design", "title": "Programação Web I & Design/UX", "recommendedDay": 4},
    {"id": "bd_aps_fi", "title": "Banco de Dados I, APS/UML & Fundamentos", "recommendedDay": 6},
    {"id": "port_ing", "title": "Português & Inglês (Base Comum)", "recommendedDay": 9},
    {"id": "ciencias_hum", "title": "Inv. Científica, Empreend., Arte, Ed.Fís & História", "recommendedDay": 10},
    {"id": "exatas", "title": "Matemática, Física & Química (Exatas)", "recommendedDay": 11},
]

def classify_taboao_area(exam_id: str, q_num: int, existing_area: str = None) -> str:
    if existing_area in {a["id"] for a in TABOAO_AREAS}:
        return existing_area
    # Map legacy exams (mtec2022, ds2025, info2025, ds2019, apostas, sim1, sim2) cleanly into the 6 Taboao areas
    if exam_id == "mtec2022":
        if q_num in range(1, 10): return "port_ing"
        if q_num in [10, 11, 12, 13, 14, 15, 16, 24, 25, 26, 27, 28, 29, 37]: return "ciencias_hum"
        if q_num in [17, 18, 19, 20, 21, 22, 23, 33]: return "exatas"
        if q_num in [30, 31, 32, 34, 35, 36]: return "bd_aps_fi"
        return "web_design"
    if exam_id == "ds2025":
        if q_num in [1, 2, 3]: return "port_ing"
        if q_num in [4, 5, 6]: return "ciencias_hum"
        if q_num in [7, 8, 9, 10, 19, 22]: return "tpa_csharp"
        if q_num in [11, 12, 13, 14, 23, 24, 25, 26, 27, 28, 29, 30]: return "bd_aps_fi"
        return "web_design"
    if exam_id == "info2025":
        if q_num in [1, 2, 3]: return "port_ing"
        if q_num in [19, 20, 21]: return "tpa_csharp"
        if q_num in [9, 10, 11, 13, 14, 15]: return "web_design"
        return "bd_aps_fi"
    if exam_id == "ds2019":
        if q_num in [28, 29, 30]: return "port_ing"
        if q_num in [1, 2, 3, 6, 26, 27]: return "tpa_csharp"
        if q_num in [13, 14, 15, 16, 17, 18, 19]: return "web_design"
        return "bd_aps_fi"
    # apostas, sim1, sim2
    if q_num in [1, 2, 3]: return "port_ing"
    if q_num in [4, 5, 6]: return "ciencias_hum"
    if q_num in [7, 8, 9, 10, 11, 12]: return "tpa_csharp"
    if q_num in [19, 20, 21, 22, 23, 24, 25]: return "web_design"
    return "bd_aps_fi"

TABOAO_FLASHCARDS = [
    # --- 1. TPA & C# (18 cards) ---
    ("Em C#, qual operador lógico verifica se AMBAS as condições são verdadeiras?", "&& (dois E comerciais). Já || significa OU, e ! significa NÃO.", "01_TPA_CSharp"),
    ("Em C#, o que faz o comando int.Parse(Console.ReadLine())?", "Lê o texto digitado pelo usuário no teclado (Console.ReadLine) e converte explicitamente para número inteiro (int.Parse).", "01_TPA_CSharp"),
    ("Qual a diferença entre while e do/while em C#?", "while (pré-teste) checa ANTES e pode rodar 0 vezes. do/while (pós-teste) executa PELO MENOS 1 VEZ antes de testar no final.", "01_TPA_CSharp"),
    ("O que acontece em C# se você esquecer o ponto e vírgula (;) no final de uma instrução?", "Ocorre erro de sintaxe: o código NÃO compila e o compilador/IDE destaca a linha provável do erro.", "01_TPA_CSharp"),
    ("Para que serve um Breakpoint durante a depuração (debug)?", "Pausa a execução do programa em uma linha marcada pelo dev para inspecionar os valores das variáveis e o fluxo em tempo real.", "01_TPA_CSharp"),
    ("Para que serve o tratamento de exceções (try / catch) ao ler um número inteiro positivo?", "Captura entradas inválidas (como letras) sem travar o programa — mas ainda é preciso um if para checar se o número é > 0!", "01_TPA_CSharp"),
    ("Em C#, dada int[,] m = { {1, 2}, {3, 4} }; qual o valor de m[1, 0]?", "7? Não: linha 1, coluna 0 vale 3! (Lembre: base 0, primeiro linha, depois coluna! Se o laço imprimir m[j, i], ele transpõe linhas por colunas).", "01_TPA_CSharp"),
    ("Verdade ou mentira: toda matriz 2D precisa ter o mesmo número de colunas em todas as linhas em qualquer linguagem?", "MENTIRA! Várias linguagens (como C#, Java, JS e Python) aceitam matrizes irregulares (jagged arrays) com linhas de tamanhos diferentes.", "01_TPA_CSharp"),
    ("Quanto vale 17 DIV 5 e quanto vale 17 MOD 5 (17 % 5)?", "17 DIV 5 = 3 (quociente inteiro). 17 % 5 = 2 (resto da divisão). Para testar se N é par: N % 2 == 0.", "01_TPA_CSharp"),
    ("Em Tabela Verdade, qual a regra de ouro do E (&&) e do OU (||)?", "E (&&) só dá V quando TODOS são V (1 F derruba tudo). OU (||) só dá F quando TODOS são F (basta 1 V para dar V; V OU V = V!).", "01_TPA_CSharp"),
    ("Qual a ordem de prioridade nos operadores lógicos?", "1º Parênteses () → 2º Relacionais (>, ==) → 3º NÃO (!) → 4º E (&&) → 5º OU (||).", "01_TPA_CSharp"),
    ("No Casting explícito (int) 8.99 em C#/Java, o resultado é 9 ou 8?", "8! Casting TRUNCA (corta fora a parte decimal) e JAMAIS arredonda!", "01_TPA_CSharp"),
    ("Quais os 4 símbolos geométricos oficiais do Fluxograma?", "Oval/Elipse = Início/Fim; Paralelogramo = Entrada/Saída; Retângulo = Processamento/Contas; Losango = Decisão (Sim/Não).", "01_TPA_CSharp"),
    ("Como calcular 5% e 12% de um valor em código/fluxograma?", "5% = valor * 0.05; 12% = valor * 0.12. Se valor < 100 aplica 0.05; senão (100 ou mais) aplica 0.12.", "01_TPA_CSharp"),
    ("Qual a diferença entre = e == em C#, Java e JavaScript?", "= (um igual) guarda valor na variável (atribuição). == (dois iguais) faz pergunta de comparação (retorna true ou false).", "01_TPA_CSharp"),
    ("Num vetor de tamanho 5 (base 0), quais são os índices válidos?", "0, 1, 2, 3 e 4 (de 0 até N-1). Acessar índice 5 gera erro de limite (Index Out of Bounds).", "01_TPA_CSharp"),
    ("O que faz uma Pilha (LIFO) vs. uma Fila (FIFO)?", "Pilha (LIFO): último a entrar é o primeiro a sair (PUSH/POP no topo, ex.: Ctrl+Z). Fila (FIFO): primeiro a entrar sai primeiro.", "01_TPA_CSharp"),
    ("Qual a diferença entre código-fonte, compilador e executável?", "Código-fonte é o texto humano (.cs/.c); o compilador traduz para código de máquina (0 e 1) gerando o executável (.exe).", "01_TPA_CSharp"),

    # --- 2. PROGRAMAÇÃO WEB I & DESIGN/UX (20 cards) ---
    ("Quais as tags HTML para: parágrafo, linha horizontal, título, pular linha e corpo?", "<p> (parágrafo), <hr> (linha horizontal), <h1>..<h6> (título), <br> (pular linha) e <body> (corpo visível).", "02_Web_Design"),
    ("Qual a função do atributo alt na tag <img> do HTML5?", "Exibir um texto alternativo caso a imagem não carregue e permitir leitura por leitores de tela (acessibilidade).", "02_Web_Design"),
    ("Qual a maneira correta de importar um arquivo JavaScript externo no HTML?", '<script src="arquivo.js"></script> (usa o atributo src, nunca href nem file!).', "02_Web_Design"),
    ("Como centralizar um elemento horizontal e verticalmente usando CSS Flexbox?", "display: flex; justify-content: center; align-items: center;", "02_Web_Design"),
    ("O que é o CSS Box Model e qual a diferença entre padding e margin?", "Todo elemento HTML é uma caixa com content, padding, border e margin. padding = espaço INTERNO (entre texto e borda); margin = espaço EXTERNO.", "02_Web_Design"),
    ("Para que servem Media Queries (@media) no CSS3?", "Criar layouts responsivos aplicando regras CSS diferentes conforme a largura da tela (ex.: @media (max-width: 600px) para celular).", "02_Web_Design"),
    ("Em formulários HTML, quando usar method='POST' vs method='GET'?", "POST envia dados ocultos no corpo HTTP (obrigatório para senhas e cadastros!). GET expõe na URL após ? (usado em buscas).", "02_Web_Design"),
    ("Quais os tipos de <input> mais cobrados em formulários HTML5?", "type='text', type='email' (valida @), type='password' (oculta bolinhas), type='number', type='submit', além de placeholder e required.", "02_Web_Design"),
    ("Qual a diferença entre <div>/<span> e tags semânticas HTML5?", "<div> (bloco) e <span> (linha) são caixas genéricas SEM valor semântico. Semânticas: <header>, <nav>, <main>, <section>, <article>, <footer>.", "02_Web_Design"),
    ("Diferencie <ol>, <ul>, <li>, <tr> e <td> no HTML5.", "<ol> = lista ordenada; <ul> = não ordenada; <li> = item. Em tabelas: <tr> = LINHA (Table Row); <td> = CÉLULA de dado (Table Data).", "02_Web_Design"),
    ("Como abrir um link <a> em uma nova aba?", 'Usando o atributo target="_blank" (ex.: <a href="..." target="_blank">).', "02_Web_Design"),
    ("O que é URI (Uniform Resource Identifier) e qual a diferença de DNS e HTTP?", "URI identifica unicamente um recurso na internet (URL é um tipo de URI). DNS traduz domínio em IP. HTTP é o protocolo de aplicação cliente-servidor.", "02_Web_Design"),
    ("Quais são os tipos de dados primitivos em JavaScript?", "Number (número), String (texto), Boolean (lógico), Undefined, Null, Symbol e BigInt.", "02_Web_Design"),
    ("Em UX Design, o que significa Usabilidade?", "A facilidade, eficiência e satisfação com que o usuário aprende e interage com o produto (não é apenas 'ser bonito'!).", "02_Web_Design"),
    ("Qual a diferença entre RGB/Hexadecimal e CMYK?", "RGB e #RRGGBB = síntese aditiva de LUZ para TELAS. CMYK = síntese subtrativa de TINTA para IMPRESSÃO GRÁFICA.", "02_Web_Design"),
    ("Qual a diferença entre Imagem Vetorial (.SVG) e Bitmap (.JPEG/.PNG)?", "Vetorial (.SVG/.PDF) usa equações matemáticas e NÃO pixela no zoom. Bitmap (.JPEG/.PNG/.BMP) usa grade de pixels e borra ao ampliar.", "02_Web_Design"),
    ("Diferencie .JPEG de .PNG em Design Digital.", ".JPEG tem compressão com perda (ótimo p/ fotos, SEM transparência). .PNG tem compressão sem perda e SUPORTA fundo transparente.", "02_Web_Design"),
    ("Quais são as 5 Leis da Gestalt mais cobradas em interfaces?", "Proximidade (perto = mesmo grupo), Semelhança (iguais = mesma função), Fechamento (cérebro completa falhas), Continuidade e Figura-Fundo.", "02_Web_Design"),
    ("Qual a diferença entre fontes Serifadas, Sem Serifa e Script?", "Serifadas (papel/livros); Sem Serifa (telas/apps); Script (imita letra cursiva — só títulos/convites, péssima para texto longo!).", "02_Web_Design"),
    ("O que é o atributo target='_self' e onde fica o conteúdo visível do HTML?", "target='_self' abre o link na mesma aba (padrão). Todo conteúdo visível fica dentro de <body> (nunca no <head>!).", "02_Web_Design"),

    # --- 3. BANCO DE DADOS I, APS/UML & FUNDAMENTOS (20 cards) ---
    ("Em Banco de Dados, o que é Tabela e o que é Registro (Tupla)?", "Tabela = grade de linhas e colunas sobre um assunto (ex.: lista de alunos). Registro (Tupla) = 1 LINHA completa com dados de um item específico.", "03_BD_APS_FI"),
    ("O que é Chave Primária (PK) e o que é Chave Estrangeira (FK)?", "PK identifica unicamente cada linha e impede registros duplicados (não pode ser NULL). FK é a PK da tabela pai que migra para a tabela filha.", "03_BD_APS_FI"),
    ("O que é o DER (Diagrama Entidade-Relacionamento)?", "Diagrama do Modelo Conceitual (Peter Chen) que ilustra como Entidades (retângulos) se relacionam entre si (losangos) com seus Atributos (elipses).", "03_BD_APS_FI"),
    ("🔁 (Repetiu 2022 e 2024!) O que é um Dicionário de Dados?", "Uma coleção/catálogo de NOMES, ATRIBUTOS e definições sobre elementos de DADOS usados no sistema.", "03_BD_APS_FI"),
    ("O que exige a 1ª Forma Normal (1FN) em bancos relacionais?", "Valores ATÔMICOS (apenas 1 dado por célula — proibido colocar 2 telefones separados por vírgula na mesma célula!).", "03_BD_APS_FI"),
    ("Como resolver relacionamentos 1:N e N:N no Modelo Lógico?", "No 1:N, a Chave Estrangeira (FK) vai sempre para a tabela do lado N. No N:N, cria-se obrigatoriamente uma 3ª Tabela Associativa com ambas as FKs.", "03_BD_APS_FI"),
    ("Diferencie DDL, DML e DQL na linguagem SQL.", "DDL (estrutura): CREATE, ALTER, DROP. DML (dados/linhas): INSERT, UPDATE, DELETE. DQL (consulta): SELECT.", "03_BD_APS_FI"),
    ("O que representa a função de um Diagrama de Casos de Uso (UML)?", "Descreve interações externas entre ATORES (usuários ou sistemas externos) e as FUNCIONALIDADES do sistema.", "03_BD_APS_FI"),
    ("Em um Diagrama de Classes (UML), o que representam as associações?", "A relação estrutural entre classes, indicando como seus objetos se conectam (além de nome, atributos e métodos).", "03_BD_APS_FI"),
    ("🔁 (Repetiu 2022 e 2024!) Qual a definição de Requisitos Funcionais vs. Não Funcionais?", "Funcionais: O QUE o sistema DEVE FAZER (suas funções e informações). Não Funcionais: COMO se comporta (desempenho, segurança, usabilidade, portabilidade).", "03_BD_APS_FI"),
    ("Quais são os 3 principais métodos/frameworks ágeis cobrados em Taboão?", "XP (Extreme Programming), SCRUM (Sprints, PO, SM, Daily 15min) e KANBAN (quadro visual com limite WIP).", "03_BD_APS_FI"),
    ("Qual a principal característica do Modelo em Cascata (Waterfall)?", "Divisão das tarefas em ETAPAS predeterminadas executadas de forma SEQUENCIAL (uma só começa após terminar a anterior).", "03_BD_APS_FI"),
    ("🔁 (Repetiu 2024 e 2025!) Qual número Hexadecimal equivale ao decimal 187?", "BB! Conta: 187 ÷ 16 = 11 (resto 11). Em hexadecimal: A=10, B=11, C=12, D=13, E=14, F=15 → 11 e 11 = BB!", "03_BD_APS_FI"),
    ("Como converter qualquer número decimal (até 255) para Hexadecimal rápido?", "Divida por 16: o quociente é o 1º dígito e o resto é o 2º dígito, trocando 10..15 por A..F (ex.: 100=64₁₆; 250=FA₁₆; 255=FF₁₆).", "03_BD_APS_FI"),
    ("🔁 (Repetiu 2024 e 2025 em Taboão!) Como a banca define Interface CLI?", "Interface monotarefa por linha de comando (Command Line Interface — opera digitando comandos no terminal, diferente da GUI gráfica).", "03_BD_APS_FI"),
    ("O que caracteriza um Sistema Multiusuário?", "Permite vários usuários utilizando aplicações diversificadas simultaneamente no mesmo servidor/sistema operacional.", "03_BD_APS_FI"),
    ("Qual a diferença entre Hardware, Software e Sistema Operacional?", "Hardware = parte física. Software = programas/lógica. Sistema Operacional = intermediário entre usuário/apps e hardware.", "03_BD_APS_FI"),
    ("Qual a vantagem do SSD sobre o HDD tradicional?", "SSD usa chips de memória Flash NAND sem partes mecânicas móveis → muito mais rápido, silencioso e resistente a choques.", "03_BD_APS_FI"),
    ("Software Livre significa necessariamente gratuito (R$ 0)?", "NÃO! Software Livre garante permissão de acessar/modificar o código-fonte (pode ser pago ou grátis). Grátis com código fechado é Freeware!", "03_BD_APS_FI"),
    ("No Git, o que fazem git branch, git diff e git merge?", "branch cria linha paralela isolada; diff compara diferenças linha por linha; merge funde a branch pronta de volta à principal.", "03_BD_APS_FI"),

    # --- 4. PORTUGUÊS & INGLÊS DE TABOÃO (14 cards) ---
    ("O que é Adequação Linguística (Variação Linguística)?", "Não existe 'português certo/errado' absoluto: a fala adequada depende dos interlocutores e do contexto/finalidade comunicativa.", "04_Port_Ingles"),
    ("Como evitar ambiguidade na referenciação ('Joana disse a Maria que ela...')?", "Troque 'ela' por 'esta' (retoma o termo mais próximo: Maria) ou 'aquela' (termo mais distante: Joana).", "04_Port_Ingles"),
    ("Diferencie Variação Diatópica, Diacrônica, Diastrática e Diafásica.", "Diatópica = região; Diacrônica = tempo histórico; Diastrática = grupo social/profissão; Diafásica = grau de formalidade na situação.", "04_Port_Ingles"),
    ("Qual função da linguagem aparece em 'Compre já! Aproveite!'?", "Função Conativa (ou Apelativa) — usa verbos no imperativo para convencer/influenciar o receptor (tipo textual: Injunção).", "04_Port_Ingles"),
    ("Quais são os 5 Tipos Textuais clássicos?", "Narração (fatos no tempo), Descrição (retrato/adjetivos), Exposição (explica neutro), Dissertação Argumentativa (defende tese) e Injunção (instruções/imperativo).", "04_Port_Ingles"),
    ("Qual a diferença entre Paradoxo e Antítese?", "Paradoxo une contradições lógicas impossíveis na mesma ideia ('dói e não se sente'). Antítese apenas aproxima opostos ('dia e noite').", "04_Port_Ingles"),
    ("Qual a diferença entre Hiperônimo e Hipônimo?", "Hiperônimo = categoria geral ('pensador', 'animal'). Hipônimo = termo específico dentro dela ('Aristóteles', 'cachorro').", "04_Port_Ingles"),
    ("Barroco: diferencie Cultismo de Conceptismo (Pegadinha clássica!).", "Cultismo = jogo de PALAVRAS/forma rebuscada. Conceptismo = jogo de IDEIAS/raciocínio lógico (Padre Antônio Vieira).", "04_Port_Ingles"),
    ("Concordância Nominal: qual o erro em 'Os alunos estavam ansiosos e atento'?", "'Os alunos' está no plural → ambos os adjetivos devem concordar no plural: 'ansiosos e ATENTOS'.", "04_Port_Ingles"),
    ("Inglês: como formar o Present Perfect (afirmativa e negativa)?", "Sujeito + have/has + Particípio Passado (ex.: 'She has danced' | 'The students haven't studied'). Atenção: plural usa HAVE/HAVEN'T!", "04_Port_Ingles"),
    ("Inglês: o que significam os Phrasal Verbs 'save up', 'give up' e 'turn off'?", "save up = economizar/poupar; give up = desistir; turn off = desligar (ex.: turn off the lights to save up energy).", "04_Port_Ingles"),
    ("Inglês: qual é o superlativo irregular de 'bad' e de 'good'?", "bad → worse → THE WORST (o pior). good → better → THE BEST (o melhor).", "04_Port_Ingles"),
    ("Falsos cognatos em Inglês: o que significam 'actually', 'data' e 'pretend'?", "actually = na verdade (NÃO atualmente); data = dados (NÃO datas); pretend = fingir (NÃO pretender).", "04_Port_Ingles"),
    ("Quais as duas vertentes do Quinhentismo (1500) no Brasil?", "Literatura Informativa (Carta de Caminha descrevendo a terra) e Literatura Jesuítica/Catequética (José de Anchieta).", "04_Port_Ingles"),

    # --- 5. INV. CIENTÍFICA, EMPREEND., ARTE, ED. FÍSICA & HISTÓRIA (14 cards) ---
    ("Qual a ordem correta das etapas do Método Científico?", "1. Definir problema / Observação → 2. Hipótese → 3. Experimento controlado → 4. Coleta e Análise de Dados → 5. Conclusão.", "05_Hum_Aprof"),
    ("Qual a diferença entre Pesquisa Qualitativa e Pesquisa Quantitativa?", "Qualitativa = busca compreensão aprofundada e subjetiva (entrevistas/análises). Quantitativa = sustenta-se em números, medições e estatísticas.", "05_Hum_Aprof"),
    ("O que avalia a Análise SWOT (FOFA) no Empreendedorismo?", "Ambiente INTERNO: Forças (S) e Fraquezas (W). Ambiente EXTERNO: Oportunidades (O) e Ameaças (T).", "05_Hum_Aprof"),
    ("Como Resiliência e Criatividade atuam juntas no perfil empreendedor?", "Resiliência permite persistir diante de falhas/obstáculos; Criatividade permite reformular e criar soluções inovadoras.", "05_Hum_Aprof"),
    ("Arte (Processos Criativos): qual a diferença entre TEMA e TÉCNICA?", "Tema = assunto/ideia inspiradora (ex.: natureza). Técnica = procedimento prático usado para construir a obra (ex.: colagem, xilogravura).", "05_Hum_Aprof"),
    ("Educação Física: quais são os 3 tipos de contração muscular?", "Concêntrica (músculo encurta vencendo carga), Excêntrica (músculo alonga controlando) e Isométrica (tensão sem movimento/mudança de tamanho).", "05_Hum_Aprof"),
    ("Qual a principal função do Aparelho Locomotor?", "Ossos, articulações e músculos atuam EM CONJUNTO para permitir que o corpo se locomova ou desloque membros.", "05_Hum_Aprof"),
    ("O que são Esportes de Invasão (e quais NÃO são)?", "Invasão: 2 equipes invadindo território para pontuar na meta (futsal, basquete, handebol, rúgbi). Vôlei, tênis, badminton, beisebol e bocha NÃO são!", "05_Hum_Aprof"),
    ("Como era dividida a sociedade feudal na Idade Média?", "Sociedade estamental em 3 ordens: Clero (legitimava a ordem), Nobreza (donos das terras/guerreiros) e Servos (trabalhavam e pagavam corveia, talha e banalidades).", "05_Hum_Aprof"),
    ("Como os médicos árabes influenciaram a Europa medieval?", "Preservaram e ampliaram obras clássicas gregas; seus tratados traduzidos para o latim foram estudados nas universidades europeias (sécs. XII–XV).", "05_Hum_Aprof"),
    ("Qual a principal característica do Renascimento Cultural (sécs. XIV–XVI)?", "Resgate da cultura greco-romana, antropocentrismo, valorização da razão humana e avanço das ciências (matemática e astronomia).", "05_Hum_Aprof"),
    ("Quem podia votar na Democracia Ateniense clássica?", "Apenas homens adultos, livres e nativos de Atenas (excluía mulheres, escravizados e estrangeiros).", "05_Hum_Aprof"),
    ("Diferencie Paleolítico de Revolução Neolítica na Pré-História.", "Paleolítico = nômade, caça/coleta, pedra lascada, fogo. Neolítico = sedentarismo, agricultura e domesticação de animais.", "05_Hum_Aprof"),
    ("O que é Biorremediação e qual o papel da Adubação Verde com leguminosas?", "Biorremediação usa microrganismos que metabolizam poluentes em substâncias atóxicas. Leguminosas fixam nitrogênio reduzindo uso de fertilizantes químicos.", "05_Hum_Aprof"),

    # --- 6. MATEMÁTICA, FÍSICA & QUÍMICA DE TABOÃO (16 cards) ---
    ("🔁 (Repetiu 2021 e 2024!) Como resolver problemas de Diagrama de Venn (ex.: 92 sim 1ª, 80 sim 2ª, 35 ambas, 33 não)?", "Comece SEMPRE pelo miolo (35)! Só 1ª = 92-35=57; Só 2ª = 80-35=45; Ambas = 35; Nenhuma = 33. Total = 57+45+35+33 = 170!", "06_Exatas"),
    ("🔁 (Repetiu 2021 e 2024!) Quais as 2 propriedades de Logaritmo mais cobradas em Taboão?", "Produto vira soma: log(m·n) = log m + log n. Potência desce multiplicando: log(m^k) = k · log m. Logo log(m²·n³) = 2·log m + 3·log n!", "06_Exatas"),
    ("🔁 (Repetiu 2021 e 2024!) Qual a fórmula do Termo Geral da Progressão Aritmética (PA)?", "aₙ = a₁ + (n - 1) · r. Ex.: depósitos de 40, 50, 60... até 520: 520 = 40 + (n-1)·10 → 480/10 = n-1 → n = 49 meses!", "06_Exatas"),
    ("Conjuntos Numéricos: Dízima periódica (0,333...) é Racional ou Irracional?", "RACIONAL (ℚ), pois toda dízima periódica vira fração (1/3)! Irracionais (𝕀) são π e raízes não exatas (√2, √3).", "06_Exatas"),
    ("Princípio da Contagem com o dígito ZERO: quantos nº de 3 algarismos distintos com {0,1,2,3,4,5}?", "O zero NÃO pode ir na 1ª casa! Logo: 5 opções (1..5) × 5 opções (volta o 0) × 4 opções = 100 números.", "06_Exatas"),
    ("Função Quadrática f(x)=ax²+bx+c: o que indicam 'a' e 'Δ = b²-4ac'?", "a > 0: boca p/ cima (mínimo); a < 0: boca p/ baixo (máximo). Δ > 0: 2 raízes reais; Δ = 0: 1 raiz; Δ < 0: nenhuma raiz real.", "06_Exatas"),
    ("Quais as fórmulas de área de Retângulo, Triângulo, Trapézio e o macete 3-4-5?", "Retângulo = b·h; Triângulo = (b·h)/2; Trapézio = [(B+b)·h]/2. Catetos 30 e 40 → hipotenusa 50 (múltiplo de 3-4-5)!", "06_Exatas"),
    ("🔁 (Repetiu 2021 e 2025!) Lei Geral dos Gases em ciclos p×V: como achar a temperatura máxima?", "Use p·V / T = constante! A temperatura é MÁXIMA no ponto do gráfico com o maior produto p × V (ex.: p₀ e 2V₀ dobra T: 300 K → 600 K!).", "06_Exatas"),
    ("Física — Cinemática MRUV partindo do repouso (v₀=0): fórmulas de velocidade e distância?", "v = a · t  e  ΔS = (a · t²) / 2. E pela 2ª Lei de Newton: Força F = m · a (onde a = Δv / Δt).", "06_Exatas"),
    ("Física — Lente Convergente (Equação de Gauss): objeto entre F e C gera qual imagem?", "1/f = 1/p + 1/p' e A = -p'/p. Objeto entre Foco (F) e Ponto Antiprincipal (C=2f) forma imagem REAL, INVERTIDA e MAIOR!", "06_Exatas"),
    ("Física — Óptica das Cores: por que um tomate vermelho sob luz verde pura parece PRETO?", "Porque o pigmento vermelho absorve o verde e não recebe luz vermelha para refletir — sem luz refletida, vemos PRETO!", "06_Exatas"),
    ("Química — Qual modelo atômico explica as cores emitidas por transições eletrônicas entre camadas?", "Modelo de Niels Bohr! Quando o elétron salta de uma camada mais externa para uma interna, libera energia em forma de luz colorida.", "06_Exatas"),
    ("Química — Diferencie reação Exotérmica (ex.: combustão) de Endotérmica + Lei de Lavoisier.", "Exotérmica LIBERA calor (combustão). Endotérmica ABSORVE calor. Lavoisier: massa dos reagentes = massa dos produtos (nada se perde).", "06_Exatas"),
    ("Química — Em oxirredução (ex.: CO → CO₂), quem oxida é agente oxidante ou redutor?", "Quem OXIDA (aumenta NOX, ex.: C de +2 para +4) perde elétrons e atua como AGENTE REDUTOR! Quem reduz atua como agente oxidante.", "06_Exatas"),
    ("Química — Como diferenciar Metal, Iônico e Molecular pela condutividade elétrica?", "Metal conduz SÓLIDO (elétrons livres). Iônico NÃO conduz sólido, só líquido/em água (íons livres). Molecular/Covalente NÃO conduz.", "06_Exatas"),
    ("Química — Metais Alcalinos (Família 1A: Sódio, Césio) e Massa Molar (C=12, H=1, O=16)?", "Família 1A reage fortemente com água liberando gás H₂. Massa Molar: Etanol C₂H₅OH = 2(12)+6(1)+16 = 46 u; Ácido Acético C₂H₄O₂ = 60 u.", "06_Exatas"),
]

TABOAO_PAIRS = [
    {"term": "187 em Hexadecimal", "def": "BB (187 ÷ 16 = 11 resto 11)"},
    {"term": "Interface CLI (Taboão)", "def": "Monotarefa por linha de comando"},
    {"term": "&& em C#", "def": "Operador lógico E (ambas verdadeiras)"},
    {"term": "Breakpoint", "def": "Pausa código para inspecionar variáveis"},
    {"term": "try / catch", "def": "Captura exceções/erros de entrada"},
    {"term": "do / while", "def": "Executa pelo menos 1 vez (pós-teste)"},
    {"term": "Flexbox centralizar", "def": "display:flex; justify-content & align-items:center"},
    {"term": "<img alt='...'>", "def": "Texto alternativo se imagem não carregar"},
    {"term": "<script src='a.js'>", "def": "Importa arquivo JavaScript externo"},
    {"term": "<hr> e <br>", "def": "Linha horizontal e quebra de linha"},
    {"term": "Chave Primária (PK)", "def": "Identifica linha única e impede duplicatas"},
    {"term": "Chave Estrangeira (FK)", "def": "PK da tabela pai que migra para a filha"},
    {"term": "Dicionário de Dados", "def": "Coleção de nomes, atributos e definições"},
    {"term": "DER", "def": "Diagrama de Entidades e Relacionamentos"},
    {"term": "Casos de Uso (UML)", "def": "Interações entre atores e funcionalidades"},
    {"term": "Diagrama de Classes", "def": "Associações estruturais entre classes"},
    {"term": "Usabilidade (UX)", "def": "Facilidade de aprender e interagir com o produto"},
    {"term": "Pesquisa Qualitativa", "def": "Compreensão aprofundada e subjetiva"},
    {"term": "Contração Isométrica", "def": "Tensão muscular sem mudar comprimento"},
    {"term": "Present Perfect", "def": "have/has + particípio (ex.: has danced)"},
    {"term": "log(m² · n³)", "def": "2·log(m) + 3·log(n)"},
    {"term": "Gás ideal (p₀, 2V₀)", "def": "Temperatura dobra (300 K → 600 K)"},
]

TABOAO_VF = [
    {"id": 1, "area": "tpa_csharp", "stmt": "Em C#, o operador lógico && retorna verdadeiro apenas quando ambas as condições são verdadeiras.", "truth": True, "why": "Exatamente! && é o operador E (AND) em C#, C, Java e JavaScript."},
    {"id": 2, "area": "tpa_csharp", "stmt": "No laço do/while em C#, se a condição inicial já for falsa, o bloco interno executa 0 vezes.", "truth": False, "why": "FALSO! do/while é pós-teste: executa PELO MENOS 1 VEZ antes de avaliar a condição no final."},
    {"id": 3, "area": "tpa_csharp", "stmt": "Um breakpoint durante a depuração serve para pausar o programa em uma linha marcada e inspecionar variáveis em tempo real.", "truth": True, "why": "VERDADEIRO! Caiu literal na prova de Taboão 05/12/2025 (Q36)."},
    {"id": 4, "area": "tpa_csharp", "stmt": "Em C#, esquecer um ponto e vírgula (;) no fim da instrução é ignorado pelo compilador e o programa roda normalmente.", "truth": False, "why": "FALSO! Gera erro de sintaxe: o compilador impede a compilação e destaca a linha do erro (Taboão 2024 Q24)."},
    {"id": 5, "area": "tpa_csharp", "stmt": "Usar try/catch já garante sozinho que um número digitado é positivo, dispensando qualquer if (n > 0).", "truth": False, "why": "FALSO! try/catch captura erros de formato (como letras), mas ainda precisamos de um if para verificar se n > 0 (Taboão 2025 Q35)."},
    {"id": 6, "area": "tpa_csharp", "stmt": "Em todas as linguagens de programação, uma matriz bidimensional obrigatoriamente precisa ter o mesmo número de colunas em todas as linhas.", "truth": False, "why": "FALSO! Linguagens como C#, Java, JS e Python aceitam matrizes irregulares (jagged arrays) com linhas de tamanhos diferentes (Taboão 2025 Q37)."},
    {"id": 7, "area": "tpa_csharp", "stmt": "Na linguagem C#, (int) 9.99 trunca o número para 9 sem arredondar para 10.", "truth": True, "why": "VERDADEIRO! Casting explícito sempre trunca (corta) a parte decimal."},
    {"id": 8, "area": "tpa_csharp", "stmt": "Na Tabela Verdade, o resultado de (Verdadeiro OU Verdadeiro) é Falso porque o OU exclui os dois juntos.", "truth": False, "why": "FALSO! O OU lógico da computação (||) é inclusivo: basta pelo menos um V, logo V OU V = VERDADEIRO!"},
    {"id": 9, "area": "tpa_csharp", "stmt": "Dada int[,] m = {{1,2},{3,4}}; imprimir m[j, i] com i variando fora e j variando dentro exibe '1 3' na primeira linha e '2 4' na segunda.", "truth": True, "why": "VERDADEIRO! Caiu literal na Q22 de Taboão 2024: trocar [i,j] por [j,i] transpõe a matriz!"},
    {"id": 10, "area": "tpa_csharp", "stmt": "No fluxograma oficial, o Losango representa cálculos aritméticos e o Retângulo representa decisões Sim/Não.", "truth": False, "why": "FALSO! Invertido: Losango = Decisão (Sim/Não); Retângulo = Processamento/Cálculos."},
    {"id": 11, "area": "web_design", "stmt": "As tags HTML para parágrafo, linha horizontal, título, pular linha e corpo são respectivamente <p>, <hr>, <h2>, <br> e <body>.", "truth": True, "why": "VERDADEIRO! Caiu literal na Q26 de Taboão 2025."},
    {"id": 12, "area": "web_design", "stmt": "O atributo alt na tag <img> define a largura em pixels da imagem na página.", "truth": False, "why": "FALSO! alt define o texto alternativo exibido caso a imagem não carregue e usado na acessibilidade (Taboão 2024 Q32)."},
    {"id": 13, "area": "web_design", "stmt": "Para importar um arquivo JavaScript externo no HTML usa-se <script src='arquivo.js'></script>.", "truth": True, "why": "VERDADEIRO! Nunca usa href nem file para <script> (Taboão 2024 Q35)."},
    {"id": 14, "area": "web_design", "stmt": "No CSS Flexbox, display: flex; justify-content: center; align-items: center; centraliza um elemento horizontal e verticalmente.", "truth": True, "why": "VERDADEIRO! Caiu literal na Q36 de Taboão 2024."},
    {"id": 15, "area": "web_design", "stmt": "No CSS Box Model, padding é o espaço externo que afasta caixas vizinhas e margin é o espaço interno entre o texto e a borda.", "truth": False, "why": "FALSO! Invertido: padding é INTERNO (conteúdo até a borda); margin é EXTERNO (fora da borda)."},
    {"id": 16, "area": "web_design", "stmt": "URI significa 'Identificador de Recursos Unilateral' e só funciona em servidores locais.", "truth": False, "why": "FALSO! URI = Uniform Resource Identifier (Identificador UNIFORME e único de recurso na internet — Taboão 2025 Q25 e Q27)."},
    {"id": 17, "area": "web_design", "stmt": "Em UX Design, o termo 'usabilidade' refere-se à facilidade com que o usuário aprende e interage com o produto.", "truth": True, "why": "VERDADEIRO! Caiu literal na Q30 de Taboão 2025."},
    {"id": 18, "area": "web_design", "stmt": "Em formulários HTML, senhas devem ser enviadas com method='GET' para ficarem ocultas no corpo da requisição.", "truth": False, "why": "FALSO! GET expõe os dados na URL! Senhas devem usar obrigatoriamente method='POST'."},
    {"id": 19, "area": "web_design", "stmt": "As tags <div> e <span> são tags semânticas do HTML5.", "truth": False, "why": "FALSO! São contêineres genéricos sem valor semântico (semânticas são <header>, <nav>, <main>, <article>, <footer>)."},
    {"id": 20, "area": "web_design", "stmt": "No HTML, <tr> cria uma linha de tabela e <td> cria uma célula de dado.", "truth": True, "why": "VERDADEIRO! TR = Table Row (linha); TD = Table Data (célula)."},
    {"id": 21, "area": "web_design", "stmt": "Imagens vetoriais (.SVG) são formadas por equações matemáticas e não perdem qualidade ao dar zoom.", "truth": True, "why": "VERDADEIRO! Já .JPEG e .PNG são bitmap (pixels) e serrilham no zoom."},
    {"id": 22, "area": "web_design", "stmt": "O padrão CMYK é usado em telas de celulares e o RGB é usado em gráficas para impressão em papel.", "truth": False, "why": "FALSO! Invertido: RGB/Hex = telas (luz); CMYK = impressão gráfica (tinta)."},
    {"id": 23, "area": "bd_aps_fi", "stmt": "Em um banco de dados, um 'registro' equivale a uma linha completa com informações sobre um item específico.", "truth": True, "why": "VERDADEIRO! Caiu literal na Q39 de Taboão 2025."},
    {"id": 24, "area": "bd_aps_fi", "stmt": "A Chave Primária (Primary Key) impede a existência de registros duplicados e nunca pode ser nula.", "truth": True, "why": "VERDADEIRO! Caiu na Q38 de Taboão 2024."},
    {"id": 25, "area": "bd_aps_fi", "stmt": "A Chave Estrangeira (Foreign Key) é a chave primária da tabela pai que migra para a tabela filha no relacionamento.", "truth": True, "why": "VERDADEIRO! No relacionamento 1:N, a FK sempre vai para o lado N."},
    {"id": 26, "area": "bd_aps_fi", "stmt": "Guardar dois números de telefone separados por vírgula na mesma célula atende à 1ª Forma Normal (1FN).", "truth": False, "why": "FALSO! Viola diretamente a 1FN, que exige valores atômicos (1 única informação por célula)."},
    {"id": 27, "area": "bd_aps_fi", "stmt": "Um Dicionário de Dados é uma coleção de nomes, atributos e definições sobre os elementos de dados do sistema.", "truth": True, "why": "VERDADEIRO! Repetiu literalmente em Taboão 2022 e 2024!"},
    {"id": 28, "area": "bd_aps_fi", "stmt": "O Diagrama de Casos de Uso descreve as interações entre atores e funcionalidades do sistema.", "truth": True, "why": "VERDADEIRO! Caiu na Q29 de Taboão 2025."},
    {"id": 29, "area": "bd_aps_fi", "stmt": "No Diagrama de Classes UML, associações representam o tempo de resposta em segundos do servidor.", "truth": False, "why": "FALSO! Representam a relação estrutural entre classes, indicando como elas se conectam (Taboão 2025 Q28/Q31)."},
    {"id": 30, "area": "bd_aps_fi", "stmt": "XP, Scrum e Kanban são metodologias/frameworks ágeis, enquanto o Modelo em Cascata executa etapas de forma sequencial.", "truth": True, "why": "VERDADEIRO! Caiu em Taboão 2024 Q27 e Q28."},
    {"id": 31, "area": "bd_aps_fi", "stmt": "Requisitos funcionais definem o que o sistema deve fazer, ou seja, suas funções e informações.", "truth": True, "why": "VERDADEIRO! Repetiu literalmente em Taboão 2022 e 2024!"},
    {"id": 32, "area": "bd_aps_fi", "stmt": "O número decimal 187 corresponde a BB no sistema Hexadecimal.", "truth": True, "why": "VERDADEIRO! 187 ÷ 16 = 11 (B) resto 11 (B) → BB! Caiu em 2024 E 2025!"},
    {"id": 33, "area": "bd_aps_fi", "stmt": "Na prova de Taboão da Serra, uma interface CLI é caracterizada como interface monotarefa por linha de comando.", "truth": True, "why": "VERDADEIRO! Repetiu idêntica em Taboão 2024 (Q30) e 2025 (Q32)!"},
    {"id": 34, "area": "bd_aps_fi", "stmt": "Todo Software Livre é obrigatoriamente gratuito (R$ 0) e tem código-fonte fechado.", "truth": False, "why": "FALSO! Software Livre exige código-fonte aberto e pode ser comercializado! Grátis e fechado é Freeware."},
    {"id": 35, "area": "bd_aps_fi", "stmt": "Na linguagem SQL, CREATE/ALTER/DROP pertencem à DDL e INSERT/UPDATE/DELETE pertencem à DML.", "truth": True, "why": "VERDADEIRO! E SELECT pertence à DQL (consulta)."},
    {"id": 36, "area": "port_ing", "stmt": "Na Sociolinguística, falar 'errado' significa usar qualquer variedade regional diferente da norma culta.", "truth": False, "why": "FALSO! O conceito central é adequação linguística conforme interlocutores e contexto comunicativo (Taboão 2022 e 2025)."},
    {"id": 37, "area": "port_ing", "stmt": "Na frase 'Joana disse a Maria que esta precisava estudar', o pronome 'esta' elimina a ambiguidade retomando 'Maria'.", "truth": True, "why": "VERDADEIRO! 'Esta' retoma o referente mais próximo (Taboão 2025 Q3)."},
    {"id": 38, "area": "port_ing", "stmt": "Em 'Compre já! Oferta imperdível!', predomina a função conativa (apelativa) da linguagem.", "truth": True, "why": "VERDADEIRO! Busca convencer/influenciar o receptor usando imperativo (Taboão 2024 Q3)."},
    {"id": 39, "area": "port_ing", "stmt": "No Barroco, Cultismo é o jogo lógico de ideias e Conceptismo é o jogo rebuscado de palavras.", "truth": False, "why": "FALSO! Pegadinha clássica invertida: CONceptismo = ideias/conceitos; CULtismo = culto à palavra/forma!"},
    {"id": 40, "area": "port_ing", "stmt": "Em Inglês, a frase 'The students haven't studied the chapter' está correta no Present Perfect.", "truth": True, "why": "VERDADEIRO! Plural usa haven't + particípio studied (Taboão 2025 Q6)."},
    {"id": 41, "area": "port_ing", "stmt": "Em Inglês, 'save up energy' significa desistir de usar energia, e 'actually' significa atualmente.", "truth": False, "why": "FALSO! save up = economizar/poupar; give up = desistir; actually = na verdade (falso cognato!)."},
    {"id": 42, "area": "ciencias_hum", "stmt": "A pesquisa qualitativa busca uma compreensão aprofundada e subjetiva, enquanto a quantitativa se sustenta em números.", "truth": True, "why": "VERDADEIRO! Caiu na Q24 de Taboão 2025."},
    {"id": 43, "area": "ciencias_hum", "stmt": "Na pesquisa científica, o pesquisador deve primeiro coletar os dados antes de definir qual é o problema de pesquisa.", "truth": False, "why": "FALSO! Primeiro se define o problema de pesquisa / observação (Taboão 2025 Q23)."},
    {"id": 44, "area": "ciencias_hum", "stmt": "Em processos criativos na Arte, 'colagem' é exemplo de técnica, enquanto 'exploração da natureza' é exemplo de tema.", "truth": True, "why": "VERDADEIRO! Caiu em Taboão 2025 Q7 e Q8."},
    {"id": 45, "area": "ciencias_hum", "stmt": "Os três tipos clássicos de contração muscular são concêntrica, excêntrica e isométrica.", "truth": True, "why": "VERDADEIRO! Caiu na Q9 de Taboão 2025."},
    {"id": 46, "area": "ciencias_hum", "stmt": "Voleibol, badminton e bocha são classificados como esportes de invasão.", "truth": False, "why": "FALSO! Esportes de invasão são futsal, basquete, handebol, rúgbi, polo aquático etc. (Taboão 2024 Q19)."},
    {"id": 47, "area": "ciencias_hum", "stmt": "Na Idade Média feudal, os servos eram isentos de taxas e obrigações perante os senhores feudais.", "truth": False, "why": "FALSO! Os servos sustentavam a nobreza pagando pesados tributos como corveia, talha e banalidades (Taboão 2025 Q19)."},
    {"id": 48, "area": "ciencias_hum", "stmt": "Na democracia ateniense clássica, mulheres e escravizados participavam normalmente da votação na Assembleia.", "truth": False, "why": "FALSO! Apenas homens adultos, livres e nativos de Atenas votavam (Taboão 2024 Q5)."},
    {"id": 49, "area": "exatas", "stmt": "Dízimas periódicas como 0,333... pertencem ao conjunto dos números Irracionais (𝕀).", "truth": False, "why": "FALSO! Toda dízima periódica pode virar fração (1/3), logo pertence aos RACIONAIS (ℚ)!"},
    {"id": 50, "area": "exatas", "stmt": "Pelas propriedades dos logaritmos, log_a(m² · n³) equivale a 2·log_a(m) + 3·log_a(n).", "truth": True, "why": "VERDADEIRO! Produto vira soma e expoente desce multiplicando."},
    {"id": 51, "area": "exatas", "stmt": "Em uma PA começando em 40 com razão 10, o valor 520 ocorre exatamente no 49º termo.", "truth": True, "why": "VERDADEIRO! 520 = 40 + (n-1)·10 → 480 = 10(n-1) → n = 49 (caiu em 2021 e 2024!)."},
    {"id": 52, "area": "exatas", "stmt": "Um gás ideal em (p₀, V₀, 300 K) expandido isobaricamente até (p₀, 2V₀) atinge 600 K.", "truth": True, "why": "VERDADEIRO! Com pressão constante, volume dobrado dobra a temperatura em Kelvin (caiu em 2021 e 2025!)."},
    {"id": 53, "area": "exatas", "stmt": "Um veículo que parte do repouso com aceleração 2 m/s² atinge 6 m/s e percorre 9 m após 3 segundos.", "truth": True, "why": "VERDADEIRO! v = 2×3 = 6 m/s e ΔS = (2×3²)/2 = 9 m (Taboão 2024 Q13)."},
    {"id": 54, "area": "exatas", "stmt": "O modelo atômico de Niels Bohr explica as diferentes cores emitidas por elementos pelas transições eletrônicas entre camadas.", "truth": True, "why": "VERDADEIRO! Caiu na Q17 de Taboão 2025."},
    {"id": 55, "area": "exatas", "stmt": "A combustão é uma reação endotérmica porque absorve calor do ambiente.", "truth": False, "why": "FALSO! A combustão LIBERA calor, portanto é EXOTÉRMICA (Taboão 2024 Q17)."},
    {"id": 56, "area": "exatas", "stmt": "Compostos iônicos (como sal NaCl) conduzem eletricidade perfeitamente no estado sólido.", "truth": False, "why": "FALSO! Sólido tem íons presos na rede cristalina; iônico só conduz líquido/fundido ou dissolvido em água! Quem conduz sólido é METAL."},
]
