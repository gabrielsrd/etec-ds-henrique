# Gabarito Dissecado das Provas Reais (Fundação FAT / Etec)

Este arquivo reúne a dissecação completa das **3 provas oficiais** incluídas nesta pasta:
1. **Prova 1 (Principal):** Desenvolvimento de Sistemas — Vestibulinho 1º SEM/2025 (aplicada em 15/12/2024) — **30 questões**.
2. **Prova 2 (Irmã Gêmea do mesmo dia):** Informática para Internet — Vestibulinho 1º SEM/2025 (aplicada em 15/12/2024) — **27 questões inéditas** (as questões 01 a 03 são idênticas às da Prova 1).
3. **Prova 3 (Histórica FAT):** Desenvolvimento de Sistemas — Vestibulinho 1º SEM/2019 (aplicada em 16/12/2018) — **30 questões**.

> **Os 4 Moldes da Fundação FAT (Legenda usada abaixo):**
> - **[Molde 1 — Tabela `I, II, III`]**: Quadro com 3 afirmações onde a banca ou valida todas, ou **inverte duas definições**, ou coloca um **absurdo técnico** em um dos itens.
> - **[Molde 2 — Lista com Intruso]**: Pede uma lista válida de ferramentas, protocolos ou formatos; as alternativas erradas escondem um **intruso**.
> - **[Molde 3 — Definição Direta]**: O próprio texto explica o conceito e a última linha pede o nome oficial exato.
> - **[Molde 4 — Micro-Execução]**: Conta ou simulação curta (matriz, fatorial, binário, pilha, tabela verdade, teste de mesa).

---

## Parte 1: Prova de Desenvolvimento de Sistemas (1º SEM/2025)

**Gabarito Oficial:**
`01-B | 02-E | 03-D | 04-B | 05-D | 06-B | 07-A | 08-C | 09-C | 10-D | 11-B | 12-E | 13-A | 14-D | 15-A | 16-E | 17-E | 18-A | 19-B | 20-B | 21-D | 22-E | 23-B | 24-E | 25-A | 26-D | 27-B | 28-B | 29-C | 30-E`

### Inglês Técnico e Soft Skills (Q01–Q03)
- **Q01 — Gabarito: (B)** *(Molde 3 — Leitura Direta)*
  - **Por que está certa:** O texto diz *"tend to be reflective, independent, and competent"* e *"become better problem-solvers compared to those who simply memorize details"*.
  - **Pegadinhas:** (A) inverte para *"memorização de detalhes"* (o texto opõe critical thinking a memorizar); (C) *"cuidados suaves"* traduz literalmente *"soft skill"* ao pé da letra; (D) *"imediatistas"*; (E) *"cálculos primários"*.
- **Q02 — Gabarito: (E)** *(Molde 3 — Vocabulário em Contexto)*
  - **Por que está certa:** *"reflect on outcomes"* = refletir sobre **resultados** (sinônimo de *results*, citado na frase seguinte).
  - **Pegadinhas:** (A) *"saídas"* confunde *outcomes* com *outputs/exits*.
- **Q03 — Gabarito: (D)** *(Molde 3 — Leitura de Infográfico)*
  - **Por que está certa:** Item 1 (*Observation*): *"predict opportunities, problems and solutions"* (antecipação de problemas). Item 4 (*Communication*): *"Sharing and receiving information"* (compartilhamento de informações).
  - **Pegadinha clássica:** (A) *"análise de datas"* — falso cognato clássico traduzindo **data** (dados) como "datas"! (B) *"falsa informação"*; (C) *"intérpretes"* (confundindo com *interpreting*); (E) *"anotação" / "inexperientes"*.

