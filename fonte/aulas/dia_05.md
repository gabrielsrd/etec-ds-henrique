## Dia 5 (25/11) — Web II: CSS e JavaScript

Ontem você montou o **esqueleto** de uma página com HTML. Hoje vem a **aparência** (CSS) e uma pitada de **comportamento** (JavaScript). Uma comparação que ajuda a separar os três:

| Camada | Linguagem | Faz o quê | No corpo humano |
|---|---|---|---|
| Estrutura | **HTML** | diz **o que** cada parte é | o esqueleto |
| Aparência | **CSS** | diz **como** cada parte fica (cor, tamanho, posição) | a pele e a roupa |
| Comportamento | **JavaScript** | faz a página **reagir** (cliques, contas, mudar conteúdo) | os músculos |

CSS aparece em toda prova recente de Taboão (box model, Flexbox, seletores, margin × padding, viewport), e no laboratório é o CSS que transforma uma página "crua" numa página apresentável.

### 1. Onde escrever o CSS

**CSS** (*Cascading Style Sheets*, folhas de estilo em cascata) pode entrar de três jeitos:

```html
<!-- 1. Inline: direto na tag (evite, fica bagunçado) -->
<p style="color: red;">Texto vermelho</p>

<!-- 2. Interno: dentro de <style> no <head> -->
<head>
  <style>
    p { color: blue; }
  </style>
</head>

<!-- 3. Externo: num arquivo separado (o jeito certo) -->
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

O **arquivo externo** (`style.css`) é o padrão profissional: um só arquivo de estilo serve para todas as páginas do site. Atenção: a tag que liga o CSS é **`<link>`** (no `<head>`), com **`href`**. Já o JavaScript externo usa **`<script src="...">`**. Trocar os dois é pegadinha clássica.

### 2. A "frase" do CSS: seletor, propriedade e valor

```css
h1 {
  color: navy;          /* propriedade: valor; */
  font-size: 32px;
  text-align: center;
}
```

```text
h1        {   color   :   navy   ;   }
│             │           │      │
seletor   propriedade   valor   ponto e vírgula
(QUEM)       (O QUÊ)    (COMO)
```

O **seletor** escolhe **quais elementos** vão receber o estilo. Comentários em CSS ficam entre `/* */`.

### 3. Seletores: escolhendo quem estilizar

| Seletor | Escreve-se | Pega | Exemplo |
|---|---|---|---|
| **de tag (elemento)** | o nome da tag | **todos** os elementos daquela tag | `p { … }` → todos os parágrafos |
| **de classe** | **ponto** + nome | todos com `class="nome"` | `.destaque { … }` |
| **de id** | **#** + nome | **o único** elemento com `id="nome"` | `#topo { … }` |
| **descendente** | dois seletores com espaço | o segundo **dentro** do primeiro | `nav a { … }` → links dentro do nav |
| **agrupamento** | vírgula | vários de uma vez | `h1, h2 { … }` |
| **pseudo-classe** | dois-pontos | um estado | `a:hover { … }` → quando o mouse passa por cima |

```html
<p>Parágrafo comum</p>
<p class="destaque">Parágrafo em destaque</p>
<div id="topo">Topo da página</div>
```

```css
p          { color: gray; }        /* todos os <p> */
.destaque  { font-weight: bold; }  /* quem tem class="destaque" */
#topo      { background: yellow; } /* o elemento com id="topo" */
```

**Classe × id:** uma **classe** pode ser usada em **vários** elementos (e um elemento pode ter várias classes: `class="card destaque"`). Um **id** é **único** na página.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2025 (questão 22):** "Seletor que estiliza todos os parágrafos" → **`p`**. As erradas eram `#p` (id), `.p` (classe), `paragraph` (não existe).

**Quem vence quando duas regras brigam? (a "cascata")**

1. A regra **mais específica** vence: **id** vence **classe**, que vence **tag**.
2. Se a força for igual, vence a que vem **por último** no arquivo.

```css
p          { color: gray; }
.destaque  { color: blue; }
```

Um `<p class="destaque">` fica **azul**: a classe é mais específica que a tag.

### 4. Cores, tamanhos e texto

**Cores** podem ser escritas de várias formas — todas fazem o mesmo:

```css
color: red;                 /* nome em inglês */
color: #ff0000;             /* hexadecimal: #RRGGBB (vermelho, verde, azul) */
color: rgb(255, 0, 0);      /* RGB de 0 a 255 */
background-color: #1e293b;  /* cor de fundo */
```

