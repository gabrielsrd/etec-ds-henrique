## Dia 7 (27/11) — Análise de Sistemas e Design: requisitos, ágil, UML e UX

Programar é só uma parte de fazer um sistema. Antes de escrever código, alguém precisa **entender o problema**, **combinar o que o sistema vai fazer** e **desenhar como ele vai ser**. Isso é **Análise e Projeto de Sistemas (APS)**. E, para o sistema ser bom de usar, entra o **Design Digital e UX**. Juntas, essas matérias rendem **de 3 a 5 questões por prova** em Taboão, quase todas de conceito — ótimas para pontuar com pouca conta.

### 1. O ciclo de vida de um software

Todo software "nasce, cresce e é mantido". As **fases** mais citadas:

```text
 Levantamento    Análise /     Projeto     Implementação    Testes    Implantação    Manutenção
 de requisitos → especificação → (desenho) → (programação) → ──────► → (entrega)   → (correções e
 (o que o                                                                              melhorias)
  cliente quer)
```

Uma forma mais resumida, cobrada em prova, agrupa tudo em **três grandes fases**:

| Fase | Pergunta | Atividades |
|---|---|---|
| **Definição** | **O que** o sistema vai fazer? | entender o problema, levantar requisitos, planejar |
| **Desenvolvimento** | **Como** vai ser feito? | projetar, programar, testar |
| **Operação** (manutenção) | Está funcionando? | corrigir erros, adaptar, melhorar |

> [!WARNING]
> **🔁 Já caiu — 2021 (questão 35):** "principais fases do ciclo de vida no desenvolvimento de software" → **Definição, Desenvolvimento e Operação**.

### 2. Modelos de processo: cascata × ágil

**Modelo em cascata (*waterfall*, linear ou sequencial)** — as fases acontecem **uma depois da outra**, como os degraus de uma cascata: só começa a programar quando todos os requisitos estão definidos; só testa quando toda a programação acabou.

```text
Requisitos
   └──► Projeto
           └──► Implementação
                    └──► Testes
                            └──► Implantação
                                     └──► Manutenção
```

- ✅ Bom quando os requisitos são **claros e estáveis** (não vão mudar).
- ❌ Ruim quando o cliente muda de ideia: descobrir um erro de requisito na fase de testes custa caro, e o cliente só vê o sistema no final.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2025 (questão 23):** "principal característica do Modelo de Ciclo de Vida **Linear/Sequencial**" → "**desenvolvimento sequencial onde um processo segue após o outro**". As outras alternativas descreviam modelos iterativos e ágeis (versões incrementais, protótipos, adaptação a mudanças).

**Outros modelos que aparecem:**

| Modelo | Ideia |
|---|---|
| **Incremental** | o sistema é entregue **em partes** (incrementos), cada uma funcionando |
| **Iterativo / evolutivo** | repete ciclos curtos, melhorando o sistema a cada volta |
| **Prototipação** | faz um **protótipo** (versão rascunho) para o cliente ver e opinar antes do sistema final |
| **Espiral** | ciclos com forte **análise de riscos** a cada volta |

**Métodos ágeis** — surgiram em 2001 com o **Manifesto Ágil**, que valoriza:

1. **Indivíduos e interações** mais que processos e ferramentas;
2. **Software funcionando** mais que documentação extensa;
3. **Colaboração com o cliente** mais que negociação de contratos;
4. **Responder a mudanças** mais que seguir um plano.

Os três métodos ágeis que caem:

**Scrum** — trabalho em ciclos curtos chamados **sprints** (de 1 a 4 semanas), cada um entregando algo pronto.

| Papel | Faz |
|---|---|
| **Product Owner** (dono do produto) | representa o cliente; decide **o que** é mais importante |
| **Scrum Master** | facilita: remove obstáculos e garante que o Scrum seja seguido |
| **Time de desenvolvimento** | faz o trabalho (programa, testa) |