### Ética e Cidadania Organizacional (Q04–Q06)
*(Todas copiadas literalmente das 3 Competências do Plano de Curso oficial da Etec!)*
- **Q04 — Gabarito: (B)** *(Molde 3 — Bem Comum)*
  - **Por que está certa:** João coletou e distribuiu alimentos para famílias vulneráveis (benefício coletivo sem interesse próprio).
  - **Pegadinhas:** (A) Maria doou *"para liberar espaço em casa"*; (C) Lucas comprou carro por status; (D) Ana quer aumento próprio; (E) João faz voluntariado *"para postagens em redes sociais"*.
- **Q05 — Gabarito: (D)** *(Molde 3 — Relações Trabalhistas e de Consumo)*
  - **Por que está certa:** Consumo consciente, produtos sustentáveis e de baixo impacto ambiental. Todas as demais prejudicam consumidores ou funcionários (propaganda enganosa, demissão em massa sem impacto social, negligência trabalhista, ignorar qualidade de vida).
- **Q06 — Gabarito: (B)** *(Molde 3 — Direito Constitucional e Legislação Ambiental)*
  - **Por que está certa:** Políticas públicas garantindo participação das comunidades locais nas decisões sobre recursos naturais. Todas as outras violam leis ambientais.

### Programação, Algoritmos e Engenharia de Software (Q07–Q10, Q19, Q22, Q23)
- **Q07 — Gabarito: (A)** *(Molde 2 — Lista com Intruso)*
  - **Por que está certa:** `Laravel` (PHP), `React Native` (Mobile), `Angular` (JavaScript) e `Bootstrap` (UI/CSS).
  - **Intrusos e Inversões:** (B) e (D) trazem **Adobe Creative Cloud** (suíte de design/edição); (C) e (D) trazem **Creative Commons** (tipo de licença); (E) **inverteu** as descrições colocando React Native como UI, Angular como Mobile e Bootstrap como JS.
- **Q08 — Gabarito: (C) — I e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - **Item I (V):** Conversão Implícita (*Type Coercion*) feita automaticamente quando compatível sem perda (ex.: `int` para `float`).
  - **Item II (F):** *"Conversão Normal"* **não existe** na teoria de tipos — nome inventado para confundir!
  - **Item III (V):** Conversão Explícita (*Casting*) forçada manualmente pelo programador (`int()`, `float()`, `str()`).
- **Q09 — Gabarito: (C)** *(Molde 3 — Definição Direta)*
  - **Por que está certa:** Seguir o fluxo anotando cada alteração de variável instrução por instrução é **Executar Linha a Linha** (etapa central do teste de mesa).
- **Q10 — Gabarito: (D)** *(Molde 4 — Micro-Execução)*
  - **Cálculo:** Matriz `M = [[1, 3, 5], [2, 4, 8], [1, 1, 1]]`.
    - Diagonal principal = elementos onde `linha == coluna` (`M[0][0]`, `M[1][1]`, `M[2][2]`):
      - `M[0][0] = 1`
      - `M[1][1] = 4`
      - `M[2][2] = 1`
    - Soma: `1 + 4 + 1 = 6`.
  - **Pegadinha:** `5 + 4 + 1 = 10` (alternativa E) é a **diagonal secundária**! Não confunda!
- **Q19 — Gabarito: (B) — I e II corretas** *(Molde 1 — Tabela `I, II, III`)*
  - **Item I (V):** Editores de Código (VS Code, Sublime Text, Atom — realce de sintaxe, autocompletar, extensões).
  - **Item II (V):** Editores WYSIWYG (Dreamweaver, Wix — arrastar e soltar visualmente).
  - **Item III (F):** Diz que **IDEs** são ferramentas básicas como *Notepad* ou *TextEdit* sem recursos avançados! Na verdade, Notepad/TextEdit são **editores de texto simples**; IDEs (Eclipse, Visual Studio, IntelliJ) são ambientes completos com compilador/depurador.