Repare no **hexadecimal** (`#RRGGBB`): cada par vai de `00` a `FF` (0 a 255). Você estuda as bases numéricas no Dia 8 — `FF` = 255.

**Unidades de tamanho:**

| Unidade | Tipo | Quando usar |
|---|---|---|
| `px` | fixa (pixels) | bordas, detalhes |
| `%` | relativa ao elemento pai | larguras (`width: 50%`) |
| `em` / `rem` | relativa ao tamanho da fonte | textos e espaçamentos |
| `vw` / `vh` | % da largura/altura da tela | blocos que ocupam a tela |

**Propriedades de texto mais usadas:**

```css
body {
  font-family: Arial, sans-serif;  /* tipo de letra (com alternativa) */
  font-size: 16px;                 /* tamanho */
  color: #222;                     /* cor do texto */
  line-height: 1.5;                /* espaço entre linhas */
}
h1 {
  text-align: center;              /* left, center, right, justify */
  font-weight: bold;               /* negrito */
}
```

### 5. O box model: toda tag é uma caixa

Esta é a ideia mais importante do CSS. **Todo elemento é uma caixa retangular** com **4 camadas**, de dentro para fora:

```text
┌──────────────────── MARGIN (margem: espaço FORA da borda) ────────────────────┐
│                                                                              │
│   ┌─────────────────── BORDER (a borda: a "moldura") ──────────────────┐     │
│   │   ┌──────────────── PADDING (preenchimento: espaço DENTRO) ───────┐ │     │
│   │   │                                                                │ │     │
│   │   │                CONTENT (o conteúdo: texto, imagem)             │ │     │
│   │   │                                                                │ │     │
│   │   └────────────────────────────────────────────────────────────────┘ │     │
│   └────────────────────────────────────────────────────────────────────┘     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Camada | Propriedade | O que é | Analogia (quadro na parede) |
|---|---|---|---|
| Conteúdo | `width`, `height` | o texto ou a imagem | a foto |
| **Preenchimento** | **`padding`** | espaço **interno**, entre o conteúdo e a borda | o *passe-partout* (a margem de papel em volta da foto) |
| **Borda** | **`border`** | a linha em volta | a moldura |
| **Margem** | **`margin`** | espaço **externo**, entre a borda e os vizinhos | o espaço na parede entre um quadro e outro |

```css
.card {
  width: 300px;
  padding: 20px;                 /* 20px de espaço por dentro, nos 4 lados */
  border: 2px solid #2563eb;     /* espessura, estilo (solid, dashed, dotted), cor */
  margin: 16px;                  /* 16px de espaço por fora */
  border-radius: 12px;           /* cantos arredondados */
}
```

**Atalhos de padding e margin** (sentido horário: cima, direita, baixo, esquerda):

```css
margin: 10px;                 /* os 4 lados */
margin: 10px 20px;            /* cima e baixo = 10; esquerda e direita = 20 */
margin: 5px 10px 15px 20px;   /* cima, direita, baixo, esquerda */
margin: 0 auto;               /* centraliza horizontalmente um bloco com largura definida */
padding-top: 8px;             /* só um lado */
```

**Quanto mede a caixa de verdade?** Por padrão, `width` é só o conteúdo. Com `width: 300px`, `padding: 20px` e `border: 2px`, a caixa ocupa **300 + 20 + 20 + 2 + 2 = 344 px** de largura (a margem fica fora disso). Para o `width` incluir padding e borda, usa-se `box-sizing: border-box;`.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2024 (questão 39):** "_____ e _____ têm funcionamento parecido. Porém, o primeiro fornece espaçamento **externo**, e o segundo, espaçamento **interno**" → **margin, padding**. Box model e margin × padding também aparecem nas provas de DS. Frase para decorar: **padding = para dentro, margin = mais fora**.

<details class="recall-box">
<summary>🧠 Sua vez — Você quer afastar o texto de dentro da borda do botão. Usa padding ou margin? E para afastar dois botões um do outro?</summary>

Texto longe da borda (espaço **interno**) → **padding**. Botões afastados entre si (espaço **externo**) → **margin**.

</details>

### 6. display: bloco, em linha e sumir

A propriedade `display` muda o comportamento da caixa:

| Valor | Comportamento |
|---|---|
| `block` | nova linha, largura toda (padrão de `div`, `p`, `h1`) |
| `inline` | dentro do texto; **ignora** width e height (padrão de `span`, `a`) |
| `inline-block` | fica na linha, mas aceita width e height (bom para botões) |
| `none` | **some** da página (não ocupa espaço) |
| **`flex`** | transforma a caixa num **contêiner flexível** → próxima seção |

### 7. Flexbox: alinhar e centralizar sem sofrer

Antes do Flexbox, centralizar uma coisa no meio da tela era um pesadelo. Com ele, você liga o "modo flex" no **pai** (o contêiner) e controla como os **filhos** se organizam.

```html
<div class="container">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```

```css
.container {
  display: flex;               /* liga o Flexbox: os filhos ficam lado a lado */
  justify-content: center;     /* alinha no EIXO PRINCIPAL (horizontal, por padrão) */
  align-items: center;         /* alinha no EIXO CRUZADO (vertical, por padrão) */
  gap: 10px;                   /* espaço entre os itens */
  height: 300px;
}
```

**Os dois eixos** — o ponto que mais confunde:

- `flex-direction: row` (padrão): eixo principal = **horizontal** → `justify-content` mexe na horizontal; `align-items`, na vertical.
- `flex-direction: column`: os itens ficam **um embaixo do outro**, e os eixos **trocam**.

**Valores de `justify-content`:**

```text
flex-start     [A][B][C]                          (tudo no começo — padrão)
center                     [A][B][C]              (tudo no meio)
flex-end                                [A][B][C] (tudo no fim)
space-between  [A]              [B]            [C] (pontas coladas, espaço igual entre)
space-around    [A]          [B]          [C]      (espaço em volta de cada um)
```

**A receita para centralizar qualquer coisa (horizontal e vertical):**

```css
.pai {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;     /* ocupa a altura inteira da tela */
}
```

Decore essas três linhas (`display: flex; justify-content: center; align-items: center;`) — elas caem em prova e são quase certas no laboratório.

Outras propriedades úteis do contêiner:

```css
.galeria {
  display: flex;
  flex-wrap: wrap;           /* quando não couber, quebra para a linha de baixo */
  flex-direction: column;    /* um embaixo do outro */
}
```

<details class="recall-box">
<summary>🧠 Sua vez — Num menu, você quer o logo na ponta esquerda e os links na ponta direita, dentro de um header com display: flex. Qual justify-content?</summary>

**`justify-content: space-between;`** — joga o primeiro item numa ponta, o último na outra e distribui o espaço entre eles.

</details>

### 8. Páginas que funcionam no celular (responsividade)

Um site **responsivo** se adapta a qualquer tamanho de tela. Três peças:

**1. A meta viewport** (no `<head>`) — sem ela, o celular "finge" ser uma tela grande e encolhe tudo:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

O **viewport** é a **área visível** da página na tela do aparelho.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2024 (questão 40):** "Por viewport entende-se: a área visível de espaço renderizável". (O gabarito oficial marcou outra letra por engano — está explicado na questão.)

**2. Medidas relativas** (`%`, `rem`, `vw`) e `max-width` no lugar de larguras fixas grandes:

```css
.conteudo { width: 90%; max-width: 800px; margin: 0 auto; }
img { max-width: 100%; height: auto; }   /* imagem nunca estoura a tela */
```

**3. Media queries** — regras que só valem em certos tamanhos de tela:

```css
.cards { display: flex; gap: 16px; }          /* no computador: lado a lado */

