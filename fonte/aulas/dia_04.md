## Dia 4 (24/11) — Web I: como a internet funciona e HTML do zero

A matéria **Programação Web I** cai em toda prova de Taboão, quase sempre com perguntas diretas: "qual tag faz isso?", "o que é URI?", "qual protocolo leva as páginas?". E no laboratório do dia 08/12, montar uma página em HTML e CSS é uma das tarefas mais prováveis. Hoje: a parte da internet e o HTML. Amanhã: CSS e JavaScript.

### 1. O que acontece quando você abre um site

Você digita `etects.cps.sp.gov.br` e a página aparece. Por trás disso, existe uma conversa entre dois computadores:

- **Cliente**: quem **pede** — o seu navegador (Chrome, Edge, Firefox).
- **Servidor**: quem **responde** — um computador ligado 24 horas que guarda os arquivos do site.

Pense num restaurante: você (cliente) faz o **pedido** ao garçom; a cozinha (servidor) prepara e devolve o **prato**. Na web, o pedido se chama **requisição** (*request*) e o prato se chama **resposta** (*response*).

```text
 SEU NAVEGADOR (cliente)                         SERVIDOR DA ETEC
        │  1. "Qual é o IP de etects.cps.sp.gov.br?" ──► DNS
        │  ◄── 2. "É 200.144.x.x"                       
        │  3. Requisição HTTP: "me manda a página inicial" ─────────────►│
        │  ◄───────────── 4. Resposta HTTP: o arquivo HTML (+ CSS, imagens)│
        ▼
 5. O navegador lê o HTML e desenha a página na tela
```

### 2. IP, DNS, URL e URI

**Endereço IP** — todo computador conectado tem um número que o identifica na rede, como um número de telefone: `200.144.12.34`. Os computadores se encontram por esses números.

**DNS** (*Domain Name System*) — ninguém decora números. O DNS funciona como uma **lista telefônica** (ou a agenda do celular): você procura pelo **nome** (`etects.cps.sp.gov.br`) e ele devolve o **número IP**. Sem DNS, você teria que digitar números para abrir sites.

**URL** (*Uniform Resource **Locator***) — o **endereço completo** de um recurso, dizendo **onde** ele está e **como** pegar:

```text
https://www.etects.com.br:443/cursos/ds.html?turma=2#horarios
└─┬─┘   └──────┬─────────┘└┬┘└─────┬──────┘ └───┬───┘└───┬───┘
protocolo    domínio     porta   caminho    parâmetros  âncora
```

**URI** (*Uniform Resource **Identifier***) — é o nome **geral** para qualquer identificador **único** de um recurso na internet. Existem dois tipos:

| | Significa | Diz | Exemplo |
|---|---|---|---|
| **URL** | *Locator* (localizador) | **onde** o recurso está | `https://etects.com.br/index.html` |
| **URN** | *Name* (nome) | **qual é** o recurso, sem dizer onde | `urn:isbn:9788575224847` (código de um livro) |

**Toda URL é uma URI**, mas nem toda URI é uma URL. A palavra-chave é **Uniform** = **Uniforme** (não "unilateral", não "universal").

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questões 25 e 27):**
> - "Em relação a URI": a certa era "**identificador do recurso disponível na internet, com identificação única**". A alternativa com `www.etects.com.br` descrevia a **URL**; a com `/index.html` descrevia a URN (nome).
> - Afirmação falsa da questão 25: "URI se refere ao Identificador de recursos **Unilateral**" (o certo é **Uniforme**).

### 3. WWW, internet e os protocolos

**Internet ≠ Web.** A **internet** é a **rede física** que liga computadores do mundo todo (cabos, roteadores, satélites). A **World Wide Web (WWW)** — "rede de alcance mundial" — é **um dos serviços** que rodam na internet: o das **páginas ligadas por links**. E-mail, jogos online e Discord também usam a internet, mas não são "a web".

**Protocolo** = um conjunto de **regras de comunicação** que os dois lados combinam para se entender (como um idioma). Os que caem:

| Protocolo | Para que serve | Como lembrar |
|---|---|---|
| **HTTP** | transferir **páginas web** (hipertexto) entre servidor e navegador | *HyperText Transfer Protocol* |
| **HTTPS** | HTTP **seguro** (criptografado — o cadeado no navegador) | S = *Secure* |
| **TCP** | garante que os dados cheguem **completos e em ordem** | "o carteiro que confere cada pacote" |
| **IP** | dá **endereço** e leva os pacotes pela rede | "o CEP de cada computador" |
| **DNS** | traduz **nome → IP** | a lista telefônica |
| **FTP** | transferir **arquivos** | *File Transfer* |
| **SMTP** | **enviar** e-mail | **S**MTP = **S**end |
| **POP3 / IMAP** | **receber** e-mail (POP3 baixa; IMAP sincroniza) | |
| **DHCP** | distribui **IP automático** na rede (o roteador da sua casa faz isso) | |

> [!WARNING]
> **🔁 Já caiu:**
> - **dez/2025 (questão 25):** WWW = rede de alcance mundial ✔; TCP é como cliente e servidor conversam ✔; HTTP é o protocolo de aplicação que define a linguagem entre clientes e servidores ✔.
> - **Informática para Internet, dez/2025 (questão 20):** protocolo que transfere páginas da internet para o navegador → **HTTP**.
> - **Informática, dez/2025 (questão 16):** protocolo de **envio** de e-mail → **SMTP**.

### 4. HTML: o esqueleto da página

**HTML** (*HyperText Markup Language*) **não é linguagem de programação** — é uma linguagem de **marcação**: ela não faz contas nem decisões, só **diz o que cada parte da página é** ("isto é um título", "isto é um parágrafo", "isto é uma imagem").

Ela usa **tags** (etiquetas) entre `< >`. A maioria vem em par — uma abre e outra fecha (com `/`):

```html
<p>Eu sou um parágrafo.</p>
```

```text
<p>   Eu sou um parágrafo.   </p>
 │            │               │
tag de     conteúdo        tag de
abertura                 fechamento
└──────────── elemento ─────────┘
```

Algumas tags **não têm conteúdo** e não precisam fechar: `<br>`, `<hr>`, `<img>`, `<input>`, `<meta>`.

Tags podem ter **atributos** — informações extras, sempre na tag de **abertura**, no formato `nome="valor"`:

```html
<a href="https://www.cps.sp.gov.br" target="_blank">Site do Centro Paula Souza</a>
```

Aqui, `href` (endereço) e `target` (onde abrir) são atributos da tag `<a>`.

**A estrutura mínima de toda página HTML:**

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha primeira página</title>
  </head>
  <body>
    <h1>Olá, Etec!</h1>
    <p>Esta página foi feita por mim.</p>
  </body>