- **Q22 — Gabarito: (E) — I, II e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - **Itens I, II e III (V):** Definições corretas de *build* (compilação, testes, minificação, pacotes finais), *bundling* (empacotar JS/CSS/imagens em menos arquivos para reduzir requisições HTTP) e qualidade (testes automatizados).
- **Q23 — Gabarito: (B)** *(Molde 3 — Licenciamento)*
  - **Por que está certa:** A frase *"cujas licenças promovem a colaboração e a transparência"* e *"acesso ao código-fonte, permitindo que modifiquem e redistribuam sob determinadas condições"* corresponde na terminologia da banca a **Licenças de Código Aberto (*Open Source*)**. *(Nota: na prova de 2022 M-Tec, Software Livre enfatiza a liberdade ética/permissão de alterar mesmo se pago ou gratuito; na FAT 2025, "colaboração e transparência" apontou especificamente para Open Source).*

### Banco de Dados (Q11–Q14)
- **Q11 — Gabarito: (B) — somente II correta** *(Molde 1 — Inversão Clássica!)*
  - **Item I (F):** Colocou a definição de **DDL** (`CREATE, ALTER, DROP`) no nome **DQL**!
  - **Item II (V):** **DML** (*Data Manipulation Language*) = `INSERT, UPDATE, DELETE`.
  - **Item III (F):** Colocou a definição de **DQL** (`SELECT`) no nome **DDL**!
- **Q12 — Gabarito: (E) — I, II e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - **Itens I, II e III (V):** Tabelas = linhas (**tuplas**) e colunas (**atributos**); Chaves = Primária (identifica unicamente) e Estrangeira (liga à PK de outra tabela); Relacionamentos = `1:1`, `1:N` e `N:N`.
- **Q13 — Gabarito: (A)** *(Molde 3 — Normalização)*
  - **Por que está certa:** Valores **atômicos (indivisíveis)**, sem grupos repetidos ou múltiplos valores na mesma célula = **Primeira Forma Normal (1NF)**.
- **Q14 — Gabarito: (D)** *(Molde 3/4 — Sintaxe SQL)*
  - **Por que está certa:** `SELECT COUNT(*) FROM clientes WHERE cidade = 'São Paulo';`.
  - **Pegadinhas:** (A) e (C) usam `COUNT` dentro do `WHERE` (proibido em SQL); (B) coloca a string `'São Paulo'` dentro de `COUNT()` e deixa `WHERE cidade` incompleto; (E) inverte `WHERE` e `FROM`.

### Design Digital (Q15–Q18)
- **Q15 — Gabarito: (A)** *(Molde 2 — Lista com Intruso)*
  - **Por que está certa:** **CMYK, RGB e Hexadecimal** são padrões de cores.
  - **Intrusos:** *"Primária"* (classificação de cor, não padrão) e *"CSS"* (linguagem de estilo).
- **Q16 — Gabarito: (E) — I, II e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - **Itens I, II e III (V):** Bancos de imagens oferecem variedade de conteúdo, tipos de licenças e múltiplas resoluções/formatos.
- **Q17 — Gabarito: (E)** *(Molde 3 — Gestalt)*
  - **Por que está certa:** *"linhas e padrões que seguem uma trajetória contínua"* = **Continuidade**.
- **Q18 — Gabarito: (A)** *(Molde 2 — Lista com Intruso)*
  - **Por que está certa:** **SVG** e **PDF** suportam gráficos vetoriais.
  - **Intrusos:** **JPEG**, **PNG** e **BMP** são todos **bitmap/raster** (compostos por pixels).

### Web, Redes, SO e Informática (Q20–Q21, Q24–Q30)
- **Q20 — Gabarito: (B)** *(Molde 3 — HTML)*
  - **Por que está certa:** Abrir em nova aba/janela = `target="_blank"`. (`_self` abre na mesma aba; `_parent` no frame pai; `_top` na janela inteira; `_none` não existe).
- **Q21 — Gabarito: (D) — II e III corretas** *(Molde 1 — Absurdo Técnico)*
  - **Item I (F):** Diz que *"Cookies são armazenados em nuvem"*! Falso: o próprio enunciado já entregava que ficam **armazenados no navegador do usuário** (armazenamento local).
  - **Item II (V):** Cada cookie tem limite de cerca de **4 KB**.
  - **Item III (V):** Podem ser de **sessão** (excluídos ao fechar o navegador) ou **permanentes**.