@media (max-width: 600px) {                    /* SÓ em telas de até 600px (celular) */
  .cards { flex-direction: column; }           /* um embaixo do outro */
  h1 { font-size: 22px; }
}
```

Leia `@media (max-width: 600px)` como: **"se a tela tiver no máximo 600 pixels de largura, aplique isto"**.

### 9. JavaScript: dando vida à página

**JavaScript (JS)** é uma **linguagem de programação de verdade** (tem variáveis, `if`, laços) que roda **no navegador**. É ela que faz a página reagir: validar um formulário, abrir um menu, mostrar uma mensagem ao clicar.

**Onde colocar** — num arquivo `.js`, ligado com `<script src>`, normalmente no **fim do `<body>`** (para a página carregar antes):

```html
<body>
  <h1 id="titulo">Olá</h1>
  <button onclick="trocar()">Clique</button>

  <script src="app.js"></script>      <!-- src = arquivo do script -->
</body>
```

Pegadinhas de prova: é `<script src="...">` (não `href`, não `file`, não `<js>`); CSS é que usa `<link href>`.

**Variáveis e tipos em JS** — parecido com C#, mas **sem declarar o tipo**: o próprio JS descobre:

```javascript
let idade = 16;            // number (número — inteiro ou decimal, é tudo number)
let nome = "Henrique";     // string (texto)
let aprovado = true;       // boolean (true/false)
let apelido;               // undefined (criada, mas sem valor)
let vazio = null;          // null (vazio de propósito)
const PI = 3.14;           // const = constante: não pode mudar depois

