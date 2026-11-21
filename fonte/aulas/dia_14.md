## Dia 14 (05/12) — Laboratório 1: uma página completa em HTML e CSS

A prova escrita passou. Agora começa o treino para **terça, 08/12, às 13h**: **avaliação prática no laboratório + entrevista**, das 13h às 15h30. É a etapa que, nos últimos 4 anos, **nenhum** dos 9 candidatos que passaram da escrita conseguiu vencer. A Etec não publica o enunciado da prática, mas o edital diz que ela avalia **a parte profissionalizante** — as matérias técnicas do 1º ano. As três tarefas mais prováveis são as dos Dias 14, 15 e 16: **uma página web**, **um programa simples** e **um banco de dados**.

> [!IMPORTANT]
> **Regra destes três dias: tudo no computador, digitando, sem copiar e colar.** No laboratório você vai estar sozinho diante de uma tela em branco. O treino é chegar lá já tendo feito isso várias vezes, cronometrando.

### 1. Como deve ser a prova prática

Não sabemos o enunciado exato, mas provas práticas de Etec costumam seguir este formato:

- um **enunciado impresso** ou na tela, pedindo algo como "crie uma página sobre X com estes elementos";
- um **tempo limitado** (o edital reserva das 13h às 15h30 para a prática **e** a entrevista);
- um **computador do laboratório** com **VS Code** (ou Bloco de Notas) e navegador — o Plano de Curso lista o VS Code, o Visual Studio e ferramentas de banco de dados;
- salvar o trabalho numa **pasta indicada** pelo professor;
- às vezes, o professor pede para você **explicar o que fez**.

O que os professores olham: **a página funciona?** **Tem os elementos pedidos?** **O código está organizado e indentado?** **Você sabe explicar o que escreveu?** Uma página simples, completa e explicada vale mais que uma página bonita pela metade.

### 2. Preparando o ambiente (5 minutos no dia)

**Com VS Code:**

1. Crie uma pasta com o nome pedido (ex.: `prova-henrique`) onde o professor indicar.
2. No VS Code: **Arquivo → Abrir Pasta** e escolha essa pasta.
3. Clique no ícone de **novo arquivo** e crie `index.html`. Depois crie `style.css`.
4. No `index.html`, digite **`!`** e aperte **Tab**: o VS Code escreve o esqueleto do HTML5 (o atalho se chama Emmet). Confira se apareceu `<meta charset="UTF-8">` e `<meta name="viewport" …>`. Troque `lang="en"` por `lang="pt-BR"`.
5. Para ver a página: abra a pasta no Explorador de Arquivos e dê **dois cliques** no `index.html`. A cada mudança: **Ctrl + S** no VS Code e **F5** no navegador.

**Sem VS Code (só Bloco de Notas):** escreva o código, vá em **Arquivo → Salvar como**, escolha **"Todos os arquivos"**, digite `index.html` e, em **Codificação**, escolha **UTF-8**. Sem isso, o arquivo vira `index.html.txt` ou os acentos quebram.

**Atalhos que economizam tempo no VS Code:**

| Atalho | Faz |
|---|---|
| `!` + Tab | esqueleto HTML |
| digitar `ul>li*3` + Tab | cria uma lista com 3 itens |
| `Ctrl + S` | salvar |
| `Shift + Alt + F` | arruma a indentação do arquivo |
| `Ctrl + /` | comenta/descomenta a linha |
| `Alt + ↑/↓` | move a linha para cima/baixo |

### 3. Construindo uma página do zero, em 5 etapas

Enunciado de treino (no estilo do que pode cair):

> *"Crie uma página de apresentação para um evento de games da escola. A página deve ter: um cabeçalho com o nome do evento e um menu com dois links; uma seção com uma descrição, uma imagem e uma lista dos jogos; uma tabela com a programação (horário e atividade); um formulário de inscrição (nome, e-mail, idade, jogo preferido e botão enviar) com método POST; e um rodapé. Use um arquivo CSS externo, com o conteúdo centralizado e o formulário em um cartão."*