- **Q24 — Gabarito: (E) — I, II e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - Aplicações reais de **IoT**: residências inteligentes, cidades inteligentes e indústria/saúde com sensores.
- **Q25 — Gabarito: (A)** *(Molde 3 — Protocolos)*
  - **Por que está certa:** Protocolo básico da internet que divide dados em pacotes e os direciona ao destino = **TCP/IP**.
- **Q26 — Gabarito: (D)** *(Molde 3 — Topologias)*
  - **Por que está certa:** *"conectados a um único cabo central (o barramento)... se o cabo principal falhar, toda a rede é afetada"* = **Topologia em Barramento (Bus)**.
- **Q27 — Gabarito: (B)** *(Molde 3 — Sistemas Operacionais)*
  - **Por que está certa:** *"organizar o uso da memória RAM, alocando e liberando espaço"* = **Gerenciamento de Memória**.
- **Q28 — Gabarito: (B) — somente II correta** *(Molde 1 — Inversão Clássica!)*
  - **Item I (F):** Colocou a definição de **IMAP** (acesso no servidor sincronizado entre dispositivos) no nome **SMTP**!
  - **Item II (V):** **POP3** baixa e geralmente exclui do servidor.
  - **Item III (F):** Colocou a definição de **SMTP** (envio de e-mails) no nome **IMAP**!
- **Q29 — Gabarito: (C)** *(Molde 2 — Lista com Intruso)*
  - **Por que está certa:** Chrome, Firefox, Edge, Safari e Opera são todos navegadores web.
  - **Intrusos:** *Telegram*, *Messenger*, *Capcut*, *Youtube* e *Truecaller*.
- **Q30 — Gabarito: (E) — I, II e III corretas** *(Molde 1 — Tabela `I, II, III`)*
  - Suítes de produtividade oferecem integração de aplicativos, colaboração em tempo real e acessibilidade na nuvem.

---

## Parte 2: Prova Irmã — Informática para Internet (1º SEM/2025, aplicada no mesmo dia)

**Gabarito Oficial:**
`01-B | 02-E | 03-D | 04-B | 05-E | 06-B | 07-E | 08-C | 09-A | 10-D | 11-B | 12-E | 13-C | 14-E | 15-B | 16-B | 17-C | 18-D | 19-D | 20-D | 21-C | 22-B | 23-D | 24-E | 25-B | 26-A | 27-E | 28-A | 29-D | 30-E`