</html>
```

| Parte | Para que serve |
|---|---|
| `<!DOCTYPE html>` | avisa o navegador que é HTML5 |
| `<html>` | envolve a página inteira (`lang="pt-BR"` diz o idioma) |
| `<head>` | **cabeça**: informações **que não aparecem** na página (título da aba, codificação, CSS) |
| `<meta charset="UTF-8">` | faz os acentos (ç, ã, é) aparecerem certo |
| `<meta name="viewport">` | faz a página se ajustar à tela do **celular** |
| `<title>` | o texto que aparece **na aba** do navegador |
| `<body>` | **corpo**: tudo o que **aparece na tela** |

> [!CAUTION]
> **`<head>` × `<header>`:** o `<head>` é a "cabeça invisível" do documento. O `<header>` é o **cabeçalho visível** da página (logo, menu) e fica **dentro do `<body>`**. E não existe tag `<corpo>` — é `<body>`.

### 5. As tags de texto que mais caem

| Tag | Nome | O que faz |
|---|---|---|
| `<h1>` … `<h6>` | *heading* | títulos, do maior (`h1`) ao menor (`h6`). Use **um** `h1` por página |
| `<p>` | *paragraph* | parágrafo |
| `<br>` | *break* | **quebra/pula linha** (sem fechar) |
| `<hr>` | *horizontal rule* | **linha horizontal** separadora (sem fechar) |
| `<strong>` | | texto importante (**negrito**) |
| `<em>` | *emphasis* | ênfase (*itálico*) |
| `<!-- ... -->` | comentário | anotação que não aparece na página |

Macete para não trocar: **br** = ***br**eak* (quebra); **hr** = ***h**orizontal **r**ule* (régua horizontal).

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questão 26):** "tags de parágrafo, linha horizontal, título, pular linha e corpo do HTML, respectivamente" → **`<p>`, `<hr>`, `<h2>`, `<br>`, `<body>`**. As erradas trocavam `<hr>` com `<br>`, colocavam `<html>` no lugar de `<body>` ou inventavam `<corpo>`.

**Bloco × em linha** — todo elemento HTML tem um comportamento padrão:

| **Bloco** (`block`) | **Em linha** (`inline`) |
|---|---|
| começa numa **nova linha** e ocupa **a largura toda** | fica **dentro da linha** do texto, ocupando só o necessário |
| `<div>`, `<p>`, `<h1>`–`<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<form>` | `<span>`, `<a>`, `<strong>`, `<em>`, `<img>` |

O **`<div>`** é uma "caixa" genérica de **bloco**, usada para agrupar coisas e montar o layout com CSS. O **`<span>`** é a versão **em linha** (para marcar um pedaço de texto).

> [!WARNING]
> **🔁 Já caiu — 2022 (questões 38, 39 e 40):** "div é um elemento: **de bloco**"; "ol e ul são, respectivamente: ***ordered list* e *unordered list***"; "o elemento body refere-se ao **corpo da página**".

### 6. Listas, links e imagens

**Listas:**

```html
<ol>                      <!-- ordered list: numerada (1, 2, 3) -->
  <li>Ligar o PC</li>     <!-- li = list item: cada item -->
  <li>Abrir o VS Code</li>
</ol>

<ul>                      <!-- unordered list: com marcadores (•) -->
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

**Links** — a tag `<a>` (*anchor*, âncora):

```html
<a href="contato.html">Fale conosco</a>                 <!-- abre outra página do mesmo site -->
<a href="https://www.google.com" target="_blank">Google</a>   <!-- _blank = abre em NOVA aba -->
<a href="#horarios">Ver horários</a>                     <!-- pula para o elemento com id="horarios" -->
```

O texto entre `<a>` e `</a>` é o que aparece clicável. O destino vai no **`href`**.

**Imagens** — a tag `<img>`:

```html
<img src="logo-etec.png" alt="Logotipo da Etec Taboão da Serra" width="200">
```

| Atributo | Para que serve |
|---|---|
| `src` | *source*: **qual arquivo** de imagem mostrar (obrigatório) |
| `alt` | **texto alternativo**: aparece se a imagem não carregar e é **lido em voz alta** por leitores de tela para pessoas cegas (**acessibilidade**) |
| `width` / `height` | largura / altura |

O `alt` é um tema que aparece em prova: ele **não** define tamanho, posição nem link — é o **texto alternativo**.

### 7. Tabelas

```html
<table border="1">
  <tr>                      <!-- tr = table row (linha) -->
    <th>Matéria</th>        <!-- th = table header (célula de título, em negrito) -->
    <th>Nota</th>
  </tr>
  <tr>
    <td>Banco de Dados</td> <!-- td = table data (célula comum) -->
    <td>8,5</td>
  </tr>
  <tr>
    <td>Programação</td>
    <td>9,0</td>
  </tr>
</table>
```

Resultado:

| Matéria | Nota |
|---|---|
| Banco de Dados | 8,5 |
| Programação | 9,0 |

A ordem é sempre: `<table>` → `<tr>` (linha) → `<th>`/`<td>` (células). Cada `<tr>` é uma linha; cada `<td>` dentro dela é uma coluna.

### 8. Formulários: enviando dados (GET × POST)

Formulários são as telas de login, cadastro e busca. A tag é `<form>`, e os campos são `<input>`:

```html
<form action="cadastrar.php" method="post">
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome" required>

  <label for="email">E-mail:</label>
  <input type="email" id="email" name="email">

  <label for="senha">Senha:</label>
  <input type="password" id="senha" name="senha">

  <label for="idade">Idade:</label>
  <input type="number" id="idade" name="idade" min="14" max="99">

  <p>Curso:</p>
  <input type="radio" id="ds" name="curso" value="ds"> <label for="ds">DS</label>
  <input type="radio" id="info" name="curso" value="info"> <label for="info">Informática</label>

  <input type="checkbox" id="termos" name="termos"> <label for="termos">Aceito os termos</label>

  <button type="submit">Cadastrar</button>
</form>
```

| Parte | Função |
|---|---|
| `action` | para **onde** os dados vão (o programa no servidor que recebe) |
| `method` | **como** vão: `get` ou `post` |
| `<label for="x">` | o texto do campo; o `for` liga ao `id` do input (clicar no texto foca o campo) |
| `name` | o nome com que o dado chega ao servidor |
| `type="text"` / `email` / `password` / `number` / `date` | tipos de campo (password esconde o que se digita) |
| `type="radio"` | escolhe **uma** opção (os rádios do mesmo grupo têm o mesmo `name`) |
| `type="checkbox"` | marca/desmarca (pode várias) |
| `required` | campo obrigatório |
| `<button type="submit">` | envia o formulário |

**GET × POST** — a pergunta mais clássica de formulário:

| | **GET** | **POST** |
|---|---|---|
| Onde vão os dados | **na URL**, visíveis: `busca.php?q=etec&pagina=2` | no **corpo** da requisição, **não aparecem** na URL |
| Tamanho | limitado | grande (textos longos, arquivos) |
| Uso | **buscar** informação (pesquisa, filtros, links compartilháveis) | **enviar/gravar** (login, cadastro, upload) |
| Padrão do `<form>` | **sim** — sem `method`, é GET | não |

Senha **nunca** vai por GET: ela ficaria escrita na barra de endereço e no histórico.

> [!WARNING]
> **🔁 Já caiu — dez/2023 (questão 30):** "No endereço do navegador é possível encontrar os dados enviados em uma requisição utilizando o método **GET**" (correta). Erradas: "o padrão é POST", "muitos dados → GET", "POST mostra os dados na barra de endereço".

### 9. HTML5 semântico

O HTML5 criou tags que dizem **o significado** de cada região. Em vez de tudo ser `<div>`, você usa:

```html
<body>
  <header>                    <!-- cabeçalho visível: logo, título do site -->
    <h1>Etec Taboão</h1>
    <nav>                     <!-- navegação: o menu de links -->
      <a href="#cursos">Cursos</a> | <a href="#contato">Contato</a>
    </nav>
  </header>

  <main>                      <!-- o conteúdo principal (só um por página) -->
    <section id="cursos">     <!-- uma seção temática -->
      <h2>Cursos</h2>
      <article>               <!-- um conteúdo independente (um post, um card) -->
        <h3>Desenvolvimento de Sistemas</h3>
        <p>Curso técnico integrado ao ensino médio.</p>
      </article>
    </section>
  </main>

  <footer>                    <!-- rodapé: contato, direitos -->
    <p>Praça Miguel Ortega, 135 — Taboão da Serra</p>
  </footer>
</body>
```

Por que usar? **Acessibilidade** (leitores de tela entendem a estrutura), **SEO** (o Google entende o site) e **organização**. Visualmente, elas se comportam como `<div>`.

### 10. Ver o código de qualquer site: DevTools

Em qualquer página, aperte **F12** (ou clique com o botão direito → **Inspecionar**). Abre o painel **DevTools** (ferramentas do desenvolvedor):

- aba **Elements/Elementos**: o HTML da página — passe o mouse e veja cada parte acender;
- à direita, o **CSS** de cada elemento (dá para mudar e ver na hora);
- aba **Console**: mensagens e erros de JavaScript.