| Artefato / evento | O que é |
|---|---|
| **Product Backlog** | a lista de **tudo** que o produto precisa ter, em ordem de prioridade |
| **Sprint Backlog** | o que o time vai fazer **nesta** sprint |
| **Daily** (reunião diária) | 15 minutos: o que fiz ontem, o que farei hoje, o que me atrapalha |
| **Sprint Review** | mostra ao cliente o que ficou pronto |
| **Retrospectiva** | o time discute como melhorar o próprio jeito de trabalhar |

**Kanban** — um **quadro** com colunas (**A fazer → Fazendo → Feito**) e cartões que andam entre elas. Deixa visível o fluxo de trabalho e limita quantas tarefas ficam "em andamento" ao mesmo tempo.

```text
┌─── A FAZER ───┐┌── FAZENDO ──┐┌──── FEITO ────┐
│ Tela de login ││ Cadastro    ││ Banco criado  │
│ Relatório     ││             ││ Layout aprov. │
└───────────────┘└─────────────┘└───────────────┘
```

**XP (*Extreme Programming*)** — foco em boas práticas de programação: **programação em par** (duas pessoas num computador), **testes automatizados** feitos antes do código (TDD), entregas pequenas e frequentes.

> [!TIP]
> **Ágeis = Scrum, XP, Kanban.** Cascata **não** é ágil. Diagrama de caso de uso, dicionário de dados e diagrama lógico **não** são métodos (são ferramentas de modelagem). Essa separação é cobrada em prova.

<details class="recall-box">
<summary>🧠 Sua vez — Num projeto Scrum, quem decide a ordem de prioridade do que vai ser feito? E qual reunião acontece todo dia?</summary>

Prioridade → **Product Owner** (ele cuida do Product Backlog). Reunião todo dia → **Daily** (*daily scrum*), de cerca de 15 minutos.

</details>

### 3. Requisitos: o que o sistema precisa ter

**Requisito** = uma necessidade que o sistema tem que atender. Eles se dividem em dois tipos — a dupla **mais cobrada** de APS:

| | **Requisito funcional (RF)** | **Requisito não funcional (RNF)** |
|---|---|---|
| Descreve | **o que** o sistema **faz** — suas **funções**, seu **comportamento** | **como** o sistema **deve ser** — qualidades e restrições |
| Pergunta | "O sistema deve permitir…?" | "Quão rápido? Quão seguro? Em que aparelho?" |
| Exemplos | cadastrar aluno; emitir boletim; enviar mensagem; calcular a média | responder em até 2 s; funcionar no celular; senha com 8+ caracteres; ficar no ar 99% do tempo; ser fácil de usar |
| Categorias | — | **desempenho**, **segurança**, **usabilidade**, **confiabilidade**, compatibilidade |

**Exemplo — um app da cantina da escola:**

- RF01: o aluno deve poder **ver o cardápio do dia**.
- RF02: o aluno deve poder **fazer um pedido** e pagar por Pix.
- RF03: a cantina deve poder **marcar o pedido como pronto**.
- RNF01: o pedido deve ser confirmado em **até 3 segundos**. (desempenho)
- RNF02: o app deve funcionar em **Android e iOS**. (compatibilidade)
- RNF03: os dados de pagamento devem ser **criptografados**. (segurança)

**Regra de negócio** é uma regra do "mundo do cliente" que o sistema precisa respeitar: "aluno só pode pedir até as 11h", "pedidos acima de R$ 30 têm 5% de desconto".

**Como se descobrem os requisitos (levantamento):** entrevista com o cliente, questionário, observação de como o trabalho é feito hoje, reuniões de *brainstorming* e protótipos.

> [!WARNING]
> **🔁 Já caiu (várias vezes):**
> - **2022 (questão 31):** "Os requisitos funcionais referem-se sobre o que o sistema **deve fazer**, ou seja, suas **funções** e informações." (Essa mesma frase voltou em outra prova recente.)
> - **Informática para Internet, dez/2024 (questão 32):** "Requisitos funcionais descrevem: o **comportamento** do sistema". Aparência, eficiência, confiabilidade e segurança são **não funcionais**.
> - **Informática para Internet, dez/2025 (questão 24):** RF = "**funcionalidades que o sistema deve executar** para atender necessidades".