**Etapa 1 — esqueleto e estrutura semântica.** Antes de qualquer conteúdo, monte as "caixas":

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Game Day Etec</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header></header>
  <main></main>
  <footer></footer>
</body>
</html>
```

Salve e abra no navegador (vai aparecer só a aba com o título). **Teste cedo e teste sempre.**

**Etapa 2 — cabeçalho e menu.**

```html
<header>
  <h1>Game Day Etec 2026</h1>
  <nav>
    <a href="#jogos">Jogos</a>
    <a href="#inscricao">Inscrição</a>
  </nav>
</header>
```

Os links com `#` levam até o elemento com aquele `id` na mesma página.

**Etapa 3 — conteúdo: texto, imagem, lista e tabela.**

```html
<main>
  <section id="jogos">
    <h2>Sobre o evento</h2>
    <p>Um sábado inteiro de campeonatos entre as turmas, com <strong>premiação</strong> para os três primeiros lugares.</p>
    <img src="https://placehold.co/400x200" alt="Foto do laboratório preparado para o campeonato">

    <h3>Jogos do campeonato</h3>
    <ul>
      <li>Minecraft (construção em dupla)</li>
      <li>FIFA (mata-mata)</li>
      <li>Valorant (equipes de 5)</li>
    </ul>

    <h3>Programação</h3>
    <table>
      <tr><th>Horário</th><th>Atividade</th></tr>
      <tr><td>9h</td><td>Abertura</td></tr>
      <tr><td>10h</td><td>Fase de grupos</td></tr>
      <tr><td>15h</td><td>Finais e premiação</td></tr>
    </table>
  </section>
```

Se o laboratório não tiver internet, use uma imagem que já esteja no computador, **na mesma pasta**: `<img src="foto.jpg" alt="…">` — o nome tem que ser **idêntico**, inclusive maiúsculas e extensão.

**Etapa 4 — formulário.**

```html
  <section id="inscricao" class="card">
    <h2>Inscrição</h2>
    <form action="#" method="post">
      <label for="nome">Nome</label>
      <input type="text" id="nome" name="nome" required>

      <label for="email">E-mail</label>
      <input type="email" id="email" name="email" required>

      <label for="idade">Idade</label>
      <input type="number" id="idade" name="idade" min="10" max="99">

      <label for="jogo">Jogo preferido</label>
      <select id="jogo" name="jogo">
        <option value="minecraft">Minecraft</option>
        <option value="fifa">FIFA</option>
        <option value="valorant">Valorant</option>
      </select>

      <button type="submit">Enviar inscrição</button>
    </form>
  </section>
</main>

<footer>
  <p>Etec de Taboão da Serra — Desenvolvimento de Sistemas</p>
</footer>
```

O `<select>` cria uma **lista suspensa**; cada `<option>` é uma opção.

**Etapa 5 — o CSS (style.css).**

```css
* { box-sizing: border-box; }               /* width passa a incluir padding e borda */

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f1f5f9;
  color: #1e293b;
}

header {
  background: #1e3a8a;
  color: white;
  padding: 16px 24px;
  display: flex;                            /* título e menu lado a lado */
  justify-content: space-between;          /* um em cada ponta */
  align-items: center;                      /* centralizados na vertical */
}

nav a { color: #bfdbfe; margin-left: 16px; text-decoration: none; }
nav a:hover { color: white; }

main {
  max-width: 800px;                         /* conteúdo não fica largo demais */
  margin: 0 auto;                           /* centraliza o main na tela */
  padding: 16px;
}

img { max-width: 100%; border-radius: 8px; }

table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #94a3b8; padding: 8px; text-align: left; }
th { background: #dbeafe; }

.card {
  background: white;
  padding: 24px;
  margin-top: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

form { display: flex; flex-direction: column; }   /* campos um embaixo do outro */
input, select { padding: 8px; margin: 4px 0 12px 0; }

button {
  background: #16a34a;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
}

footer { text-align: center; padding: 16px; color: #64748b; }

@media (max-width: 600px) {
  header { flex-direction: column; gap: 8px; }
}
```