**Ctrl + U** mostra o código-fonte inteiro em outra aba.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2025 (questão 21):** "Qual ferramenta permite visualizar o código HTML de uma página?" → **DevTools do navegador**.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Esquecer de fechar** a tag (`<p>texto` sem `</p>`) ou fechar na ordem errada: `<p><strong>oi</p></strong>` → o certo é `<p><strong>oi</strong></p>` (a última aberta é a primeira fechada).
> - **Trocar `<br>` com `<hr>`** — br quebra a linha; hr desenha uma linha.
> - **Colocar conteúdo visível no `<head>`** — tudo que aparece vai no `<body>`.
> - **Esquecer as aspas** nos atributos ou usar `link=` no lugar de `href=`.
> - **Usar `<link>` para link clicável** — `<link>` (no head) é para carregar **CSS**; link clicável é `<a href>`.
> - **Esquecer o `alt`** nas imagens.
> - **Mandar senha por GET**.
> - **Esquecer `<meta charset="UTF-8">`** → os acentos viram símbolos estranhos (Ã©).

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Você digita "google.com" e o navegador precisa do número do servidor. Quem faz essa tradução? (A) HTTP (B) FTP (C) DNS (D) SMTP (E) HTML</summary>

**C — DNS**, a "lista telefônica" da internet: nome → IP.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Classifique como URL ou URN: (a) https://www.cps.sp.gov.br/etecs (b) urn:isbn:9788575224847</summary>

(a) **URL** (diz onde está e como acessar). (b) **URN** (só dá o nome único). As duas são **URIs**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — Qual sequência cria uma lista com marcadores de dois itens?</summary>

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

`<ul>` = lista não ordenada (marcadores). Com `<ol>`, os itens viriam numerados.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Ache os 4 erros: &lt;img source="foto.jpg"&gt; &lt;a link="pagina.html"&gt;Clique&lt;a&gt; &lt;p&gt;Oi&lt;br&gt;&lt;/br&gt;</summary>

1. `source` → o certo é **`src`** (e falta o `alt`).
2. `link=` → o certo é **`href=`**.
3. `<a>` no final deveria ser **`</a>`** (fechamento).
4. `<br>` **não fecha** (`</br>` está errado) e o `<p>` ficou sem `</p>`.

Corrigido:

```html
<img src="foto.jpg" alt="Descrição da foto">
<a href="pagina.html">Clique</a>
<p>Oi<br>tudo bem?</p>
```

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Num formulário de busca de produtos, qual método faz a pesquisa aparecer na URL para poder compartilhar o link? E num formulário de login?</summary>

Busca → **GET** (os dados ficam na URL: `?q=tenis`). Login → **POST** (a senha não pode aparecer na URL).

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Em uma tabela HTML, qual tag representa uma LINHA? (A) td (B) th (C) tr (D) tl (E) table</summary>

**C — `<tr>`** (*table row*). `td` é célula, `th` é célula de cabeçalho.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Qual protocolo deixa o cadeado no navegador? E qual garante que os pacotes cheguem completos e em ordem?</summary>

Cadeado → **HTTPS** (HTTP seguro, criptografado). Pacotes completos e em ordem → **TCP**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — Onde fica o título que aparece na ABA do navegador e onde fica o título grande que aparece na página?</summary>

Aba → `<title>` dentro do **`<head>`**. Título grande na página → `<h1>` dentro do **`<body>`**.

</details>

### 🖥️ Mão na massa (30–40 minutos)

**Sem instalar nada:** abra **codepen.io** → "Start coding" (ou **jsfiddle.net**) e digite no painel HTML. A página aparece embaixo, ao vivo.

**No computador (o jeito do laboratório):**

1. Crie uma pasta `meu-site` na Área de Trabalho.
2. Abra o **VS Code** (ou o Bloco de Notas) e crie o arquivo `index.html` dentro dela.
3. Digite a estrutura mínima da seção 4. No VS Code, digitar **`!`** e apertar **Tab** cria o esqueleto pronto — mas digite à mão pelo menos uma vez.
4. Salve e **dê dois cliques no arquivo**: ele abre no navegador. Depois de cada mudança, salve (Ctrl + S) e atualize o navegador (F5).