console.log(typeof idade); // "number"
console.log("Olá, " + nome);
```

Os **tipos primitivos** do JavaScript são: **`number`, `string`, `boolean`, `undefined`, `null`** (e os avançados `symbol` e `bigint`). **Array e object não são primitivos.**

**Comparação C# × JavaScript:**

| | C# | JavaScript |
|---|---|---|
| Declarar | `int idade = 16;` | `let idade = 16;` |
| Mostrar | `Console.WriteLine(x);` | `console.log(x);` ou `alert(x);` |
| Ler do usuário | `Console.ReadLine()` | `prompt("Digite:")` |
| if / for / while | igual | igual |
| Onde roda | no computador (.NET) | no **navegador** |

**Mexendo na página (DOM)** — o JS consegue achar elementos do HTML e mudá-los:

```javascript
function trocar() {
  const t = document.getElementById("titulo");   // acha o elemento com id="titulo"
  t.textContent = "Você clicou!";                // troca o texto
  t.style.color = "green";                       // muda o estilo
}
```

O **DOM** (*Document Object Model*) é a "árvore" de elementos da página que o JavaScript enxerga e altera.

**Cliente × servidor:** JavaScript, HTML e CSS rodam no **navegador** (lado do **cliente**). Linguagens como **PHP**, C#, Java e Python podem rodar no **servidor** (lado do servidor), gerando a página antes de enviá-la. Uma questão de dez/2023 cobrou características do PHP: variáveis sem declarar tipo, nomes de variáveis que **diferenciam** maiúsculas (`$nome` ≠ `$Nome`), funções globais.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Esquecer o `;`** entre propriedades CSS ou as chaves `{ }` → as regras seguintes param de funcionar.
> - **Ponto × cerquilha:** `.menu` é **classe**, `#menu` é **id**. No HTML, `class="menu"` e `id="menu"` (sem ponto, sem #).
> - **Inverter padding e margin** — padding é **dentro**, margin é **fora**.
> - **Colocar `justify-content`/`align-items` no filho** — eles vão no **pai**, junto com `display: flex`.
> - **Esquecer a meta viewport** → a página aparece minúscula no celular.
> - **Ligar o CSS com `<style src>` ou o JS com `<link>`** — CSS: `<link rel="stylesheet" href>`; JS: `<script src>`.
> - **Esquecer de salvar o arquivo** antes de atualizar o navegador (é o erro mais comum no laboratório!).

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Qual regra deixa VERDES apenas os elementos com class="aviso"? (A) aviso { color: green; } (B) #aviso { color: green; } (C) .aviso { color: green; } (D) *aviso { color: green; } (E) class=aviso { color: green; }</summary>

**C.** Classe = **ponto**. A pegaria uma tag `<aviso>` (que não existe); B pegaria o id.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Uma caixa tem width: 200px; padding: 10px; border: 5px solid; margin: 20px. Qual a largura ocupada pela caixa até a borda (sem contar a margem)?</summary>

200 + 10 + 10 + 5 + 5 = **230 px**. Contando também a margem, o espaço ocupado na página seria 230 + 20 + 20 = 270 px.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — Qual alternativa centraliza um elemento na horizontal E na vertical usando Flexbox? (A) display: block; margin: 0 auto; (B) display: flex; justify-content: center; align-items: center; (C) display: grid; justify-items: center; (D) text-align: center; (E) display: flex; justify-content: space-between;</summary>

**B.** A centraliza só na horizontal (e sem Flexbox); C é Grid e só horizontal; D centraliza só texto; E espalha os itens pelas pontas.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — O que significa @media (max-width: 768px) { nav { display: none; } }?</summary>