<details class="recall-box">
<summary>🧠 Sua vez — Classifique: (a) "o sistema deve gerar o boletim em PDF" (b) "o boletim deve abrir em até 1 segundo" (c) "só o coordenador pode alterar notas" (d) "a tela deve ter letras grandes para alunos com baixa visão"</summary>

(a) **RF** (uma função). (b) **RNF** de desempenho. (c) **RNF de segurança** (controle de acesso) — também pode ser vista como regra de negócio. (d) **RNF** de usabilidade/acessibilidade.

</details>

### 4. Modelagem e UML

**Modelar** é fazer um **desenho simplificado** (uma **abstração**) do sistema para **entender** a complexidade **antes** de construir — como a planta de uma casa. Os modelos mostram a **estrutura** (do que o sistema é feito) e o **comportamento** (o que ele faz). Eles **não substituem** o código nem a documentação; ajudam a pensar e a conversar.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet:** dez/2024 (questão 33): técnica para visualizar estrutura e comportamento → **modelagem de sistemas**. Dez/2025 (questão 25): objetivo da modelagem → **criar abstrações para entender a complexidade antes da construção**.

**UML** (*Unified Modeling Language*, Linguagem de Modelagem **Unificada**) é o padrão de **diagramas** para modelar sistemas (principalmente orientados a objetos). É uma linguagem **visual** — **não** é linguagem de programação, **não** é metodologia, **não** é ferramenta de teste.

> [!WARNING]
> **🔁 Já caiu:** **2022 (questão 30)** "O que é UML?" → "uma linguagem de diagramas **unificada** que habilita profissionais de TI a **modelar e documentar** aplicações". **Informática para Internet, dez/2025 (questão 26):** "uma **linguagem visual** para modelagem de sistemas".

Os dois diagramas UML que caem em Taboão:

**a) Diagrama de casos de uso** — mostra o sistema **do ponto de vista de quem usa**:

- **Ator** (bonequinho): quem interage com o sistema — uma pessoa ou outro sistema (Aluno, Professor, Sistema do banco).
- **Caso de uso** (elipse): uma **função** que o sistema oferece, escrita com verbo (Fazer pedido, Ver notas).
- **Linha**: liga o ator aos casos de uso que ele usa.
- Retângulo em volta: o limite do sistema.

```text
                ┌──────────── App da Cantina ────────────┐
    O           │   ( Ver cardápio )                      │
   /|\ ─────────┼── ( Fazer pedido ) ─ ─ «include» ─ ─► ( Pagar por Pix )
   / \          │                                          │
  Aluno         │   ( Marcar pedido pronto ) ─────────────┼──────  O
                │                                          │      /|\
                └──────────────────────────────────────────┘      / \
                                                               Cantineira
```

(**«include»** = um caso de uso que **sempre** faz parte de outro; **«extend»** = um comportamento **opcional**.)

> [!WARNING]
> **🔁 Já caiu — 2021 (questão 40) e dez/2025 (questão 29):** o diagrama que representa a funcionalidade **do ponto de vista do usuário** é o de **caso de uso**; sua função é "**descrever interações entre atores e funcionalidades do sistema**".

**b) Diagrama de classes** — mostra a **estrutura**: as **classes**, seus **atributos** (dados) e **métodos** (ações), e como elas se ligam.

```text
┌────────────────────┐ 1          0..* ┌─────────────────────┐
│       Aluno        │─────────────────│       Pedido        │
├────────────────────┤      faz        ├─────────────────────┤
│ - ra: int          │                 │ - numero: int       │
│ - nome: string     │                 │ - valor: double     │
├────────────────────┤                 ├─────────────────────┤
│ + fazerPedido()    │                 │ + calcularTotal()   │
└────────────────────┘                 └─────────────────────┘
   (nome da classe / atributos / métodos)
```

- A **linha entre as classes** é uma **associação**: a **relação estrutural** entre elas ("um Aluno faz Pedidos").
- Os números nas pontas são a **multiplicidade**: 1 aluno faz de **0 a muitos** (`0..*`) pedidos.
- `-` = privado; `+` = público.
- Outras ligações: **herança** (seta com triângulo vazio: "Professor **é um** Funcionário") e **composição/agregação** (losango: "Carro **tem** Motor").

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questões 28 e 31 — a mesma pergunta repetida na prova):** "Em um diagrama de classes, as **associações** entre classes representam: **a relação estrutural entre classes, indicando como elas se conectam**". As erradas descreviam requisitos, tempo de resposta e caso de uso.

