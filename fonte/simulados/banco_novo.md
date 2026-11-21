---
id: novas
titulo: Questões inéditas no estilo de Taboão
data: 11/2026
curso: DS
gabarito: elaborado para a plataforma
completa: nao
---

## 1 | web | Onde ligar o CSS externo
Qual linha, colocada dentro do `<head>`, liga corretamente uma folha de estilos externa chamada `estilo.css` a uma página HTML?

A) `<style src="estilo.css"></style>`
B) `<script src="estilo.css"></script>`
C) `<css href="estilo.css">`
D) `<link rel="stylesheet" href="estilo.css">`
E) `<a href="estilo.css">`

> Resposta: D

CSS externo entra com **`<link rel="stylesheet" href="…">`** no `<head>`. `<script src>` é para **JavaScript**; `<style>` serve para CSS escrito **dentro** da página (não tem `src`); `<css>` não existe; `<a href>` é um link clicável.

## 2 | web | Seletor de classe
Na página há `<p class="alerta">Atenção!</p>`. Qual regra CSS deixa esse parágrafo vermelho, sem afetar os outros parágrafos?

A) `.alerta { color: red; }`
B) `#alerta { color: red; }`
C) `p { color: red; }`
D) `alerta { color: red; }`
E) `class.alerta { color: red; }`

> Resposta: A

Classe se seleciona com **ponto**: `.alerta`. `#alerta` pegaria um elemento com `id="alerta"`; `p` pegaria **todos** os parágrafos; `alerta` sem ponto procuraria uma tag `<alerta>`.

## 3 | web | Ordem das camadas do box model
No box model do CSS, qual é a ordem correta das camadas, **de dentro para fora**?

A) margin → border → padding → conteúdo
B) conteúdo → border → padding → margin
C) conteúdo → padding → border → margin
D) padding → conteúdo → margin → border
E) conteúdo → margin → border → padding

> Resposta: C

De dentro para fora: **conteúdo → padding (espaço interno) → border (borda) → margin (espaço externo)**. A alternativa A é a ordem certa, mas **de fora para dentro**.

## 4 | web | Largura total de uma caixa
Um elemento tem `width: 300px; padding: 15px; border: 3px solid black; margin: 10px;` e usa o `box-sizing` padrão (`content-box`). Qual é a largura dele **da borda esquerda até a borda direita**?

A) 300 px
B) 318 px
C) 330 px
D) 356 px
E) 336 px

> Resposta: E

Com `content-box`, o `width` é só o conteúdo. Some o padding e a borda **dos dois lados**: 300 + 15 + 15 + 3 + 3 = **336 px**. A margem (10 px de cada lado) fica **fora** da borda, por isso não entra. Quem esquece de contar os dois lados marca 318.

## 5 | web | justify-content
Em um contêiner com `display: flex;` e `flex-direction: row;`, qual valor de `justify-content` coloca o primeiro item colado na esquerda, o último colado na direita e distribui o espaço restante **igualmente entre** os itens?

A) `center`
B) `space-between`
C) `flex-start`
D) `stretch`
E) `flex-end`

> Resposta: B

**`space-between`** = espaço **entre** os itens, com as pontas coladas nas bordas. `center` junta tudo no meio; `flex-start` e `flex-end` juntam no começo ou no fim. `stretch` é valor de `align-items`, não de `justify-content`.

## 6 | web | Media query
Considere o CSS:

```css
.menu { display: flex; }
@media (max-width: 600px) {
  .menu { flex-direction: column; }
}
```

É correto afirmar que:

A) em telas com **mais** de 600 px, os itens do menu ficam um embaixo do outro.
B) a regra dentro do `@media` vale para todas as telas.
C) em telas de **até** 600 px de largura, os itens do menu ficam um embaixo do outro.
D) o `@media` só funciona se o HTML tiver uma tag `<media>`.
E) `max-width: 600px` limita a largura do menu a 600 px em qualquer tela.

> Resposta: C

`@media (max-width: 600px)` significa "**se a tela tiver no máximo 600 px**". Nessas telas (celulares), o menu vira coluna. Em telas maiores, vale só o `display: flex` normal (itens lado a lado). E erra porque aqui o `max-width` é uma **condição da tela**, não uma propriedade do menu.

## 7 | web | Tipos primitivos em JavaScript
Observe o código JavaScript:

```javascript
let a = "16";
let b = 16;
let c = false;
```

Os tipos de `a`, `b` e `c` são, respectivamente:

A) number, number, boolean
B) string, string, boolean
C) string, number, undefined
D) string, number, boolean
E) number, string, boolean

> Resposta: D

`"16"` está **entre aspas** → **string** (texto). `16` sem aspas → **number**. `false` → **boolean**. A pegadinha é achar que `"16"` é número: com aspas, é texto.

## 8 | web | Incluir JavaScript externo
Qual é a forma correta de incluir o arquivo `app.js` em uma página HTML?

A) `<link rel="script" href="app.js">`
B) `<javascript src="app.js"></javascript>`
C) `<script href="app.js"></script>`
D) `<js file="app.js"></js>`
E) `<script src="app.js"></script>`

> Resposta: E

JavaScript externo: **`<script src="…"></script>`** (src = *source*, origem). `href` é atributo do `<link>` e do `<a>`; `<javascript>` e `<js>` não existem.

## 9 | web | Display none
Ao aplicar `display: none;` a um elemento, o que acontece?

A) O elemento fica transparente, mas continua ocupando espaço.
B) O elemento some da página e não ocupa espaço.
C) O elemento passa a ficar em linha com o texto.
D) O elemento é apagado do arquivo HTML.
E) O elemento fica em negrito.

> Resposta: B

`display: none` **esconde** o elemento e o **tira do layout** (os outros ocupam o lugar dele). Ele continua no HTML (D errada). Ficar transparente ocupando espaço é o que faz `visibility: hidden` ou `opacity: 0` (A).

## 10 | web | Especificidade
Considere o HTML `<p id="aviso" class="texto">Olá</p>` e o CSS:

```css
p { color: black; }
.texto { color: blue; }
#aviso { color: green; }
```

De que cor o texto aparece?

A) verde
B) azul
C) preto
D) vermelho, a cor padrão dos avisos
E) depende da ordem das regras no arquivo

> Resposta: A

Quando várias regras mandam no mesmo elemento, vence a **mais específica**: **id > classe > tag**. O seletor `#aviso` (id) vence `.texto` (classe) e `p` (tag), então o texto fica **verde**. A ordem só desempata regras de **mesma** força (E errada).