- **Q01–Q03:** **Idênticas** às questões 01–03 da prova de Desenvolvimento de Sistemas (*What is critical thinking?*).
- **Q04 — Gabarito: (B)** *(Molde 4)*: `255` em binário (8 bits ligados) = `11111111` ($128+64+32+16+8+4+2+1 = 255$).
- **Q05 — Gabarito: (E)** *(Molde 1)*: Virtualização de Servidor (I), SO (II) e Rede (III) — todas corretas.
- **Q06 — Gabarito: (B)** *(Molde 3)*: Listas com símbolos ou números no Word = **marcadores e numeração**.
- **Q07 — Gabarito: (E)** *(Molde 2)*: Webmails válidos: **Gmail, Outlook.com e iCloud Mail**. Intrusos: *Canva* (design), *Splice* (edição de vídeo), *Norton Safe Web* (segurança).
- **Q08 — Gabarito: (C) — I e III** *(Molde 1/2)*: Softwares de multimídia: **Adobe Creative Cloud** (I) e **Camtasia** (III). Intruso: *Office 365* (II — suíte de escritório).
- **Q09 — Gabarito: (A)** *(Molde 3)*: Organização circular de cores primárias, secundárias e terciárias = **Círculo Cromático**.
- **Q10 — Gabarito: (D)** *(Molde 3)*: Converter gráficos vetoriais (fórmulas matemáticas) para pixels exibíveis em telas = **Rasterização** (o inverso de *Vetorização*).
- **Q11 — Gabarito: (B)** *(Molde 3)*: Estratégias digitais com análise de ROI = **Marketing Digital**.
- **Q12 — Gabarito: (E)** *(Molde 1)*: Hospedagem Compartilhada (I), Dedicada (II) e VPS (III) — todas corretas.
- **Q13 — Gabarito: (C)** *(Molde 3)*: Elementos estruturais do HTML = **Tags**; propriedades extras dentro das tags = **Atributos**.
- **Q14 — Gabarito: (E)** *(Molde 3)*: Cada regra CSS tem duas partes: **Seletor e Bloco de Declarações** (ex.: `p { color: red; }`).
- **Q15 — Gabarito: (B)** *(Molde 2)*: Repositórios/serviços de fontes personalizadas para web = **Google Fonts e Adobe Fonts** (as outras opções misturam fontes de sistema como *Times New Roman* e *Arial*).
- **Q16 — Gabarito: (B)** *(Molde 3)*: Operar contêineres individualmente sem interferir uns nos outros = **Isolamento**.
- **Q17 — Gabarito: (C)** *(Molde 3)*: Protocolo gráfico de acesso remoto da Microsoft = **RDP** (*Remote Desktop Protocol*). (Pegadinhas: FTP transfere arquivos, SSH é terminal texto criptografado, SSL é segurança TLS, UTP é cabo de par trançado).
- **Q18 — Gabarito: (D)** *(Molde 2 — Pegadinha Genial!)*: Diretórios padrão do Linux = **`/bin, /etc, /home, /lib, /usr, /var e /tmp`**. As erradas colocaram comandos como se fossem pastas (`/cd`, `/pwd`, `/mkdir`, `/rm`, `/ls`)!
- **Q19 — Gabarito: (D) — I e II** *(Molde 1)*: `int` (I) e `float` (II) corretos; **Item III (F)** diz que `char` (caractere) representa `true` ou `false` (que na verdade é **boolean**!).
- **Q20 — Gabarito: (D) — II e III** *(Molde 1/4)*: Tabela verdade de `P ∧ Q` (`AND`): se P e Q são verdadeiros, `P ∧ Q` é **verdadeiro** (Item I falso!). Se qualquer um for falso (II e III), `P ∧ Q` é falso.
- **Q21 — Gabarito: (C)** *(Molde 4)*: Fatorial recursivo `4! = 4 × 3 × 2 × 1 = 24`.
- **Q22 — Gabarito: (B)** *(Molde 2)*: Bons requisitos têm **Clareza, Testabilidade, Consistência, Rastreabilidade e Viabilidade**. Intrusos nas outras: *Ambiguidade*, *Inconsistência*, *Irrelevância*.
- **Q23 — Gabarito: (D) — II e III** *(Molde 1)*: **Item I (F)** dá o nome de **Viabilidade Legal**, mas escreve o texto da **Viabilidade Operacional** (*"capacidade operacional, recursos humanos, infraestrutura"*).
- **Q24 — Gabarito: (E)** *(Molde 3)*: Diagrama UML comportamental que mostra interações entre **atores** e o sistema = **Diagrama de Casos de Uso**.
- **Q25 — Gabarito: (B)** *(Molde 2)*: As 4 camadas do modelo TCP/IP = **Link (Acesso à Rede), Internet, Transporte e Aplicação**. (Pegadinha: *Sessão* e *Física* pertencem ao modelo OSI de 7 camadas).
- **Q26 — Gabarito: (A)** *(Molde 3)*: Protocolo de envio de e-mail = **SMTP**.
- **Q27 — Gabarito: (E)** *(Molde 1)*: Funcionalidades do SSL/TLS: Criptografia, Autenticação e Integridade dos Dados.
- **Q28 — Gabarito: (A)** *(Molde 3)*: Cláusula `WHERE` restringindo resultados = **Filtragem e Condições**.
- **Q29 — Gabarito: (D)** *(Molde 2)*: Bancos **NoSQL** = **MongoDB e Cassandra**. Intrusos relacionais (SQL): *MySQL, PostgreSQL, Oracle*.
- **Q30 — Gabarito: (E)** *(Molde 1)*: **Mesmo quadro** de DQL (`SELECT`), DML (`INSERT/UPDATE/DELETE`) e DDL (`CREATE/ALTER/DROP`) da Q11 de DS, só que desta vez **todas estão certas**!