Outros diagramas UML (bom saber o nome): **sequência** (troca de mensagens no tempo), **atividades** (parecido com fluxograma), **estados**.

### 5. Trabalho em equipe e versionamento (Git)

Projetos são feitos em **equipe**, com **divisão de tarefas e prazos** (caiu em 2022, questão 37). Para várias pessoas mexerem no mesmo código sem bagunça, usa-se um **sistema de controle de versão** — o mais famoso é o **Git** (e o site **GitHub**, que guarda os projetos na nuvem).

| Comando Git | Faz |
|---|---|
| `git init` | começa a controlar uma pasta |
| `git add arquivo` | separa a mudança para salvar |
| `git commit -m "mensagem"` | **salva uma versão** (um "ponto de restauração" com descrição) |
| `git push` | envia as versões para o GitHub |
| `git pull` | baixa as mudanças dos colegas |
| `git branch` / `git merge` | cria uma "linha paralela" de trabalho / junta de volta |

(Esta plataforma, aliás, é guardada no GitHub e cada atualização é um *commit*.)

### 6. Design Digital: cores

**RGB × CMYK** — a pergunta de design que mais aparece:

| | **RGB** | **CMYK** |
|---|---|---|
| Cores | **R**ed, **G**reen, **B**lue (vermelho, verde, azul) | **C**yan, **M**agenta, **Y**ellow, blac**K** (ciano, magenta, amarelo, preto) |
| Funciona com | **luz** (cada pixel acende) | **tinta** (cada cor absorve parte da luz) |
| Sistema | **aditivo**: somar as três dá **branco** | **subtrativo**: somar as cores tende ao **preto** |
| Usado em | **telas**: celular, monitor, site, jogo | **impressão**: gráfica, panfleto, camiseta |

Regra prática: **vai para a tela → RGB; vai para o papel → CMYK.** No CSS, as cores são RGB (`#ff0000`, `rgb(255,0,0)`).

**Círculo cromático:**

- **Primárias** (no modelo de pigmento tradicional): vermelho, amarelo, azul.
- **Secundárias**: misturas de duas primárias (laranja, verde, roxo).
- **Complementares**: **opostas** no círculo (azul × laranja, vermelho × verde) — dão **contraste** forte.
- **Análogas**: **vizinhas** no círculo (azul, azul-esverdeado, verde) — dão **harmonia**.
- **Quentes** (vermelho, laranja, amarelo: energia, urgência) × **frias** (azul, verde, roxo: calma, confiança).

### 7. Design Digital: bitmap × vetor e os formatos de imagem

| | **Bitmap (raster)** | **Vetor (vetorial)** |
|---|---|---|
| É feito de | **pixels** (quadradinhos coloridos) | **fórmulas matemáticas** (pontos, linhas, curvas) |
| Ao ampliar | **perde qualidade** (fica "pixelado", serrilhado) | **não perde qualidade** nenhuma |
| Bom para | **fotos**, imagens com muitos detalhes | **logotipos**, ícones, ilustrações, fontes |
| Formatos | **JPEG/JPG, PNG, GIF, BMP, WEBP** | **SVG, AI, EPS, CDR** (e PDF pode conter vetor) |
| Programas | Photoshop, GIMP | Illustrator, CorelDRAW, Inkscape |

**Formatos que caem:**

| Formato | Tipo | Característica |
|---|---|---|
| **JPEG / JPG** | bitmap | compressão **com perda**; ótimo para **fotos**; não tem transparência |
| **PNG** | bitmap | compressão **sem perda**; aceita **transparência** |
| **GIF** | bitmap | até 256 cores; aceita **animação** |
| **SVG** | **vetor** | escalável sem perder qualidade; usado em sites para logos e ícones |
| **PSD** | bitmap (Photoshop) | guarda **camadas** |