Salve tudo e confira no navegador. Aperte **F12** e use o modo celular para ver a versão pequena.

### 4. Quando algo não funciona (os 8 problemas mais comuns)

| Sintoma | Causa provável | Conserto |
|---|---|---|
| Mudei e nada mudou | não **salvou** o arquivo | Ctrl + S e F5 |
| O CSS não aplica nada | o `<link>` está errado (nome, pasta) ou faltou `rel="stylesheet"` | confira `href="style.css"` e se o arquivo se chama exatamente assim |
| Só parte do CSS funciona | faltou `;` ou `}` numa regra anterior | olhe a regra **antes** da que falhou |
| Imagem não aparece (ícone quebrado) | nome/caminho errado, maiúsculas diferentes | o arquivo está na mesma pasta? o nome bate letra por letra? |
| Acentos viram "Ã©" | faltou `<meta charset="UTF-8">` ou o arquivo não foi salvo em UTF-8 | coloque a meta e salve em UTF-8 |
| A página mostra o código em vez de rodar | o arquivo está salvo como `.txt` | renomeie para `.html` |
| Um pedaço da página "sumiu" ou ficou torto | tag não fechada (`<div>` sem `</div>`) | use Shift + Alt + F para indentar e veja onde a estrutura quebra |
| O link `#inscricao` não funciona | o `id` não existe ou está escrito diferente | `href="#inscricao"` precisa de `id="inscricao"` |

**O DevTools (F12) é seu melhor amigo no laboratório:** clique com o botão direito no elemento que está estranho → **Inspecionar**. À direita aparecem as regras de CSS aplicadas — as riscadas foram vencidas por outras.

### 5. Explicando o que você fez

Se o professor perguntar, explique **com as palavras da matéria**. Ensaie em voz alta:

- "Usei as tags semânticas **header, main e footer** para organizar a estrutura."
- "Liguei o CSS **externo** com a tag **link** dentro do **head**."
- "No cabeçalho, usei **display flex** com **justify-content space-between** para deixar o título de um lado e o menu do outro."
- "O formulário usa o método **POST** porque envia dados pessoais; o GET deixaria os dados na URL."
- "Coloquei o **alt** na imagem por **acessibilidade**: leitores de tela leem esse texto."
- "O **padding** é o espaço interno do cartão; o **margin** é o espaço externo."

### 6. Desafios cronometrados

Faça **sem consultar** a aula. Ligue o cronômetro do celular. Só depois de terminar, abra o modelo.

<details class="recall-box">
<summary>⏱️ Desafio 1 (15 min) — Cartão de perfil: página com um cartão centralizado na tela (vertical e horizontal) contendo uma foto (com alt), seu nome em h1, um parágrafo e uma lista de 3 hobbies. CSS externo.</summary>

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meu perfil</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="card">
    <img src="https://placehold.co/120" alt="Foto de perfil">
    <h1>Henrique</h1>
    <p>Estudante de Desenvolvimento de Sistemas.</p>
    <ul>
      <li>Games</li>
      <li>Música</li>
      <li>Futebol</li>
    </ul>
  </div>
</body>
</html>
```

```css
body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #e2e8f0;
  font-family: Arial, sans-serif;
}
.card {
  background: white;
  padding: 24px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}
.card img { border-radius: 50%; }
.card ul { text-align: left; }
```

O segredo da centralização total: o **pai** (`body`) com `display: flex`, `justify-content: center`, `align-items: center` e **altura** (`min-height: 100vh`).

</details>

<details class="recall-box">
<summary>⏱️ Desafio 2 (20 min) — Cardápio da cantina: título, uma tabela com 5 itens (produto, preço), os preços alinhados à direita, linhas alternando cor de fundo, e um link "Voltar ao topo" que leva ao título.</summary>

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Cantina</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1 id="topo">Cardápio da Cantina</h1>
  <table>
    <tr><th>Produto</th><th>Preço</th></tr>
    <tr><td>Coxinha</td><td class="preco">R$ 7,00</td></tr>
    <tr><td>Pão de queijo</td><td class="preco">R$ 4,00</td></tr>
    <tr><td>Suco</td><td class="preco">R$ 6,00</td></tr>
    <tr><td>Bolo</td><td class="preco">R$ 5,00</td></tr>
    <tr><td>Água</td><td class="preco">R$ 3,00</td></tr>
  </table>
  <a href="#topo">Voltar ao topo</a>
</body>
</html>
```