---

## Parte 3: Prova Histórica FAT — Desenvolvimento de Sistemas (1º SEM/2019)

**Gabarito Oficial:**
`01-A | 02-E | 03-C | 04-E | 05-A | 06-B | 07-D | 08-C | 09-B | 10-E | 11-A | 12-D | 13-B | 14-C | 15-A | 16-E | 17-E | 18-B | 19-C | 20-C | 21-A | 22-C | 23-E | 24-A | 25-C | 26-B | 27-D | 28-D | 29-A | 30-A`

- **Q01 — Gabarito: (A)** *(Molde 4)*: Tabela Verdade: `p ∧ q` = `V, F, F, F`; `p ∨ q` = `V, V, V, F`.
- **Q02 — Gabarito: (E)** *(Molde 4)*: Algoritmo em Portugol que converte decimal para binário usando `DIV 2` e `MOD 2` (concatenando resto à esquerda). `10` = `1010`; `250` = `11111010`.
- **Q03 — Gabarito: (C)** *(Molde 4)*: Pilha (LIFO). Rastreando passo a passo:
  - `01: [10]` -> `02: [10, 5]` -> `03 POP: [10]` -> `04: [10, 7]` -> `05: [10, 7, 3]` -> `06 POP: [10, 7]` -> `07: [10, 7, 10]` -> `08 POP: [10, 7]` -> `09: [10, 7, 2]` -> `10: [10, 7, 2, 7]` -> `11 POP: [10, 7, 2]` -> `12 POP: [10, 7]` -> `13 POP: [10]` -> `14: [10, 3]` -> `15 POP: [10]`. Valor residual = **10**.