> [!WARNING]
> **🔁 Já caiu — 2021 (questão 31):** "O que significa JPEG?" → ***Joint Photographic Experts Group*** (o grupo que criou o formato). O gabarito oficial daquele ano marcou a alternativa com a sigla errada; a explicação está na questão.

**Resolução:** a quantidade de pixels de uma imagem. **PPI/DPI** = pixels (ou pontos) por polegada: para tela, ~72 a 96; para **impressão** de qualidade, **300**.

### 8. UX, UI e usabilidade

- **UI** (*User Interface*, interface do usuário): o que você **vê e toca** — botões, cores, ícones, telas.
- **UX** (*User Experience*, experiência do usuário): **como é usar** o produto do começo ao fim — se é fácil, rápido, agradável, se resolve o problema.

**Usabilidade** é uma parte da UX: o quanto o sistema é **fácil de aprender e de usar**, com **eficiência** e **satisfação**. Um app com boa usabilidade você usa **sem precisar de manual**.

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questão 30):** "Em UX Design, o termo usabilidade está relacionado a: **a facilidade com que o usuário aprende e interage com o produto**". As pegadinhas: "quão **bonito** é o layout" (estética ≠ usabilidade), memória RAM, número de telas, resolução.

**Boas práticas de usabilidade** (heurísticas de Nielsen, resumidas):

1. Mostrar o que está acontecendo (barra de carregamento, "mensagem enviada ✓").
2. Falar a língua do usuário (nada de "Erro 0x80070005").
3. Deixar o usuário desfazer (botão "voltar", "desfazer").
4. Ser consistente (o mesmo botão sempre no mesmo lugar e com a mesma cor).
5. Prevenir erros (pedir confirmação antes de apagar).
6. Mensagens de erro claras, que dizem **como resolver**.

**Wireframe** = rascunho da tela, só com caixas e textos, sem cores (o "esqueleto"). **Protótipo** = uma versão clicável da tela para testar antes de programar (feito em ferramentas como **Figma**).

**Acessibilidade** = o sistema poder ser usado por todos, inclusive pessoas com deficiência: `alt` nas imagens, bom contraste, letras que aumentam, navegação pelo teclado.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Chamar cascata de ágil** — cascata é sequencial; ágeis são Scrum, XP e Kanban.
> - **Confundir RF e RNF**: se é **uma função** ("cadastrar", "emitir", "calcular") → RF. Se é **uma qualidade** (rápido, seguro, fácil, compatível) → RNF.
> - **Confundir caso de uso com diagrama de classes**: caso de uso = atores e funções (visão do usuário); classes = atributos, métodos e associações (estrutura).
> - **Dizer que UML é linguagem de programação ou metodologia** — é linguagem **de modelagem** (visual).
> - **Usar CMYK em site ou RGB para gráfica.**
> - **Achar que JPEG/PNG são vetores** — são bitmaps. Vetor é SVG.
> - **Achar que usabilidade é "deixar bonito".**

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Assinale a alternativa que contém SOMENTE métodos ágeis: (A) Cascata, Scrum, XP (B) Scrum, Kanban, XP (C) UML, Scrum, Kanban (D) Espiral, Cascata, Kanban (E) Dicionário de dados, XP</summary>

**B — Scrum, Kanban e XP.** Cascata e espiral são modelos tradicionais; UML e dicionário de dados são ferramentas de modelagem.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — "O sistema deve suportar 500 usuários conectados ao mesmo tempo" é um requisito: (A) funcional (B) não funcional de desempenho (C) regra de negócio (D) caso de uso (E) ator</summary>

**B — não funcional (desempenho).** Não é uma função que o sistema executa, e sim uma qualidade (capacidade).

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — No diagrama de casos de uso de uma biblioteca, quais são os atores e quais são os casos de uso: Aluno, Emprestar livro, Bibliotecário, Devolver livro, Consultar acervo?</summary>

**Atores** (quem usa): Aluno, Bibliotecário. **Casos de uso** (funções, com verbo): Emprestar livro, Devolver livro, Consultar acervo.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Numa classe "Produto", "preco" e "calcularDesconto()" são, respectivamente: (A) método e atributo (B) atributo e método (C) associação e classe (D) ator e caso de uso (E) objeto e classe</summary>