**Missão — "Minha ficha de inscrição":** uma página com:

- um `<header>` com `<h1>` "Inscrição — Etec Taboão" e um `<nav>` com dois links (um deles abrindo em nova aba);
- um `<main>` com: um `<h2>`, um parágrafo apresentando você, uma **lista ordenada** com 3 jogos que você gosta, uma **imagem** com `alt`, um `<hr>`;
- uma **tabela** com 3 matérias e suas notas (use `<th>` na primeira linha);
- um **formulário** com nome, e-mail, senha (POST), um grupo de rádio com 2 cursos e um botão;
- um `<footer>` com seu nome.

Depois, aperte **F12** na sua página e encontre cada parte na aba Elements.

<details class="recall-box">
<summary>✅ Um modelo de resposta (confira depois de tentar)</summary>

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inscrição — Etec Taboão</title>
</head>
<body>
  <header>
    <h1>Inscrição — Etec Taboão</h1>
    <nav>
      <a href="#ficha">Ficha</a> |
      <a href="https://etects.cps.sp.gov.br" target="_blank">Site da Etec</a>
    </nav>
  </header>

  <main>
    <h2>Sobre mim</h2>
    <p>Meu nome é Henrique e quero estudar <strong>Desenvolvimento de Sistemas</strong>.</p>
    <ol>
      <li>Minecraft</li>
      <li>Valorant</li>
      <li>FIFA</li>
    </ol>
    <img src="https://placehold.co/300x150" alt="Imagem de exemplo com 300 por 150 pixels">
    <hr>

    <table border="1">
      <tr><th>Matéria</th><th>Nota</th></tr>
      <tr><td>Matemática</td><td>7,5</td></tr>
      <tr><td>Português</td><td>8,0</td></tr>
      <tr><td>Inglês</td><td>9,0</td></tr>
    </table>

    <form id="ficha" action="#" method="post">
      <label for="nome">Nome:</label>
      <input type="text" id="nome" name="nome" required><br>
      <label for="email">E-mail:</label>
      <input type="email" id="email" name="email"><br>
      <label for="senha">Senha:</label>
      <input type="password" id="senha" name="senha"><br>
      <input type="radio" id="ds" name="curso" value="ds"> <label for="ds">DS</label>
      <input type="radio" id="inf" name="curso" value="inf"> <label for="inf">Informática</label><br>
      <button type="submit">Enviar</button>
    </form>
  </main>

  <footer>
    <p>Feito por Henrique — 2026</p>
  </footer>
</body>
</html>
```

</details>

### ✅ Resumo de 1 minuto

- **Cliente** (navegador) faz a **requisição**; **servidor** devolve a **resposta**.
- **IP** = número do computador; **DNS** = lista telefônica (nome → IP).
- **URI** = identificador **uniforme** de recurso. **URL** = onde está; **URN** = nome. Toda URL é URI.
- **WWW** = rede mundial de páginas; **HTTP/HTTPS** = páginas; **TCP** = entrega completa; **SMTP** = enviar e-mail; **FTP** = arquivos.
- HTML é **marcação**, não programação. Estrutura: `<!DOCTYPE html>`, `<html>`, `<head>` (invisível: title, meta), `<body>` (visível).
- **`<p>`** parágrafo, **`<br>`** quebra linha, **`<hr>`** linha horizontal, **`<h1>`–`<h6>`** títulos.
- **`<ol>`** numerada, **`<ul>`** marcadores, **`<li>`** item. **`<a href>`** link (`target="_blank"` = nova aba). **`<img src alt>`** (alt = texto alternativo).
- **`<div>`** = bloco; **`<span>`** = em linha. Tabela: **table → tr → th/td**.
- **GET** = dados na URL (buscar); **POST** = dados escondidos (enviar, login). Padrão do form = GET.
- Semânticas: **header, nav, main, section, article, footer**. **F12** = DevTools.