- **Q04 — Gabarito: (E)** *(Molde 3)*: Atributos atômicos, sem grupos repetidos = **1ª Forma Normal**. (Repare que caiu quase igual na Q13 de 2025!).
- **Q05 — Gabarito: (A)** *(Molde 1)*: Relacionamento recursivo (auto-relacionamento) pode ser `1:N`, `N:1` ou `N:N` (todas corretas).
- **Q06 — Gabarito: (B)** *(Molde 4)*: Lei de formação da tabela: `× 3` e depois `- 2` alternadamente. Assim: `a = 2×3 = 6`; `b = 9-2 = 7`; `c = 30-2 = 28`; `d = 37×3 = 111`. Soma = `6 + 7 + 28 + 111 = 152`.
- **Q07 — Gabarito: (D)** *(Molde 2)*: DDL=`CREATE`, DML=`SELECT` *(nota: em 2019 a banca ainda agrupava DQL dentro de DML; a partir de 2025 passou a cobrar DQL separado para `SELECT` e DML para `INSERT/UPDATE/DELETE`)*, DCL=`GRANT`, TCL=`COMMIT`.
- **Q08 — Gabarito: (C)** *(Molde 3)*: Ordem do Modelo Cascata (*Waterfall*): **Requerimento → Projeto → Construção → Teste/Depuração → Instalação → Manutenção**.
- **Q09 — Gabarito: (B)** *(Molde 1)*: Chave Primária (I), Chave Alternativa (II — chaves candidatas não escolhidas como PK) e Chave Estrangeira (III) — todas corretas.
- **Q10 — Gabarito: (E)** *(Molde 3)*: Facilidade de transferir software de um ambiente/sistema para outro = **Portabilidade**.
- **Q11 — Gabarito: (A) — I e II** *(Molde 1)*: Requisito Funcional (o que faz) e Não Funcional (como faz) são definidos **antes** da construção; o item III afirma que devem ser especificados *depois* do desenvolvimento (Falso).
- **Q12 — Gabarito: (D)** *(Molde 3)*: Reunião diária curta do Scrum = **Daily Scrum**.
- **Q13 — Gabarito: (B)** *(Molde 2)*: Combinações harmônicas de **3 cores** no círculo cromático = **Análogas, Triangulação e Meio-complementares**. *(Complementares = 2 cores; Retângulo e Quadrado = 4 cores)*.
- **Q14 — Gabarito: (C)** *(Molde 3)*: Fontes que reproduzem escrita humana, elegância, usadas em convites = **Fontes Script**.
- **Q15 — Gabarito: (A)** *(Molde 3)*: Falar a linguagem do usuário e seguir seu modelo mental = **Equivalência entre o sistema e o mundo real** (Heurística de Nielsen).
- **Q16 — Gabarito: (E)** *(Molde 3)*: Tags semânticas estruturais do HTML5 = **`<nav><header><footer><section>`** (`<div>` e `<span>` não são semânticas; `<body>` já existia antes do HTML5).
- **Q17 — Gabarito: (E)** *(Molde 3)*: Transformações CSS3: Aumentar = **`scale`**, Modificar ângulos = **`skew`**, Movimentar X/Y = **`translate`**, Rotacionar = **`rotate`**.
- **Q18 — Gabarito: (B)** *(Molde 3)*: Classes do Bootstrap: `btn btn-default` (**botão**), `form-inline` (**formulário**), `col-md-1` (**grid**), `img-responsive` (**imagem**), `text-primary` (**ajuda/texto contextual**).
- **Q19 — Gabarito: (C)** *(Molde 3)*: Métodos DOM em JavaScript: buscar por ID (`getElementById`), criar nodo texto (`createTextNode`), elemento raiz `<html>` (`documentElement`), nodo pai (`parentNode`).
- **Q20 — Gabarito: (C)** *(Molde 4)*: Conversão de bases: `100(10) = 01100100(2) = 64(16)` e `250(10) = 11111010(2) = FA(16)`.
- **Q21 — Gabarito: (A)** *(Molde 3)*: Armazenamento em chips flash, sem partes mecânicas, menor consumo e tempo de acesso = **SSD**.
- **Q22 — Gabarito: (C)** *(Molde 3)*: Comandos Linux na ordem: mostrar (`ls`), criar pasta (`mkdir`), copiar (`cp`), gerenciar pacotes (`apt`), ler arquivo (`cat`), desligar/reiniciar (`shutdown`).
- **Q23 — Gabarito: (E)** *(Molde 3)*: Topologia com unidade central inteligente (*switches*) distribuindo tráfego = **Estrela**.
- **Q24 — Gabarito: (A)** *(Molde 1)*: Vantagens do *Pair Programming* (XP): compartilhamento de conhecimento, correção rápida de falhas e manutenibilidade — todas corretas.
- **Q25 — Gabarito: (C)** *(Molde 3)*: Verificar a menor unidade individual de código (métodos/classes) = **Teste de Unidade**.
- **Q26 — Gabarito: (B)** *(Molde 3)*: Controle de versão (Git): quebrar linha = **`branch`**, comparar = **`diff`**, fundir = **`merge`**.
- **Q27 — Gabarito: (D)** *(Molde 2)*: Os **4 pilares da POO** = **Abstração, Encapsulamento, Herança e Polimorfismo**. *(Atributos e Métodos são elementos da classe, não pilares!)*.
- **Q28–Q30 — Gabarito: 28-D, 29-A, 30-A**: Interpretação de texto em português e conectivos (*"apesar de"* = oposição/concessão; *"pois"* = justificativa/explicação).