**B.** `preco` é um **dado** (atributo); `calcularDesconto()` é uma **ação** (método — tem parênteses).

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — A logo da Etec vai aparecer no site e também num banner impresso de 3 metros. Qual formato e quais modos de cor usar?</summary>

Logo em **vetor** (SVG, AI, EPS) — amplia para 3 metros sem perder qualidade. Para o **site**, cores em **RGB**; para o **banner impresso**, em **CMYK**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Um projeto em que o cliente muda de ideia toda semana combina mais com cascata ou com ágil? Por quê?</summary>

Com **ágil**: entregas curtas e frequentes, com o cliente vendo e opinando a cada sprint, e mudanças são bem-vindas. Na cascata, mudar um requisito no meio do caminho obriga a refazer várias fases.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Num app, o botão "Excluir conta" abre uma caixa "Tem certeza? Essa ação não pode ser desfeita". Que boa prática de usabilidade é essa?</summary>

**Prevenção de erros** (e controle do usuário): confirmar antes de uma ação grave e irreversível.

</details>

### 🖥️ Mão na massa (30 minutos)

Escolha um sistema que você conhece bem (um jogo online, o app da escola, um delivery) e, numa folha:

1. Escreva **5 requisitos funcionais** (começando com "O sistema deve permitir…") e **3 não funcionais** (um de desempenho, um de segurança, um de usabilidade).
2. Desenhe o **diagrama de casos de uso**: o retângulo do sistema, pelo menos **2 atores** e **5 casos de uso** ligados a eles.
3. Desenhe **duas classes** com **2 atributos e 1 método** cada, ligadas por uma **associação** com multiplicidade (ex.: `1` e `0..*`).
4. Monte um mini **quadro Kanban** (A fazer / Fazendo / Feito) com as tarefas de estudo desta semana — e use ele de verdade até o dia 04/12.
5. Abra **figma.com** (grátis, funciona no navegador) e faça o **wireframe** da tela de login do seu sistema: só caixas e textos.

<details class="recall-box">
<summary>✅ Exemplo para um app de delivery</summary>

**RF:** o sistema deve permitir (1) cadastrar cliente; (2) buscar restaurantes por nome; (3) adicionar itens ao carrinho; (4) pagar o pedido; (5) acompanhar a entrega no mapa.

**RNF:** (1) a busca deve responder em até 2 s (desempenho); (2) senhas armazenadas criptografadas (segurança); (3) fazer um pedido em no máximo 4 toques (usabilidade).

**Casos de uso:** Cliente → Buscar restaurante, Montar pedido, Pagar, Acompanhar entrega. Restaurante → Aceitar pedido, Marcar como pronto. Entregador → Retirar pedido, Confirmar entrega.

**Classes:**

```text
Cliente (- cpf: string, - nome: string, + fazerPedido())  1 ──── 0..*  Pedido (- numero: int, - valor: double, + calcularTotal())
```

</details>

### ✅ Resumo de 1 minuto

- Ciclo de vida em 3 fases: **Definição** (o quê) → **Desenvolvimento** (como) → **Operação** (manutenção).
- **Cascata** = **sequencial**, uma fase após a outra. **Ágeis** = **Scrum** (sprints, Product Owner, Scrum Master, daily), **Kanban** (quadro A fazer/Fazendo/Feito), **XP** (programação em par, testes).
- **RF** = o que o sistema **faz** (funções, comportamento). **RNF** = **como** deve ser (desempenho, segurança, usabilidade).
- **Modelar** = abstrair para entender **antes** de construir. **UML** = linguagem **visual unificada** de modelagem.
- **Caso de uso** = **atores** × **funções** (visão do usuário). **Diagrama de classes** = atributos, métodos e **associações** (relação estrutural).
- **RGB** = luz/telas (aditivo); **CMYK** = tinta/impressão (subtrativo).
- **Bitmap** (pixels: JPEG, PNG, GIF) perde qualidade ao ampliar; **vetor** (SVG) não perde. JPEG = *Joint Photographic Experts Group*.
- **Usabilidade** = facilidade de aprender e usar (não é beleza). UI = interface; UX = experiência.