"Em telas de **até 768 pixels** de largura (celulares e tablets), **esconda** o `<nav>`." É assim que muitos sites somem com o menu grande e mostram um botão de menu no celular.

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Qual destes NÃO é tipo primitivo do JavaScript? (A) number (B) string (C) boolean (D) undefined (E) array</summary>

**E — array** (é um objeto). Primitivos: number, string, boolean, undefined, null, symbol, bigint.

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Ligue: (1) estrutura (2) aparência (3) comportamento — com HTML, CSS e JavaScript.</summary>

(1) estrutura → **HTML**; (2) aparência → **CSS**; (3) comportamento → **JavaScript**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Escreva o CSS: todo link dentro do footer deve ficar branco e, ao passar o mouse, amarelo.</summary>

```css
footer a { color: white; }
footer a:hover { color: yellow; }
```

`footer a` = seletor **descendente** (links dentro do footer). `:hover` = quando o mouse está em cima.

</details>

### 🖥️ Mão na massa (40 minutos)

Pegue a ficha de inscrição que você fez ontem (`index.html`) e dê estilo a ela:

1. Na mesma pasta, crie o arquivo **`style.css`**.
2. No `<head>` do `index.html`, ligue o CSS: `<link rel="stylesheet" href="style.css">`.
3. No `style.css`, faça:
   - `body` com uma fonte sem serifa, fundo cinza bem claro e margem zero;
   - o `header` com fundo azul-escuro, texto branco, `padding` de 16 px e **Flexbox** com `justify-content: space-between` e `align-items: center` (título de um lado, links do outro);
   - envolva o formulário numa `<div class="card">` e deixe o card branco, com `padding`, borda arredondada e sombra (`box-shadow: 0 2px 8px rgba(0,0,0,0.15);`);
   - uma `<section class="centro">` que **centraliza** o card na tela com a receita do Flexbox;
   - uma **media query** que, em telas de até 600 px, coloca o header em coluna (`flex-direction: column`).
4. Abra a página no navegador, aperte **F12**, clique no botão de **celular** (ícone de dispositivo, no topo do DevTools) e veja a versão mobile.
5. **Bônus de JavaScript:** um botão que, ao ser clicado, troca o texto do `<h1>`.
6. **Jogo:** abra **flexboxfroggy.com** (escolha português no canto) e jogue até a **fase 12**. Cada fase é um exercício de `justify-content`, `align-items` e `flex-direction` — exatamente o que cai.

<details class="recall-box">
<summary>✅ Um modelo de style.css (confira depois de tentar)</summary>

```css
body {
  font-family: Arial, Helvetica, sans-serif;
  background: #f1f5f9;
  margin: 0;
  color: #1e293b;
}

header {
  background: #1e3a8a;
  color: white;
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header a { color: #bfdbfe; margin-left: 12px; }
header a:hover { color: white; }

.centro {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
}

.card {
  background: white;
  width: 90%;
  max-width: 420px;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.card input { width: 100%; padding: 8px; margin: 4px 0 12px 0; box-sizing: border-box; }

button {
  background: #16a34a;
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 8px;
  cursor: pointer;
}

@media (max-width: 600px) {
  header { flex-direction: column; gap: 8px; }
}
```

E o bônus de JavaScript, no fim do `<body>`:

```html
<button onclick="document.getElementById('titulo').textContent = 'Inscrição enviada!'">Testar JS</button>
<!-- o <h1> precisa ter id="titulo" -->
```

</details>

### ✅ Resumo de 1 minuto

- **HTML** = estrutura; **CSS** = aparência; **JavaScript** = comportamento.
- CSS externo: `<link rel="stylesheet" href="style.css">`. JS externo: `<script src="app.js"></script>`.
- Regra: `seletor { propriedade: valor; }`. Seletores: **tag** (`p`), **classe** (`.nome`), **id** (`#nome`), descendente (`nav a`), `:hover`.
- Especificidade: **id > classe > tag**; empate → vence a última regra.
- **Box model**: conteúdo → **padding** (dentro) → **border** → **margin** (fora).
- **Flexbox** no pai: `display: flex; justify-content: center; align-items: center;` centraliza tudo. `space-between` = pontas.
- **Responsivo**: meta **viewport** (área visível), medidas relativas e `@media (max-width: …)`.
- **JS**: `let`/`const`, `console.log`, tipos primitivos **number, string, boolean, undefined, null**. `document.getElementById(...)` mexe na página.