```css
table { border-collapse: collapse; width: 300px; }
th, td { padding: 8px; border-bottom: 1px solid #ccc; }
th { background: #1e3a8a; color: white; }
tr:nth-child(even) { background: #f1f5f9; }   /* linhas pares com fundo */
.preco { text-align: right; }
```

`tr:nth-child(even)` pega as linhas **pares** — o jeito de fazer a "zebra".

</details>

<details class="recall-box">
<summary>⏱️ Desafio 3 (30 min) — Página de 3 cursos: header com título e menu, três "cards" lado a lado (cada um com título, texto e botão), que ficam um embaixo do outro no celular, e um rodapé.</summary>

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cursos</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Etec Cursos</h1>
    <nav><a href="#">Início</a> <a href="#">Contato</a></nav>
  </header>
  <main class="cursos">
    <article class="card">
      <h2>DS</h2>
      <p>Desenvolvimento de Sistemas.</p>
      <button>Saiba mais</button>
    </article>
    <article class="card">
      <h2>Informática</h2>
      <p>Hardware, redes e programação.</p>
      <button>Saiba mais</button>
    </article>
    <article class="card">
      <h2>Internet</h2>
      <p>Sites e aplicações web.</p>
      <button>Saiba mais</button>
    </article>
  </main>
  <footer>Etec de Taboão da Serra</footer>
</body>
</html>
```

```css
body { margin: 0; font-family: Arial, sans-serif; }
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  background: #0f172a;
  color: white;
}
nav a { color: white; margin-left: 12px; }
.cursos { display: flex; gap: 16px; padding: 24px; }
.card {
  flex: 1;                         /* os três dividem o espaço igualmente */
  padding: 16px;
  border: 1px solid #cbd5e1;
  border-radius: 10px;
}
footer { text-align: center; padding: 16px; background: #e2e8f0; }
@media (max-width: 600px) {
  .cursos { flex-direction: column; }
  header { flex-direction: column; }
}
```

</details>

### ✅ Checklist do laboratório (repita até fazer sem pensar)

- [ ] Esqueleto com `<!DOCTYPE html>`, `lang="pt-BR"`, `<meta charset="UTF-8">`, viewport e `<title>`
- [ ] CSS externo ligado com `<link rel="stylesheet" href="style.css">`
- [ ] Estrutura com `header`, `nav`, `main`, `section`, `footer`
- [ ] Títulos em ordem (`h1` → `h2` → `h3`), parágrafos, `strong`
- [ ] Lista (`ul`/`ol` + `li`), imagem **com alt**, link com `href`
- [ ] Tabela com `tr`, `th`, `td`
- [ ] Formulário com `label for` + `id`, tipos de input, `method="post"` e botão `submit`
- [ ] Flexbox: `display: flex`, `justify-content`, `align-items`
- [ ] Box model: `padding`, `border`, `margin`, `border-radius`
- [ ] `@media (max-width: 600px)` mudando o layout
- [ ] Código indentado (Shift + Alt + F) e salvo na pasta certa
- [ ] Saber explicar cada parte em voz alta

### ✅ Resumo de 1 minuto

- A prática de 08/12 avalia as **matérias técnicas do 1º ano**; a página web é uma das tarefas mais prováveis.
- No laboratório: pasta → VS Code → `index.html` (`!` + Tab) → `style.css` → **salvar e testar a cada etapa**.
- Construa em etapas: **esqueleto → cabeçalho → conteúdo → formulário → CSS**.
- Problemas: não salvou, `<link>` errado, `;` faltando, nome da imagem, `charset`.
- Saiba **explicar**: semântica, CSS externo, Flexbox, POST, alt, padding × margin.
