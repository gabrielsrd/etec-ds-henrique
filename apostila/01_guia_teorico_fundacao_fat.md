# Guia Teórico Completo — Vagas Remanescentes Etec (2º Ano M-Tec / Desenvolvimento de Sistemas)

Este manual reúne **explicações completas passo a passo, contexto no mundo real, exemplos comentados linha a linha, quadros comparativos e questões dissecadas** cobrindo 100% do programa técnico (Fundação FAT / CPS) e da Base Comum do 1º ano M-Tec.

---

## 🗣️ Portugol & Sintaxe do Zero: Guia para Ler Qualquer Código na Prova (Sem Nunca Ter Programado!)

Se você nunca programou em C, Java, JavaScript ou Python, pode respirar aliviado: **na prova da Etec (Fundação FAT / M-Tec) você NÃO precisa escrever programas do zero nem decorar ponto e vírgula**. Todas as 30 ou 40 questões são de múltipla escolha (`A` a `E`).

O que você precisa é **saber LER trechos curtos de 4 a 10 linhas** que já vêm prontos na questão. Este guia traduz cada símbolo estranho para português claro!

---

### 1. O que é Portugol (Pseudocódigo) e Por que Cai na Prova?

**Portugol** é uma forma didática de escrever algoritmos usando palavras em **Português** (como `leia`, `escreva`, `se`, `entao`, `enquanto`) para que qualquer estudante entenda a lógica sem depender de inglês ou de compiladores complexos.

Todo algoritmo clássico em Portugol (estilo VisuAlg) tem esta cara:

```portugol
algoritmo "MediaDoHenrique"
var
    n1, n2, media: real      // Declara as "caixinhas" (variáveis) e o tipo delas
inicio                       // Aqui começa a execução linha por linha
    leia(n1, n2)             // Lê o que a pessoa digitou (ex.: 8 e 6)
    media <- (n1 + n2) / 2   // Calcula e GUARDA 7.0 dentro de 'media'
    se (media >= 6) entao
        escreva("Aprovado!") // Mostra na tela
    senao
        escreva("Recuperação")
    fimse
fimalgoritmo
```

> [!TIP]
> **Regras visuais rápidas:** Tudo depois de `//` (ou entre `/* ... */`) é apenas **comentário explicativo** para humanos — o computador ignora na hora de rodar! E `;` (ponto e vírgula) em C/Java/JS serve apenas como o "ponto final" de uma frase.

---

### 2. Tabela Tradutora Completa: Português ↔ Portugol ↔ C / Java / JS / Python

Sempre que bater o olho numa questão da prova com código, use esta tabela mental:

| O que faz na prática | Como vem em **Portugol** | Como vem em **C / Java / JS / Python** | Atenção à pegadinha! |
| :--- | :--- | :--- | :--- |
| **Guardar valor** *(Atribuição)* | `x <- 10` ou `x := 10` | `x = 10;` (C/Java/JS) ou `x = 10` (Py) | `=` sozinho ou `<-` significa **"recebe / guarda dentro"**, NÃO é pergunta de igualdade! |
| **Comparar igualdade** *(Pergunta)* | `x = 10` ou `x == 10` | `x == 10` (ou `x === 10` no JS) | Pergunta: *"O valor dentro de x é igual a 10?"* (Responde Verdadeiro ou Falso). |
| **Diferente de** | `x <> 10` ou `x != 10` | `x != 10` | Retorna Verdadeiro quando `x` **não** for `10`. |
| **Somar +1** *(Incremento)* | `x <- x + 1` | `x++` ou `x += 1` | **`x++` é apenas um atalho preguiçoso para `x = x + 1`!** (`x--` subtrai 1). |
| **Acumular soma** | `soma <- soma + x` | `soma += x;` | Pega o valor antigo de `soma`, soma `x` e guarda o total de volta em `soma`. |
| **Quociente Inteiro** | `17 DIV 5` (dá **`3`**) | `17 / 5` (entre 2 `int` em C/Java) ou `17 // 5` (Py) | Descarta o que sobrou e fica só com a parte inteira! |
| **Resto da Divisão** | `17 MOD 5` (dá **`2`**) | `17 % 5` | Símbolo **`%`** em código **NÃO** é porcentagem — é **MOD (resto da divisão)**! |
| **Bloco de Decisão** | `se (cond) entao ... senao ... fimse` | `if (cond) { ... } else { ... }` | As chaves **`{ }`** em C/Java/JS fazem exatamente o papel de **`entao ... fimse`** (agrupam o bloco)! |
| **Repetição Pré-Teste** | `enquanto (x <= 5) faca ... fimenquanto` | `while (x <= 5) { ... }` | Testa antes! Se já começar falso, não executa nenhuma vez. |
| **Repetição Pós-Teste** | `repita ... ate (x > 5)` | `do { ... } while (x <= 5);` | **Executa pelo menos 1 vez** e só testa a parada no final! |
| **Repetição Contada** | `para i de 0 ate 2 faca ... fimpara` | `for (int i = 0; i <= 2; i++) { ... }` | Começa em `0`, repete enquanto `i <= 2`, somando `+1` (`i++`) a cada volta (`i = 0, 1, 2`). |
| **Vetor e Matriz** | `v[0]`, `M[i, j]` ou `M[i][j]` | `v[0]`, `M[i][j]` | Em C/Java/JS/Python a contagem sempre começa na gaveta **`0`** (`M[linha][coluna]`). |

---

### 3. O Mesmo Algoritmo Escrito Lado a Lado (Para Nunca Mais Estranhar!)

Veja como somar os números pares de `0` a `4` parece idêntico quando você entende as chaves `{}` e o `%`:

**Em Portugol (Estilo Prova Teórica):**
```portugol
soma <- 0
para i de 0 ate 4 faca
    se (i MOD 2 == 0) entao
        soma <- soma + i
    fimse
fimpara
escreva(soma)
```

**Exatamente o mesmo algoritmo em JavaScript / C / Java:**
```javascript
let soma = 0;
for (let i = 0; i <= 4; i++) {
    if (i % 2 == 0) {
        soma += i;
    }
}
console.log(soma);
```
> **Por que imprime `6` nos dois?**
> - Volta `i = 0`: `0 % 2 == 0` (V) → `soma` = `0 + 0 = 0`
> - Volta `i = 1`: `1 % 2 == 1` (F) → ignora
> - Volta `i = 2`: `2 % 2 == 0` (V) → `soma` = `0 + 2 = 2`
> - Volta `i = 3`: `3 % 2 == 1` (F) → ignora
> - Volta `i = 4`: `4 % 2 == 0` (V) → `soma` = `2 + 4 = 6`
> - Próximo passo `i` vira `5`, falha em `i <= 4` → **Fim! Resultado: `6`!**

---

### 4. Guia Relâmpago das Outras 3 Sintaxes que Caem Prontas na Prova

Você também não precisa decorar comandos avançados de Banco de Dados ou Web — basta reconhecer visualmente estas peças:

#### A. Como Ler SQL em 30 Segundos (Dias 6 e 7)
Olhe sempre para a **PRIMEIRA PALAVRA** em maiúsculo do comando:
1. **`CREATE` / `ALTER` / `DROP`** → É **DDL** (*mexe na estrutura/tabela inteira*). Ex.: `ALTER TABLE alunos ADD cpf VARCHAR(11);`
2. **`INSERT` / `UPDATE` / `DELETE`** → É **DML** (*insere, altera ou apaga linhas/dados dentro da tabela*). Ex.: `DELETE FROM alunos WHERE id = 2;`
3. **`SELECT`** → É **DQL** (*consulta/lê dados*). Fórmula favorita da banca FAT:
   `SELECT COUNT(*) FROM tabela WHERE condicao;`
   *(Tradução direta: "**SELECIONE A CONTAGEM DE LINHAS** (`COUNT(*)`) **DA TABELA** `tabela` **ONDE** (`WHERE`) a condição for verdadeira!").* **Regra fatal:** `COUNT(*)` nunca vai depois do `WHERE`!

#### B. Como Ler Tags HTML5 em 30 Segundos (Dia 9)
HTML usa etiquetas entre sinais de menor/maior abrindo `<tag>` e fechando com barra `</tag>`:
```html
<a href="https://etec.sp.gov.br" target="_blank">Clique aqui</a>
```
- `a` = é o nome da **Tag** (aqui, um **link**).
- `href="..."` e `target="_blank"` = são **Atributos** dando superpoderes à tag (`_blank` manda abrir em **nova aba**!).
- **Tags para reconhecer de olho fechado:**
  - `<body>...</body>` → Todo conteúdo **visível** na página (`<head>` é invisível/configuração).
  - `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` → **Tags Semânticas HTML5**.
  - `<div>` e `<span>` → **Caixas Genéricas SEM semântica**.
  - `<ol>` → Lista **Ordenada** (`1, 2, 3`); `<ul>` → Lista **Não Ordenada** (`• • •`); `<li>` → cada **Item** dentro delas.
  - `<table>` → Tabela; **`<tr>`** → **Linha** (*Table Row*); **`<td>`** → **Célula comum** (*Table Data*); **`<th>`** → Título da coluna.
  - `<form method="POST">` → Esconde dados como **senha** no corpo da requisição (nunca use `GET` para senhas, pois aparece na URL!).

#### C. Como Ler Regras CSS3 em 30 Segundos (Dia 9)
Toda regra CSS segue este único modelo visual:
```css
.cartao {
    padding: 16px;
    margin: 20px;
    transform: scale(1.2);
}
```
- **Antes da chave `{` é o Seletor** (quem vai mudar de visual: `h1` muda toda tag `<h1>`; **`.`** muda uma **classe**; **`#`** muda um **ID único**).
- **Dentro de `{ ... }` vêm `propriedade: valor;`**:
  - `padding` = acolchoamento **interno** (entre o texto e a borda).
  - `margin` = espaçamento **externo** (afasta caixas vizinhas).
  - `transform: scale(...) / rotate(...) / translate(...) / skew(...)` = aumenta/gira/move/inclina o elemento.


---

## Dia 1 — Raio-X da Banca FAT, Memória, Tipos de Dados, DIV/MOD e Tabela Verdade do Zero

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine que você vai fazer um **Pix** no aplicativo do banco. Na tela aparecem várias informações bem diferentes entre si:
- O **nome** de quem vai receber (`"Maria Oliveira"`);
- O **valor** em reais com centavos (`150.75`);
- A **quantidade** de parcelas de uma compra (`3`);
- Uma **letra** indicando o tipo de conta (`'C'` de Corrente ou `'P'` de Poupança);
- Uma **confirmação** simples de "Sim ou Não" (`Você tem saldo suficiente? Sim`).

Para você, tudo na tela parece apenas "coisas escritas". Mas um computador **não enxerga texto nem dinheiro como nós** — lá dentro, os chips só entendem sinais elétricos ligados ou desligados (`0` e `1`). Para que o aplicativo **não tente multiplicar o nome `"Maria"` por `2`** e **não corte os centavos `0.75` fora**, o programador precisa etiquetar cada informação dizendo o que ela é (número inteiro, decimal, texto, letra única ou resposta Sim/Não) e ensinar o programa a fazer **contas e comparações lógicas**. É exatamente esse alicerce que cai logo nas primeiras questões da **Fundação FAT / Etec**!

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

Mesmo sem nunca ter escrito uma linha de código na vida, você já usa toda a lógica da aula de hoje quando joga no PC/celular ou conversa no Discord:
- Na barra de status do seu personagem, sua **vida (`100`)** é um número exato sem vírgula; a **taxa de acertos (`2.45`)** precisa de casas decimais; o **nick (`"Henrique_BR"`)** é um texto livre; o **time (`'A'` ou `'B'`)** é uma única letra; e **"Está vivo?"** só pode responder **Sim ou Não**.
- Quando você tem **150 blocos de ferro no Minecraft** e cada espaço da mochila fecha em **64 blocos**, você faz automaticamente duas contas: **quantos pacotes cheios deu (`2`)** e **quantos blocos ficaram soltos no último espaço (`22`)**. Em programação, essas duas contas têm nomes famosos que vamos aprender hoje.
- Quando um jogo decide se você pode entrar numa **partida ranqueada**, ele testa regras do tipo: *"Você tem nível mínimo **E** não está banido?"* — basta uma dessas condições falhar para o servidor barrar a entrada.

Tudo na aula de hoje é transformar essas situações óbvias em linguagem que a banca da prova cobra!

---

### 📚 Parte 1 — Os 4 Moldes Secretos da Banca Fundação FAT

Antes de entrar nos cálculos, vale conhecer **como a banca que faz a prova da Etec pensa**. Analisando provas oficiais anteriores (*DS 2025, Informática 2025, DS 2019 e M-Tec 2022*), quase 100% das questões técnicas repetem sempre apenas **4 formatos (moldes) previsíveis**:

| Molde da Banca | Como a Questão Aparece na Prova | Como Resolver Sem Cair em Armadilha |
| :--- | :--- | :--- |
| **Molde 1 — Afirmativas I, II e III** | Mostra 3 frases sobre um assunto e pergunta quais são verdadeiras (ex.: *Apenas I e II estão corretas*). | **9 em cada 10 vezes**, a banca pega duas definições parecidas e **troca uma pela outra** (inverte os conceitos!). Encontrou **1 frase claramente falsa**? Risque todas as alternativas (A–E) que citam esse número — você quase sempre elimina 3 letras na hora! |
| **Molde 2 — Lista com Intruso** | *"Assinale a alternativa que apresenta APENAS [itens de uma mesma categoria]."* | Nas 4 alternativas erradas existe **1 único item "intruso"** misturado no meio de itens certos (ex.: colocar *Excel* no meio de navegadores de internet, ou misturar uma licença no meio de frameworks — você verá cada lista dessas nos próximos dias!). |
| **Molde 3 — Cenário / Definição Direta** | Descreve um problema real e pede o nome técnico da solução. | Procure a palavra-chave exata do enunciado: por exemplo, *"corta fora as casas decimais"* aponta para um tipo específico de conversão; *"imagem que não borra no zoom"* aponta para imagem vetorial (que veremos no Dia 8). |
| **Molde 4 — Micro-Execução (Conta na Mão)** | Traz de 4 a 10 linhas de código curto ou tabela numérica e pergunta o resultado final na tela. | **Regra sagrada:** nunca faça de cabeça! Anote o passo a passo no rascunho acompanhando o valor de cada item linha por linha até o final. |

---

### 📚 Parte 2 — Como a Memória do PC Funciona: Bits, Bytes, Variáveis e os 5 Tipos Primitivos

#### 1. Primeiro: O que são Bits, Bytes e Memória RAM?
- **Bit:** É a menor unidade de informação do computador. Pense em uma lâmpada que só pode estar **apagada (`0`)** ou **acesa (`1`)**. Um único bit guarda só `0` ou `1`.
- **Byte:** Como `0` ou `1` sozinho guarda quase nada, os engenheiros juntaram grupinhos de **8 bits**, formando **1 Byte** (que permite criar `256` combinações diferentes de zeros e uns — o suficiente para representar uma letra do teclado ou um número pequeno).
- **Memória RAM (*Random Access Memory* — Memória de Acesso Aleatório):** É a **"mesa de trabalho" temporária** do computador enquanto um aplicativo está aberto. Tudo que o programa está calculando agora fica guardado ali em milhões de caixinhas/gavetas numeradas. *(Atenção: desligou o programa ou o PC, a RAM esvazia!)*

#### 2. Variável vs. Constante (As Gavetas com Rótulo)
Quando um programa precisa guardar uma informação na Memória RAM, ele cria uma **Variável**:
1. Reserva uma gaveta na memória;
2. Dá um **nome (rótulo)** para ela, por exemplo `vidas`;
3. Cola uma **etiqueta de tipo** dizendo o que cabe ali (número inteiro? texto?);
4. Coloca um valor lá dentro.

**Regra fundamental da Variável:** Como o próprio nome diz, o valor pode **variar** (mudar) durante o programa — **mas uma gaveta só guarda 1 valor por vez!** Se você faz:
```portugol
vidas <- 3      // A gaveta 'vidas' guarda o número 3
vidas <- 5      // O 3 é APAGADO da gaveta e substituído por 5!
```
No final, `vidas` vale **`5`**, nunca `3 e 5 ao mesmo tempo`!

Já uma **Constante** é uma gaveta especial **trancada com cadeado**: depois que você grava o valor uma vez (por exemplo `PI <- 3.14` ou `TAXA_FIXA <- 10`), o programa **proíbe alterar esse valor** até o fim.

#### 3. Por que o Computador Exige "Etiqueta de Tipo"? (E o que é a Tabela ASCII?)
A Memória RAM guarda só `0` e `1`. Como o computador sabe se a sequência binária `01000001` dentro de uma gaveta significa o número **`65`** ou a letra **`'A'`**?
Por causa da **etiqueta de tipo** e da **Tabela ASCII** (*American Standard Code for Information Interchange*):
- A **Tabela ASCII** é o dicionário padrão mundial que dá um número inteiro para cada letra, dígito e símbolo do teclado: na tabela ASCII, **`65` representa `'A'`**, **`66` representa `'B'`**, **`97` representa `'a'`**, e **`48` representa o caractere `'0'`**.
- Se a etiqueta da gaveta for **Inteiro**, o computador lê `65` (e deixa somar `+ 1`). Se a etiqueta for **Caractere**, o computador olha na Tabela ASCII e enxerga a letra **`'A'`**!
- Além disso, tipos diferentes reservam tamanhos diferentes na RAM: um inteiro comum costuma ocupar **4 bytes** (32 bits), um decimal de alta precisão ocupa **8 bytes** (64 bits), e um único caractere costuma usar **1 ou 2 bytes**.

#### 4. Os 5 Tipos Primitivos Oficiais da Prova

| Tipo Técnico | Outros nomes que aparecem na prova | O que guarda na memória | Exemplos válidos | Armadilha mortal da banca! |
| :--- | :--- | :--- | :--- | :--- |
| **Inteiro (`int`)** | `integer`, `Inteiro` (Portugol) | Apenas números **exatos, sem vírgula/ponto decimal** (positivos, negativos ou zero). | `0`, `16`, `-250`, `4096` | Se dividir dois números inteiros em linguagens como C ou Java (`5 / 2`), o computador descarta o `.5` e devolve **`2`**! |
| **Real (`float` / `double`)** | Ponto Flutuante, `Real` (Portugol) | Números com **casas decimais** (`double` tem o dobro da precisão e guarda mais casas que `float`). | `3.14`, `7.5`, `-0.05`, `10.0` | Em programação usa-se **ponto (`.`)**, nunca vírgula (`,`). E atenção: `10.0` é tratado como **Real**, mesmo valendo dez! |
| **Caractere (`char`)** | `Caractere` (letra/símbolo único) | **Exatamente 1 único símbolo** (uma letra, um dígito isolado, um `@` ou um espaço `' '`). | `'A'`, `'s'`, `'7'`, `'@'` | Costuma vir entre **aspas simples (`'A'`)**. A banca adora perguntar qual tipo guarda uma resposta `'A'`–`'E'` ou `'S'`/`'N'`! **Resposta: `char`!** |
| **Texto (`string`)** | `Cadeia`, `Literal`, `varchar` | Sequência com **0, 1 ou muitos caracteres** juntos em fila. | `"Etec DS"`, `"123"`, `""` (texto vazio) | Vem entre **aspas duplas (`"..."`)**. **`"10"` + `"20"`** não dá `30`, dá **`"1020"`** (o PC só gruda os dois textos = **concatenação**)! |
| **Booleano (`bool`)** | `Lógico` (Portugol), `boolean` | Apenas **dois estados lógicos** possíveis (sim ou não). | `true` (`Verdadeiro`) ou `false` (`Falso`) | **NUNCA usa aspas!** Se você escrever `"true"` entre aspas, vira texto (`string`) de 4 letras, não um booleano! |

> [!TIP]
> **Veja a diferença prática entre `7`, `7.0`, `'7'` e `"7"`:**
> - `7` → **`int`** (número inteiro, faz conta normalmente);
> - `7.0` → **`float`/`double`** (número real decimal);
> - `'7'` → **`char`** (apenas o desenho do símbolo 7 sozinho entre aspas simples);
> - `"7"` → **`string`** (um texto de 1 letra entre aspas duplas; se somar `"7" + "2"`, vira `"72"`!).

> [!WARNING]
> **Pegadinha real da banca (INFO 2025 Q19):** A questão pergunta qual tipo primitivo armazena adequadamente **um único caractere** (como `'M'` ou `'F'`). A resposta correta é **`char` / Caractere** — **NUNCA** marque `boolean` (que só guarda `true`/`false`) nem `float` (que guarda decimais)!

#### 🎮 Conexão Gamer: Os 5 Tipos na HUD de um Jogo
Olhando a tela de um FPS ou RPG:
- `hp = 100` → **`int`** (vida exata);
- `taxaKDA = 2.45` → **`float` / `double`** (precisa de vírgula decimal);
- `nick = "Henrique_BR"` → **`string`** (texto completo do nome);
- `ranking = 'S'` → **`char`** (uma única letra isolada);
- `estaVivo = true` / `mutado = false` → **`bool`** (ligado ou desligado).

---

### 🗣️ Como Ler Símbolos de Código na Prova (Mesmo Sem Nunca Ter Programado!)

Antes de olharmos exemplos com código, guarde esta "tradução instantânea" de 6 símbolos que aparecem em questões de prova:

| Símbolo no Código | Como se lê em Português | O que faz na prática |
| :---: | :--- | :--- |
| **`<-`** ou **`=`** (sozinho) | *"Recebe / Guarda dentro"* | **Atribuição:** `x <- 10` (Portugol) ou `x = 10;` (C/Java/JS/Python) guarda `10` na gaveta `x`. **NÃO é pergunta de igualdade!** |
| **`==`** (dois iguais juntos) | *"É igual a?"* | **Comparação (Pergunta):** `x == 10` testa se `x` vale `10` e responde `Verdadeiro` ou `Falso`. |
| **`!=`** ou **`<>`** | *"É diferente de?"* | **Comparação:** `x != 10` dá `Verdadeiro` se `x` for qualquer número diferente de `10`. |
| **`++`** / **`--`** | *"Soma +1 / Subtrai -1"* | **Atalho:** `i++` é só um jeito preguiçoso de escrever **`i <- i + 1`**. (`i--` significa `i <- i - 1`). |
| **`+=`** | *"Soma e guarda de volta"* | **Atalho acumulador:** `soma += 5` é o mesmo que **`soma <- soma + 5`**. |
| **`{ ... }`** e **`;`** | *"Abraça o bloco / Ponto final"* | Em C, Java e JS, `{ }` agrupa instruções juntas, e `;` funciona apenas como o ponto final da linha. |

---

### 📚 Parte 3 — Conversão de Tipos: Implícita (*Coerção*) vs. Explícita (*Type Casting*)

Quando o usuário digita a idade no campo de um formulário na tela, tudo o que vem do teclado costuma chegar como **texto (`string`)**, como `"16"`. Para somar `+ 1`, precisamos transformar texto em número. Às vezes também precisamos guardar um número decimal dentro de uma variável inteira.

Na computação, existem exatamente **2 formas** de trocar o tipo de um dado *(atenção: antes, vale lembrar que o programa responsável por ler e executar seu código chama-se **tradutor** — um compilador ou interpretador, cuja diferença técnica veremos em detalhes no Dia 4)*:

#### 1. Conversão Implícita (*Coerção Automática*)
Acontece **automaticamente nos bastidores**: o próprio programa tradutor converte o tipo sem você escrever nenhum comando especial para isso.
- **Quando acontece?** Quando **não há risco de perder informação** — por exemplo, pegar um **`int` (gaveta menor)** e guardar dentro de um **`double` (gaveta maior)**:
  - `int pontos = 10;`
  - `double bonus = pontos;` → Automaticamente o computador transforma `10` em **`10.0`**! Cabe com folga e nada foi cortado fora.
- **Outro caso famoso (em JavaScript):** se você somar um texto com um número (`"Nota: " + 9`), o sistema converte o `9` no texto `"9"` sozinho e gruda virando `"Nota: 9"`.

#### 2. Conversão Explícita (*Type Casting*)
Acontece quando **o programador escreve no código uma ordem explícita forçando a mudança de tipo**.
- **Quando é obrigatória?** Quando existe **risco de perder pedaços do valor** (como passar de `double` decimal para `int` inteiro) ou transformar texto em número.
- **Como se escreve na prova?**
  - Em **C / Java / C#:** coloca-se o novo tipo entre **parênteses** na frente: `(int) valor`.
  - Em **Python / JavaScript:** usam-se comandos explícitos como `int("16")`, `float("7.5")`, `Number("42")` ou `parseInt("42")`.

#### 💻 Exemplo Passo a Passo: O Perigo do Truncamento!
```java
double media = 8.95;              // 1. Guarda exatamente 8.95 na memória RAM
int notaInteira = (int) media;    // 2. CASTING EXPLÍCITO: programador forçou virar inteiro!
double copia = notaInteira;       // 3. CONVERSÃO IMPLÍCITA: int -> double automático

System.out.println(notaInteira);  // Mostra na tela: 8
System.out.println(copia);        // Mostra na tela: 8.0
```
**Entendendo o que aconteceu:**
- Na linha 2, o `(int)` **não faz arredondamento matemático**! Ele literalmente **passa a tesoura (trunca)** no `.95` e joga os centavos no lixo. Por isso `8.95` vira **`8`** (e até `9.999` viraria `9`!).
- Na linha 3, como `notaInteira` já estava valendo `8`, a conversão implícita transformou `8` em **`8.0`** (os `.95` perdidos nunca mais voltam!).

#### 🎮 Conexão Gamer
Sabe quando seu personagem bate **`99.9` de dano crítico**, mas o número gigante na tela só exibe inteiros fazendo `(int) dano`? Na tela aparece **`99`**, e **não `100`**, porque o casting truncou o `.9` fora!

> [!CAUTION]
> **PEGADINHA MORTAL DA PROVA (DS 2025 Q8):**
> 1. **Casting NÃO arredonda — Casting TRUNCA (corta a parte decimal)!** `(int) 49.99` dá **`49`**.
> 2. A banca inventa nomes falsos nas alternativas como *"Conversão Normal"*, *"Conversão Indireta"* ou *"Conversão Automática Explícita"*. Os únicos dois nomes oficiais são **Implícita** (automática, sem perda) e **Explícita / *Type Casting*** (forçada pelo programador no código)!

---

### 📚 Parte 4 — Operadores Aritméticos, Ordem de Conta, `DIV` e `MOD`

Além das 4 contas básicas da escola (`+` soma, `-` subtração, `*` multiplicação com asterisco, `/` divisão normal), na programação existem dois operadores irmãos que caem o tempo todo na Etec: **`DIV`** e **`MOD`**.

#### 1. O Desenho da Divisão no Caderno (O Segredo para Nunca Confundir `DIV` e `MOD`)
Lembra como fazemos divisão inteira "na chave" no papel? Pegue `17 ÷ 5` (sem colocar vírgula no quociente!):

```text
   Dividendo ->  17  |  5  <- Divisor
                -15  +-----
                ----    3  <- QUOCIENTE INTEIRO = 17 DIV 5  (ou 17 // 5)
     RESTO  ->    2        <- RESTO INTEIRO     = 17 MOD 5  (ou 17 % 5)
```

Olhe para o desenho acima e guarde para a vida:
- **`DIV`** (ou **`//`** em Python, ou **`/`** entre dois `int` em C/Java): devolve o **QUOCIENTE INTEIRO** — quantas vezes inteiras o `5` coube dentro do `17` → **`3`**!
- **`MOD`** (ou **`%`** em C, Java, JavaScript e Python): devolve o **RESTO DA DIVISÃO** — o que sobrou sem conseguir formar outro grupo completo de `5` → **`2`**! *(Atenção: na programação, `%` entre dois números é **MOD**, não é porcentagem!)*

#### 💻 Dois Exemplos Práticos Passo a Passo
1. **🎮 Minecraft (`150` ferros em packs de `64`):**
   - `150 ÷ 64`: quantas vezes `64` cabe em `150`? Cabe **`2`** vezes (`2 × 64 = 128`). E sobra `150 - 128 =` **`22`**.
   - Logo: `150 DIV 64 =` **`2 packs cheios`** e `150 MOD 64 =` **`22 ferros soltos`**!
2. **⏱️ Converter `130` minutos em Horas e Minutos:**
   - Quantas horas cheias de `60` minutos cabem em `130`? `130 DIV 60 =` **`2` horas** (`2 × 60 = 120`).
   - Quantos minutos sobram fora das horas? `130 MOD 60 =` **`10` minutos**! Resultado: **`2h 10min`**.

#### Os 3 Usos Favoritos de `MOD` na Prova:
1. **Descobrir se um número é PAR ou ÍMPAR:** Divida por `2`. Se **`N MOD 2 == 0`** (sobrou zero), é **PAR**! Se **`N MOD 2 == 1`**, é **ÍMPAR**!
2. **Descobrir se é múltiplo de um número:** Se `numero MOD 3 == 0`, o número é divisível por `3` sem resto.
3. **Converter números para Binário *(DS 2019 Q2)*:** Dividir repetidamente por `2` guardando cada resto (`n MOD 2` gera os bits `0` e `1`) e atualizando `n <- n DIV 2` até zerar!

#### Ordem de Precedência Matemática (Quem Executa Primeiro!)
Igual na escola, uma conta como `2 + 3 * 4` **NÃO** soma `2 + 3` primeiro! A ordem oficial de prioridade é:
1. **Parênteses `()`** (sempre de dentro para fora);
2. **Potenciação e Raiz** (`**`, `^`);
3. **Multiplicação (`*`), Divisão (`/`), `DIV` e `MOD`** (empate entre si → resolve da **esquerda para a direita**);
4. **Soma (`+`) e Subtração (`-`)** (da esquerda para a direita).

Teste rápido: quanto vale `10 + 17 MOD 5 * 2`?
1º: `17 MOD 5` = `2` → fica `10 + 2 * 2`
2º: `2 * 2` = `4` → fica `10 + 4`
3º: **`14`**!

---

### 📚 Parte 5 — Lógica Proposicional e Tabela Verdade COMPLETA DO ZERO

Essa é a seção que muita gente tenta decorar correndo e acaba errando por bobeira na prova. Vamos construir do **zero absoluto**, tijolo por tijolo!

#### Passo 1: Operadores Relacionais (Como Perguntas Viram `V` ou `F`)
Na matemática e na programação, antes de usar **`E`** ou **`OU`**, normalmente comparamos dois números ou textos usando **Operadores Relacionais**. Toda comparação responde exclusivamente **`V` (Verdadeiro)** ou **`F` (Falso)**:

| Operador | Significado | Exemplo com `nota = 6` | Resultado | Pegadinha clássica |
| :---: | :--- | :--- | :---: | :--- |
| **`>`** | Estritamente **maior que** | `nota > 6` | **`F`**! | **`6` NÃO é maior que `6`!** Eles são iguais! |
| **`>=`** | **Maior ou igual a** | `nota >= 6` | **`V`**! | Aqui o `6` entra porque tem o sinal de igual junto! |
| **`<`** | Estritamente **menor que** | `nota < 10` | **`V`** | `10 < 10` daria `F`! |
| **`<=`** | **Menor ou igual a** | `nota <= 6` | **`V`** | Aceita `6` e qualquer menor que `6`. |
| **`==`** | **É igual a?** | `nota == 6` | **`V`** | Lembre: dois iguais (`==`) pergunta; um igual (`=`) guarda valor! |
| **`!=`** / **`<>`** | **É diferente de?** | `nota != 5` | **`V`** | Só dá `F` se os dois lados forem iguais. |

---

#### Passo 2: O que é (e o que NÃO é) uma Proposição Lógica?
Uma **Proposição** é qualquer afirmação completa declarativa à qual conseguimos atribuir claramente o valor **Verdadeiro (`V`)** ou **Falso (`F`)**.
- **São proposições:** `"O Brasil fica na América do Sul"` (`V`), `"3 + 2 = 7"` (`F`), `"nota >= 6"` (pode ser `V` ou `F`).
- **NÃO são proposições:** perguntas (*"Qual seu nome?"*), ordens/comandos (*"Feche a janela!"*), exclamações (*"Que dia lindo!"*) ou frases sem verbo/sentido completo. Você não consegue dizer se *"Feche a janela!"* é verdadeira ou falsa!

Na lógica, batizamos proposições simples com letras maiúsculas como **`P`**, **`Q`**, **`R`** — por exemplo:
- `P` = *"Você tem nível 20"*
- `Q` = *"Você não está banido"*

---

#### Passo 3: Como Construir uma Tabela Verdade do Zero (Regra do $2^n$)
A **Tabela Verdade** é simplesmente um mapa com **TODAS as combinações possíveis** de `V` e `F` que as proposições podem assumir ao mesmo tempo!

Quantas linhas tem a tabela? Depende de quantas letras diferentes existem (**Regra: `2` elevado ao número de letras**):
- **1 letra (`P`):** `2¹ = 2 linhas` (`P` só pode ser `V` ou `F`).
- **2 letras (`P` e `Q`):** `2² = 4 linhas` (para nunca esquecer ou repetir nenhuma combinação, siga sempre este truque de preenchimento!):
  - Na **1ª coluna (`P`)**, divida as 4 linhas ao meio: **2 `V` em cima, 2 `F` embaixo** (`V, V, F, F`).
  - Na **2ª coluna (`Q`)**, alterne de 1 em 1: **`V, F, V, F`**.
  - Confira as 4 combinações criadas sem falha: `(V,V)`, `(V,F)`, `(F,V)` e `(F,F)`!
- **3 letras (`P`, `Q`, `R`):** `2³ = 8 linhas` (`P` = 4 `V` e 4 `F`; `Q` = `V,V,F,F,V,V,F,F`; `R` = `V,F,V,F,V,F,V,F`).

---

#### Passo 4: Entendendo CADA Operador Lógico Um por Um (Sem Pressa!)

##### 1. Operador `NÃO` (Negação — Símbolo: `¬P` ou `!P` ou `not P`)
O `NÃO` trabalha com **1 única proposição** e simplesmente **vira ela do avesso** (`V` vira `F`; `F` vira `V`).

| `P` | Exemplo prático: `P = "Está chovendo"` | `¬P` (`NÃO P` = `"NÃO está chovendo"`) |
| :---: | :--- | :---: |
| **V** | Sim, está chovendo lá fora | **F** *(é falso dizer que não chove)* |
| **F** | Não está chovendo lá fora | **V** *(é verdade que não chove)* |

##### 2. Operador `E` (Conjunção — Símbolo: `P ∧ Q` ou `P && Q` ou `P and Q`)
Pense numa **porta com 2 cadeados em série**: só entra quem abrir o cadeado 1 **E** o cadeado 2.
**Regra de ouro do `E`:** Ele é **SUPER EXIGENTE**! **Só dá `V` quando TODOS forem `V`**. Basta **1 único `F`** para derrubar o resultado inteiro para `F`!

Exemplo do mundo real: Para entrar na balada é preciso ter **`P`: Ingresso** **E** **`Q`: Ser maior de 18 anos**. Vamos testar **todas as 4 pessoas da fila** linha por linha:

| `P` (Tem Ingresso?) | `Q` (Tem ≥ 18 anos?) | `P ∧ Q` (`P E Q` — Pode entrar?) | Explicação Linha a Linha |
| :---: | :---: | :---: | :--- |
| **V** | **V** | **V** | Tem ingresso **e** é maior de idade → **Entra (`V`)!** |
| **V** | **F** | **F** | Tem ingresso, mas é menor de idade → **Barrado (`F`)!** |
| **F** | **V** | **F** | É maior de idade, mas não tem ingresso → **Barrado (`F`)!** |
| **F** | **F** | **F** | Não tem nenhum dos dois → **Barrado (`F`)!** |

##### 3. Operador `OU` (Disjunção Inclusiva — Símbolo: `P ∨ Q` ou `P || Q` ou `P or Q`)
Pense num **cinema que aceita desconto se você tiver `P`: Carteira de Estudante OU `Q`: Carteira de Doador de Sangue**.
**Regra de ouro do `OU`:** Ele é **FLEXÍVEL**! **Basta PELO MENOS UM ser `V` para tudo dar `V`**! Ele **só dá `F`** quando **TODOS os lados forem `F`**! *(Atenção: se a pessoa tiver as DUAS carteirinhas — linha 1 `(V, V)` — ela continua ganhando desconto! Por isso em lógica `V OU V` dá `V`!)*

| `P` (É Estudante?) | `Q` (É Doador?) | `P ∨ Q` (`P OU Q` — Ganha desconto?) | Explicação Linha a Linha |
| :---: | :---: | :---: | :--- |
| **V** | **V** | **V** | Tem as duas carteiras → ótimo, pelo menos 1 vale → **Ganha (`V`)!** |
| **V** | **F** | **V** | Só estudante → já basta → **Ganha (`V`)!** |
| **F** | **V** | **V** | Só doador → já basta → **Ganha (`V`)!** |
| **F** | **F** | **F** | Não tem nenhuma das duas → **Sem desconto (`F`)!** |

*(Nota bônus caso apareça em alguma prova: existe o **OU Exclusivo (`XOR`)**, em que "ou escolhe só P ou escolhe só Q, **nunca os dois juntos**" — ex.: escolher entre carne **ou** peixe no prato feito: `V XOR V = F`. Mas o `OU` padrão da computação é sempre o **Inclusivo** acima, onde `V OU V = V`!)*

#### 🎮 Conexão Gamer: A Tabela Verdade da Fila Ranqueada
Regra do jogo para abrir partida: `(nivel >= 20) E (servidor == "BR" OU servidor == "LATAM") E (NAO estaBanido)`.
- Se você está no nível `25` (`V`), no servidor `"EU"`, mas está no `"LATAM"`? Não, só `"EU"` (`F OU F = F`), já bloqueia por causa do `E`!
- Se você tem nível `30` (`V`), joga no `"BR"` (`V`), mas `estaBanido = true`? Então `NAO true = F`, e como tudo está ligado pelo `E`, esse único `F` derruba a expressão inteira para **`F`** (banido não joga)!

---

#### Passo 5: Como Resolver Expressões Lógicas Grandes Sem Errar (Prioridade + Exemplos!)

Igual nas contas de `+` e `*`, operadores lógicos têm uma **fila de preferência obrigatória**:
1. **Parênteses `()`** (de dentro para fora);
2. **Aritméticos e Relacionais** (`+`, `*`, `>`, `<`, `==`, `!=`);
3. **`NÃO` (`¬` / `!`)** → executa sempre antes do `E` e do `OU`!
4. **`E` (`∧` / `&&`)** → executa **antes** do `OU`!
5. **`OU` (`∨` / `||`)** → fica por último!

##### 💻 Exemplo 1 (Resolvendo do Zero):
Considere **`A = Verdadeiro`** e **`B = Falso`**. Quanto vale **`NAO A OU (A E NAO B)`**?
1. Resolva o parêntese primeiro: dentro de `(A E NAO B)`, quem manda antes entre `E` e `NAO`? O **`NAO`**!
   - `NAO B` = `NAO Falso` = **`V`**
   - Agora faz o `E` do parêntese: `A E V` = `V E V` = **`V`**! *(O parêntese inteiro virou `V`!)*
2. Substitua na frase original: ficou `NAO A OU V`.
3. Entre `NAO` e `OU`, quem executa primeiro? O **`NAO`**!
   - `NAO A` = `NAO V` = **`F`**.
4. Sobrou só o `OU` no final: `F OU V` = **`V` (Verdadeiro)**!

##### 💻 Exemplo 2 (Estilo Prova da Etec — Misturando Números e Lógica):
Na Etec, o aluno passa direto se `(nota >= 6 E NAO (faltas > 25)) OU conselho == true`.
Teste um aluno com **`nota = 7.5`**, **`faltas = 30`** e **`conselho = false`**:
1. Troque os números por `V` ou `F`:
   - `nota >= 6` → `7.5 >= 6` → **`V`**
   - `faltas > 25` → `30 > 25` → **`V`**
   - `conselho == true` → `false == true` → **`F`**
2. Agora a frase limpa é: `(V E NAO (V)) OU F`
3. Dentro do parêntese grande, resolva `NAO (V)` primeiro → **`F`**!
4. Ainda no parêntese grande: `V E F` → basta um `F` no `E` para dar **`F`**!
5. Por último, fora do parêntese: `F OU F` → **`F` (Reprovado!)**

> [!TIP]
> **Bônus: Como Negar uma Frase Composta (Leis de De Morgan)**
> Como negamos corretamente *"Eu tenho 16 anos **E** estudo na Etec"*?
> Cuidado: **NÃO** é *"Não tenho 16 anos E não estudo na Etec"*! Para a frase original ser falsa, basta **uma** das duas coisas falhar!
> - Negar **`(P E Q)`** vira **`(NÃO P) OU (NÃO Q)`** → *"Não tenho 16 anos **OU** não estudo na Etec"*.
> - Negar **`(P OU Q)`** vira **`(NÃO P) E (NÃO Q)`** → troca o `OU` pelo `E` e nega os dois!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q8 — Conversão de Tipos)
*Um desenvolvedor Java escreveu `double preco = 49.99; int inteiro = (int) preco;` e, em seguida, `double copia = inteiro;`. Avalie as afirmativas:*
- *I. Na segunda instrução ocorreu uma conversão implícita com arredondamento para 50.*
- *II. Na segunda instrução ocorreu um type casting explícito que truncou o valor para 49.*
- *III. Na terceira instrução (`double copia = inteiro;`) ocorreu conversão implícita sem perda de dados.*

**Análise:**
- **Item I é FALSO:** Há dois erros! O `(int)` foi escrito pelo programador, logo é **explícita / casting** (não implícita); e *casting* **trunca** para `49`, nunca arredonda para `50`.
- **Item II é VERDADEIRO:** `(int) preco` é explícito e descarta `.99`, deixando `49`.
- **Item III é VERDADEIRO:** Passar `int` para `double` amplia o espaço sem perda; o tradutor faz sozinho (`49` vira `49.0`).
**Gabarito:** **II e III corretas**.

#### Questão Resolvida 2 (Baseada em INFO 2025 Q20 & DS 2019 Q1 — Tabela Verdade)
*Considere `P = Verdadeiro`, `Q = Falso` e `R = Verdadeiro`. Qual é o resultado lógico da expressão `(P E Q) OU (NAO Q E R)`?*

**Passo a passo:**
1. Parêntese esquerdo: `P E Q` = `V E F` = **`F`**.
2. Parêntese direito: primeiro faz **`NAO Q`** = `NAO F` = **`V`**. Depois **`V E R`** = `V E V` = **`V`**.
3. Por último liga os dois com `OU`: `F OU V` = **`V` (Verdadeiro)**!


---

## Dia 2 — Algoritmos, Fluxogramas, Decisão (`se/senao`), Laços (`enquanto`/`para`/`repita`) e Teste de Mesa

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Antes de um arquiteto construir uma casa, ele desenha a **planta baixa** no papel para garantir que não vai faltar porta nem janela. Antes de criar um programa em Python, JavaScript ou C#, nós também planejamos a lógica do passo a passo usando um **Algoritmo**.

Pense no aplicativo do **iFood** na hora em que você fecha um pedido:
1. Primeiro ele segue uma **sequência** (lê seu endereço e os itens do carrinho);
2. Depois toma **decisões** (*"Se tiver cupom válido, aplique 10% de desconto; senão, cobre o preço normal"*);
3. Por fim faz **repetições** (*"Para cada lanche dentro do carrinho, some o valor e reduza 1 unidade do estoque"*).

Na prova da Etec, aparecem pequenos códigos com essas decisões e repetições para você descobrir o número exato que sai na tela no final. Quem tenta "adivinhar de cabeça" cai nas pegadinhas; quem usa o **Teste de Mesa** no rascunho acerta todas!

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

Imagine uma luta contra um **Chefe (*Boss*) num jogo**:
- Para vencer, você não sai chutando números no escuro: se alguém perguntar *"Com quantos golpes e quanto de vida você termina a luta?"*, o jeito mais garantido é anotar no papel: **Turno 1** (vida do boss cai de 100 para 70, sua estamina vai para 80), **Turno 2** (vida cai para 40...), **Turno 3**... até a vida zerar!
- Isso é exatamente o **Teste de Mesa**: você acompanha o programa passo a passo anotando os números no papel como se fosse um jogo em turnos.

---

### 📚 Parte 1 — O que é um Algoritmo? (1 Problema Visto de 3 Jeitos!)

Um **Algoritmo** nada mais é do que uma **receita finita, ordenada e clara (sem ambiguidade)** com o passo a passo exato para resolver um problema.

Todo algoritmo segue sempre a mesma estrutura básica chamada **E → P → S**:
1. **Entrada (*Input*):** O programa recebe os dados de fora (o que você digita no teclado, clica com o mouse ou lê de um arquivo).
2. **Processamento (*Processing*):** O processador faz as contas, comparações e guarda os resultados nas variáveis.
3. **Saída (*Output*):** O programa devolve o resultado pronto (mostra na tela, toca um som ou salva num arquivo).

#### Veja O MESMO Problema Escrito nas 3 Formas Oficiais
Problema: *"Ler duas notas de um aluno (`n1` e `n2`), calcular a média e avisar se ele passou (média `>= 6`) ou ficou de recuperação."*

**Forma 1 — Descrição Narrativa (em Português comum):**
1. Início.
2. Perguntar ao aluno a nota 1 e a nota 2.
3. Somar as duas notas e dividir por 2, guardando na variável `media`.
4. Verificar: se `media` for maior ou igual a `6`, mostrar `"Aprovado"`; caso contrário, mostrar `"Recuperação"`.
5. Fim.

**Forma 2 — Fluxograma (Desenho com Símbolos Geométricos):**
```text
[ ⬭ Início ]
     ↓
[ ▱ Ler n1, n2 ]                    <- Entrada de dados (Paralelogramo)
     ↓
[ ▭ media <- (n1 + n2) / 2 ]        <- Cálculo/Processamento (Retângulo)
     ↓
[ ◇ media >= 6 ? ] ──(NÃO)──→ [ ▱ Escrever "Recuperação" ] ──┐
     │ (SIM)                                                 │
     ↓                                                       ↓
[ ▱ Escrever "Aprovado" ] ────────────────────────────────→ [ ⬭ Fim ]
```

**Forma 3 — Pseudocódigo / Portugol (Parecido com código real):**
```portugol
leia(n1, n2)
media <- (n1 + n2) / 2
se (media >= 6) entao
    escreva("Aprovado")
senao
    escreva("Recuperação")
fimse
```

#### Os 4 Símbolos Oficiais do Fluxograma que Caem na Prova

| Símbolo Geométrico | Nome Oficial na Prova | Para Que Serve Exatamente | O que Vai Escrito Dentro |
| :--- | :--- | :--- | :--- |
| **⬭ Oval / Cápsula / Elipse** | **Terminal** | Marca **apenas** onde o algoritmo começa e termina. | `Início` ou `Fim` |
| **▱ Paralelogramo** *(retângulo inclinado)* | **Entrada / Saída (E/S)** | Comunicar com o mundo externo: **ler** o que foi digitado ou **exibir** a resposta na tela. | `Ler renda` / `Escrever resultado` |
| **▭ Retângulo** | **Processamento** | **Contas matemáticas e atribuições** (`<-`), feitas internamente na memória. | `limite <- renda * 0.30` |
| **◇ Losango** | **Decisão / Condicional** | Faz uma pergunta cujo resultado é `V` (`Sim`) ou `F` (`Não`). **Sempre tem 1 seta entrando e 2 setas saindo (`Sim` / `Não`).** | `parcela <= limite?` |

*(Nota rápida sobre porcentagem em código: em cálculos como `limite <- renda * 0.30`, multiplicamos por `0.30` porque `30% = 30 ÷ 100 = 0.30`! Se fosse 15%, seria `* 0.15`.)*

> [!WARNING]
> **Pegadinha clássica de Fluxograma:** Nunca confunda **Retângulo** com **Losango** ou **Paralelogramo**!
> - Pergunta com Sim/Não (`se/senão`) = **Losango** (◇).
> - Cálculo ou guardar valor (`soma = a + b`) = **Retângulo** (▭).
> - Ler do usuário / Imprimir na tela = **Paralelogramo** (▱).

---

### 🗣️ Parte 2 — Dicionário Visual: Portugol ↔ C / Java / JavaScript

Na prova da Etec, algumas questões vêm escritas em **Portugol** e outras vêm em **JavaScript, C, Java ou Python**. Não se assuste quando vir `console.log(x);` ou `System.out.println(x);` — **ambos são apenas o jeito que o JavaScript e o Java escrevem o comando `escreva(x)` para mostrar algo na tela!**

| Ação que queremos fazer | Em **Portugol** | Em **JavaScript / Java / C** |
| :--- | :--- | :--- |
| Mostrar valor na tela | `escreva(x)` | `console.log(x);` *(JS)* / `System.out.println(x);` *(Java)* / `printf("%d", x);` *(C)* |
| Guardar valor em variável | `x <- 5` | `x = 5;` (ou `let x = 5;` em JS, `int x = 5;` em C/Java) |
| Se ... Senão | `se (x > 5) entao ... senao ... fimse` | `if (x > 5) { ... } else { ... }` |
| Enquanto (repete testando antes) | `enquanto (x <= 6) faca ... fimenquanto` | `while (x <= 6) { ... }` |
| Para (repete contando) | `para i de 0 ate 3 faca ... fimpara` | `for (let i = 0; i <= 3; i++) { ... }` |
| Resto da divisão (`MOD`) | `x MOD 2 == 0` | `x % 2 == 0` |

Repare que as duas versões abaixo fazem **exatamente a mesma coisa** (se `x` começa em `1`, somam `+2` até passar de `5`):
- Portugol: `enquanto (x <= 5) faca x <- x + 2; fimenquanto`
- JavaScript/C: `while (x <= 5) { x += 2; }` *(A lógica é 100% idêntica!)*

---

### 📚 Parte 3 — Estruturas de Decisão Passo a Passo

#### 1. Decisão Simples (`se`) — Só Faz Algo Se For Verdadeiro
```portugol
saldo <- -50
se (saldo < 0) entao
    escreva("Atenção: saldo negativo!")
fimse
escreva("Fim da consulta")
```
- Se `saldo` for `-50`, a pergunta `saldo < 0` dá **`V`**, então ele imprime `"Atenção: saldo negativo!"` e depois imprime `"Fim da consulta"`.
- Se `saldo` fosse `200`, `200 < 0` daria **`F`**: o computador simplesmente **pula** tudo que está dentro do `se ... fimse` e vai direto para `"Fim da consulta"`.

#### 2. Decisão Composta (`se ... senao`) — Dois Caminhos Opostos
Aqui existem **dois caminhos**: ou entra no bloco do `se` (quando dá `V`), ou entra no bloco do `senao` (quando dá `F`). **Nunca entra nos dois ao mesmo tempo!**
```portugol
idade <- 16
se (idade >= 18) entao
    escreva("Pode tirar CNH")
senao
    escreva("Ainda não tem 18 anos")   // Como 16 >= 18 é Falso, vem para cá!
fimse
```

#### 3. Decisão Encadeada (`else if`) vs. a Armadilha dos Vários `if` Seguidos!
Compare estes dois códigos com **`nota = 9.0`**. Um está certo e o outro tem um erro clássico que cai na prova!

**Código A — Correto (Encadeado com `else if` / `senao se`):**
```javascript
if (nota >= 9.0) {
    conceito = "MB (Muito Bom)";
} else if (nota >= 7.0) {
    conceito = "B (Bom)";
} else if (nota >= 5.0) {
    conceito = "R (Regular)";
} else {
    conceito = "I (Insatisfatório)";
}
```
Como `9.0 >= 9.0` dá **`V`** logo na 1ª linha, `conceito` vira **`"MB"`** e o programa **PULA fora da estrutura inteira**, ignorando o `7.0` e o `5.0`!

**Código B — A Armadilha dos `if` Independentes (Sem `else`!):**
```javascript
if (nota >= 9.0) { conceito = "MB"; }   // 1) 9.0 >= 9.0 é V -> conceito = "MB"
if (nota >= 7.0) { conceito = "B"; }    // 2) Testa DE NOVO! 9.0 >= 7.0 é V -> APAGA "MB" e põe "B"!
if (nota >= 5.0) { conceito = "R"; }    // 3) Testa DE NOVO! 9.0 >= 5.0 é V -> APAGA "B" e põe "R"!
```
No Código B, como **não existe `else` ligando os blocos**, o computador trata os três `if` como três perguntas separadas e **sobrescreve** a gaveta `conceito` — dando `"R"` para quem tirou 9! Fique sempre de olho se há `else` antes do próximo `if`!

#### 4. Decisão Múltipla (`escolha ... caso` / `switch ... case`)
Útil quando queremos comparar **uma variável exata** com várias opções fixas (como um menu `1, 2, 3`):
```javascript
switch (opcao) {
    case 1: console.log("Jogar"); break;   // O 'break' manda sair do switch ao terminar!
    case 2: console.log("Opções"); break;
    default: console.log("Opção inválida");
}
```
*(Atenção: em C/Java/JS, se esquecer a palavra `break`, depois de executar o `case 1`, o código continua "caindo" e executando o `case 2` também!)*

---

### 📚 Parte 4 — Estruturas de Repetição (Laços / *Loops*) Um por Um!

Um **laço de repetição** manda o computador repetir um bloco de código várias vezes sem precisarmos copiar e colar a mesma linha 100 vezes.

Para não travar num **Loop Infinito** (um laço que nunca termina e trava o programa), quase todo laço precisa de **3 peças obrigatórias**:
1. **Inicialização:** Criar a variável contadora antes de começar (`i <- 1`);
2. **Condição:** A pergunta `V/F` que decide se continua repetindo (`enquanto i <= 3`);
3. **Atualização (Passo):** Mudar a variável dentro do laço (`i <- i + 1`) para que um dia a condição acabe e ele consiga sair! *(Se você esquecer de somar `+1`, `i` fica valendo `1` para sempre e o programa congela em loop infinito!)*

Agora vamos estudar **cada um dos 4 laços separadamente**:

#### 1. Laço `enquanto` / `while` — Repetição com Pré-Teste (Testa ANTES de Entrar)
O `while` **olha para a condição antes de dar o primeiro passo**.
- **Se for Verdadeira (`V`):** entra, executa o bloco, volta no topo e testa de novo.
- **Se já nascer Falsa (`F`):** **não executa NEM UMA ÚNICA VEZ (0 vezes)**!

```javascript
// Exemplo A: Executa 3 vezes
let x = 1;
while (x <= 3) {
    console.log(x);   // Imprime 1, depois 2, depois 3
    x = x + 1;        // Atualiza para 2, depois 3, depois 4 (quando x=4, 4<=3 é F e sai!)
}

// Exemplo B: Executa 0 VEZES!
let vida = 0;
while (vida > 0) {    // Logo de cara: 0 > 0 é FALSO!
    console.log("Atacando...");  // NUNCA executa essa linha!
}
```
- **🎮 Analogia Gamer:** `while (hp > 0)` — enquanto sua vida estiver acima de zero, você joga a fase. Se entrar já morto (`hp = 0`), nem joga (`0 vezes`)!

#### 2. Laço `do ... while` (em C/Java/JS) vs. `repita ... ate` (em Portugol) — Pós-Teste!
Diferente do `while`, os laços de **Pós-Teste** **primeiro executam o bloco inteiro** e **só perguntam a condição lá embaixo, no final**.
- **Consequência sagrada de prova:** Mesmo que a condição já comece falsa, um laço pós-teste **executa PELO MENOS 1 VEZ GARANTIDA**!

Compare o mesmo cenário (`x` já começa valendo `10`):
```javascript
// Em C / Java / JavaScript:
let x = 10;
do {
    console.log(x);   // Executa 1ª vez! Imprime 10!
    x = x + 1;        // x vira 11
} while (x <= 5);     // Testa NO FINAL: 11 <= 5 é FALSO -> Para! (Rodou 1 vez garantida!)
```

> [!CAUTION]
> **PEGADINHA DO PORTUGOL (`repita ... ate`) vs. `do ... while`!**
> - No **`do ... while`** (C/Java/JS): o laço **CONTINUA** enquanto a condição for **VERDADEIRA**, e **PARA** quando der **FALSA**.
> - No **`repita ... ate`** (Portugol): significa **"repita ATÉ QUE isso vire verdade"**! Ou seja, ele **CONTINUA enquanto a condição for FALSA** e **PARA quando a condição ficar VERDADEIRA**!
> Exemplo em Portugol: `repita leia(senha) ate (senha == 1234)` → Se errar a senha (`F`), ele continua repetindo; quando acertar `1234` (`V`), ele sai!

- **🎮 Analogia Gamer:** Tela de *"Continue? Inserir ficha / Tentar de novo?"* — aparece **pelo menos 1 vez** depois da derrota, e só no fim pergunta se você quer continuar.

#### 3. Laço `para` / `for` — Repetição Contada (Tudo Numa Linha Só)
Quando você já sabe de quantos até quantos quer contar (por exemplo: *"conte de `0` até `3`"*, ou *"percorra todas as 5 gavetas de um vetor"*), o `for` junta os **3 pilares** no mesmo cabeçalho:

```javascript
for (let i = 0; i <= 3; i++) {
//   ↑ Inicia  ↑ Condição ↑ Passo (soma +1 após cada volta)
    console.log(i);
}
```
**Entendendo peça por peça na ordem em que a CPU executa:**
1. **`let i = 0`** → Executa **1 única vez no início** (`i` começa em `0`).
2. **`i <= 3`** → Pergunta: `0 <= 3` é `V`? Sim → **entra** e imprime `0`.
3. **`i++`** → Só no fim da volta, soma `+1` (`i` vira `1`). Volta para o teste `1 <= 3` (`V`, imprime `1`)...
4. Imprime `0, 1, 2, 3`. Na volta final, `i++` faz **`i` virar `4`**, testa `4 <= 3` (`F`) e **sai do `for`**!
- **🎮 Analogia Gamer:** Varrer todos os `10` *slots* da mochila um por um (`i` indo de `0` até `9`).

| Resumo Rápido | Momento do Teste | Mínimo de Execuções | Continua Repetindo Quando... |
| :--- | :---: | :---: | :--- |
| **`enquanto` / `while`** | **No início** (Pré-teste) | **0 vezes** | Condição for **VERDADEIRA** |
| **`do ... while`** | **No final** (Pós-teste) | **1 vez** | Condição for **VERDADEIRA** |
| **`repita ... ate`** *(Portugol)* | **No final** (Pós-teste) | **1 vez** | Condição for **FALSA** (para quando der `V`!) |
| **`para` / `for`** | **No início** (Contado) | **0 ou N vezes** | Condição for **VERDADEIRA** |

---

### 📚 Parte 5 — Teste de Mesa Passo a Passo (O Método Anti-Erro)

**Teste de Mesa** é fingir que **você é o processador**: você desenha no rascunho da prova uma **coluna para cada variável** e executa o código **linha por linha**, riscando o valor antigo sempre que uma gaveta muda.

#### Passo Preparatório: Como Trocar o Valor de Duas Variáveis (`A` e `B`)?
Imagine que você tem um **Copo A (com Suco de Laranja)** e um **Copo B (com Suco de Uva)** e quer trocar o conteúdo dos dois sem misturar. O que precisa? **De um 3º copo vazio (`aux`)!**
```text
Passo 1: aux <- A     (Despeja Laranja no copo vazio 'aux' -> A ficou livre!)
Passo 2: A   <- B     (Despeja Uva dentro do copo A -> B ficou livre!)
Passo 3: B   <- aux   (Despeja a Laranja de 'aux' dentro do copo B -> Trocados!)
```
*(Armadilha clássica: fazer `A <- B; B <- A;` sem `aux`! Na 1ª linha você joga fora o que tinha em `A` e coloca `B`; na 2ª linha, os dois copos ficam com Suco de Uva para sempre!)*

#### 💻 Exemplo #1 (Iniciante): Somador Simples com `while`
```javascript
let i = 1;
let total = 0;
while (i <= 3) {
    total = total + i;
    i = i + 1;
}
console.log(total, i);
```
| Passo | Condição `i <= 3`? | `total` | `i` |
| :--- | :---: | :---: | :---: |
| **Início** | — | `0` | `1` |
| **Volta 1** | `1 <= 3` (**V** entra) | `0 + 1 = 1` | `1 + 1 = 2` |
| **Volta 2** | `2 <= 3` (**V** entra) | `1 + 2 = 3` | `2 + 1 = 3` |
| **Volta 3** | `3 <= 3` (**V** entra) | `3 + 3 = 6` | `3 + 1 = 4` |
| **Teste 4** | `4 <= 3` (**F** SAI!) | **`6`** | **`4`** |

**Resultado impresso:** `total = 6` e **`i = 4`**! *(Muita gente erra achando que `i` terminou em `3`, esquecendo que `i` virou `4` na Volta 3 para poder falhar no teste!)*

#### 💻 Exemplo #2 (Nível Prova FAT): Acumulador + Filtro `MOD 3` + Contador
```portugol
cont <- 1
soma <- 0
achados <- 0
enquanto (cont <= 7) faca
    se (cont MOD 3 == 0) entao
        soma <- soma + cont
        achados <- achados + 1
    fimse
    cont <- cont + 2
fimenquanto
escreva(soma, achados, cont)
```
| Passo | `cont <= 7`? | `cont MOD 3 == 0`? | `soma` | `achados` | `cont` (soma +2) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Início** | — | — | `0` | `0` | `1` |
| **Volta 1 (`cont=1`)** | `1 <= 7` (**V**) | `1 % 3 = 1` (**F** pula `se`) | `0` | `0` | `1 + 2 = 3` |
| **Volta 2 (`cont=3`)** | `3 <= 7` (**V**) | `3 % 3 = 0` (**V** entra!) | `0 + 3 = 3` | `1` | `3 + 2 = 5` |
| **Volta 3 (`cont=5`)** | `5 <= 7` (**V**) | `5 % 3 = 2` (**F** pula `se`) | `3` | `1` | `5 + 2 = 7` |
| **Volta 4 (`cont=7`)** | `7 <= 7` (**V**) | `7 % 3 = 1` (**F** pula `se`) | `3` | `1` | `7 + 2 = 9` |
| **Teste 5 (`cont=9`)** | `9 <= 7` (**F** SAI!) | *(não roda)* | **`3`** | **`1`** | **`9`** |

**Saída:** `soma = 3`, `achados = 1`, **`cont = 9`**!

#### 💻 Exemplo #3: Desvendando a Sequência de Fibonacci com `for`
A famosa **Sequência de Fibonacci** é uma sequência numérica da matemática em que os dois primeiros termos são `1` e `1`, e **cada próximo termo é a soma dos dois anteriores**: `1, 1, 2, 3, 5, 8, 13, 21...`
Veja o algoritmo que calcula os próximos passos usando uma variável auxiliar `prox`:
```javascript
let a = 1, b = 1;
for (let i = 1; i <= 4; i++) {
    let prox = a + b;
    a = b;
    b = prox;
}
console.log(a, b);
```
- **Início:** `a = 1`, `b = 1`
- **`i = 1` (`1 <= 4` V):** `prox = 1 + 1 = 2` → `a = 1`, `b = 2` → fim da volta: `i` vira `2`
- **`i = 2` (`2 <= 4` V):** `prox = 1 + 2 = 3` → `a = 2`, `b = 3` → `i` vira `3`
- **`i = 3` (`3 <= 4` V):** `prox = 2 + 3 = 5` → `a = 3`, `b = 5` → `i` vira `4`
- **`i = 4` (`4 <= 4` V):** `prox = 3 + 5 = 8` → `a = 5`, `b = 8` → `i` vira `5` (`5 <= 4` F → sai!)
- **Saída:** `a = 5`, `b = 8`!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q9 — Teste de Mesa)
*Analise o algoritmo:* `x <- 10; y <- 4; enquanto (x > y) faca { x <- x - 2; y <- y + 1; } escreva(x, y);` *Quais valores serão impressos?*
- **Início:** `x = 10`, `y = 4`.
- **Volta 1:** `10 > 4` (`V`) → `x = 8`, `y = 5`.
- **Volta 2:** `8 > 5` (`V`) → `x = 6`, `y = 6`.
- **Teste 3:** `6 > 6` (**`F`!** Pois é estritamente `>`, não `>=`!) → **SAI DO LAÇO!**
- **Gabarito:** Imprime **`x = 6` e `y = 6`**.

#### Questão Resolvida 2 (Estilo Molde 1 — Fluxograma & Laços)
*Julgue: I. No fluxograma, o retângulo representa entrada e saída via teclado/tela. II. `do...while` garante pelo menos 1 execução pois testa no final. III. Se a condição de um `while` já começa falsa, o bloco roda 0 vezes.*
- **I é FALSO:** Entrada/saída usa **paralelogramo**; retângulo é **processamento/contas**.
- **II é VERDADEIRO.**
- **III é VERDADEIRO.**
**Gabarito:** Apenas **II e III**.


---

## Dia 3 — Vetores (1D), Matrizes (2D), Pilha (LIFO), Fila (FIFO) e Funções com Recursividade

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine fazer um sistema escolar para guardar as notas dos **40 alunos** de uma turma criando 40 variáveis soltas chamadas `nota1`, `nota2`, `nota3`... até `nota40`! Só de pensar já dá cansaço, e você nem conseguiria usar um laço `for` para somar todas! E como o computador guardaria uma tabela do Excel ou um tabuleiro `3 × 3` do Jogo da Velha?

Para guardar **muitos dados do mesmo tipo sob um único nome**, existem os **Vetores (1 linha)** e as **Matrizes (tabelas com linhas e colunas)**. Além disso, os programas organizam filas de tarefas usando duas regras que você vê todo dia na vida real:
- Uma **Fila de banco** (quem chegou primeiro é atendido primeiro);
- Uma **Pilha de pratos** (o último prato lavado colocado em cima é o primeiro que você pega de volta — igual o comando **`Ctrl+Z` Desfazer**!).

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

- A **Barra de Atalhos (*Hotbar*)** na parte de baixo da tela do Minecraft tem vários quadradinhos lado a lado sob um único nome (`hotbar`) — isso é um **Vetor**.
- Um **Minimapa ou Tabuleiro** com fileiras e colunas onde cada ponto tem 2 coordenadas (fileira e coluna) é uma **Matriz**.
- A **Fila de espera da partida ranqueada** atende primeiro quem clicou em "Jogar" antes; já apertar **`ESC`** depois de abrir 3 menus seguidos (`Configurações → Áudio → Microfone`) fecha **primeiro o último menu aberto** (`Microfone`).

---

### 📚 Parte 1 — Vetores (*Arrays* 1D): Gaveteiro Numerado a Partir do Zero

Um **Vetor** é uma fila única de gavetas coladas lado a lado na memória RAM, todas guardando o **mesmo tipo de dado** (por exemplo, só inteiros ou só textos — por isso dizemos que é uma estrutura **homogênea** e **unidimensional**).

#### Por que os Índices Começam no `0`? (A Regra Base Zero)
Na imensa maioria das linguagens reais (**C, C++, Java, JavaScript, Python, PHP**), a numeração das gavetas **NÃO começa no `1` — começa no `0`**! (Porque `0` significa "zero passos de distância do início da fila na memória".)

Portanto, um vetor `notas` com **5 gavetas (`N = 5`)** fica assim na memória:

| Endereço (Índice) | `notas[0]` | `notas[1]` | `notas[2]` | `notas[3]` | `notas[4]` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Posição humana** | 1º item | 2º item | 3º item | 4º item | 5º (último!) |
| **Valor guardado** | `8.5` | `6.0` | `9.0` | `7.5` | `10.0` |

- Quanto vale `notas[2]`? Vale **`9.0`** (é o **3º** elemento, pois contamos `0, 1, 2`!).
- Qual é sempre o **último índice válido**? É **`N - 1`** (aqui `5 - 1 = 4`).
- Se você tentar acessar `notas[5]`, o programa dá **erro grave (*Index Out of Bounds* — fora do limite)** porque a gaveta `5` não existe!

#### Como Usar um Vetor Passo a Passo (Criar, Ler, Mudar e Varrer com `for`)
```javascript
// 1. Criando o vetor com 4 números (índices válidos: 0, 1, 2, 3):
let v = [10, 15, 20, 25];

// 2. Lendo e mudando uma única posição na mão:
console.log(v[0]);   // Mostra 10
v[1] = 16;           // Troca o 15 (gaveta 1) por 16

// 3. Descobrindo o tamanho automaticamente com .length:
// Em JavaScript, 'v.length' significa "quantos itens existem dentro do vetor v" -> aqui vale 4!
```

Agora veja um **exemplo clássico de prova** percorrendo o vetor com um laço `for` para somar **apenas os números pares**:
```javascript
let v = [10, 15, 20, 25];
let soma = 0;
for (let i = 0; i < v.length; i++) {   // i vai de 0 enquanto i < 4 (ou seja: 0, 1, 2, 3)
    if (v[i] % 2 === 0) {              // O resto da divisão por 2 é zero (PAR)?
        soma = soma + v[i];            // Se sim, soma esse elemento!
    }
}
// Rastreamento volta a volta:
// i = 0 -> v[0] vale 10 (10 % 2 == 0 -> V!) -> soma = 0 + 10 = 10
// i = 1 -> v[1] vale 15 (15 % 2 == 1 -> F!) -> pula o if!
// i = 2 -> v[2] vale 20 (20 % 2 == 0 -> V!) -> soma = 10 + 20 = 30
// i = 3 -> v[3] vale 25 (25 % 2 == 1 -> F!) -> pula o if!
// i = 4 -> 4 < 4 é Falso -> FIM! Resultado impresso: soma = 30
```

> [!WARNING]
> **Atenção ao cabeçalho em Portugol (VisuAlg):** Algumas questões escritas em Portugol escolar escrevem explicitamente `vetor[1..5] de inteiro` (forçando começar no `1`). Leia sempre o texto da questão! Se estiver em **JS, C, Java, Python ou PHP** — ou se não disser `1..5` — começa sempre no **`0`**!

---

### 📚 Parte 2 — Matrizes Bidimensionais (`M[i][j]`): Tabelas com 2 Coordenadas

Enquanto o Vetor é uma única fila (precisa de **1 número** `[i]`), uma **Matriz Bidimensional** é um "vetor de vetores", igual a uma **grade de batalha naval ou planilha do Excel**: você precisa de **2 números** para achar qualquer quadradinho:
**Regra universal sagrada:** **`M[i][j]`** lê-se **PRIMEIRO a Linha `i` (de cima para baixo)**, **DEPOIS a Coluna `j` (da esquerda para a direita)**!

Olhe esta **Matriz `M` de ordem `3 × 3`** (3 linhas `0, 1, 2` e 3 colunas `0, 1, 2`):

| `Linha (i) \ Coluna (j)` | Coluna `j = 0` | Coluna `j = 1` | Coluna `j = 2` |
| :---: | :---: | :---: | :---: |
| **Linha `i = 0`** | **`5`** (`M[0][0]`) | `8` (`M[0][1]`) | **`2`** (`M[0][2]`) |
| **Linha `i = 1`** | `4` (`M[1][0]`) | **`7`** (`M[1][1]`) | `9` (`M[1][2]`) |
| **Linha `i = 2`** | **`6`** (`M[2][0]`) | `1` (`M[2][1]`) | **`3`** (`M[2][2]`) |

Teste rápido de localização:
- Quem está em **`M[1][2]`**? Vá na **Linha `1`**, depois ande até a **Coluna `2`** → é o **`9`**!
- Quem está em **`M[2][0]`**? Vá na **Linha `2`**, **Coluna `0`** → é o **`6`**!

#### Como Percorrer uma Matriz com "Laço Dentro de Laço"?
Para ler os 9 quadradinhos, colocamos um **`for`** das linhas (`i`) abraçando outro **`for`** das colunas (`j`):
- *(Nota de Python: quando você vir `range(3)` em Python, significa **"gere os 3 números começando do zero: `0, 1, 2`"**, parando antes do `3`!)*
- Como funciona na prática? O `i` trava no **`0`** enquanto o `j` gira todinho (`0, 1, 2` → lê a 1ª linha inteira!). Só depois `i` vira **`1`** e o `j` gira tudo de novo (`0, 1, 2` → lê a 2ª linha inteira!).

#### As 4 Regiões Clássicas da Matriz Quadrada (Ordem `N = 3`)
1. **Diagonal Principal:** Desce do **canto superior esquerdo ao inferior direito**.
   - **Regra exata:** os dois índices são iguais → **`i == j`**!
   - Posições: `M[0][0] = 5`, `M[1][1] = 7`, `M[2][2] = 3`. Soma = `5 + 7 + 3 =` **`15`**.
2. **Diagonal Secundária:** Desce do **canto superior direito ao inferior esquerdo**.
   - **Regra exata:** a soma dos índices vale `N - 1` → **`i + j == N - 1`** (como `N = 3`, **`i + j == 2`**!).
   - Posições: `M[0][2] = 2` (`0+2=2`), `M[1][1] = 7` (`1+1=2`), `M[2][0] = 6` (`2+0=2`). Soma = `2 + 7 + 6 = 15`.
3. **Acima da Diagonal Principal:** `j > i` (`[0][1], [0][2], [1][2]`).
4. **Abaixo da Diagonal Principal:** `i > j` (`[1][0], [2][0], [2][1]`).

#### 💻 Exemplo Real da Prova Comentado em Python *(Baseado em DS 2025 Q10)*
```python
M = [
    [1, 3, 5],   # linha i = 0
    [2, 4, 8],   # linha i = 1
    [1, 1, 1]    # linha i = 2
]
soma_dp = 0
for i in range(3):          # i passa por 0, 1, 2
    for j in range(3):      # para cada linha i, j passa por 0, 1, 2
        if i == j:          # entra APENAS na Diagonal Principal! ([0][0], [1][1], [2][2])
            soma_dp += M[i][j]

print(soma_dp)              # 1 + 4 + 1 = 6!
```

> [!CAUTION]
> **Pegadinha clássica da DS 2025 Q10:** Na questão oficial com essa exata matriz `[[1,3,5],[2,4,8],[1,1,1]]`, a banca colocou **`10`** nas alternativas — que é a soma da diagonal **secundária** (`5 + 4 + 1 = 10`) — para pegar quem errou a direção da diagonal! Sempre escreva `[0][0]`, `[1][1]`, `[2][2]` no rascunho antes de somar!

---

### 📚 Parte 3 — Pilha (`LIFO`) vs. Fila (`FIFO`) na Prática

Ambas guardam uma lista de elementos, mas a **regra de quem tem direito de sair** é completamente oposta:

#### 1. Pilha (*Stack*) — Princípio `LIFO` (*Last In, First Out*)
Pense num **tubo de batatinhas ou caixa de papelão fechada no fundo**: você só consegue pôr ou tirar coisas **pela boca de cima (o TOPO)**!
- **`LIFO`:** *"Último a Entrar é o Primeiro a Sair"* (também chamado às vezes de `FILO` — *Primeiro a Entrar é o Último a Sair*).
- **Inserir no topo:** chama-se **`PUSH`** (empilhar).
- **Remover do topo:** chama-se **`POP`** (desempilhar).

```text
   Entra (PUSH) e Sai (POP) sempre pelo TOPO!
                 ↓   ↑
             ┌───────────┐
   TOPO  →   │    "C"    │  <- Último que entrou: sai PRIMEIRO no POP!
             ├───────────┤
             │    "B"    │
             ├───────────┤
   BASE  →   │    "A"    │  <- Primeiro que entrou: fica preso lá embaixo!
             └───────────┘  (fundo fechado!)
```

**💻 Rastreamento Passo a Passo de uma Pilha *(baseado em DS 2019 Q3)*:**
1. Começa vazia: `[]`
2. `PUSH("A")` → `["A"]` *(Base = A, Topo = A)*
3. `PUSH("B")` → `["A", "B"]` *(Topo = B)*
4. `PUSH("C")` → `["A", "B", "C"]` *(Topo = C)*
5. `POP()` → **Remove o TOPO (`"C"`)!** Sobra `["A", "B"]` *(Topo = B)*
6. `PUSH("D")` → Entra em cima do B: `["A", "B", "D"]` *(Topo = D)*
7. `POP()` → **Remove o TOPO (`"D"`)!** Sobra **`["A", "B"]`** *(Base = `"A"`, Topo = `"B"`)*.

#### 2. Fila (*Queue*) — Princípio `FIFO` (*First In, First Out*)
Pense numa **fila de supermercado ou fila de impressão**: quem chegou primeiro fica na **FRENTE (Cabeça)** e sai primeiro; quem chega depois entra atrás, no **FIM (Cauda)**!
- **`FIFO`:** *"Primeiro a Entrar é o Primeiro a Sair"*.
- **Inserir no fim:** **`Enqueue`** / Inserir.
- **Remover da frente:** **`Dequeue`** / Remover.

```text
   Sai (Dequeue) pela FRENTE       Entra (Enqueue) pelo FIM
              ←  ┌──────┬──────┬──────┐  ←
    INÍCIO       │  "A" │  "B" │  "C" │      FIM
                 └──────┴──────┴──────┘
     Primeiro que entrou ("A")          Último que entrou ("C")
     é o PRIMEIRO a sair!               espera todos na frente saírem!
```

**💻 Rastreamento Passo a Passo de uma Fila:**
Usando **os mesmos comandos** que testamos na Pilha, olhe como o resultado muda totalmente:
1. Começa vazia: `[]`
2. `Inserir("A")` → `["A"]`
3. `Inserir("B")` → `["A", "B"]`
4. `Inserir("C")` → `["A", "B", "C"]` *(Frente = A, Fim = C)*
5. `Remover()` → **Sai o da FRENTE (`"A"`)!** Sobra `["B", "C"]` *(Frente agora = B)*
6. `Inserir("D")` → Entra no fim: `["B", "C", "D"]`
7. `Remover()` → **Sai o da FRENTE (`"B"`)!** Sobra **`["C", "D"]`**!

#### Comparação Direta de Prova
| Critério | Pilha (*Stack*) | Fila (*Queue*) |
| :--- | :--- | :--- |
| **Sigla Oficial** | **LIFO** *(Último entra, Primeiro sai)* | **FIFO** *(Primeiro entra, Primeiro sai)* |
| **Inserir / Remover** | **`PUSH`** (topo) / **`POP`** (topo) | **`Enqueue`** (fim) / **`Dequeue`** (frente) |
| **Se entrar `10, 20, 30` e tirar 1** | Sai o **`30`** (sobra `10, 20`) | Sai o **`10`** (sobra `20, 30`) |
| **Uso real no PC** | **`Ctrl+Z` (Desfazer)**, botão **Voltar** do navegador, **Call Stack** (veremos abaixo!) | **Fila da impressora (*Spooler*)**, **fila do Matchmaking**, fila de atendimento |

---

### 📚 Parte 4 — Funções e Recursividade do Zero

#### 1. Primeiro: O que é uma Função Comum?
Uma **Função** (ou sub-rotina) é um **mini-programa com nome próprio** criado para ser reaproveitado várias vezes sem repetir código. Pense numa calculadora ou num liquidificador:
- Ele recebe ingredientes na entrada (**Parâmetros**);
- Executa um cálculo lá dentro;
- Cospe a resposta pronta de volta (**`return`**).

```javascript
function somar(a, b) {      // Recebe dois números nos parâmetros 'a' e 'b'
    let res = a + b;
    return res;             // Devolve o resultado para quem chamou!
}

let total1 = somar(5, 3);   // Passa a=5, b=3 -> devolve 8 e guarda em total1!
let total2 = somar(10, 20); // Reaproveita a mesma função -> devolve 30!
```

#### 2. Agora sim: O que é Recursividade?
Uma função é chamada **Recursiva** quando ela **chama a si própria dentro do próprio código**, dividindo um problema grande em uma versão menor dele mesmo (igual abrir uma boneca russa que tem uma boneca menor dentro, e outra menor, até chegar na última bonequinha sólida!).

Para funcionar sem quebrar o computador, **toda função recursiva tem 2 partes obrigatórias**:
1. **Caso Base (Critério de Parada):** O ponto mais simples onde ela **NÃO** chama a si mesma e apenas devolve uma resposta direta! *(Se você esquecer o Caso Base, ela se chama infinitamente até lotar toda a memória disponível — um travamento famoso chamado **`Stack Overflow`**, "estouro de pilha"!)*
2. **Passo Recursivo:** Quando ainda não chegou no Caso Base, ela chama a si própria com um valor **menor**, caminhando rumo à parada.

#### 3. Como Funciona a *Call Stack* (Pilha de Chamadas da Memória)?
Quando uma função chama outra (ou a si mesma), o computador **pausa** a primeira e anota numa **Pilha LIFO da Memória RAM** chamada ***Call Stack*** (*Pilha de Chamadas*) o ponto onde parou, esperando a nova chamada responder!

Veja o exemplo clássico da **INFO 2025 Q21 — Fatorial Recursivo (`4!`)**.
*(Lembrete rápido: na matemática, o fatorial `n!` multiplica todos os inteiros positivos até `1`: `4! = 4 × 3 × 2 × 1 = 24`, e por regra **`0! = 1`** e **`1! = 1`**!)*

```javascript
function fat(n) {
    if (n <= 1) return 1;        // 1. CASO BASE: para quando n chega em 1 (ou 0)!
    return n * fat(n - 1);       // 2. PASSO RECURSIVO: pausa para calcular fat(n - 1)
}
console.log(fat(4));
```

**Acompanhe a Pilha de Chamadas (*Call Stack*) subindo e descendo passo a passo:**
1. **Descida (empilhando *PUSH* até achar o Caso Base):**
   - `fat(4)` precisa de `4 * fat(3)` → **pausa** na Pilha e chama `fat(3)`
   - `fat(3)` precisa de `3 * fat(2)` → **pausa** na Pilha e chama `fat(2)`
   - `fat(2)` precisa de `2 * fat(1)` → **pausa** na Pilha e chama `fat(1)`
   - `fat(1)` bate no **Caso Base (`1 <= 1`)** → devolve **`1`**!
2. **Subida (desempilhando *POP* e entregando as respostas de baixo pra cima):**
   - `fat(2)` destrava e calcula `2 * 1 =` **`2`** → devolve para `fat(3)`
   - `fat(3)` destrava e calcula `3 * 2 =` **`6`** → devolve para `fat(4)`
   - `fat(4)` destrava e calcula `4 * 6 =` **`24`**!

> [!TIP]
> **Duas dicas fáceis de lembrar:**
> - **`0! = 1`** (não é `0`!).
> - Se calcular fatorial usando `for` em vez de recursão, o acumulador de multiplicação precisa começar com **`1`** (ex.: `res = 1`), porque começar com `0` multiplicaria tudo por zero!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q3 — Pilha LIFO)
*Em uma Pilha vazia inseriram-se os números `5`, `10` e `15` (nessa ordem). Em seguida aplicou-se `POP`, inseriu-se `20` e aplicou-se outro `POP`. Qual o elemento no TOPO e qual a BASE restante?*
- Passo a passo: `[]` → `[5]` → `[5, 10]` → `[5, 10, 15]` → `POP` tira `15` (`[5, 10]`) → `PUSH 20` (`[5, 10, 20]`) → `POP` tira `20` (**`[5, 10]`**).
- **Resposta:** Base = **`5`**, Topo = **`10`**. *(Se fosse uma **Fila FIFO**, o 1º `Dequeue` teria tirado o `5` em vez do `15`!)*

#### Questão Resolvida 2 (Estilo Matriz com Regra Condicional)
*Considere a matriz quadrada `A` 3×3 preenchida por: `se (i + j == 2) entao A[i][j] <- 10 senao A[i][j] <- i * 2`. Qual o valor de `A[2][1]` e qual diagonal recebeu o valor 10?*
- Em `A[2][1]`: linha `i = 2`, coluna `j = 1`. Soma `2 + 1 = 3` (não é igual a `2`, cai no `senao`!). Logo `A[2][1] = 2 * 2 =` **`4`**.
- Como `N = 3`, a regra `i + j == 2` (`i + j == N - 1`) preenche exatamente a **Diagonal Secundária**!


---

## Dia 4 — Front-end/Back-end, Frameworks, Editores/IDEs, Compilação/Build, Git e Licenças

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine que você decidiu abrir uma hamburgueria com mais 3 amigos. Você não vai plantar trigo para fazer a farinha do pão nem fabricar o fogão do zero: você usa equipamentos profissionais prontos, trabalha em equipe sem um amigo jogar fora o que o outro cozinhou, empacota o lanche rápido para entrega e respeita as regras comerciais.

No mundo da programação profissional acontece igualzinho! Um sistema real raramente é feito por uma pessoa só no Bloco de Notas inventando tudo do zero. A Fundação FAT testa justamente se você conhece as ferramentas, os papéis, o trabalho em equipe (**Git**) e as leis (**Licenças de Software**) usadas pelos programadores!

---

### 📚 Parte 1 — Primeiro o Básico: Front-end, Back-end, Responsividade e Frameworks

Antes de falar nomes de ferramentas famosas, entenda **onde** cada pedaço de um site ou aplicativo trabalha:

```text
   [ SEU CELULAR OU NAVEGADOR ]                   [ SERVIDOR DA EMPRESA (NUVEM) ]
   ┌──────────────────────────┐                   ┌──────────────────────────────┐
   │        FRONT-END         │ ── Pedido HTTP ─→ │           BACK-END           │
   │  Telas, botões, menus,   │                   │  Regras de negócio, senhas,  │
   │  cores e interação que   │ ←─ Resposta ───── │  cálculos secretos e conexão │
   │  você vê e clica!        │                   │  com o Banco de Dados!       │
   └──────────────────────────┘                   └──────────────────────────────┘
```

- **Front-end (*Lado do Cliente*):** É **tudo o que roda no navegador ou celular do usuário** — botões, cores, textos, menus e cliques.
- **Back-end (*Lado do Servidor*):** É o **"cérebro nos bastidores"** que roda lá no computador da empresa — confere se sua senha bate, calcula frete, valida estoque e grava dados no banco (o usuário não enxerga esse código rodando).
- **Layout Responsivo:** Significa fazer o **mesmo site se adaptar automaticamente** a qualquer tamanho de tela — em colunas lado a lado no monitor widescreen, ou empilhado certinho numa tela estreita de celular, sem cortar botões nem precisar dar zoom com os dedos!

#### Biblioteca vs. Framework (Qual a diferença?)
- **Biblioteca (*Library*):** É como **uma caixa de ferramentas** ou baixar um pacote de texturas num jogo: seu código está no comando e só chama uma função pronta da biblioteca quando precisar (ex.: uma biblioteca que gera PDF).
- **Framework:** É um **esqueleto arquitetural completo** (como usar uma *Game Engine* — Unity/Unreal — ou *Mod Loader* pronto): ele já traz a estrutura pronta organizada (rotas, telas, segurança) e **você encaixa o seu código dentro das regras dele**. (Na computação, isso chama-se *Inversão de Controle*: é o framework que chama as partes do seu código na hora certa!)

#### Os 4 Frameworks que Mais Caem na Etec *(DS 2025 Q7 & DS 2019 Q18)*

| Framework | Linguagem Base | Onde Atua? | Como Explicar em Linguagem Simples (E O Que Cai na Prova) |
| :--- | :--- | :--- | :--- |
| **Bootstrap** | HTML + CSS + JS | **Front-end Web Responsivo** | Traz um **sistema de grade de 12 colunas** e componentes visuais prontos (botões, menus, alertas, cards) que fazem o site se ajustar automaticamente do PC para o celular (*mobile-first*). *(DS 2019 Q18)* |
| **Angular** *(Google)* | **TypeScript** / JavaScript | **Front-end Web SPA** | *(**TypeScript** é um "JavaScript turbinado com etiqueta de tipos" criado pela Microsoft. **SPA = Single Page Application**: site que parece um app de 1 página só, trocando telas e dados instantaneamente sem recarregar a aba inteira!).* O Angular organiza grandes sistemas web em **componentes** reutilizáveis. |
| **Laravel** | **PHP** | **Back-end Web (Servidor)** | Ajuda a construir sistemas no servidor seguindo o padrão **MVC** (*Model-View-Controller*): divide o código em **3 camadas** — **`Model`** conversa com o banco de dados, **`View`** monta a tela visual entregue ao navegador e **`Controller`** recebe o clique/pedido do usuário e decide o que fazer. |
| **React Native** *(Meta)* | JavaScript / React | **Aplicativos Mobile Nativos** *(Android e iOS)* | Permite escrever o aplicativo **uma única vez** em JavaScript e gerar botões e telas **nativas reais** tanto para Android quanto para iPhone (não é só um site colado dentro de um navegador!). |

> [!CAUTION]
> **Pegadinha clássica da DS 2025 Q7 (Molde 2 — Lista com Intruso):** A banca pede *"quais são frameworks de desenvolvimento"* e mistura no meio **Creative Commons** (que é uma **licença de direitos autorais**!) e **Adobe Creative Cloud** (que é o pacote pago de Photoshop/Illustrator/Premiere para design e vídeo!). Também costuma trocar as camadas dizendo que **Laravel** serve para fazer apps mobile ou front-end visual puro!

---

### 📚 Parte 2 — Onde Programadores Escrevem Código: Bloco de Notas vs. Editor vs. IDE vs. WYSIWYG

A Fundação FAT cobra literalmente a diferença entre esses 4 tipos de programas *(DS 2025 Q19)*:

*(Antes da tabela, tradução de 2 termos usados nela: **`UTF-8`** é o padrão internacional de texto que garante que acentos como `ç`, `ã`, `é` e emojis apareçam certinhos; e **`Debugger com Breakpoints`** é uma ferramenta que deixa você colocar "pontos de pausa" no meio do código para congelar o programa na linha 5 e espiar quanto cada variável está valendo na memória!)*

| Categoria | O que Tem Dentro? | Exemplos Oficiais da Prova | Pegadinha Clássica |
| :--- | :--- | :--- | :--- |
| **1. Editor de Texto Simples** | Digita apenas texto puro (`UTF-8`), **SEM** colorir códigos, **SEM** autocompletar e **SEM** compilador/debugger. | **Bloco de Notas (Notepad)** do Windows, TextEdit | Você *até pode* digitar HTML no Bloco de Notas e salvar como `.html`, **mas ele NÃO é uma IDE!** |
| **2. Editor de Código-Fonte** | Programa leve e rápido feito para escrever código: oferece **realce de sintaxe** (colore palavras-chave para facilitar leitura), numeração de linhas, fechamento automático e extensões. | **VS Code (*Visual Studio Code*)**, Sublime Text, Notepad++ | **Cuidado:** **VS Code** recém-instalado é classificado oficialmente como **Editor de Código** — **NÃO confunda com *Visual Studio*!** |
| **3. IDE** (*Integrated Development Environment*) | **Ambiente Integrado de Desenvolvimento:** é uma suíte completa que já junta dentro dela **Editor + Tradutor (Compilador/Interpretador) + Depurador (*Debugger* com breakpoints) + Gerenciador de Projeto**. | **Visual Studio** (Microsoft), **Eclipse**, **IntelliJ IDEA**, **NetBeans**, **PyCharm**, **Android Studio** | *Visual Studio* (pesado, completo) = **IDE**! *Visual Studio Code* (leve) = **Editor de Código**! |
| **4. Editor WYSIWYG** (*What You See Is What You Get*) | *"O que você vê é o que você obtém"*: você monta a tela **arrastando botões e fotos visualmente com o mouse**, vendo o resultado pronto na hora enquanto o programa gera o HTML/CSS escondido. | **Adobe Dreamweaver** (modo visual), **Wix**, **WordPress Elementor**, Google Sites | Foca em montagem visual rápida sem digitar código linha a linha. |

---

### 📚 Parte 3 — Traduzindo e Empacotando Código: Compilação, Interpretação, *Build* e *Bundling*

#### 1. Código-Fonte vs. Código de Máquina (`0 e 1`)
Quando você escreve `if (hp > 0)` em Portugol, JavaScript ou C, isso se chama **Código-Fonte** (escrito em texto legível para humanos). O processador (CPU), porém, só entende pulsos binários de **`0` e `1`** (**Código de Máquina**). Como traduzimos o código humano para a máquina executar? Existem **3 modelos**:

1. **Compilador (ex.: C, C++, Go, Rust):** Traduz o projeto inteiro **antes** de rodar:
   `Código-Fonte (.c)` → **Compilador** → `Código-Objeto (.o, binário parcial)` → **Linker (Ligador)** *(encaixa bibliotecas prontas do sistema)* → **Arquivo Executável final (`.exe` no Windows)**.
   - *Vantagem:* Roda super rápido e o cliente abre o `.exe` sem precisar instalar nada nem ver seu código-fonte!
2. **Interpretador (ex.: Python, JavaScript, PHP):** Não cria `.exe` antes — ele lê e traduz o código **linha por linha na hora em que está rodando**.
   - *Vantagem:* Fácil testar na hora no navegador ou terminal, mas exige que o PC tenha o interpretador (navegador / Python) instalado.
3. **Modelo Híbrido (Java e C#):** Mistura os dois! Primeiro o compilador transforma o código em um formato intermediário chamado ***Bytecode*** (`.class` no Java). Depois, uma "mini-máquina tradutora" instalada em qualquer PC ou celular chamada **JVM (*Java Virtual Machine*)** lê esse bytecode e roda no Windows, Linux ou Mac (*"Escreva uma vez, rode em qualquer lugar"*).

#### 2. *Build*, *Bundling*, *Minificação* e *Tree Shaking* na Web Moderna *(DS 2025 Q22)*
Imagine que um site profissional feito com React ou Angular foi dividido pelo time em **150 arquivos `.js` e `.css` separados** para ficar fácil de organizar. Se o celular de quem acessa tivesse que baixar 150 arquivos um por um pela internet, o site abriria muito devagar!

Por isso, antes de colocar o site no ar (em produção), rodamos ferramentas automatizadas (como **Webpack** ou **Vite**):

```text
  [ 150 arquivos organizados p/ dev ] ──(Build & Bundling)──→ [ 1 arquivo bundle.min.js leve ]
  (.ts, .js, .css, códigos extras)                               (pronto para abrir rápido!)
```

- ***Transpilação*:** Traduzir código de uma linguagem moderna para uma versão que todo navegador antigo entende (ex.: converter **TypeScript → JavaScript** padrão).
- ***Build* (Construção):** É o **processo completo automatizado** que prepara o projeto para ser publicado — faz transpilação, confere erros/testes, otimiza imagens e gera a pasta final pronta para o servidor (`dist/` ou `build/`).
- ***Bundling* (Empacotamento):** É a etapa específica feita pelos *bundlers* (**Webpack, Vite, Parcel**) de **juntar dezenas de arquivos JS e CSS picados em poucos arquivos consolidados (*bundles*)**, diminuindo dezenas de downloads individuais na rede!
- **Minificação (*Minification*):** Apaga espaços vazios, comentários e encurta nomes internos gigantes (`calculaTotalDePontos` vira `a`) só para o arquivo pesar menos KB e baixar instantaneamente.
- ***Tree Shaking* ("Sacudir a árvore"):** O empacotador detecta funções que você importou de uma biblioteca mas **nunca usou** no site, e **"sacode para fora"**, excluindo esse código morto do arquivo final!

---

### 📚 Parte 4 — Git: Trabalhando em Equipe Sem Destruir o Código *(DS 2019 Q26)*

Se dois programadores tentarem editar o mesmo arquivo `jogo.js` trocando cópias no pendrive (`jogo_final_agora_vai_v3.zip`), um apaga o trabalho do outro ou ninguém lembra o que mudou ontem.

Para evitar esse caos existe o **Git**: um **Sistema de Controle de Versão Distribuído** (cada programador tem uma cópia inteira do histórico no próprio PC). Já sites como **GitHub, GitLab e Azure DevOps** são a **nuvem na internet** onde os programadores sincronizam seus projetos Git.

#### Linha do Tempo Visual do Git (Como Funciona na Prática)
```text
   Arquivos editados        git add          git commit
   no seu computador  ───→  Staging   ────→  Histórico Permanente (Snapshot)
     (Working Dir)        (Preparação)       c1 ─── c2 ─── c3  [ramo principal: main]
                                                      \
                                                       └─ c4 ── c5  [git branch nova-tela]
                                                                  \
                                                           (testou e deu bom -> git merge!)
```
- **`git init` / `git clone <url>`:** Cria um repositório Git novo numa pasta / Baixa um projeto inteiro da nuvem para o seu PC.
- **`git status`:** Mostra na hora quais arquivos foram mexidos depois do último *commit*.
- **`git add <arquivo>` (ou `git add .`):** Coloca as alterações escolhidas na **área de preparação (*Staging Area*)**, marcando o que entrará na próxima "foto".
- **`git commit -m "Corrige soma da média"`:** Tira uma **"foto permanente" (*snapshot*)** das mudanças preparadas com data, autor e mensagem de explicação no histórico.
- **`git branch nova-tela` *(MUITO COBRADO! DS 2019 Q26)*:** Cria uma **ramificação paralela e isolada** do projeto (`main`) — igual criar um *Save Slot* separado no jogo antes de testar um mod arriscado, para poder programar uma função nova sem estragar o site que está no ar!
- **`git diff` *(DS 2019 Q26)*:** **Compara** e exibe exatamente **o que mudou linha por linha** entre versões, arquivos ou branches.
- **`git merge nova-tela` *(DS 2019 Q26)*:** Depois que você testou a `branch` e garantiu que não tem bugs, o **`merge` funde (mescla)** o trabalho daquela ramificação de volta para dentro da `main`!
- **`git push` / `git pull`:** **`push`** empurra seus commits locais para a nuvem (GitHub); **`pull`** puxa e integra para o seu PC o que seus colegas enviaram.

---

### 📚 Parte 5 — Licenças de Software: Código Aberto vs. Fechado, Livre vs. Grátis *(DS 2025 Q23 & M-Tec Q36)*

Essa é uma das pegadinhas jurídicas favoritas da banca: **NUNCA confunda "ser de código aberto/livre" com "custar R$ 0 (grátis)"!**

- **Código-Fonte Aberto:** Qualquer pessoa consegue baixar e **ler como o programa foi feito** por dentro (os arquivos em Python, C, JS...).
- **Código-Fonte Fechado:** A empresa entrega apenas o programa compilado (`.exe`), **escondendo totalmente** como ele funciona por dentro para ninguém copiar nem alterar.

| Modelo / Licença | Código-Fonte é Aberto? | Pode Modificar e Redistribuir? | Precisa Custar `R$ 0`? | Exemplos Reais (Conexão Dia a Dia) |
| :--- | :---: | :---: | :---: | :--- |
| **Software Livre** *(Free Software — FSF)* | **SIM (Aberto)** | **SIM** | **NÃO obrigatoriamente!** Pode ser vendido! | Defende as **4 Liberdades Fundamentais** (1. usar p/ qualquer fim, 2. estudar/alterar o código, 3. redistribuir cópias, 4. distribuir modificações). Ex.: **Linux**, **LibreOffice**, **GIMP**, **OBS Studio**. |
| ***Open Source*** *(Código Aberto — OSI)* | **SIM (Aberto)** | **SIM** | Quase sempre sim | Foca na colaboração técnica. Principais licenças: **MIT, Apache 2.0, BSD** (permissivas — empresas podem fechar produtos em cima) e **GPL** (*copyleft* — exige que projetos derivados continuem abertos!). |
| **Proprietário / Comercial** | **NÃO (Fechado)** | **PROIBIDO** | Pago (ou assinatura) | Protegido por contrato **EULA (*End User License Agreement*)** — aquele termo que diz *"não copie, não revenda, não faça engenharia reversa"*. Ex.: **Windows, Photoshop, Jogos da Steam**. |
| ***Freeware*** | **NÃO (Fechado)** | **PROIBIDO modificar** | **SIM (`R$ 0`)** | **Grátis para baixar, MAS código fechado!** Ex.: **Discord, Valorant, Spotify grátis, Adobe Reader**. ***Freeware* NÃO é Software Livre!** |
| ***Shareware* / *Trial*** | **NÃO (Fechado)** | **PROIBIDO** | Grátis só por tempo limitado | Libera por ex. 30 dias (ou funções travadas) até você pagar a licença definitiva. |
| **Assinatura (*SaaS*)** | Geralmente fechado | **PROIBIDO** | Mensalidade / Anuidade | Você paga todo mês para continuar usando e recebendo atualizações (ex.: **Microsoft 365, Adobe Creative Cloud**). |

> [!CAUTION]
> **Pegadinha clássica da banca (DS 2025 Q23 & M-Tec 2022 Q36):**
> 1. ***"Todo Software Livre precisa ser gratuito (R$ 0)?"*** → **FALSO!** Em inglês *"Free Software"* significa *"livre como liberdade de expressão, não como cerveja grátis"*! Uma empresa pode cobrar pela mídia, instalação ou suporte de um Software Livre — a exigência obrigatória é entregar as **4 liberdades + código-fonte aberto**!
> 2. ***"Discord e Skype são Open Source porque são grátis?"*** → **FALSO!** Eles são ***Freeware*** (código-fonte fechado distribuído sem custo)!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q26 & DS 2025 Q19 — Editores, Git e Bundling)
*Analise: I. O Bloco de Notas (Notepad) é classificado como IDE por permitir salvar arquivos `.html`. II. No Git, `git branch` cria linha paralela de desenvolvimento, `git diff` mostra diferenças linha a linha e `git merge` une ramificações. III. Bundlers como Webpack agrupam vários módulos JS/CSS para diminuir requisições na rede.*
- **Item I é FALSO:** Bloco de Notas é editor de texto simples (não possui compilador, realce avançado nem debugger integrados).
- **Item II é VERDADEIRO:** Definição exata de cada comando Git.
- **Item III é VERDADEIRO:** Função exata de *bundling*.
**Gabarito:** **II e III corretas**.

#### Questão Resolvida 2 (Baseada em DS 2025 Q23 — Licenças)
*Qual afirmação está INCORRETA sobre licenciamento?*
- *A) Software Open Source permite ler e melhorar o código-fonte.* (Verdadeira)
- *B) Softwares proprietários usam EULA restringindo cópia e modificação.* (Verdadeira)
- *C) Software Livre proíbe cobrança financeira e entrega apenas o executável sem código-fonte.* (**FALSA!** Ele tanto permite cobrar distribuição/suporte quanto **exige** acesso aberto ao código-fonte!)
**Gabarito:** **C**.


---

## Dia 5 — Engenharia de Software, Requisitos, SWOT, UML (Diagramas), Scrum/XP, Testes e POO

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine construir um prédio de 15 andares **sem engenheiro nem planta**: os pedreiros simplesmente chegam no terreno no dia 1 e começam a empilhar tijolos no chute. No quinto andar, descobrem que esqueceram o espaço do elevador, os canos de esgoto não batem e o solo não aguenta o peso!

Na década de 1960 aconteceu exatamente isso com a computação — a famosa **Crise do Software**: os programas ficaram grandes, mas os programadores apenas sentavam e saíam digitando código sem planejar nada. Os projetos estouravam o orçamento em 300%, atrasavam anos e davam erro toda hora. Foi aí que nasceu a **Engenharia de Software**: um conjunto organizado de métodos, desenhos e regras de equipe para construir aplicativos confiáveis dentro do prazo e do orçamento.

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

Pense no desenvolvimento de um **grande jogo online** por um estúdio:
- Se o estúdio passar 5 anos fazendo o jogo escondido sem mostrar nem testar com nenhum jogador e só lançar no final, se os jogadores odiarem a mecânica, já era (**Modelo em Cascata**).
- Se o estúdio soltar uma base jogável cedo e for lançando atualizações pequenas toda quinzena ouvindo a comunidade, corrige o rumo rápido (**Métodos Ágeis**).
- Antes mesmo de programar, a equipe lista **o que o personagem faz** (pular, atirar, comprar skin) separado de **como o jogo precisa rodar** (a 120 FPS e sem travar com lag). E dentro do código, em vez de criar um boneco do zero para Mago, Guerreiro e Arqueiro, cria-se um molde geral de "Personagem" que cada classe aproveita!

---

### 📚 Parte 1 — Modelos de Ciclo de Vida (Como um Software Nasce e Evolui)

Todo software passa pelas mesmas etapas: **Entender o que o cliente quer (Requisitos) → Planejar a arquitetura → Programar → Testar → Colocar no ar → Dar manutenção**. O jeito que a equipe organiza a sequência dessas etapas define o **Modelo de Ciclo de Vida**:

```text
  CASCATA (Só vai para frente!)        ÁGIL / ITERATIVO (Ciclos curtos com entrega!)
  [Requisitos]                         ┌─ Ciclo 1 (2 sem): Planeja -> Faz -> Entrega v1!
       ↓                               ↓
  [Planejamento]                       └─ Ciclo 2 (2 sem): Ouve cliente -> Melhora -> v2!
       ↓
  [Código] -> [Testes] -> [Só vê no fim!]
```

| Modelo | Como Funciona Passo a Passo | Quando Usar | Maior Ponto Fraco |
| :--- | :--- | :--- | :--- |
| **Cascata (*Waterfall*)** *(DS 2019 Q8)* | **Sequencial e rígido:** uma etapa só começa quando a anterior terminar 100% e for assinada (desce como uma cachoeira que não sobe). | Sistemas onde as regras nunca mudam no meio (ex.: controle de avião, equipamento hospitalar). | Se o cliente mudar de ideia na metade, voltar etapas sai caríssimo; **cliente só vê o sistema pronto no final!** |
| **Prototipação** | Faz rapidamente uma **versão rascunho (protótipo)** de telas simuladas para o cliente olhar e testar antes de programar de verdade. | Quando o cliente não sabe explicar direito o que quer e precisa "ver para entender". | Risco de o cliente olhar o rascunho visual e achar que o sistema já está pronto! |
| **Espiral** *(Boehm)* | Roda em ciclos (voltas de uma espiral), e **toda volta começa analisando os riscos** antes de prototipar e construir mais um pedaço. | Sistemas gigantes, caros e arriscados (bancos, defesa). | Caro e burocrático demais para aplicativos pequenos ou médios. |
| **Metodologias Ágeis** *(Scrum, Kanban, XP)* | Divide o projeto em **ciclos curtos (1 a 4 semanas)**. Cada ciclo entrega um pedaço funcionando de verdade; **abraça mudanças**! | 90% dos projetos modernos (sites, apps de celular, jogos, startups). | Exige contato constante com o cliente e equipe comunicativa. |

> [!WARNING]
> **Pegadinha clássica (DS 2019 Q8):** No **Modelo em Cascata**, as fases avançam de forma **sequencial** e só se passa para a fase seguinte após concluir a anterior. É **FALSO** afirmar que o Cascata entrega pequenas partes semanais ou pula documentação!

---

### 📚 Parte 2 — Levantando Regras: Viabilidade, Requisitos e Análise SWOT

Antes de contratar programadores, o Analista de Sistemas conversa com os ***Stakeholders*** (**todas as pessoas ou grupos interessados ou afetados pelo sistema**: dono da empresa, clientes, vendedores, estudantes).

*(Tradução de 2 siglas antes de avançar: **`API`** significa uma **"ponte / mensageiro"** que permite dois sistemas diferentes conversarem com segurança — por exemplo, quando o app do iFood mostra o mapa sem ter construído um satélite próprio, ele usa a **API do Google Maps**; e **`ROI` (*Retorno sobre Investimento*)** mede se o lucro ou economia que o software vai trazer paga o dinheiro gasto para fazê-lo!)*

#### 1. Estudo de Viabilidade *(INFO 2025 Q23)*
Antes de gastar dinheiro, responde: *"Dá mesmo para fazer e vale a pena?"* Avalia **3 pilares principais** (além da conformidade com a lei):
- **Viabilidade Técnica:** Existem tecnologias, computadores, APIs e equipe com conhecimento para construir esse sistema?
- **Viabilidade Econômica / Financeira:** Temos orçamento, e o benefício/retorno (**ROI**) compensa o custo de fazer e manter?
- **Viabilidade Operacional:** Quando ficar pronto, as pessoas reais da empresa vão conseguir e querer usar o sistema no dia a dia?

#### 2. Requisitos Funcionais (RF) vs. Requisitos Não Funcionais (RNF)
Vamos aplicar ao exemplo real de um **aplicativo de delivery (tipo iFood)**:

| Tipo | Pergunta-chave | O que descreve na prática | Exemplos reais no App de Delivery |
| :--- | :--- | :--- | :--- |
| **Requisito Funcional (RF)** | **"O QUÊ o sistema faz?"** | Ações, botões, cadastros, regras de cálculo e funções oferecidas ao usuário. | **RF01:** Permitir que o cliente se cadastre com CPF.<br>**RF02:** Calcular a taxa de entrega pela distância.<br>**RF03:** Permitir cancelar o pedido em até 2 minutos. |
| **Requisito Não Funcional (RNF)** | **"COMO o sistema se comporta?"** | Qualidade, velocidade (**desempenho**), **segurança**, **portabilidade**, disponibilidade e regras técnicas. | **RNF01 (Desempenho):** Abrir o cardápio em menos de **2 segundos**.<br>**RNF02 (Segurança):** Guardar senhas embaralhadas (*criptografadas*) e usar conexão com cadeado seguro (**HTTPS**, que veremos no Dia 11).<br>**RNF03 (Portabilidade):** *(DS 2019 Q10)* Conseguir rodar ou ser transferido entre **Android, iPhone e Windows/Linux** sem quebrar! |

> [!TIP]
> **Critérios de um Bom Requisito *(INFO 2025 Q22)*:** Um requisito **NUNCA pode ser vago** como *"O aplicativo deve ser bonito e bem rapidinho"*. Ele precisa ser **Claro, Não Ambíguo e Testável** (ex.: *"responder em até 2 segundos"* dá para medir no relógio!) e **Rastreável** (saber de onde veio aquela regra).

#### 3. Análise SWOT / FOFA *(M-Tec 2022 Q29 & Sim2 Q30)*
Ferramenta visual em **4 quadrantes (`2 × 2`)** para planejar estratégias de um projeto ou empresa separando **o que está dentro da empresa** do **que vem de fora (mercado)**:

```text
               AJUDA A CONQUISTAR O OBJETIVO      ATRAPALHA / TRAZ RISCO
             ┌────────────────────────────────┬────────────────────────────────┐
  INTERNO    │ S — Strengths (FORÇAS)         │ W — Weaknesses (FRAQUEZAS)     │
  (Você      │ Ex.: Equipe experiente, marca  │ Ex.: Servidor antigo, app sem  │
   controla) │ conhecida, código bem feito.   │ suporte à noite, equipe pequena│
             ├────────────────────────────────┼────────────────────────────────┤
  EXTERNO    │ O — Opportunities              │ T — Threats (AMEAÇAS)          │
  (Fora do   │ (OPORTUNIDADES)                │ Ex.: Concorrente gigante       │
   controle) │ Ex.: Nova lei incentivando TI, │ estrangeiro chegando, crise ou │
             │ rival fechou as portas.        │ aumento de imposto/dólar.      │
             └────────────────────────────────┴────────────────────────────────┘
```

---

### 📚 Parte 3 — UML (Desenhando Sistemas Visualmente) e Dicionário de Dados

**UML (*Unified Modeling Language*)** **NÃO** é uma linguagem de programação — é uma **linguagem visual padronizada de diagramas** usada no mundo inteiro para desenhar sistemas antes e durante a criação do código *(M-Tec 2022 Q30 & INFO 2025 Q24)*.

Veja os **2 Diagramas UML campeões de prova** desenhados na prática:

#### 1. Diagrama de Casos de Uso (*Use Case Diagram* — Comportamental)
Mostra **quem usa o sistema** (o **Ator** = bonequinho, que pode ser humano ou outro sistema!) e **o que ele faz** (elipses com ações no infinitivo).

```text
           ┌────────────── Sistema Escolar Etec ──────────────┐
    O      │                                                  │
   /|\ ────┼──→ ( Realizar Matrícula )                        │
   / \     │          │                   ▲                   │
  Aluno    │          │ <<include>>       │ <<extend>>        │
           │          ▼ (OBRIGATÓRIO)     │ (OPCIONAL)        │
           │    ( Validar CPF )     ( Imprimir 2ª Via Cartão )│
           └──────────────────────────────────────────────────┘
```
- **`<<include>>` (Inclusão OBRIGATÓRIA):** Toda vez que você faz *Realizar Matrícula*, o sistema **OBRIGATORIAMENTE executa junto** *Validar CPF*! (A seta tracejada aponta **para o que é incluído**).
- **`<<extend>>` (Extensão OPCIONAL):** *Imprimir 2ª Via* **só acontece às vezes**, se o aluno marcar essa opção extra — a matrícula funciona normalmente sem ela! (A seta tracejada aponta **da extensão para o caso base**).

#### 2. Diagrama de Classes (Estrutural / Estático)
Desenha os moldes dos objetos do código como **caixas divididas em 3 andares**:
```text
┌──────────────────────────────────┐
│              Aluno               │  ← 1º Andar: NOME DA CLASSE
├──────────────────────────────────┤
│ - cpf: string      (Privado: -)  │  ← 2º Andar: ATRIBUTOS (Dados/Características)
│ + nome: string     (Público: +)  │     Símbolos de visibilidade na prova:
│ # media: float     (Protegido:#) │     + Público | - Privado | # Protegido
├──────────────────────────────────┤
│ + calcularMedia(): float         │  ← 3º Andar: MÉTODOS (Ações que ela faz)
└──────────────────────────────────┘
```

#### 3. Dicionário de Dados *(M-Tec 2022 Q32)*
É um **catálogo descritivo complementar** onde cada dado do sistema tem nome, tipo, tamanho máximo, obrigatoriedade e regras anotados para ninguém na equipe usar nomes ou regras diferentes:

| Nome do Campo | Tipo e Tamanho | Obrigatório? | Regra / Domínio | Significado |
| :--- | :--- | :---: | :--- | :--- |
| `cpf_aluno` | `CHAR(11)` | Sim (`NOT NULL`) | Exatamente 11 dígitos únicos | CPF do estudante sem pontos |
| `nota_final` | `DECIMAL(4,2)` | Não | Valores apenas de `0.00` a `10.00` | Média final no bimestre |

---

### 📚 Parte 4 — Scrum, Kanban, XP (*Pair Programming*) e Níveis de Teste

#### 1. Como Funciona o **Scrum** Passo a Passo (Sem Confusão de Papéis!)
Imagine uma equipe usando **Scrum** para criar o sistema da escola:
1. O **Product Owner (PO)** conversa com a diretoria e monta o ***Product Backlog*** (uma lista priorizada por valor: o que é mais urgente fazer primeiro!). **O PO decide O QUÊ construir e em qual ordem** — ele é a voz do negócio/cliente!
2. A equipe escolhe as tarefas do topo da lista para construir numa **Sprint** (um ciclo fixo de **1 a 4 semanas** que termina com parte do sistema funcionando!).
3. Todo dia, no mesmo horário, o **Time de Desenvolvimento (*Developers*)** faz a ***Daily Scrum***: uma reunião rápida de **no máximo 15 minutos**, geralmente em pé (ou na call do Discord), respondendo o que fez ontem, o que fará hoje e se há algo travando o trabalho *(DS 2019 Q12)*.
4. Apareceu algum problema travando a equipe (ex.: falta senha do servidor)? Entra o **Scrum Master (SM)**: ele **NÃO é o "chefe mandão"** que distribui ordens nem quem escreve as regras! O SM é um **líder servidor/facilitador** cujo trabalho é garantir que o time entenda o Scrum e **remover impedimentos** para a equipe produzir bem!
5. Ao fim da Sprint ocorrem a ***Sprint Review*** (mostra o sistema funcionando para o cliente aprovar) e a ***Sprint Retrospective*** (o time conversa internamente sobre como melhorar na próxima Sprint).

#### 2. **Kanban** & Limite de Trabalho em Progresso (**WIP**)
É um quadro visual com cartões andando por colunas para enxergar gargalos na hora:
```text
┌───────────────┬─────────────────┬──────────────────┬───────────┐
│  A FAZER      │ FAZENDO (WIP=2) │ EM TESTE (WIP=2) │  FEITO    │
├───────────────┼─────────────────┼──────────────────┼───────────┤
│ [Criar Login] │ [Tela Notas]    │ [Ajuste Menu]    │ [BD Base] │
│ [Relatório]   │ [Botão Pix]     │                  │           │
└───────────────┴─────────────────┴──────────────────┴───────────┘
```
- **Regra de ouro do Kanban:** **Limitar o `WIP` (*Work In Progress* — Trabalho em Progresso)**! Significa proibir pegar 10 tarefas ao mesmo tempo sem terminar nenhuma ("empurrar tarefas"), focando em **terminar** o que começou antes de puxar outra!

#### 3. **XP (*Extreme Programming*) — *Pair Programming*** *(DS 2019 Q24)*
Uma prática famosa da metodologia ágil **XP** muito cobrada na FAT:
- **Programação em Par (*Pair Programming*):** **Dois programadores sentam juntos NO MESMO COMPUTADOR** (ou compartilham exatamente a mesma tela/arquivo ao vivo)!
  - Um é o **Piloto (*Driver*):** fica com o teclado, concentrado em digitar a linha atual.
  - O outro é o **Copiloto (*Navigator*):** observa, pega erros na hora e pensa na estratégia geral. Depois eles **trocam de lugar**! *(Pegadinha de prova: dizer que cada um fica em uma sala diferente fazendo códigos separados — FALSO!)*

#### 4. Os 4 Níveis Oficiais de Teste de Software *(DS 2019 Q25)*
1. **Teste de Unidade (Unitário):** Testa a **menor peça isolada** do programa — uma única função sozinha (ex.: testar `calcularFrete(10)` sem ligar banco de dados nem internet).
2. **Teste de Integração:** Testa se **peças diferentes conversam direito juntas** (ex.: o *Controller* que controla o pedido + o Banco de Dados MySQL + o *Gateway de pagamento*, que é o sistema intermediário de cartão/Pix como MercadoPago/PagSeguro).
3. **Teste de Sistema:** Testa o aplicativo **inteiro de ponta a ponta** num ambiente igual ao real (clica em tudo: login → busca → carrinho → pagamento).
4. **Teste de Aceitação (UAT):** Validação final feita **com o cliente/usuário** confirmando que o sistema atende às regras combinadas.

---

### 📚 Parte 5 — Programação Orientada a Objetos (POO) do Zero

Até o Dia 3 vimos programação passo a passo por funções soltas. Em projetos grandes, a **POO (Programação Orientada a Objetos)** organiza o código imitando objetos do mundo real!

#### Passo 1: O Básico — **Classe** vs. **Objeto** vs. **Atributos** vs. **Métodos**
- **Classe:** É o **molde / forma de bolo / planta da casa**. Ela **não** é um objeto vivo ainda — ela apenas descreve o que todo objeto daquele tipo **tem** (**Atributos** = características, ex.: `nome`, `hp`) e o que ele **faz** (**Métodos** = ações/funções lá dentro, ex.: `atacar()`).
- **Objeto (Instância):** É **o bolo pronto assado a partir da forma** — existe de verdade ocupado espaço na Memória RAM! Com 1 única Classe `ContaBancaria`, você cria milhares de Objetos independentes (a conta da Ana com `R$ 500`, a conta do João com `R$ 1.200`).

**Antes de olhar o código Python abaixo, entenda 3 detalhezinhos da sintaxe dele:**
- **`def __init__(self, ...):`** → É o **Construtor**: a função especial que roda automaticamente no segundo em que um novo Objeto é fabricado a partir da Classe, servindo para preencher os valores iniciais dele (`nome`, `peso`).
- **`self`** → Em Python significa **"eu mesmo"** (aquele objeto específico que está sendo criado ou usado agora, para não confundir o `nome` do Rex com o `nome` do Mingau!).
- **`__nome`** *(com dois underscores `__` na frente)* → Marca o atributo como **Privado**! Ninguém de fora da classe consegue mudar `rex.__nome` diretamente sem permissão!

```python
class Animal:                           # CLASSE (o molde geral)
    def __init__(self, nome, peso):     # CONSTRUTOR: monta o objeto na memória
        self.__nome = nome              # PRIVADO (__): protegido de alteração direta!
        self.__peso = peso

    def get_nome(self):                 # MÉTODO público para ler o nome com segurança
        return self.__nome

    def emitir_som(self):               # MÉTODO padrão
        return "..."

class Cachorro(Animal):                 # HERANÇA: Cachorro herda tudo de Animal!
    def emitir_som(self):               # POLIMORFISMO: adapta o som do jeito dele!
        return "Au au!"

class Gato(Animal):                     # HERANÇA: Gato também herda de Animal!
    def emitir_som(self):               # POLIMORFISMO: responde diferente ao mesmo método!
        return "Miau!"

# Criando dois OBJETOS reais (instâncias) na memória RAM:
rex = Cachorro("Rex", 12)
mingau = Gato("Mingau", 4)
print(rex.get_nome(), "faz:", rex.emitir_som())       # Rex faz: Au au!
print(mingau.get_nome(), "faz:", mingau.emitir_som()) # Mingau faz: Miau!
```

#### Passo 2: Os **4 Pilares Oficiais da POO** Explicados Um por Um *(DS 2019 Q27)*
1. **Abstração:** Focar **apenas nas características e ações que importam para o sistema**, ignorando detalhes inúteis do mundo real. *(Ex.: num sistema de escola, o objeto `Aluno` tem `nome`, `cpf` e `notas` — não importa qual a cor da meia ou o prato favorito dele!)*
2. **Encapsulamento:** **Esconder e proteger os dados internos** (`private` / `__`) dentro de uma "cápsula", proibindo que qualquer código de fora coloque valores absurdos (ex.: `conta.saldo = -999999`), e liberando acesso apenas por métodos seguros com regras de checagem (ex.: `depositar(valor)` que confere se `valor > 0`).
   - *🎮 Conexão Gamer:* É deixar o `hp` como privado para jogadores não editarem a vida direto com cheat!
3. **Herança:** Permite criar uma **Classe Filha (Subclasse)** que **herda automaticamente** atributos e métodos já prontos de uma **Classe Mãe (Superclasse)**, evitando repetir código. *(Ex.: `Mago` e `Guerreiro` herdam `hp`, `nome` e `andar()` de `Personagem`, e cada um só adiciona suas próprias magias/armas!)*
4. **Polimorfismo** (*"Muitas Formas"*): Permite que **objetos diferentes respondam de maneiras diferentes ao mesmo nome de comando/método**. *(Ex.: tanto `rex.emitir_som()` quanto `mingau.emitir_som()`, ou apertar `Q` (`usarHabilidade()`) com `Mago` solta bola de fogo e com `Guerreiro` dá golpe de escudo!)*

> [!CAUTION]
> **Pegadinha clássica da DS 2019 Q27:** A banca pergunta quais são os **4 Pilares da POO** e coloca distratores como *"Classe, Objeto, Atributo, Método, Compilação"*.
> **Classe, Objeto, Atributo e Método são ELEMENTOS / CONCEITOS BÁSICOS!**
> Os **4 PILARES OFICIAIS da POO** são exclusivamente: **Abstração, Encapsulamento, Herança e Polimorfismo**!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q12 & Q24 — Scrum e XP)
*Julgue: I. O Scrum Master é o chefe tradicional que dita as linhas de código e impõe prazos. II. A Daily Scrum dura no máximo 15 minutos. III. No Pair Programming (XP), dois programadores compartilham o mesmo computador alternando Piloto e Copiloto.*
- **Item I é FALSO:** O Scrum Master é **líder facilitador** que remove impedimentos (quem prioriza o produto é o PO, e o time é auto-organizável).
- **Itens II e III são VERDADEIROS.**

#### Questão Resolvida 2 (Baseada em DS 2019 Q10 & Q27 — Requisitos e POO)
*Um app precisa rodar sem mudanças no Windows, Linux e Android; e na classe `Conta`, `saldo` é `private` só podendo ser alterado por `sacar()`. Quais conceitos aparecem?*
- Rodar em múltiplos ambientes = Requisito Não Funcional de **Portabilidade**;
- Proteger `saldo` como `private` liberando acesso controlado via método = Pilar do **Encapsulamento**!


---

## Dia 6 — Banco de Dados Relacional do Zero, ACID, SQL (DDL/DML/DQL/DCL/TCL) e NoSQL

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine uma loja online vendendo o **último celular do estoque** pela internet. No mesmo segundo, João clica em "Comprar" em São Paulo e Maria clica em "Comprar" em Campinas. Se a loja salvasse o estoque num arquivo de texto simples ou numa planilha do Excel compartilhada, os dois pedidos poderiam passar ao mesmo tempo vendendo **2 aparelhos onde só existia 1**, ou a planilha travaria com 50 mil clientes abrindo juntos!

Para resolver fila simultânea de acessos, buscas ultrarrápidas, permissões de quem pode ler ou apagar e segurança financeira, usamos um **SGBD (*Sistema Gerenciador de Banco de Dados*)** — como **MySQL, PostgreSQL, Oracle, SQL Server ou SQLite** — controlado pela linguagem padrão **SQL (*Structured Query Language*)**.

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

Onde ficam salvos seus servidores do Discord, mensagens enviadas há 2 anos e a lista de skins da sua conta? Num **Banco de Dados**! Quando você troca uma skin na Steam com outro jogador, ou os dois itens trocam de dono exatamente juntos, ou se a internet cair no meio o sistema cancela tudo para ninguém sair roubado. Veremos já como o banco garante isso!

---

### 📚 Parte 1 — O Básico do Zero: O que é Tabela, Coluna, Linha, Chave (`PK`/`FK`) e `JOIN`?

Antes de ler qualquer comando SQL estranho, entenda a **estrutura visual** de um **Banco de Dados Relacional** (que funciona como planilhas inteligentes interligadas entre si):

```text
  TABELA: turmas                           TABELA: alunos
  ┌──────────┬──────────┐                  ┌──────────┬──────────┬──────┬──────────┐
  │ id_turma │ nome     │                  │ id_aluno │ nome     │ nota │ id_turma │
  │ (PK)     │          │                  │ (PK)     │          │      │ (FK) ────┼──┐
  ├──────────┼──────────┤                  ├──────────┼──────────┼──────┼──────────┤  │
  │    10    │ 2º DS    │ ◄────────────────┼──────────┼──────────┼──────┼─── 10    │◄─┘
  │    20    │ 1º Info  │                  │    1     │ Henrique │ 8.50 │    10    │
  └──────────┴──────────┘                  │    2     │ Ana      │ 9.20 │    20    │
                                           └──────────┴──────────┴──────┴──────────┘
```

Olhe o desenho acima e aprenda **os 6 nomes fundamentais**:
1. **Tabela:** É a grade inteira que guarda coisas de um mesmo assunto (ex.: a grade `alunos`, a grade `turmas`).
2. **Coluna (Campo):** É cada informação na vertical (ex.: `nome`, `nota`, `id_turma`). Toda coluna tem um **Tipo de Dado**:
   - **`INT`** → números inteiros (`1`, `10`);
   - **`VARCHAR(100)`** → texto de tamanho variável até `100` letras (`"Henrique"`);
   - **`DECIMAL(4,2)`** → número decimal com precisão exata para notas/dinheiro (`4` dígitos no total, sendo `2` depois do ponto: cabe até `99.99`, perfeito para nota `8.50`!);
   - **`NOT NULL`** → regra dizendo **"campo obrigatório: proibido deixar vazio!"**
3. **Linha (Registro):** É uma ficha completa na horizontal (ex.: toda a ficha `(1, 'Henrique', 8.50, 10)`).
4. **Chave Primária (`PRIMARY KEY` ou `PK`):** É a coluna escolhida como **código único de identificação** de cada linha — igual ao seu CPF! **Nunca pode repetir** (não existem dois alunos com `id_aluno = 1`) e **nunca pode ficar vazia**. Geralmente colocamos **`AUTO_INCREMENT`** para o banco gerar os números `1, 2, 3...` sozinho!
5. **Chave Estrangeira (`FOREIGN KEY` ou `FK`):** Em vez de repetir o nome `"2º DS"` em 40 linhas, gravamos apenas o código **`id_turma = 10`** dentro da tabela `alunos` apontando para a `PK` da tabela `turmas`. Isso garante **integridade**: o banco bloqueia cadastrar um aluno numa turma `999` que não existe!
6. **O que é um `JOIN` (Junção)?** Como os dados ficaram separados em duas tabelas para não repetir informação, na hora de exibir `"Henrique - 2º DS"` num relatório, o banco faz um **`JOIN`**: ele **junta (costura) as duas tabelas lado a lado** combinando onde `alunos.id_turma == turmas.id_turma`! *(Guarde o que é `JOIN`, pois vamos comparar isso lá na frente com os bancos NoSQL!)*

#### O Papel do SGBD e as 4 Garantias **ACID**
O **SGBD** (ex.: MySQL, PostgreSQL) garante as 4 propriedades **ACID** em transações importantes (como um **Pix** ou **Trade na Steam**):
- **A — Atomicidade (*Tudo ou Nada*):** Num Pix de R$ 100 de João para Maria, ou tira R$ 100 de João **E** entra R$ 100 para Maria, ou cancela os dois — jamais some no meio!
- **C — Consistência:** O banco nunca aceita quebrar regras (como `NOT NULL` ou salvar uma `FK` que aponta para turma inexistente).
- **I — Isolamento:** Dois compradores clicando "Comprar" no mesmo milissegundo são organizados em fila segura sem corromper o saldo ou o estoque.
- **D — Durabilidade:** Depois de confirmado definitivamente (`COMMIT`), os dados estão salvos no SSD/HD e não se perdem mesmo se faltar energia elétrica 1 segundo depois!

---

### 📚 Parte 2 — As 5 Sublinguagens Oficiais da SQL (Questão Certa na Prova!)

A linguagem **SQL** organiza seus comandos em **5 famílias (sublinguagens)**. A Fundação FAT cobra **quase todo ano** uma tabela ou questão I-II-III misturando **DDL**, **DML** e **DQL** (**DS 2025 Q11**, **DS 2019 Q7**)!

| Sublinguagem | Significado da Sigla | Comandos Principais | Onde Atua? (Regra de Ouro) | Analogia da Estante de Arquivo |
| :---: | :--- | :--- | :--- | :--- |
| **DDL** | *Data **Definition** Language* (Definição) | **`CREATE`**, **`ALTER`**, **`DROP`**, `TRUNCATE` | Mexe na **ESTRUTURA (esqueleto/desenho)** do banco: cria a tabela, adiciona/muda coluna ou **destrói a tabela inteira**. | **Construir, reformar ou demolir** a estante de aço. |
| **DML** | *Data **Manipulation** Language* (Manipulação) | **`INSERT`**, **`UPDATE`**, **`DELETE`** | Mexe nos **DADOS (linhas/registros)** dentro de uma tabela que já existe! | **Colocar, editar ou tirar pastas** de dentro da estante. |
| **DQL** | *Data **Query** Language* (Consulta) | **`SELECT`** *(com `FROM`, `WHERE`, `JOIN`, `ORDER BY`)* | Apenas **LÊ / CONSULTA** os dados sem modificar nada! *(Alguns livros antigos chamavam de DML, mas a **Etec/FAT cobra separado como DQL**!)* | **Procurar e ler** uma pasta e devolver no lugar. |
| **DCL** | *Data **Control** Language* (Controle) | **`GRANT`**, **`REVOKE`** | Gerencia **PERMISSÕES** (quem pode ler, alterar ou não). *🎮 Igual dar/tirar cargo de Admin no Discord!* | **Dar ou tomar a chave** da sala do arquivo. |
| **TCL** | *Transaction **Control** Language* (Transação) | **`BEGIN`**, **`COMMIT`**, **`ROLLBACK`**, `SAVEPOINT` | Controla **TRANSAÇÕES**: confirma de vez (`COMMIT`) ou desfaz tudo se der erro (`ROLLBACK`). *🎮 Igual sistema anti-golpe de Trade na Steam!* | **Carimbar "Confirmado"** no Pix ou **estornar** tudo. |

#### Veja Cada Sublinguagem Transformando uma Tabela Passo a Passo!

**1. DDL — Criando e Reformando a Tabela (Estrutura):**
```sql
CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,   -- Código único automático (1, 2, 3...)
    nome VARCHAR(100) NOT NULL,          -- Texto até 100 letras, obrigatório!
    turma VARCHAR(10),
    nota DECIMAL(4,2)
);
-- Esquecemos a coluna de e-mail! Usamos ALTER TABLE (DDL) para mexer na estrutura:
ALTER TABLE alunos ADD email VARCHAR(120);
```

**2. DML — Inserindo, Editando e Apagando Linhas (Dados):**
```sql
-- INSERT coloca linhas novas na tabela:
INSERT INTO alunos (nome, turma, nota, email)
VALUES
    ('Lucas Ferreira', '2MTEC', 8.50, 'lucas@etec.sp.gov.br'),
    ('Ana Beatriz',    '2MTEC', 9.20, 'ana@etec.sp.gov.br'),
    ('Bruno Costa',    '1MTEC', 5.80, 'bruno@etec.sp.gov.br');

-- UPDATE altera uma linha específica (SEMPRE use WHERE!!):
UPDATE alunos SET nota = 6.50 WHERE id = 3;

-- DELETE apaga APENAS a linha do id = 3 (a tabela 'alunos' continua existindo!):
DELETE FROM alunos WHERE id = 3;
```

**3. DQL — Consultando Sem Modificar Nada:**
```sql
-- Mostra nome e nota apenas dos alunos da '2MTEC' com nota >= 6, da maior para a menor:
SELECT nome, nota
FROM alunos
WHERE turma = '2MTEC' AND nota >= 6.0
ORDER BY nota DESC;
```

**4. DCL & 5. TCL — Segurança e Transação Segura:**
```sql
GRANT SELECT ON alunos TO professor_estagiario;   -- DCL: autoriza apenas leitura (SELECT)
REVOKE SELECT ON alunos FROM professor_estagiario;-- DCL: remove a permissão

BEGIN;                                            -- TCL: abre a transação do Pix!
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;                                           -- TCL: salva os dois juntos! Se falhasse, usaria ROLLBACK;
```

> [!CAUTION]
> **PEGADINHA Nº 1 (`DROP` vs. `DELETE` — DS 2025 Q11):**
> - **`DROP TABLE alunos;`** é **DDL**: **demole a estante inteira** (apaga estrutura e dados). Se tentar fazer `SELECT` depois, dá erro *"Tabela não existe"*.
> - **`DELETE FROM alunos WHERE id = 3;`** é **DML**: tira apenas a pasta do Bruno; a tabela vazia/restante continua de pé!
> - **Esquecer o `WHERE`** num `UPDATE` ou `DELETE` altera ou apaga **TODAS as linhas da tabela de uma vez**!

---

### 📚 Parte 3 — Dominando `WHERE`, Filtros e Funções de Contagem/Soma (`COUNT(*)`)

#### 1. Cláusulas de Filtro e Ordenação do `SELECT` *(INFO 2025 Q28)*
A ordem obrigatória das palavras em um `SELECT` é sempre: **`SELECT ... FROM ... WHERE ... ORDER BY ...`**:
- `WHERE cidade = 'São Paulo' AND idade >= 18` → Traz a linha só se as **duas** condições forem verdadeiras.
- `WHERE turma = 'A' OR turma = 'B'` → Basta **uma** ser verdadeira.
- `WHERE nome LIKE 'An%'` → Busca textos que **começam** com `"An"` (`%` funciona como coringa: `"Ana"`, `"Anderson"`).
- `WHERE nota BETWEEN 6 AND 10` → Intervalo fechado de `6` até `10`.
- `ORDER BY nome ASC` (crescente A→Z, padrão) ou `DESC` (decrescente Z→A ou maior→menor).

#### 2. A Diferença Entre `COUNT(*)` e `SUM()` *(DS 2025 Q14)*
Considere esta mini-tabela **`vendas`**:

| `id_venda` | `vendedor` | `cidade` | `valor` |
| :---: | :--- | :--- | :---: |
| `1` | João | São Paulo | `200` |
| `2` | Maria | Campinas | `500` |
| `3` | Pedro | São Paulo | `150` |

Veja como cada função responde algo completamente diferente após filtrar `WHERE cidade = 'São Paulo'` (sobram as linhas `1` e `3`):
- **`SELECT COUNT(*) FROM vendas WHERE cidade = 'São Paulo';`** → Retorna **`2`**! *(Porque existem **2 linhas** de São Paulo — `COUNT(*)` apenas **CONTA QUANTAS LINHAS** passaram no filtro!)*
- **`SELECT SUM(valor) FROM vendas WHERE cidade = 'São Paulo';`** → Retorna **`350`** (`200 + 150` — `SUM` **SOMA os números** daquela coluna).
- **`SELECT AVG(valor) FROM vendas WHERE cidade = 'São Paulo';`** → Retorna **`175`** (`350 ÷ 2` — `AVG` faz a **média**).
- **`SELECT MAX(valor)`** → **`500`** | **`SELECT MIN(valor)`** → **`150`**.

> [!CAUTION]
> **Pegadinha clássica da DS 2025 Q14:** A banca cria alternativas erradas escrevendo `SELECT * FROM vendas WHERE COUNT(cidade) = 2;` ou trocando `FROM` e `WHERE` de lugar. **Regra sagrada:** **`COUNT(*)` vai SEMPRE na parte do `SELECT` (entre `SELECT` e `FROM`), e JAMAIS dentro do `WHERE`!**

---

### 📚 Parte 4 — Bancos NoSQL (*Not Only SQL*) do Zero *(INFO 2025 Q29)*

Por que existem bancos chamados **NoSQL (*"Não Apenas SQL"*)** se o SQL já é tão bom?
Porque bancos relacionais (MySQL/PostgreSQL) usam tabelas rígidas com colunas fixas (se um produto precisar de um campo extra só para ele, você precisa dar `ALTER TABLE`), e quando crescem muito costumam exigir **Escalabilidade Vertical** (colocar o banco inteiro num servidor único gigantesco e super caro).

Quando redes sociais, Netflix e Amazon passaram a guardar bilhões de dados variados por dia, precisaram de **Escalabilidade Horizontal (*Sharding*)**: em vez de comprar 1 supercomputador de R$ 100 mil, você **fatia e espalha os dados por 20 computadores comuns trabalhando em rede**! Daí nasceu o mundo **NoSQL** com **esquema flexível (*schema-less*)** e **sem JOINs complexos** (tudo do mesmo assunto fica guardado junto num pacote só!).

#### Primeiro: O que é um Documento **JSON**?
No mundo NoSQL mais famoso, os dados são salvos em **JSON (*JavaScript Object Notation*)**: um formato de texto super leve em pares **`"chave": valor`** entre chaves **`{ ... }`** (onde listas ficam entre colchetes **`[ ... ]`**):
```json
{
  "_id": "user_901",
  "nome": "Henrique Silva",
  "curso": "DS M-Tec",
  "telefones": ["1199999-0001", "1198888-0002"],
  "endereco": { "cidade": "São Paulo", "uf": "SP" }
}
```
Repare que **os telefones e o endereço moram aninhados dentro do mesmo documento!** Na hora de ler o perfil do Henrique, o MongoDB lê **1 documento só**, sem precisar fazer `JOIN` costurando 3 tabelas separadas!

#### As 4 Famílias Principais de NoSQL na Prova
| Família NoSQL | Como Organiza os Dados | Exemplos Famosos | Onde É Usada (Mundo Real + Gamer) |
| :--- | :--- | :--- | :--- |
| **1. Documentos** | Objetos flexíveis **JSON / BSON** dentro de coleções | **MongoDB**, Firebase Firestore, CouchDB | Perfis de usuários, inventários com atributos variáveis de personagens em RPG, catálogos de loja. |
| **2. Chave-Valor (*Key-Value*)** | Dicionário ultrarrápido na memória RAM (`chave -> valor`) | **Redis**, Amazon DynamoDB | Saber em milissegundos *"Fulano está online jogando Valorant?"*, carrinhos temporários, cache. |
| **3. Colunar (*Wide-Column*)** | Colunas agrupadas por família otimizadas para escrita massiva | Apache **Cassandra**, HBase | Logs gigantes, sensores IoT gravando milhões de medições por segundo. |
| **4. Grafos (*Graph*)** | Nós (pessoas/coisas) ligados por setas/arestas (relacionamentos) | **Neo4j** | Redes sociais (*"amigos em comum"*), recomendações da Netflix, detecção de fraude. |

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q11 & DS 2019 Q7 — Sublinguagens SQL)
*Julgue: I. `CREATE`, `ALTER` e `DROP` são comandos DDL. II. `SELECT` pertence à DQL. III. `INSERT`, `UPDATE` e `DELETE` pertencem à TCL, pois desfazem transações.*
- **I:** VERDADEIRO (DDL = estrutura).
- **II:** VERDADEIRO (DQL = consulta).
- **III:** **FALSO!** `INSERT/UPDATE/DELETE` são **DML** (dados). Quem pertence à **TCL** são `COMMIT`, `ROLLBACK` e `SAVEPOINT`.

#### Questão Resolvida 2 (Baseada em DS 2025 Q14 & INFO 2025 Q28)
*Para descobrir quantos alunos têm nota `>= 7` na tabela `notas`, qual comando está correto?*
- `A) SELECT COUNT(*) FROM notas WHERE nota >= 7;` → **CORRETA!** Ordem exata `SELECT ... FROM ... WHERE ...` com `COUNT(*)` no `SELECT`.
- *B) SELECT * FROM notas WHERE COUNT(nota) >= 7;* → **ERRADA!** `COUNT` jamais vai no `WHERE`.


---

## Dia 7 — Modelagem de Dados (3 Níveis), DER Desenhado, Chaves, Cardinalidades e Normalização (1FN–3FN)

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Imagine uma escola que, por preguiça de criar várias tabelas organizadas, resolve guardar **tudo numa única tabelona gigante** chamada `MATRICULAS`. Em cada linha repetem: o nome do aluno, o CPF, **dois telefones espremidos juntos na mesma célula** (`"11999-1111, 11888-2222"`), o nome do curso e o telefone da coordenação do curso.

Olhe as **3 catástrofes** que acontecem nessa tabela mal projetada:
1. **Desperdício e erro ao atualizar:** Se 500 alunos fazem *Desenvolvimento de Sistemas* e a coordenação muda de telefone, você precisa editar 500 linhas (se esquecer 1 linha, metade dos alunos fica com o telefone antigo errado!).
2. **Não consegue cadastrar coisa nova (*Anomalia de Inserção*):** Se a escola abrir um curso novo que ainda não tem nenhum aluno matriculado, você **nem consegue registrar o curso na tabela**, porque a tabela obriga preencher o CPF de um aluno!
3. **Apagar sem querer outro assunto (*Anomalia de Exclusão*):** Se o único aluno de um curso trancar a matrícula e você apagar a linha dele, **apaga junto o cadastro inteiro do curso!**

Para construir bancos de dados limpos que nunca sofrem esses erros, fazemos a **Modelagem em 3 Níveis** e aplicamos a **Normalização (1FN, 2FN e 3FN)**!

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

No **Discord**, você pode mudar seu apelido toda semana, mas por trás existe um número de conta único que nunca muda e nunca repete (**Chave Primária**). Um servidor tem muitos canais, mas cada canal pertence a 1 servidor (**1 para Muitos**). E tentar guardar todos os itens da sua mochila numa única frase `"Espada, Escudo, Poção"` impede o jogo de contar quantas poções você tem — dividir em 1 linha por item coloca tudo na **Primeira Forma Normal (1FN)**!

---

### 📚 Parte 1 — As 3 Etapas da Modelagem (Do Desenho no Papel até o Código SQL!)

Quando projetamos um banco de dados escolar, evoluímos **o mesmo projeto** por **3 estágios**, indo do mais próximo ao cliente até o mais próximo da máquina:

```text
  1. MODELO CONCEITUAL (DER)        2. MODELO LÓGICO             3. MODELO FÍSICO (SQL)
  Desenho visual independente       Vira Tabelas, PK e FK!       Código exato do MySQL/Postgres:
  ┌───────┐   ◇    ┌──────────┐     ALUNO(id PK, nome)           CREATE TABLE aluno (
  │ ALUNO │──CURSA─│DISCIPLINA│  →  DISCIPLINA(id PK, titulo) →    id INT PRIMARY KEY,
  └───────┘        └──────────┘     MATRICULA(id_a FK, id_d FK)    nome VARCHAR(80) NOT NULL);
```

| Etapa | Nível de Abstração | Como Funciona e Ferramenta Usada | O que Não Pode Esquecer na Prova |
| :--- | :--- | :--- | :--- |
| **1. Modelo Conceitual** | Mais alto (linguagem do cliente/negócio) | Desenhado usando o **DER (Diagrama Entidade-Relacionamento — notação de Peter Chen)**: retângulos para Entidades, losangos para Relacionamentos e elipses para Atributos. | É **100% independente do programa/SGBD**! Não tem `VARCHAR` nem `INT` aqui! |
| **2. Modelo Lógico** | Intermediário (estrutura relacional) | Traduz o DER para o formato de **Tabelas**, define as **Chaves Primárias (`PK`)**, **Chaves Estrangeiras (`FK`)** e resolve ligações muitos-para-muitos criando tabelas intermediárias. | Ainda não depende do fabricante específico (MySQL vs Oracle). |
| **3. Modelo Físico** | Mais próximo da máquina (execução real) | São os comandos SQL **`CREATE TABLE`** escritos exatamente para o SGBD escolhido (MySQL, PostgreSQL etc.), definindo tipos (`VARCHAR(80)`), índices e limites. | **Depende diretamente do SGBD** escolhido! |

---

### 📚 Parte 2 — Vocabulário Formal Relacional & Os 4 Tipos de Atributos no DER

Na prova teórica, a Fundação FAT cobra os nomes acadêmicos oficiais criados por **Edgar Codd** (o criador do modelo relacional) *(DS 2025 Q12)*:

| Nome Formal na Prova | O que É na Prática | Exemplo Real |
| :--- | :--- | :--- |
| **Relação (*Relation*)** | A **Tabela** inteira | A grade `ALUNOS` *(Pegadinha: "Relação" NÃO é a linha, é a tabela!)* |
| **Tupla (*Tuple*)** | Uma **Linha / Registro** completo | `(1, 'Henrique', '2DS', '2010-05-14')` |
| **Atributo (*Attribute*)** | Uma **Coluna / Campo** | A coluna `nome` ou `cpf` |
| **Domínio (*Domain*)** | Os **valores válidos permitidos** numa coluna | Para `nota`, apenas números entre `0.0` e `10.0` |

#### Os 4 Tipos de Atributos no DER *(Apostas Q15)*

```text
   ○ Simples: ( cpf )              ◎ Multivalorado (Elipse Dupla!): ⦅ telefones ⦆
   ○ Composto: ( Endereço ) ─┬─ ( rua )     ◌ Derivado (Tracejado!): ┆ idade ┆
                             └─ ( cep )       (calculado via data_nasc!)
```
- **Atributo Simples (Atômico):** Não se quebra em partes menores com significado próprio (ex.: `cpf`, `nota`, `sexo`).
- **Atributo Composto:** Pode ser fatiado em sub-partes menores (ex.: `Endereco` se divide em `logradouro`, `numero`, `bairro`, `cep`).
- **Atributo Multivalorado *(Elipse dupla no DER)*:** Uma mesma pessoa pode ter **vários valores** daquela informação ao mesmo tempo (ex.: `telefones` ou `idiomas falados`). *Regra importante:* quando virar tabela no banco, isso terá que sair para outra tabela (1FN)!
- **Atributo Derivado *(Elipse pontilhada/tracejada no DER)*:** **Não precisa ser salvo no HD/SSD**, porque o sistema **calcula ele na hora** a partir de outros dados já salvos!
  - Exemplos clássicos de prova: **`idade`** (calculada usando `data_nascimento`), **`valor_total`** (calculado por `quantidade × preco_unitario`) e, nos games, seu *winrate* (`vitorias / partidas`).

---

### 📚 Parte 3 — Chaves (`PK`, Composta, Candidata, `FK`) e Cardinalidades

#### 1. Entendendo TODOS os Nomes de Chaves Sem Confusão *(DS 2019 Q9)*
- **Chave Primária (`PK` — *Primary Key*):** Coluna escolhida para **identificar de forma ÚNICA cada linha**. Regras absolutas: **jamais repete** e **jamais é vazia (`NULL`)**!
- **Chave Primária Simples vs. Chave Primária Composta *(Essencial para entender a 2FN logo abaixo!)*:**
  - **Simples:** Usa apenas **1 coluna** (ex.: `id_aluno` na tabela `ALUNOS`).
  - **Composta:** Às vezes **1 coluna sozinha se repete**, então precisamos **juntar 2 colunas** para formar a identidade única da linha! Exemplo: numa tabela `ITENS_DO_PEDIDO`, o `id_pedido = 101` se repete se o cliente comprou 3 coisas, e o `id_produto = 5` (Mouse) se repete em vários pedidos! Mas o par **`(id_pedido = 101 + id_produto = 5)`** nunca repete no mesmo carrinho! Isso é uma **Chave Primária Composta**.
- **Chave Candidata & Chave Alternativa *(DS 2019 Q9)*:** Na tabela `FUNCIONARIO(id_func, cpf, rg, email, nome)`, tanto `id_func`, quanto `cpf`, quanto `email` identificam uma pessoa sem repetir — todas essas colunas aptas são **Chaves Candidatas**. Escolhemos uma para ser a `PK` oficial (`id_func`). Todas as outras candidatas que ficaram na reserva (`cpf`, `email`) passam a se chamar **Chaves Alternativas (*Alternate Keys*)**!
- **Chave Estrangeira (`FK` — *Foreign Key*):** É a coluna de vínculo que guarda o valor da `PK` de outra tabela. Garante a **Integridade Referencial** (o banco proíbe gravar nota para um `id_aluno` inexistente).

#### 2. Cardinalidades e Como Elas Viram Tabelas Reais *(DS 2019 Q5)*
1. **`1:1` (Um para Um):** Cada funcionário usa no máximo 1 crachá exclusivo, e cada crachá pertence a 1 funcionário. A `FK` vai em um dos lados.
2. **`1:N` (Um para Muitos):** Uma `TURMA` tem **vários (`N`)** `ALUNOS`, mas cada `ALUNO` pertence a **1** `TURMA`.
   - **Regra sagrada:** **A Chave Estrangeira (`FK`) vai SEMPRE para a tabela do lado `N` (Muitos)**! Logo, `id_turma` mora dentro da tabela `ALUNO`.
3. **`N:N` (Muitos para Muitos):** Um `ALUNO` cursa **várias (`N`)** `DISCIPLINAS` e uma `DISCIPLINA` tem **vários (`N`)** `ALUNOS`.
   - **Como o banco relacional resolve `N:N`?** Não cabe uma FK só de cada lado! Por isso **criamos obrigatoriamente uma 3ª Tabela Associativa (Intermediária)** — ex.: `MATRICULA(id_matricula PK, id_aluno FK, id_disciplina FK, media)` — recebendo as duas FKs!
4. **Auto-Relacionamento (Relacionamento Unário / Recursivo — *DS 2019 Q5*):** Quando **uma tabela se relaciona com ela mesma**!
   ```text
     ┌────────────────────────────────┐
     │ FUNCIONARIO (id_func PK, ...,  │◄──┐
     │              id_supervisor FK) ├───┘ (A FK aponta para a PK da PRÓPRIA tabela!)
     └────────────────────────────────┘
   ```
   Por quê? Porque o supervisor também é um funcionário cadastrado ali dentro!

---

### 📚 Parte 4 — Normalização 100% Visual: Passo a Passo da 1FN, 2FN e 3FN!

**Normalizar** é aplicar **3 regras progressivas (Formas Normais)** para limpar tabelas bagunçadas, eliminando dados duplicados e anomalias. Antes de começar, traduza os 3 termos que a banca usa:
- **Atômico (1FN):** Significa **1 única informação indivisível por quadradinho/célula** (proibido juntar `"119999-1111, 118888-2222"` na mesma célula!).
- **Dependência Parcial (2FN):** Só acontece quando a tabela tem **Chave Composta (`Coluna A + Coluna B`)** e outra coluna depende **apenas de metade** dessa chave (só de A, ou só de B).
- **Dependência Transitiva (3FN):** Quando a `Coluna C` não depende da chave primária, mas depende de **outra coluna comum (`Coluna B`)** que está ali no meio!

Agora acompanhe com os olhos **exatamente a mesma tabela sendo consertada passo a passo**:

#### 🔴 Tabela Original Bagunçada (`PEDIDOS_BAGUNCADOS`)
| `id_pedido` | `id_produto` | `id_cliente` | `nome_cliente` | `telefones_cliente` *(Vários juntos!)* | `nome_produto` | `qtd` |
| :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| `101` | `10` | `5` | Lucas | **`119999-1111, 118888-2222`** | Teclado | `2` |
| `101` | `20` | `5` | Lucas | **`119999-1111, 118888-2222`** | Mouse | `1` |

---

#### 🔹 Passo 1: Primeira Forma Normal (1FN) — *Campeã de Prova! (DS 2025 Q13 & DS 2019 Q4)*
- **Problema encontrado:** A coluna `telefones_cliente` tem **dois telefones espremidos na mesma célula** (não é atômico / é atributo multivalorado!).
- **Regra da 1FN:** Toda célula deve conter **apenas 1 único valor atômico** — nada de listas com vírgula ou sub-tabelas presas dentro de uma célula!
- **Como consertamos:** Tiramos `telefones_cliente` dali e criamos uma tabela separada `TELEFONES_CLIENTE` ligada por `id_cliente`!

**Tabela `PEDIDOS_1FN` (Chave Composta: `id_pedido + id_produto`):**
| `id_pedido` *(PK)* | `id_produto` *(PK)* | `id_cliente` | `nome_cliente` | `nome_produto` | `qtd` |
| :---: | :---: | :---: | :--- | :--- | :---: |
| `101` | `10` | `5` | Lucas | Teclado | `2` |
| `101` | `20` | `5` | Lucas | Mouse | `1` |

**Nova Tabela `TELEFONES_CLIENTE`:**
| `id_tel` *(PK)* | `id_cliente` *(FK)* | `numero` |
| :---: | :---: | :--- |
| `1` | `5` | `119999-1111` |
| `2` | `5` | `118888-2222` |

*(Agora TODAS as células têm 1 só valor! A **1FN** foi atingida!)*

---

#### 🔹 Passo 2: Segunda Forma Normal (2FN) — *Eliminando Dependência Parcial*
- **Regra da 2FN:** Já estar na **1FN** **+** se a Chave Primária for **composta** (`id_pedido + id_produto`), todas as colunas comuns têm que depender das **DUAS partes da chave juntas**!
- **Problema em `PEDIDOS_1FN`:**
  - `qtd` (`2` Teclados no pedido `101`) depende dos **dois** juntos → OK!
  - Mas **`nome_produto`** (`"Teclado"`) depende **APENAS do `id_produto = 10`**! Não interessa qual foi o pedido!
  - E **`id_cliente`** / **`nome_cliente`** dependem **APENAS do `id_pedido = 101`**! Não interessa qual produto!
- **Como consertamos:** Quebramos cada assunto para depender da sua própria chave inteira:

**1) `PEDIDO`:** | `id_pedido` *(PK)* | `id_cliente` | `nome_cliente` | → `101 | 5 | Lucas`
**2) `PRODUTO`:** | `id_produto` *(PK)* | `nome_produto` | → `10 | Teclado` e `20 | Mouse`
**3) `ITEM_PEDIDO`:** | `id_pedido` *(PK,FK)* | `id_produto` *(PK,FK)* | `qtd` | → `101 | 10 | 2` e `101 | 20 | 1`

*(Acabaram as dependências parciais! A **2FN** foi atingida!)*

---

#### 🔹 Passo 3: Terceira Forma Normal (3FN) — *Eliminando Dependência Transitiva*
- **Regra da 3FN:** Já estar na **2FN** **+** nenhuma coluna comum pode depender de **outra coluna que NÃO é chave**! (Regra famosa: *"tudo depende da chave, apenas da chave e nada além da chave!"*)
- **Problema restante na tabela `PEDIDO`:** Olhe para `(id_pedido PK, id_cliente, nome_cliente)`:
  - `nome_cliente` (`"Lucas"`) não depende do pedido `101` — quem determina que o nome é Lucas é **`id_cliente` (`5`)**! Isso é **dependência transitiva** (`id_pedido` → `id_cliente` → `nome_cliente`). Se Lucas mudar o nome ou tiver 50 pedidos, ficaríamos repetindo `"Lucas"` 50 vezes!
- **Como consertamos:** Tiramos `nome_cliente` da tabela `PEDIDO` e criamos a tabela própria **`CLIENTE`**!

**Resultado Final 100% Normalizado (na 3FN):**
- **`CLIENTE`:** | `id_cliente` *(PK)* | `nome_cliente` | → `5 | Lucas`
- **`PEDIDO`:** | `id_pedido` *(PK)* | `id_cliente` *(FK)* | → `101 | 5`
- **`PRODUTO`:** | `id_produto` *(PK)* | `nome_produto` | → `10 | Teclado`, `20 | Mouse`
- **`ITEM_PEDIDO`:** | `id_pedido` *(PK,FK)* | `id_produto` *(PK,FK)* | `qtd` | → `101 | 10 | 2`, `101 | 20 | 1`

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q13 & DS 2019 Q4 — 1FN)
*Uma tabela `FORNECEDORES(cnpj, razao_social, telefones_contato)` armazena na coluna `telefones_contato` o texto `"(11) 3333-1111; (11) 99999-2222"`. Qual forma normal foi diretamente violada e como corrigir?*
- **Análise:** A célula armazena dois valores juntos (não atômico / multivalorado). Viola diretamente a **1ª Forma Normal (1FN)**. Correção: criar tabela separada `TELEFONES_FORNECEDOR` ligada por Chave Estrangeira (`cnpj`) com apenas 1 telefone por linha.

#### Questão Resolvida 2 (Baseada em DS 2019 Q5 & Apostas Q15 — Auto-relacionamento e Derivado)
*I. Em uma tabela `COLABORADOR`, o campo `id_lider` aponta para `id_colaborador` da própria tabela, configurando auto-relacionamento. II. O campo `valor_total` calculado por `quantidade * preco` na hora da consulta é um atributo derivado.*
- **Análise:** Ambos os itens são **VERDADEIROS**!


---

## Dia 8 — Design Digital: Cores (RGB/CMYK/Hex), Vetor vs. Bitmap, Gestalt, Tipografia e UX

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Você já abriu um aplicativo em que a letra cinza clara quase some no fundo branco, os botões ficam todos espremidos sem saber qual confirma a compra, ou o logo da empresa fica cheio de "quadradinhos borrados" quando você dá zoom no celular? Mesmo que toda a programação funcione bem, um design ruim faz o usuário desistir do site na hora — e pior: se você mandar uma arte feita para tela de celular direto para a gráfica imprimir um cartaz, as cores saem escuras e erradas porque **luz da tela** mistura diferente de **tinta no papel**!

A Fundação FAT dedica **4 a 5 questões inteiras por prova** a **Design Digital, Cores, Imagens, Gestalt, Tipografia e Usabilidade (UX)**!

---

### 📚 Parte 1 — Teoria das Cores: Luz (`RGB`/`Hex`) vs. Tinta (`CMYK`) e Círculo Cromático

#### 1. Por que Tela e Impressora Usam Sistemas Opostos?
- **No monitor, celular ou TV (`RGB` — Síntese Aditiva / LUZ):** A tela começa toda escura (preta) e acende mini-lâmpadas vermelhas, verdes e azuis. **Quanto MAIS luz somamos, MAIS CLARO fica!** Somando o máximo das três luzes nasce a luz **BRANCA**.
- **No papel impresso (`CMYK` — Síntese Subtrativa / TINTA):** O papel já começa **branco** (refletindo a luz do ambiente). **Quanto MAIS tinta jogamos em cima, MAIS luz é absorvida e MAIS ESCURO fica!**

| Sistema | Canais e Faixa de Valores | Onde Usar | Mistura Extrema / Detalhe de Prova |
| :--- | :--- | :--- | :--- |
| **RGB** | **R**ed (Vermelho), **G**reen (Verde), **B**lue (Azul)<br>Vai de **`0` a `255`** por canal (`16,7` milhões de cores!) | **Telas digitais** (sites, jogos, celular, TV, LEDs RGB) | `rgb(255, 255, 255)` = **BRANCO** (todas as luzes no talo)<br>`rgb(0, 0, 0)` = **PRETO** (tudo apagado) |
| **Hexadecimal** | **`#RRGGBB`** *(base 16: dígitos `0–9` e `A–F`)* | **Código HTML / CSS** e seletores de cor (como no Discord!) | É **exatamente o mesmo RGB**, só escrito de outro jeito! **`00`** equivale a **`0`** e **`FF`** equivale a **`255`**! |
| **CMYK** | **C**yan (Ciano), **M**agenta, **Y**ellow (Amarelo), blac**K** (Preto)<br>Vai de **`0%` a `100%`** | **Impressão gráfica em papel** (banners, cartões, apostilas, caixas) | O **K (Preto)** existe porque misturar C+M+Y na vida real gera um marrom sujo impuro além de desperdiçar muita tinta! |

#### Como Ler Qualquer Código Hexadecimal `#RRGGBB` em 3 Segundos!
Quebre os 6 caracteres em **3 pares**: **`#` | `RR` (Vermelho) | `GG` (Verde) | `BB` (Azul)**!
- `#FF0000` → Máximo vermelho (`FF`), zero verde, zero azul = **Vermelho puro**
- `#00FF00` → Zero vermelho, máximo verde (`FF`), zero azul = **Verde puro**
- `#0000FF` → Zero vermelho, zero verde, máximo azul (`FF`) = **Azul puro**
- `#FFFF00` → Máximo vermelho + máximo verde = na luz RGB dá **Amarelo!**
- `#FFFFFF` → Tudo no máximo (`255, 255, 255`) = **Branco!** | `#000000` = **Preto!**
- `#5865F2` *(Cor oficial do Discord!)* → Pouco vermelho, médio verde, quase máximo azul = Azul-arroxeado (*Blurple*)!
- `#808080` ou `#CCCCCC` → Quando os **3 pares são iguais**, você sempre tem um tom de **Cinza**!

#### 2. Círculo Cromático e Harmonias *(INFO 2025 Q9 & DS 2019 Q13)*
Imagine um relógio colorido redondo com 12 cores em volta:
- **Cores Primárias (Modelo tradicional de arte RYB):** **Vermelho, Amarelo e Azul**.
- **Cores Secundárias:** Mistura de duas primárias (**Laranja, Verde e Roxo/Violeta**). *(Primária + Secundária = **Terciária**, ex.: verde-azulado).*
- **Cores Análogas:** Ficam **coladas lado a lado** no círculo (ex.: Amarelo + Laranja + Vermelho) → visual suave e calmo.
- **Cores Complementares:** Ficam em **lados diretamente opostos (180°, frente a frente)** no círculo (ex.: **Azul × Laranja**; **Roxo × Amarelo**; **Vermelho × Verde**) → criam **contraste máximo**, ótimo para destacar botões importantes!
- **Harmonia em Tríade *(DS 2019 Q13)*:** **3 cores à mesma distância (120°)** formando um triângulo equilátero perfeito no círculo (ex.: Vermelho + Amarelo + Azul).

> [!CAUTION]
> **Pegadinha da DS 2025 Q15 (Molde 2 — Lista com Intruso):** A banca pede *"exclusivamente sistemas/padrões de representação de cores"* e coloca palavras intrusas como **"CSS"**, **"HTML"**, **"Primária"** ou **"Bitmap"** junto de `RGB`, `CMYK` e `Hexadecimal`! Só são sistemas de representação de cor: **`RGB`**, **`CMYK`**, **`Hexadecimal`** (e `HSL`/`HSB`).

---

### 📚 Parte 2 — Imagem Vetorial vs. Bitmap (Raster), Compressão e Bancos de Imagens

Você já chegou com a câmera bem colada numa parede ou numa foto ampliada e viu **quadradinhos borrados (serrilhado)**, enquanto os logos e ícones da tela ficam **100% lisos** mesmo em telas gigantes 4K?

```text
  BITMAP / RASTER (Grade fixa de pixels)       VETORIAL (Fórmula matemática!)
  Normal:  ▄█▄     Zoom 800%:  ████            Normal:  /\     Zoom 800%:    /\
           ███                 ████                    /__\                 /  \
          (liso)        ████   ████  ████             (liso)               /____\
                          (BORRA / PIXELA!)                             (100% LISO SEMPRE!)
```

#### Antes da tabela, entenda 2 termos rápidos que aparecem nela:
1. **Curvas de Bézier:** São fórmulas matemáticas com pontos de controle que permitem desenhar **curvas suaves e perfeitas** em qualquer tamanho sem usar pixels.
2. **Compressão Com Perda (*Lossy*) vs. Sem Perda (*Lossless*):**
   - **Com Perda (ex.: `.JPEG`):** Para o arquivo da foto ficar bem levinho, o algoritmo **joga fora pequenos detalhes** de cor que o olho humano quase não nota. Depois de salvo, aqueles dados descartados nunca mais voltam (se salvar em JPEG 20 vezes seguidas, a foto vai borrando!).
   - **Sem Perda (ex.: `.PNG`):** Diminui o peso sem apagar **nenhum único pixel original** (igual compactar num `.zip`) — qualidade perfeita garantida, porém o arquivo é maior!

| Critério | Imagem Vetorial | Imagem Bitmap (*Matricial / Raster*) |
| :--- | :--- | :--- |
| **Do que é feita?** | **Equações e fórmulas matemáticas** (linhas, pontos, polígonos e curvas de Bézier). | Uma **grade fixa (matriz) de pixels** (milhares de quadradinhos coloridos). |
| **Ao dar Zoom de 800%** | O PC **recalcula a matemática na hora**: fica **100% nítida, lisa e sem perder qualidade**! | Os pixels esticam e a imagem **pixela / serrilha / borra**! |
| **Melhor uso** | **Logotipos, ícones, letras/fontes, gráficos e ilustrações planas**. | **Fotografias reais** (rostos, paisagens com milhões de tons e sombras). |
| **Formatos na prova** | **`.SVG`** (web/HTML), **`.PDF`** (quando salva vetores), **`.AI`** (Illustrator), **`.CDR`** (CorelDraw), **`.EPS`** | **`.JPEG`/`.JPG`** (com perda; **NÃO tem fundo transparente**), **`.PNG`** (sem perda + **aceita fundo transparente!**), **`.BMP`**, **`.GIF`**, **`.WEBP`** |

- **O que é Rasterização? *(INFO 2025 Q10)*:** É o processo de **converter um desenho Vetorial em Bitmap (grade de pixels)** para exibir na tela ou imprimir (ex.: exportar um logo `.SVG` para `.PNG`).
- **PPI vs. DPI:** **PPI** (*Pixels Per Inch*) mede nitidez de **telas** (`72–96 PPI` antigo vs. telas Retina modernas); **DPI** (*Dots Per Inch*) mede gotinhas de tinta da **impressora** (**`300 DPI`** é o padrão profissional para imprimir sem borrar!).

#### Bancos de Imagens e Direitos Autorais *(DS 2025 Q16)*
Achar uma foto no Google Imagens **NÃO** significa que ela é gratuita nem livre para usar em sites comerciais!
- **Domínio Público / `CC0`:** Uso 100% livre para qualquer finalidade (inclusive comercial) sem precisar nem pagar nem pedir autorização.
- ***Creative Commons* (`CC`):** Licença gratuita onde o autor coloca regras com siglinhas: **`BY`** (obrigatório dar crédito citando o autor), **`NC`** (proibido uso comercial), **`ND`** (proibido editar/modificar a foto).
- ***Royalty-Free* ("Livre de Royalties"):** Você **paga uma única vez** (ou paga uma assinatura em bancos como Shutterstock/Adobe Stock) e pode usar aquela foto em vários projetos sem ter que pagar uma taxa nova a cada impressão ou visualização! *(Pegadinha de prova: *"Royalty-Free"* **NÃO significa "grátis"** — significa sem cobrança repetida por uso!)*

---

### 📚 Parte 3 — Princípios da Gestalt na Design & Interfaces *(DS 2025 Q17)*

A **Gestalt** é uma psicologia da percepção que estuda **como o cérebro humano agrupa e enxerga formas automaticamente**. Designers usam essas 5 leis para deixar telas óbvias sem precisar explicar nada:

| Lei da Gestalt | Desenho / Como o Cérebro Interpreta | Exemplo Real em Sites e Jogos |
| :--- | :--- | :--- |
| **1. Proximidade** | `[CPF:     ]` *(perto!)*<br><br>`[Senha:   ]` *(longe do CPF!)* | O rótulo `"CPF:"` fica colado na caixinha dele e distante do `"Senha:"` — sem nenhuma linha divisória, o cérebro agrupa o que está **perto**! *(Apostas Q21)* |
| **2. Semelhança** | `[ # geral ]  [ # avisos ]` vs. `[ 🔊 Call ]` | No Discord, todos os canais de texto têm **`#`** e os de voz têm **`🔊`**; num site, todos os botões de erro são vermelhos — formas/cores **iguais** significam funções iguais! |
| **3. Fechamento** | `┌─   ─┐` <br>`└─   ─┘` *(Você vê um retângulo!)* | Mesmo com traços faltando, o cérebro **preenche os buracos mentalmente** para completar a figura inteira (ex.: logo da **WWF** ou da **IBM** feito de listras!). |
| **4. Continuidade** | `●────●────●────●────▶` | O olhar desliza naturalmente seguindo um alinhamento reto ou curvo contínuo (barra de progresso, menu lateral alinhado, carrossel de cards). |
| **5. Figura e Fundo** | `[ JANELA EM FOCO ]` sobre fundo escuro | Separa o objeto principal (figura) do fundo (cenário). Um bom contraste (texto escuro no fundo claro) evita forçar a vista! |

---

### 📚 Parte 4 — Tipografia e Heurísticas de Usabilidade (UI vs. UX)

#### 1. Classificação das Fontes *(DS 2019 Q14 & INFO 2025 Q15)*
```text
   SERIFADA (tem "pezinho"!)     SEM SERIFA (reta e limpa)     MONOESPAÇADA (largura fixa)
       _A_                           A                             i i i  |  m m m
      /   \                         / \                            (mesma largura exata!)
     ─     ─  <-- Serifas!         /   \
```
- **Serifadas** (*Times New Roman, Georgia*): Os "pezinhos" (serifas) nas pontas ajudam a guiar a leitura em **textos longos impressos no papel** (livros e jornais).
- **Sem Serifa (*Sans-Serif*)** (*Arial, Roboto, Inter*): Linhas retas e limpas sem enfeite — padrão para **telas de celular, sites e menus** pela ótima leitura mesmo pequeno.
- ***Script* / Caligráficas *(DS 2019 Q14)*:** Imitam **letra cursiva / escrita à mão**. Lindas em convites de casamento, assinaturas ou títulos decorativos, mas **péssimas para textos longos** porque cansam rápido e dificultam a leitura!
- **Monoespaçadas** (*Consolas, Courier New, Fira Code*): Todas as letras ocupam exatamente a **mesma largura** horizontal (`i` ocupa o mesmo espaço que `m`) — perfeitas para **editores de código-fonte e terminais** para alinhar tabelas e códigos!
- **Google Fonts *(INFO 2025 Q15)*:** Biblioteca online gratuita de fontes web que você importa no `<head>` do HTML (e usa no CSS com `font-family`), garantindo que o site mostre exatamente aquela fonte em qualquer aparelho mesmo que ela não venha instalada no Windows do usuário!

#### 2. **UI** vs. **UX** & Heurísticas de Nielsen *(DS 2019 Q15)*
- **UI (*User Interface*):** A aparência visual — cores, botões, ícones, fontes.
- **UX (*User Experience*):** A **experiência completa** de facilidade e satisfação da pessoa usando o produto do início ao fim.

As **4 Heurísticas de Jakob Nielsen** mais cobradas:
1. **Equivalência entre o sistema e o mundo real *(DS 2019 Q15)*:** Falar a **língua humana normal do usuário** e usar símbolos conhecidos do dia a dia!
   - ❌ Tela ruim: `ERR_SOCKET_TIMEOUT_0x800F` | ✅ Tela boa: *"Sem conexão com a internet. Verifique o Wi-Fi."*
   - Ícone de **Lixeira** para apagar e **Carrinho de Supermercado** para compras seguem essa regra!
2. **Visibilidade do status do sistema:** Nunca deixar o usuário no escuro achando que travou — mostrar barra `%`, *"Enviando..."* ou *"Salvo com sucesso!"*.
3. **Prevenção de erros:** Mais vale impedir o acidente antes que ele aconteça (ex.: caixa *"Tem certeza que deseja excluir permanentemente?"* antes de deletar uma conta).
4. **Consistência e padrões:** Não inverter significados tradicionais (ex.: não fazer um botão verde enorme escrito *"Deletar Conta"* nem vermelho para *"Confirmar Compra"*!).

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q17 & Q18 — Vetor e Gestalt)
*Um designer criou um logotipo em SVG e aplicou tanto no ícone do app (48px) quanto num painel gigante de 4 metros sem serrilhar. Na tela de login, colou cada rótulo encostado na sua caixa de texto e colocou ícones vermelhos em todas as mensagens de erro. Identifique os conceitos:*
- Logo em **`.SVG`** que não serrilha no zoom = **Imagem Vetorial** (fórmulas matemáticas).
- Rótulo próximo do campo = Lei da **Proximidade** (Gestalt).
- Todos os erros com a mesma cor vermelha = Lei da **Semelhança** (Gestalt).

#### Questão Resolvida 2 (Baseada em DS 2019 Q15 & INFO 2025 Q9 — Cores e UX)
*I. Cores análogas ficam em lados diretamente opostos no círculo cromático buscando contraste máximo. II. Usar ícone de carrinho num site de compras exemplifica a heurística de "equivalência entre o sistema e o mundo real" de Nielsen.*
- **Item I é FALSO:** Opostas buscando máximo contraste são as **Complementares** (Análogas ficam **lado a lado**!).
- **Item II é VERDADEIRO.**


---

## Dia 9 — Desenvolvimento Web Front-end: HTML5, Listas/Tabelas/Formulários, CSS3 Box Model, DOM e Cookies

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Quando você digita `www.etec.sp.gov.br` ou abre sua loja favorita no Chrome/Edge, seu navegador recebe arquivos de texto simples enviados pela internet e os transforma na hora numa página colorida com botões, imagens e menus. Além disso, mesmo quando você fecha a aba e abre de novo no dia seguinte, o site ainda lembra que você está logado ou que havia 2 itens no carrinho!

Por trás de praticamente todo site da internet trabalham **3 tecnologias separadas** (a **Tríade da Web**), junto com pequenos arquivos de memória guardados no seu próprio navegador (**Cookies**).

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

Já apertou **`F12` (Inspecionar Elemento)** no Chrome para brincar de mudar o texto de uma página na sua tela? Isso funciona porque o navegador guarda um mapa vivo de todos os elementos da página na memória — e é assim também que um chat do **Discord Web** faz uma mensagem nova aparecer instantaneamente sem recarregar a página inteira! E se você apagar os dados de navegação do Chrome, sua conta do Discord desloga na mesma hora porque aqueles dados pequenos que guardam seu login (**Cookies**) moram **no seu próprio PC**, e **NUNCA "na nuvem"**!

---

### 📚 Parte 1 — A Tríade da Web & Anatomia Completa do HTML5 do Zero

| Tecnologia | O que Faz Exatamente | Analogia da Construção de uma Casa |
| :--- | :--- | :--- |
| **HTML5** (*HyperText Markup Language*) | **Estrutura e Significado (Semântica):** diz o que cada pedaço é (título, menu, parágrafo, botão, tabela). *(**Regra de ouro:** HTML **NÃO** é linguagem de programação — é linguagem de **marcação**!)* | **Paredes, colunas, portas e janelas** (o esqueleto da casa) |
| **CSS3** (*Cascading Style Sheets*) | **Aparência e Layout:** cores, fontes, tamanhos, margens, bordas, grade responsiva e animações. | **Pintura, piso, iluminação e decoração** |
| **JavaScript (JS)** | **Comportamento e Interatividade:** valida formulários, calcula totais, abre menus e altera a página ao vivo no clique. | **Parte elétrica, lâmpadas e portão automático** |

#### Primeiro: O que são **Tags** e **Atributos** no HTML?
HTML funciona usando etiquetas chamadas **Tags** escritas entre `<` e `>`. Quase toda tag **abre** `<p>` e **fecha** `</p>` abraçando o conteúdo; algumas poucas tags que não têm texto dentro fecham sozinhas (como `<meta>`, `<link>` e `<img>`).
Muitas tags também recebem **Atributos** na abertura (`nome="valor"`) para configurar detalhes extras:

```html
<a href="https://cps.sp.gov.br" target="_blank">Acessar Portal CPS</a>
 ↑  └───────── Atributo 1 ────┘ └ Atributo 2 ──┘  └── Texto visível ──┘
Tag 'a' (link)
```

#### 💻 Código Real Comentado: Página HTML5 Semântica Completa *(M-Tec Q38–40 & DS 2019 Q16)*
```html
<!DOCTYPE html>                    <!-- Avisa o navegador que o arquivo usa HTML5 moderno -->
<html lang="pt-BR">                <!-- Tag raiz: abraça toda a página -->
<head>                             <!-- Cabeçalho INVISÍVEL: título da aba, acentos e estilos CSS -->
    <meta charset="UTF-8">         <!-- Garante que ç, ã, é apareçam sem caracteres quebrados -->
    <title>Portal Etec DS</title>  <!-- Texto que aparece escrito lá em cima na aba do Chrome -->
    <link rel="stylesheet" href="estilos.css">  <!-- Liga este HTML ao arquivo de estilos CSS -->
</head>
<body>                             <!-- CORPO VISÍVEL: tudo o que aparece na tela mora AQUI! -->
    <header>                       <!-- Tag semântica: cabeçalho do site -->
        <h1>Desenvolvimento de Sistemas</h1>
        <nav>                      <!-- Tag semântica: barra de menu de navegação -->
            <a href="horarios.html">Mesma Aba (padrão _self)</a>
            <a href="https://cps.sp.gov.br" target="_blank" rel="noopener">Site CPS (Nova Aba)</a>
        </nav>
    </header>

    <main>                         <!-- Tag semântica: conteúdo principal da página -->
        <section>                  <!-- Seção temática dentro da página -->
            <article>              <!-- Conteúdo independente (card, notícia, post) -->
                <h2>Edital de Vagas Remanescentes</h2>
                <p>Prova em <span class="destaque">04 de dezembro</span>.</p>
            </article>
        </section>
        <div class="caixa-visual"> <!-- DIV: caixa GENÉRICA em bloco SEM valor semântico! -->
            Aviso em bloco genérico.
        </div>
    </main>

    <footer>                       <!-- Tag semântica: rodapé da página -->
        <p>© 2026 Etec M-Tec</p>
    </footer>
</body>
</html>
```

> [!WARNING]
> **Pegadinhas clássicas de HTML5 na Banca:**
> 1. **`<div>` e `<span>` NÃO são tags semânticas!** São apenas caixas genéricas (`<div>` ocupa uma linha inteira em bloco; `<span>` fica na mesma linha) usadas para layout visual *(M-Tec 2022 Q38)*. Tags **semânticas reais** dão significado para leitores de tela e Google: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` e `<footer>` *(DS 2019 Q16)*.
> 2. **Link em nova aba *(DS 2025 Q20)*:** Na tag `<a>`, `href` indica o endereço e **`target="_blank"` faz o link abrir em uma NOVA ABA (ou janela)**! O padrão sem colocar nada (ou `target="_self"`) abre na mesma aba.
> 3. **`<head>` vs. `<body>` *(M-Tec 2022 Q40)*:** Tudo que o usuário vê desenhado na página vai dentro de **`<body>`**, nunca dentro de `<head>`!

---

### 📚 Parte 2 — Listas, Tabelas HTML e Formulários (`GET` vs. `POST`)

#### 1. Listas (`<ol>` vs. `<ul>`) *(M-Tec 2022 Q39)*
- **`<ol>` (*Ordered List*):** Lista **ordenada/numerada** (`1., 2., 3.`) — para sequências em ordem.
- **`<ul>` (*Unordered List*):** Lista **não ordenada** (pontinhos `•`) — para menus e listas sem ordem numérica.
- Em ambas, cada item da lista vai dentro da tag **`<li>`** (*List Item*).

#### 2. Tabelas HTML (`<table>`, `<tr>`, `<th>`, `<td>`) *(Apostas Q24)*
```html
<table>
    <thead>
        <tr>                        <!-- TR = Table Row: cria UMA LINHA na horizontal! -->
            <th>Matéria</th>        <!-- TH = Table Header: célula de título da coluna -->
            <th>Nota</th>
        </tr>
    </thead>
    <tbody>
        <tr>                        <!-- Segunda linha da tabela -->
            <td>Banco de Dados</td> <!-- TD = Table Data: uma CÉLULA comum de dado -->
            <td>9.5</td>
        </tr>
    </tbody>
</table>
```
**Pegadinha fatal:** **`<tr>`** (*Table **Row***) cria uma **LINHA** inteira; **`<td>`** (*Table **Data***) cria uma **CÉLULA** com valor! Nunca inverta `<tr>` com `<td>`!

#### 3. Formulários e Requisições HTTP: `GET` vs. `POST` *(Apostas Q24)*
Quando você preenche um formulário (ex.: barra de busca ou tela de login) e clica em "Enviar", o navegador monta uma **Requisição HTTP** (um pacote de pedido enviado pela rede ao servidor) usando um de dois métodos:

| Critério | `method="GET"` | `method="POST"` |
| :--- | :--- | :--- |
| **Onde os dados viajam?** | Vão **visíveis no final da URL** após `?` (ex.: `youtube.com/results?search_query=minecraft`). | Vão **escondidos dentro do corpo (*body*)** da mensagem HTTP (invisíveis na barra de endereços!). |
| **Segurança e Limite** | Ficam expostos na tela, no histórico do navegador e têm limite de tamanho. | **Não aparecem na URL!** Suporta grandes textos e envio de arquivos/fotos. |
| **Quando usar** | Pesquisas, filtros de loja, links que você quer compartilhar. | **Login (usuário e senha!), cadastros, cartões e dados sensíveis!** |

---

### 📚 Parte 3 — CSS3: Seletores, Especificidade, Box Model e `transform`

#### 1. Como o CSS Escolhe Quem Vai Mudar: Seletores e Especificidade *(INFO 2025 Q14)*
No arquivo CSS, escrevemos regras no formato **`seletor { propriedade: valor; }`**:
```css
p { color: gray; }               /* Seletor de TAG: pinta TODOS os parágrafos <p> */
.destaque { color: blue; }       /* Seletor de CLASSE (.): atinge quem tem class="destaque" */
#aviso-unico { color: red; }     /* Seletor de ID (#): identificador ÚNICO para 1 elemento só! */
```
**O que é Especificidade?** Se o mesmo parágrafo tiver `<p id="aviso-unico" class="destaque">`, qual cor vence (cinza, azul ou vermelho)?
- Regra oficial de força: **`#id` (mais forte!) > `.classe` (médio) > `tag` (mais fraco)**! Portanto ele ficaria **vermelho**!

#### 2. CSS Box Model (*Modelo de Caixa* — *Apostas Q25*)
Para o CSS, **todo botão, texto ou imagem na tela é uma caixa retangular** com **4 camadas**, de dentro para fora:

```text
┌────────────── MARGIN (Espaço EXTERNO: empurra caixas vizinhas p/ longe) ──────┐
│ ┌──────────── BORDER (A linha da borda desenhada em volta da caixa) ────────┐ │
│ │ ┌────────── PADDING (Acolchoamento INTERNO entre o texto e a borda!) ───┐ │ │
│ │ │           CONTENT (O texto ou imagem em si: ex. "Comprar")            │ │ │
│ │ └───────────────────────────────────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Exemplo prático de prova:** Num botão azul com a palavra `"Entrar"`:
  - Aumentar **`padding: 16px;`** deixa o **fundo azul do botão maior por dentro**, afastando o texto da borda;
  - Aumentar **`margin: 20px;`** **NÃO** aumenta o botão azul — ele cria um espaço vazio invisível **do lado de fora**, empurrando os botões vizinhos para longe!

#### 3. Propriedade CSS3 `transform` *(DS 2019 Q17)*
Altera forma e posição visual sem desmontar o resto da página:
- **`scale(1.3)`** → **Aumenta ou diminui proporcionalmente** o tamanho (`1.3` = 130%).
- **`rotate(45deg)`** → **Gira** o elemento em graus (`45deg`).
- **`translate(20px, -10px)`** → **Desloca / Move** no eixo X (horizontal) e Y (vertical).
- **`skew(15deg, 5deg)`** → **Inclina / Distorce** os ângulos (deixa retângulos inclinados como paralelogramos).

---

### 📚 Parte 4 — A Árvore DOM no JavaScript e Cookies HTTP

#### 1. O que é o **DOM** (*Document Object Model*)? *(DS 2019 Q19)*
Quando o navegador termina de ler o texto do arquivo HTML, ele monta **na memória RAM um organograma vivo parecido com uma árvore genealógica**, chamado **Árvore DOM**! Veja como aquele nosso HTML do começo vira uma árvore de "pais e filhos":

```text
                    document (A página inteira)
                         │
              <html>  (document.documentElement — Raiz!)
             /      \
        <head>      <body>  (Pais dos elementos visíveis!)
         /           /   \
    <title>     <header>  <main>
                   │        │
                 <h1>      <p>
                            │
                   "Prova em 04/12" (Nó de Texto)
```

Como tudo está ligado nessa árvore viva, o JavaScript consegue ler, mudar texto, trocar cor ou criar botões novos sem recarregar a página:
- `document.documentElement` → Aponta para a raiz **`<html>`**!
- `document.getElementById("aviso")` → Busca o elemento com `id="aviso"`.
- `document.querySelector(".cartao")` → Busca usando qualquer seletor CSS (`.classe`, `#id`, `tag`).
- `document.createElement("li")` / `document.createTextNode("Item")` → Cria uma nova tag ou texto na memória.
- `pai.appendChild(filho)` → Encaixa o novo elemento dentro de um pai visível na tela.
- `elemento.parentNode` → Sobe um degrau na árvore pegando o **nó pai** daquele elemento!

#### 2. Cookies no Navegador: A Verdade Contra a Pegadinha! *(DS 2025 Q21)*
O protocolo da Web (**HTTP**) é ***stateless* ("sem memória")**: toda vez que você clica num novo link, o servidor esquece quem você era há 2 segundos! Para você não ter que digitar e-mail e senha a cada clique dentro de um site, o servidor pede ao seu navegador para guardar um **crachá de identificação** chamado **Cookie**.

**Os 6 fatos oficiais sobre Cookies (Campa de Prova!):**
1. **O que são?** Pequenos **arquivos de texto puro** com pares `nome=valor` (ex.: `sessao=abc987` ou `tema=escuro`).
2. **Onde ficam armazenados?** **EXCLUSIVAMENTE NO NAVEGADOR / COMPUTADOR LOCAL DO USUÁRIO (CLIENTE)**! Eles viajam nos cabeçalhos HTTP quando o navegador conversa com o site, **mas NUNCA ficam armazenados "na nuvem" como arquivos pesados**!
3. **Tamanho máximo tradicional:** Bem pequeno — cerca de **4 KB (~4.096 bytes)** por cookie! Não servem para guardar vídeos, músicas nem bancos grandes.
4. **Validade — os 2 tipos:**
   - **Cookie de Sessão (*Session Cookie*):** Não tem prazo de validade (`Expires`/`Max-Age`). **É apagado automaticamente assim que você fecha o navegador!**
   - **Cookie Persistente / Permanente:** Tem data/prazo de validade gravado (ex.: 30 dias). Continua salvo no disco do seu navegador mesmo se você desligar e ligar o computador!
5. **Acesso e Segurança:** O JavaScript da página lê/cria cookies via `document.cookie` — **exceto** quando o servidor marca a trava de segurança **`HttpOnly`**. *(Por que isso importa? Para proteger contra ataques **XSS** — quando um invasor consegue injetar um código JavaScript malicioso numa página tentando roubar seu cookie de login! Com `HttpOnly`, nenhum script JS consegue enxergar o cookie!)*
6. **Diferença para *Web Storage* (`localStorage` / `sessionStorage`):** Enquanto Cookies são minúsculos (`~4 KB`) e viajam juntos em toda requisição HTTP para o servidor, **`localStorage`** guarda cerca de **5–10 MB** apenas localmente no navegador sem ficar trafegando toda hora pela rede.

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q21 — Cookies)
*Julgue: I. Cookies são grandes arquivos multimídia armazenados diretamente nos servidores em nuvem da hospedagem. II. Cookies possuem tamanho pequeno (~4 KB) e ficam armazenados localmente no navegador do usuário. III. Cookies podem ser temporários (de sessão) ou permanentes (com validade).*
- **Item I é FALSO:** Cookies são arquivos de **texto pequenos (~4 KB)** armazenados **no navegador local do cliente**, jamais na nuvem!
- **Itens II e III são VERDADEIROS.**

#### Questão Resolvida 2 (Baseada em M-Tec Q38–39 & Apostas Q24–25)
*I. A tag `<tr>` representa uma célula de dado na tabela HTML e `<td>` cria uma linha. II. Formulários com senha devem usar `method="POST"` em vez de `GET` para não expor os campos na URL. III. No CSS Box Model, `padding` é o espaço interno entre o conteúdo e a borda.*
- **Item I é FALSO:** O contrário (`<tr>` = linha / *table row*; `<td>` = célula / *table data*).
- **Itens II e III são VERDADEIROS.**


---

## Dia 10 — Sistemas Numéricos (Binário/Hex), Hardware, Memórias, SO, VMs/Docker e Linux

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Dentro do processador do seu celular ou PC não existem letras `'A'`, números `255` nem cores `#FF0000` flutuando soltos. Toda imagem, áudio do Discord e comando em Python precisa ser traduzido para sequências elétricas binárias (**`0`** = sem energia / **`1`** = com energia). Como escrever sequências gigantes de zeros e uns cansa a vista humana, engenheiros compactam grupos binários usando o sistema **Hexadecimal**.

Ao mesmo tempo, entender **o que está dentro do computador** (Processador, RAM, SSD vs. HD), como o **Sistema Operacional** evita que programas travem tudo e qual a diferença entre **Máquinas Virtuais**, **Contêineres Docker** e pastas do **Linux** garante várias questões diretas da prova!

---

### 🎮 Para Entender Sem Medo (Antes de Qualquer Sigla!)

- Por que abrir GTA V ou Valorant instalado num **SSD** carrega o mapa em segundos, enquanto num **HD antigo** demora e trava? Porque o HD antigo é um disco girando com uma agulha física mecânica procurando o arquivo, enquanto o SSD é puramente eletrônico em chips de memória rápida!
- Por que um jogo pesado começa a engasgar (*stuttering*) quando você abre 20 abas do Chrome ao mesmo tempo num PC com pouca RAM? Quando a RAM lota, o Windows salva o excesso temporariamente no SSD/HD (que é muito mais lento que a RAM) para não fechar o jogo à força — fazendo o FPS cair na hora!

---

### 📚 Parte 1 — Bits, Bytes e Conversões Passo a Passo: Decimal ↔ Binário ↔ Hexadecimal

#### 1. Vocabulário de Capacidade Digital
- **1 Bit (*Binary Digit*):** Menor unidade possível — vale **`0` ou `1`**.
- **1 Byte = `8 bits` juntados:** Com 8 posições ligando/desligando existem `2⁸ = 256` combinações possíveis. Contando a partir do zero, **1 Byte representa exatamente de `0` (`00000000`) até `255` (`11111111`)**!
  - *(Curiosidade real: é exatamente por isso que cores RGB `rgb(255, 255, 255)` e máscaras de roteador `255.255.255.0` param no **`255`** — é 1 Byte cheio!)*
- **Múltiplos comuns:** `1 KB ≈ 1.024 bytes` → `1 MB ≈ 1.024 KB` → `1 GB ≈ 1.024 MB` → `1 TB ≈ 1.024 GB`.

#### 2. Como Converter Decimal (Base 10) ↔ Binário (Base 2) — 2 Métodos Infalíveis!

**Método 1 — A Régua das 8 Potências de 2 (Mais rápido para números até 255!):**
Escreva as potências dobrando da direita para a esquerda:
`128  |  64  |  32  |  16  |  8  |  4  |  2  |  1`

Vamos converter **`100₁₀`** *(caiu igual na DS 2019 Q20!)*: percorra da esquerda para a direita perguntando *"esse valor cabe no que falta?"*. Se couber, coloca **`1`** e subtrai; se não couber, coloca **`0`**:
- `128` cabe em `100`? Não → **`0`**
- `64` cabe em `100`? **Sim** → **`1`** *(sobra `100 - 64 = 36`)*
- `32` cabe em `36`? **Sim** → **`1`** *(sobra `36 - 32 = 4`)*
- `16` cabe em `4`? Não → **`0`**
- `8` cabe em `4`? Não → **`0`**
- `4` cabe em `4`? **Sim** → **`1`** *(sobra `4 - 4 = 0`)*
- `2` → **`0`** | `1` → **`0`**
Resultado em 8 bits: **`01100100₂`** *(ou `1100100₂` sem o zero à esquerda)*. Conferindo: `64 + 32 + 4 = 100`!

**Método 2 — Divisões Sucessivas por `2` (`DIV 2` e `MOD 2`):**
Divida o número sempre por `2` até o quociente zerar, e no final leia todos os restos **DE BAIXO PARA CIMA**:
Para **`250₁₀`** *(DS 2019 Q20)*:
- `250 ÷ 2 = 125`, resto **`0`**  ↑
- `125 ÷ 2 = 62`, resto **`1`**   |
- `62 ÷ 2 = 31`, resto **`0`**    |  *(Leia os restos*
- `31 ÷ 2 = 15`, resto **`1`**    |   *de baixo para cima!)*
- `15 ÷ 2 = 7`, resto **`1`**     |
- `7 ÷ 2 = 3`, resto **`1`**      |
- `3 ÷ 2 = 1`, resto **`1`**      |
- `1 ÷ 2 = 0`, resto **`1`**      |
Resultado lido de baixo para cima: **`11111010₂`** (`128+64+32+16+8+2 = 250`)!

#### 3. Como Converter Decimal / Binário ↔ Hexadecimal (Base 16)
Na Base 16 existem 16 símbolos: os dígitos **`0` a `9`** e, para valores de `10` a `15` sem precisar de dois dígitos, usamos **letras**:
**`A = 10`** | **`B = 11`** | **`C = 12`** | **`D = 13`** | **`E = 14`** | **`F = 15`**.

Você tem **2 jeitos rápidos** de achar o Hexadecimal na prova:
- **Jeito A (Divisão por 16):** Divida o número decimal por `16`; troque quociente e resto ≥ 10 pelas letras `A–F`!
  - **`100₁₀`:** `100 ÷ 16 =` quociente **`6`** (`6 × 16 = 96`), resto **`4`** → **`64₁₆`**!
  - **`250₁₀`:** `250 ÷ 16 =` quociente **`15`** (`15 × 16 = 240`), resto **`10`**. Como `15 = F` e `10 = A` → **`FA₁₆`**!
- **Jeito B (Truque dos Blocos de 4 Bits — Máxima Velocidade!):** Cada grupo de **4 bits binários** (usando a mini-régua **`8 | 4 | 2 | 1`**) vale exatamente **1 dígito Hexadecimal**!
  - Pegue `250₁₀` = `1111 1010₂`:
    - Esquerda `1111` = `8 + 4 + 2 + 1 = 15` = **`F`**
    - Direita `1010` = `8 + 0 + 2 + 0 = 10` = **`A`** → **`FA₁₆`** em 3 segundos!
  - Pegue **`255₁₀`** *(INFO 2025 Q4)* = `1111 1111₂` → `15` (`F`) e `15` (`F`) = **`FF₁₆`**!

---

### 📚 Parte 2 — Arquitetura de Hardware do Zero e Hierarquia de Memórias

#### 1. O Desenho do Computador Clássico (Arquitetura de **Von Neumann**)
Quase todo computador moderno segue o modelo projetado por John von Neumann, onde peças conversam enviando dados por trilhas elétricas na placa-mãe chamadas **Barramentos** (*Buses*):

```text
   ┌──────────┐       ┌──────────────── CPU (Processador) ─────────────────┐       ┌───────────┐
   │ ENTRADA  │ ────→ │  [ UC ] Unidade de Controle (O "Maestro")          │ ────→ │   SAÍDA   │
   │ Teclado, │       │  [ ULA ] Unidade Lógica/Aritmética (Calculadora)   │       │  Monitor, │
   │ Mouse    │       │  [ Registradores ] (Mini-memórias ultrarrápidas)   │       │  Som      │
   └──────────┘       └────────────────────────┬───────────────────────────┘       └───────────┘
                                               ↕  (Barramentos de dados/endereço)
                                     ┌───────────────────┐
                                     │ Memória Principal │ ◄──→ [ Armazenamento: SSD / HDD ]
                                     │       (RAM)       │
                                     └───────────────────┘
```
- **CPU (Processador):** É o cérebro. Lá dentro: a **UC** (*Unidade de Controle*) coordena quem faz o quê; a **ULA** (*Unidade Lógica e Aritmética*) executa todas as contas (`+`, `-`, `>`, `E/OU`); e os **Registradores** são gavetinhas minúsculas ultrarrápidas segurando os números exatos da conta atual.

#### 2. Vocabulário Antes da Tabela de Memórias
- **Memória Volátil:** **Apaga tudo instantaneamente** quando acaba a energia elétrica (RAM, Cache, Registradores).
- **Memória Não Volátil:** **Guarda seus dados mesmo fora da tomada** (SSD, HD, Pendrive, ROM).
- **`SRAM` (Estática) vs. `DRAM` (Dinâmica):** `SRAM` é super veloz e cara (usada no **Cache** dentro do chip da CPU); `DRAM` é um pouco mais barata e permite ter muitos GB (usada nos pentes de **RAM**).
- **`BIOS / UEFI` + `POST` + *Boot*:** Quando você aperta o botão Power do PC, a CPU ainda não sabe onde está o Windows no SSD. Ela lê primeiro um pequeno chip gravado de fábrica chamado **ROM** contendo o programa **BIOS/UEFI**, que roda um autoteste rápido nas peças chamado **POST** (*Power-On Self-Test*) e depois dá o ***Boot*** (carrega o Windows/Linux do SSD para a RAM!).

#### 3. Hierarquia das Memórias *(Quanto mais perto da CPU: MAIS RÁPIDA, MENOR capacidade, MAIS CARA por GB)*

| Memória | Volátil? | Tecnologia / Papel Exato | O que Cai na Prova da FAT |
| :--- | :---: | :--- | :--- |
| **Registradores & Cache (L1/L2/L3)** | **Sim (Volátil)** | `SRAM` embutida dentro do próprio chip do processador. | Velocidade máxima; guarda dados repetidos para a CPU não ficar esperando a RAM. |
| **Memória RAM** *(Principal)* | **Sim (Volátil)** | `DRAM` (pentes DDR4, DDR5). | Carrega o Windows/Linux e todos os **programas em execução agora**. Desligou o PC, apaga tudo! |
| **Memória ROM** *(BIOS / UEFI)* | **Não (Não volátil)** | Chip de fábrica com firmware de inicialização. | Executa o **POST** ao ligar e inicializa (*boot*) o Sistema Operacional. |
| **SSD** *(Solid State Drive)* | **Não (Não volátil)** | Armazenamento secundário usando **chips de memória Flash NAND**. | **SEM partes móveis mecânicas!** Muito mais rápido, silencioso e resistente a quedas/vibrações do que o HDD. *(DS 2019 Q21)* |
| **HDD** *(Hard Disk Drive)* | **Não (Não volátil)** | Discos magnéticos giratórios + braço mecânico com agulha de leitura. | Bom para guardar terabytes baratos (backups/arquivos), mas lento e frágil a pancadas físicas. |

---

### 📚 Parte 3 — Sistema Operacional (SO), Memória Virtual (`Swap`) e VM vs. Contêiner Docker

Um **Sistema Operacional (SO)** — como Windows, Linux, macOS ou Android — atua como o **intermediário (gerente)** entre o hardware físico (CPU/RAM/SSD) e o usuário/programas (*M-Tec 2022 Q35*). Sua peça mais central, que conversa diretamente com o hardware, chama-se **Kernel (Núcleo)**.

#### 1. Como o SO Gerencia a Memória RAM *(DS 2025 Q27)*
1. **Proteção e Isolamento:** Garante que o Chrome travado não consiga invadir nem apagar o espaço de RAM usado pelo seu jogo ou pelo Kernel.
2. **Alocação e Desalocação:** Entrega pedaços de RAM quando você abre um aplicativo e recolhe de volta quando você fecha.
3. **Memória Virtual (*Paginação / Swap*):** Se a RAM física de 8 GB encher, o SO pega blocos ("páginas") menos usados no momento e move temporariamente para uma área reservada no **SSD/HD** (*arquivo de paginação* no Windows / *partição swap* no Linux). Isso impede os apps de fecharem sozinhos por falta de memória, **porém deixa o computador bem mais lento** porque ler do SSD/HD é muito mais lento que ler da RAM!

#### 2. Máquina Virtual (VM) vs. Contêiner (Docker) *(INFO 2025 Q5 e Q16)*
*(Antes: o que é um **Hypervisor**? É um programa especial — como VirtualBox ou VMware — que simula um computador inteiro virtualizado "de mentira" dentro do seu PC para rodar outros Sistemas Operacionais!)*

Olhe no esquema visual **por que Contêineres Docker são gigantes na nuvem hoje em dia**:

```text
  MÁQUINAS VIRTUAIS (VM — VirtualBox/VMware)       CONTÊINERES (Docker)
  ┌──────────────┐   ┌──────────────┐              ┌───────┐  ┌───────┐  ┌───────┐
  │    App A     │   │    App B     │              │ App A │  │ App B │  │ App C │
  ├──────────────┤   ├──────────────┤              ├───────┴──┴───────┴──┴───────┤
  │ Linux/Win    │   │ Linux/Win    │ ← SO inteiro │         Docker Engine         │
  │ (Guest OS)   │   │ (Guest OS)   │   duplicado! ├───────────────────────────────┤
  ├──────────────┴───┴──────────────┤              │  SO & Kernel ÚNICO do PC Host │
  │     Hypervisor (Emula HW!)      │              └───────────────────────────────┘
  ├─────────────────────────────────┤              (NÃO instala outro SO por dentro!
  │      Hardware / SO Host         │               COMPARTILHA o mesmo Kernel!)
  └─────────────────────────────────┘
```

| Critério | Máquina Virtual (VM) | Contêiner (Docker / Podman) |
| :--- | :--- | :--- |
| **Como funciona** | Um **Hypervisor** emula hardware completo e instala **um Sistema Operacional inteiro (*Guest OS* + Kernel próprio)** para cada VM. | Isola apenas o aplicativo e suas bibliotecas em caixinhas leves, **COMPARTILHANDO o mesmo Kernel** do sistema hospedeiro! |
| **Peso e Velocidade** | **Pesada** (vários GB de RAM/disco; demora minutos dando *boot* completo). | **Ultraleve** (megabytes; inicia em **fração de segundo** pois não liga outro SO!). |
| **Para que brilha** | Rodar um Windows completo isolado dentro de um Linux/Mac. | Empacotar sites/servidores + dependências com garantia de rodar igualzinho no PC do programador e no servidor (*INFO 2025 Q16*). |

---

### 📚 Parte 4 — Sistema de Arquivos Linux (FHS), Comandos, Permissões e Windows/Office

#### 1. A Árvore de Diretórios Oficiais do Linux (*FHS*) *(INFO 2025 Q18)*
No Windows existem unidades separadas por letra (`C:\`, `D:\`). No **Linux não existe `C:\`!** Tudo nasce numa única árvore começando na pasta principal chamada **raiz `/`**. Memorize o mapa visual dos diretórios que caem na prova:

```text
  /  (Raiz absoluta do sistema — NÃO confunda com /root!)
  ├── /bin    → Comandos EXECUTÁVEIS binários básicos do sistema (ls, cp, cat)
  ├── /etc    → Arquivos de CONFIGURAÇÃO do sistema, usuários e servidores
  ├── /home   → Pastas pessoais dos USUÁRIOS comuns (ex.: /home/henrique)
  ├── /root   → Pasta pessoal EXCLUSIVA do administrador máximo (superusuário 'root')!
  ├── /lib    → Bibliotecas compartilhadas necessárias para os programas rodarem
  ├── /usr    → Programas e utilitários instalados para os usuários
  ├── /var    → Arquivos VARIÁVEIS que crescem com o uso (especialmente LOGS em /var/log)
  └── /tmp    → Arquivos TEMPORÁRIOS (geralmente apagados ao reiniciar o PC)
```

> [!CAUTION]
> **Pegadinha clássica da INFO 2025 Q18 (Molde 2 — Lista com Intruso):** A banca pergunta qual alternativa contém **APENAS diretórios padrão Linux** e coloca no meio palavras como **`/mkdir`**, **`/ls`**, **`/rm`**, **`/cd`**, **`/cat`** ou **`/apt`**!
> **`mkdir`, `ls`, `rm`, `cd`, `cat` são COMANDOS digitados no terminal — NUNCA são nomes de pastas oficiais do sistema!**

#### 2. Comandos Essenciais de Terminal Linux *(DS 2019 Q22)*
| Comando | Sigla / Significado | O que Faz na Prática | Exemplo Real |
| :--- | :--- | :--- | :--- |
| **`pwd`** | *Print Working Directory* | Mostra o caminho da pasta onde você está agora | `pwd` → `/home/henrique` |
| **`ls`** | *List* | Lista arquivos e pastas dentro do local (`ls -la` mostra ocultos) | `ls -l` |
| **`cd`** | *Change Directory* | Entra em outra pasta (`cd ..` sobe uma pasta atrás) | `cd /etc` |
| **`mkdir`** | *Make Directory* | Cria uma nova pasta vazia | `mkdir projeto` |
| **`cp` / `mv`** | *Copy / Move* | **`cp`** copia arquivo/pasta (`cp -r`); **`mv`** **move OU renomeia**! | `mv velho.txt novo.txt` |
| **`rm`** | *Remove* | Apaga arquivos (`rm -rf` apaga pastas recursivamente — cuidado!) | `rm temp.txt` |
| **`chmod`** | *Change Mode* | Muda **permissões** usando soma de bits: **Ler (`r=4`)**, **Gravar (`w=2`)**, **Executar (`x=1`)**. Logo `7 = 4+2+1` (tudo liberado pro dono) e `5 = 4+1` (ler+executar pros outros)! | `chmod 755 script.sh` |

#### 3. Produtividade Windows & Word *(INFO 2025 Q6 & Apostas Q30)*
- No **Microsoft Word**, os botões de **Listas com Marcadores (`•`) e Numeração (`1, 2, 3`)** ficam na guia **Página Inicial**; já o recurso que gera centenas de cartas/certificados personalizados pegando nomes de uma planilha Excel chama-se **Mala Direta**!
- No **Windows**, **`Ctrl+Shift+Esc`** abre direto o Gerenciador de Tarefas para encerrar aplicativos travados; `Ctrl+C` (copiar), `Ctrl+X` (recortar), `Ctrl+V` (colar), `Ctrl+Z` (desfazer).

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q20 & INFO 2025 Q4 — Conversões)
*Converta os valores decimais `255`, `100` e `250` para binário (8 bits) e hexadecimal.*
- `255` = `128+64+32+16+8+4+2+1` = **`11111111₂`** = **`FF₁₆`**.
- `100` = `64+32+4` = **`01100100₂`**; `100 ÷ 16` = `6` resto `4` = **`64₁₆`**.
- `250` = `128+64+32+16+8+2` = **`11111010₂`**; `250 ÷ 16` = `15 (F)` resto `10 (A)` = **`FA₁₆`**.

#### Questão Resolvida 2 (Baseada em INFO 2025 Q16 & Q18 — Docker e Linux)
*Julgue: I. Contêineres Docker são iguais a Máquinas Virtuais porque cada contêiner emula um hardware completo e instala um novo Kernel por dentro. II. No Linux, `/etc` guarda configurações e `/var` guarda logs variáveis.*
- **Item I é FALSO:** Contêineres **compartilham o mesmo Kernel** do sistema hospedeiro (por isso são tão leves e rápidos!).
- **Item II é VERDADEIRO.**


---

## Dia 11 — Redes de Computadores (TCP/IP, E-mail, Topologias), Cloud, IoT, Inglês Técnico e Ética

### 🎯 Por que Você Precisa Dominar Isso? (Começando do Mundo Real)

Quando você envia um "oi" no WhatsApp ou acessa um site seguro com cadeado (`https://`), a mensagem não atravessa a internet inteira de uma vez em bloco gigante. Ela é quebrada em pequenos pedaços endereçados, viaja por cabos de fibra óptica ou ondas Wi-Fi passando por vários aparelhos intermediários até servidores na Nuvem (*Cloud*), e chega certinha na tela do amigo! Além disso, esse módulo completa **Inglês Técnico e Ética/LGPD** — juntos, esses temas valem facilmente **10 a 12 pontos de uma prova de 30 questões**!

---

### 📚 Parte 1 — O Básico de Redes do Zero e a Pilha TCP/IP *(DS 2025 Q25 & INFO 2025 Q25)*

#### 1. Primeiro: 6 Termos Essenciais Antes dos Protocolos
- **Protocolo:** É um **"idioma e conjunto de regras combinadas"** entre máquinas diferentes (um iPhone e um servidor Linux) para saberem como começar, empacotar, checar erros e encerrar uma conversa pela rede.
- **Pacote de Dados:** Em vez de mandar uma foto de 10 MB de uma só vez (que entupiria a rede para todo mundo), a rede **fatia os dados em centenas de pequenos pacotes** numerados e depois remonta tudo no destino.
- **Endereço MAC (*Media Access Control*):** É o **"número de chassi único" gravado de fábrica** na placa de rede/Wi-Fi do seu aparelho (ex.: `A4:83:E7:12:0B:FF`). Serve para identificar o aparelho **aqui dentro da rede local** (sua casa ou sala de aula).
- **Endereço IP (*Internet Protocol*):** É o **"CEP / endereço postal lógico"** que seu computador ganha na rede (ex.: `192.168.0.15` no IPv4 de 32 bits, ou endereços gigantes como `2001:db8::1` no IPv6 de 128 bits). Ele pode mudar quando você muda de Wi-Fi!
- **Switch vs. Roteador:**
  - **Switch:** Liga vários PCs próximos na **mesma rede local** (ex.: os 30 PCs do laboratório da Etec), entregando cada quadro pelo endereço **MAC** certinho para o PC dono sem mandar para todo mundo!
  - **Roteador:** Conecta **redes diferentes** (sua casa ↔ Internet) e escolhe a **melhor rota** até o destino usando o endereço **IP**!
- **Sinal `ACK`, `ICMP (ping)` e `VoIP`:**
  - **`ACK` (*Acknowledgement*):** Recibo de confirmação (*"Chegou o pacote nº 4 perfeitamente, pode mandar o 5!"*).
  - **`ICMP` (`ping`):** Protocolo de diagnóstico — quando você mede seu *ping* em milissegundos no jogo, está testando com `ICMP` quanto tempo leva para ir e voltar do servidor!
  - **`VoIP` (*Voice over IP*):** Tecnologia de transmitir voz pela internet (como chamadas de voz no **Discord** e WhatsApp!).

#### 2. A Arquitetura TCP/IP em **4 Camadas** *(Padrão Cobrado pela FAT)*
*(Nota rápida: alguns livros acadêmicos dividem redes em **7 camadas no Modelo OSI** — Física, Enlace, Rede, Transporte, Sessão, Apresentação, Aplicação — mas a internet real e as questões práticas da Fundação FAT usam a **pilha TCP/IP de 4 camadas**!)*

| Camada TCP/IP | Papel na Viagem dos Dados | Protocolos e Aparelhos dessa Camada |
| :--- | :--- | :--- |
| **4. Aplicação** | Onde moram os programas que o usuário usa (navegador, e-mail, arquivos). | **HTTP, HTTPS, FTP, SFTP, SMTP, POP3, IMAP, DNS, DHCP, SSH, RDP** |
| **3. Transporte** | Pega a conversa ponta a ponta: escolhe entrega **confiável** ou **ultrarrápida**! | **TCP** *(confiável: exige confirmação **`ACK`** e reenvia pacote perdido! Ex.: baixar jogo na Steam, sites, bancos)* vs. **UDP** *(ultrarrápido sem confirmação: não para esperando pacote velho! Ex.: **call no Discord**, tiro no CS2/Valorant, live ao vivo)* |
| **2. Internet (Rede)** | Coloca o endereço **IP** de origem/destino e escolhe as rotas pelo planeta. | **IP (IPv4 32 bits / IPv6 128 bits)**, **ICMP (`ping`)**, **Roteadores** |
| **1. Acesso à Rede** *(Enlace + Física)* | Coloca o endereço físico **MAC** local e transforma `0 e 1` em pulsos no cabo, fibra ou Wi-Fi. | **Ethernet** (cabos UTP de rede/fibra), **Wi-Fi**, Placa de Rede, **Switch** |

#### Protocolos que Mais Caem na Prova:
- **HTTP vs. HTTPS *(INFO 2025 Q27)*:** **HTTP** manda páginas da web em texto aberto pela rede (qualquer espião no Wi-Fi público conseguiria ler suas senhas!). **HTTPS** coloca o HTTP dentro de um túnel criptografado usando **SSL/TLS** (o **cadeado** no navegador), garantindo **sigilo (confidencialidade) e autenticidade**!
- **DNS (*Domain Name System*):** A "agenda telefônica" da internet — traduz nomes fáceis que humanos lembram (`discord.com`) nos números de **IP** reais que o roteador precisa (`162.159...`). *(Trocar DNS para `1.1.1.1` ou `8.8.8.8` agiliza essa tradução!)*
- **DHCP:** Entrega endereços **IP automaticamente** para todo celular ou notebook que entra no Wi-Fi (senão você teria que digitar IP na mão toda vez!).
- **FTP / SFTP:** Protocolos específicos para **enviar e baixar arquivos** de servidores (`SFTP` faz isso criptografado).
- **SSH vs. RDP *(INFO 2025 Q17)*:** Acesso remoto à distância! **SSH** abre um **terminal de comandos criptografado** (padrão em servidores Linux); **RDP (*Remote Desktop Protocol*)** da Microsoft transmite a **tela gráfica inteira** (área de trabalho com janelas e mouse) de um Windows remoto!

---

### 📚 Parte 2 — Protocolos de E-mail: SMTP, POP3, IMAP e Webmail *(DS 2025 Q28 & INFO 2025 Q7/Q26)*

Esse tema cai **praticamente em toda prova**! Olhe no desenho exatamente o caminho do e-mail e o que cada protocolo faz:

```text
  [ SEU CELULAR / APP ] ──(1. SMTP: ENVIA!)──→ [ SERVIDOR DE E-MAIL ]
                                                       │
                          ┌────────────────────────────┴─────────────────────────────┐
                          ▼                                                          ▼
         [ 2A. POP3 (Baixa e APAGA!) ]                             [ 2B. IMAP (SINCRONIZA!) ]
         Faz download para o PC e APAGA                            Mantém tudo guardado NO SERVIDOR
         a cópia do servidor por padrão!                           e espelha lido/pastas em todo lugar!
```

| Ferramenta / Protocolo | Direção | O que Acontece na Prática | Macete Definitivo |
| :--- | :---: | :--- | :--- |
| **SMTP** *(Simple Mail Transfer Protocol)* | **SAÍDA / ENVIO** | Envia seu e-mail para o servidor e entrega de um provedor até outro (`@etec` → `@gmail`). **NÃO lê caixa de entrada!** | **S**MTP = **S**ubir / **S**air (Enviar!) |
| **POP3** *(Post Office Protocol v3)* | **RECEBIMENTO** *(Baixa local)* | Conecta ao servidor, **baixa os e-mails para a memória do dispositivo e, por padrão, EXCLUI do servidor**. Se abrir no celular depois, os antigos não estão lá! | **POP3** = **P**uxa pro PC e **P**assa a borracha no servidor! |
| **IMAP** *(Internet Message Access Protocol)* | **RECEBIMENTO** *(Sincroniza)* | **Mantém as mensagens no servidor** e sincroniza em tempo real (se marcou como lido no celular, já aparece lido no notebook também!). | **IMAP** = espelho sincronizado multi-aparelho! |
| **Webmail** | **Navegador** | Interface acessada direto pelo navegador via **HTTP/HTTPS** (ex.: Gmail Web no Chrome), sem instalar programa cliente desktop (como Thunderbird). | Acesso direto no browser! |

---

### 📚 Parte 3 — Topologias de Rede, Cloud Computing, IoT e Navegadores

#### 1. Topologias de Rede *(DS 2025 Q26 & DS 2019 Q23)* — Olhe o Desenho de Cada Uma!

```text
  BARRAMENTO (Bus)                      ESTRELA (Star) — Padrão Moderno (Switch!)
  [PC1]   [PC2]   [PC3]                      [PC1]
    │       │       │                          │
  ──┴───X───┴───────┴── (Cabo único!)  [PC2]──[SWITCH]──[PC3]   (Cabo próprio por PC!)
  *Cortou em X? TODOS CAEM!*            *Se cabo do PC2 cair, só PC2 para!*

  ANEL (Ring)                           MALHA (Mesh)
  [PC1] ─── [PC2]                       [PC1]───[PC2]
    │         │                           │ \   / │
  [PC4] ─── [PC3]                       [PC3]───[PC4]
  (Circuito fechado c/ Token)           (Vários caminhos -> máxima tolerância a falhas!)
```

| Topologia | Como Liga | Ponto Forte | Ponto Fraco / Pegadinha de Prova |
| :--- | :--- | :--- | :--- |
| **Barramento (*Bus*)** *(DS 2025 Q26)* | Todos ligados ao **mesmo cabo central (*backbone*)** com terminadores nas pontas. | Simples e barata em cabo. | **Ponto único de falha:** se o cabo principal romper em qualquer ponto, **A REDE INTEIRA PARA!** |
| **Estrela (*Star*)** *(DS 2019 Q23)* | Cada PC tem seu cabo exclusivo indo até um **Switch** central. | Se **o cabo de 1 PC romper, só ele cai** — o resto continua normal! Fácil ampliar/manutenção. | Se o **Switch central** queimar ou desligar da tomada, todos perdem rede. |
| **Anel (*Ring*)** | Ligados em círculo fechado passando um sinal chamado *Token* (dando a vez de falar). | Sem colisões aleatórias. | Em anel simples, se um nó falhar quebra o circuito. |
| **Malha (*Mesh*)** | Cada dispositivo liga diretamente a vários/todos os outros. | **Maior tolerância a falhas!** Se 1 cabo cai, o dado desvia por outro caminho. | Caríssima em cabeamento para redes com muitos PCs. |
| **Híbrida** | Junta duas ou mais topologias (ex.: várias Estrelas interligadas). | Flexível para escolas e empresas grandes. | Gerenciamento mais complexo. |

#### 2. Computação em Nuvem (*Cloud Computing*) — Quem Cuida do Quê? *(Apostas Q26)*
Em vez de comprar servidores físicos caros e colocar numa sala refrigerada da sua empresa, você aluga poder computacional pela internet em **3 modelos principais**:

```text
  Modelo        Você (Cliente) Cuida de:          Provedor Cloud (AWS/Azure/Google) Cuida de:
  ───────────────────────────────────────────────────────────────────────────────────────────
  IaaS          [App] + [SO + Banco + Firewall]   [Hardware Virtual, Rede, Energia, Prédio]
  PaaS          [Apenas o SEU Código/App!]        [SO + Runtime + Hardware + Banco gerenciado]
  SaaS          [NADA! Só entra e usa pronto!]    [TUDO! App pronto rodando no navegador!]
```
- **IaaS (*Infraestrutura como Serviço* — ex.: AWS EC2, Azure VMs, VPS Linux):** Como **alugar a cozinha e o forno** (ou uma máquina virtual para montar seu servidor de Minecraft do zero) — você mesmo instala e configura o Windows/Linux, patches de segurança e seu app!
- **PaaS (*Plataforma como Serviço* — ex.: Vercel, Heroku, Azure App Service):** Como **comprar massa e recheio prontos só para assar** — o provedor já cuida do Sistema Operacional e servidor; o programador só sobe o **código** (ex.: seu Bot de Discord!).
- **SaaS (*Software como Serviço* — ex.: Gmail, Google Docs, Microsoft 365, Canva, Discord Web, GeForce NOW):** Como **pedir ou comer a pizza 100% pronta** — você não instala nem programa nada, apenas abre a conta e usa!

#### 3. Internet das Coisas (**IoT**), Navegadores e Suítes *(DS 2025 Q24, Q29 e Q30)*
- **IoT (*Internet of Things*):** Conecta objetos físicos comuns à internet usando **Sensores** (medem o ambiente: temperatura, umidade, batimento cardíaco) + conectividade + **Atuadores** (agem no ambiente físico: ligam a válvula de irrigação, trancam a porta, acendem o ar-condicionado). Ex.: relógios smart, casas inteligentes, agricultura 4.0.
- **Navegadores (*Browsers*) *(DS 2025 Q29)*:** Programas que leem HTML/CSS/JS e desenham sites: **Chrome, Firefox, Edge, Safari, Opera, Brave**. **Intrusos clássicos da prova:** ***Google Search* (é BUSCADOR, NÃO é navegador!)**, *Outlook*, *Excel*, *VS Code*.
- **Suítes de Escritório *(DS 2025 Q30)*:** Pacotes com Editor de Texto + Planilha + Apresentação — **Microsoft 365 / Office** (Word, Excel, PowerPoint), **LibreOffice** (Writer, Calc, Impress) e **Google Workspace** (Docs, Sheets, Slides).

---

### 📚 Parte 4 — Inglês Técnico & Ética Socioambiental CPS *(DS 2025 Q1–Q6 & M-Tec Q7–Q9)*

Quase toda prova começa com **Q1–Q3 de Inglês** e **Q4–Q6 de Ética/Cidadania**! Não dê esses pontos fáceis de graça:

#### 1. Técnicas de Leitura & Vocabulário Obrigatório de Inglês Técnico
- ***Skimming*:** Passada de olhos rápida no título, subtítulos e primeiras frases dos parágrafos só para pescar o **tema principal** do texto.
- ***Scanning*:** Leitura "scanner" buscando exatamente uma informação específica pedida pela questão (um ano, sigla, porcentagem ou nome próprio).
- **Gramática já cobrada:**
  - **Comparativo / Superlativo irregular *(M-Tec 2022 Q7)*:** `bad → worse (pior que) → the worst (o pior)`; `good → better (melhor que) → the best (o melhor)`.
  - **Sufixos *(M-Tec 2022 Q9)*:** `-able / -ible` formam **adjetivos** indicando possibilidade (*debatable, readable, scalable*); `-ive` forma **adjetivos** (*positive, interactive*); `-tion / -ment / -ness` formam **substantivos**; `-ly` costuma formar **advérbios** (*rapidly, quickly*).
- **Falsos Cognatos (Parecem português, mas significam outra coisa!):**
  - **`data`** = **dados** *(NUNCA "datas"! Data do calendário é `date`!)*
  - **`actually`** = **na verdade / de fato** *(NÃO é "atualmente" = `currently`!)*
  - **`pretend`** = **fingir** *(NÃO é "pretender" = `intend`!)*
  - **`library`** = **biblioteca** (ou biblioteca de código) *(NÃO é "livraria" = `bookstore`!)*
  - **`support`** = **apoiar / dar suporte** *(NÃO é "aguentar dor" = `bear/stand`!)*
- **Palavras campeãs em textos de TI:**
  `outcomes` (resultados/desfechos) • `troubleshooting` (diagnóstico e solução de falhas) • `critical thinking` (pensamento crítico) • `inference` (dedução implícita nas entrelinhas) • `daunting` (intimidante/assustador) • `bias` (viés/parcialidade) • `awareness` (consciência).

#### 2. Ética em TI, Lixo Eletrônico e LGPD *(DS 2025 Q4–Q6)*
Antes de marcar, veja os **3 termos ambientais/legais** cobrados com frequência:
- **Logística Reversa:** Sistema que garante que produtos eletrônicos, pilhas e baterias velhos **façam o caminho de volta** dos consumidores até os fabricantes/lojas/pontos certificados para reciclagem segura (em vez de irem para o lixo comum contaminar o solo com metais pesados como chumbo, mercúrio e cádmio!).
- **Obsolescência Programada:** Prática antiética em que empresas fabricam aparelhos ou travam softwares propositalmente para durarem pouco ou ficarem lentos rápido, forçando o cliente a comprar outro novo gerando mais lixo eletrônico.
- **TI Verde (*Green IT*):** Conjunto de boas práticas para economizar energia em servidores, usar computação em nuvem eficiente, digitalizar papéis e reciclar hardware.
- **LGPD (*Lei Geral de Proteção de Dados*):** Lei brasileira que exige **consentimento claro**, **finalidade transparente** (dizer exatamente para que aquele dado vai ser usado), **coleta mínima** (não pedir o que não precisa!) e proteção contra vazamentos de dados pessoais.

> [!TIP]
> **Regra infalível nas questões de Ética da FAT:** A alternativa certa busca **sempre o bem comum real, direitos coletivos/trabalhistas e consciência ambiental**. Descarte na hora opções ligadas a *autopromoção em redes sociais, vaidade, esconder falhas por dinheiro ou jogar hardware velho no lixo comum*!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q26 & Q28 — Topologias e E-mail)
*Julgue: I. Na topologia Barramento, romper o cabo central derruba toda a rede. II. O protocolo POP3 envia mensagens do app cliente até o servidor de saída. III. O protocolo IMAP mantém e-mails sincronizados no servidor para ler em vários dispositivos.*
- **I:** VERDADEIRO.
- **II:** **FALSO** (quem **envia** é o **SMTP**; POP3 baixa e apaga do servidor).
- **III:** VERDADEIRO.

#### Questão Resolvida 2 (Baseada em DS 2025 Q1 & M-Tec Q7 — Inglês Técnico)
*No trecho "Effective troubleshooting produces reliable outcomes, even when legacy bugs feel daunting and represent the worst scenario", as palavras destacadas significam respectivamente:*
- `troubleshooting` = **solução/diagnóstico de falhas**; `outcomes` = **resultados**; `daunting` = **intimidante**; `worst` = **o pior** (superlativo de *bad*).


---

## Dia 12 — Base Comum M-Tec I: Português, Interpretação, Literatura e História (1º Ano EM)

### 🎯 Por que Português e História Decidem Vagas no M-Tec?

Na prova de **Vagas Remanescentes do 2º Ano M-Tec (Ensino Médio Integrado ao Técnico)**, você não disputa apenas com quem decorou programação: cerca de **metade da prova oficial** *(como vimos na prova real M-Tec 2022, questões Q1–Q6 e Q24–Q27)* cobra conteúdos da **Base Nacional Comum da 1ª Série do Ensino Médio**!

E há um bônus enorme: dominar interpretação precisa de textos (saber distinguir uma contradição real de uma simples oposição, ler entrelinhas e entender variações de linguagem) afia diretamente sua visão para desmontar as pegadinhas verbais da parte técnica!

---

### 🎮 Para Entender Sem Medo (Conexão com Jogos & Internet)

- **Tipos Textuais nos Games:** A *lore* / cutscene que conta o passado do herói no tempo é **Narração**; a ficha descrevendo a armadura é **Descrição**; o tutorial (*"Pressione `Espaço` para pular"*) é **Injunção**; a *wiki* explicando neutro os atributos da arma é **Exposição**; já um vídeo defendendo *"Por que essa arma deve ser nerfada"* é **Dissertação Argumentativa**.
- **Variação Linguística:** Falar *"Mano, dropa a spike no B e dá call no Disc"* jogando com amigos está 100% adequado ao contexto; escrever isso numa redação da Etec seria inadequado!
- **Pré-História tipo *Age of Empires / Civilization*:** Começar andando pelo mapa caçando frutas e animais até acabar (**Paleolítico Nômade**) → desbloquear agricultura e criação de gado perto do rio, criando aldeias fixas (**Revolução Neolítica / Sedentarismo**) → mapa dividido em feudos isolados com servos e suseranos (**Feudalismo**).

---

### 📚 Parte 1 — Tipologia Textual vs. Gênero Textual *(M-Tec 2022 Q3)*

Não confunda esses dois conceitos básicos de Língua Portuguesa:
- **Gênero Textual:** É o **formato concreto** que o texto assume no dia a dia da sociedade (existem dezenas: *notícia, receita de bolo, crônica, bula de remédio, e-mail, contrato, tweet, cardápio, tutorial*).
- **Tipo Textual (Tipologia):** É a **estrutura interna predominante** dentro do texto — **existem apenas 5 tipos principais**:

| Tipo Textual | Objetivo Central | Pistas Gramaticais na Prova | Exemplo Real |
| :--- | :--- | :--- | :--- |
| **1. Narração** | **Contar acontecimentos** vividos por personagens ao longo do **tempo e do espaço** (enredo com começo, meio e fim). | Verbos de ação no passado (*abriu, testou, ganhou*), marcadores de tempo (*ontem, logo depois*). | *"Ontem à noite, Henrique abriu o computador, resolveu o exercício de lógica e comemorou o acerto."* |
| **2. Descrição** | Fazer uma **"fotografia em palavras"** retratando características físicas ou psicológicas (**sem passar o tempo**!). | Adjetivos, substantivos, verbos de estado (*era, parecia, tinha*), foco em detalhes visuais/sensoriais. | *"O laboratório tinha vinte monitores brilhantes, cadeiras confortáveis pretas e ar silencioso e frio."* |
| **3. Exposição** *(Dissertativo-Expositivo)* | **Informar, definir e explicar** um assunto de maneira **clara, didática e impessoal**, sem tentar convencer de uma opinião pessoal. | 3ª pessoa, definições objetivas, dados neutros (ex.: apostilas, enciclopédias, verbetes, manuais técnicos). | *"O protocolo HTTPS adiciona criptografia sobre o HTTP para proteger dados enviados na internet."* |
| **4. Dissertação Argumentativa** | **Defender uma tese (opinião fundamentada)** com argumentos e provas para **persuadir/convencer** o leitor. | Tese clara, conectivos lógicos (*portanto, logo, contudo*), conclusões avaliativas (ex.: editorial de jornal, redação ENEM). | *"O ensino técnico integrado é essencial porque une formação cidadã e preparação prática real."* |
| **5. Injunção / Instrucional** | **Instruir, orientar, aconselhar ou mandar** fazer algo passo a passo. | Verbos no **imperativo** (*clique, abra, adicione, respeite*) ou infinitivo instrucional (*manter em local seco*). | *"1. Leia a questão com calma. 2. Risque os itens falsos. 3. Preencha o gabarito."* |

---

### 📚 Parte 2 — Figuras de Linguagem, Semântica e Variações Linguísticas

#### 1. Figuras de Linguagem Campeãs de Prova *(M-Tec 2022 Q4)*

| Figura de Linguagem | Como Identificar Sem Errar | Exemplo Comentado |
| :--- | :--- | :--- |
| **Antítese** | **Aproxima palavras opostas** na mesma frase, **MAS sem contradição impossível** (as duas coisas existem normalmente!). | *"Na vida há **alegria** e **tristeza**, **dia** e **noite**."* (Opostos lógicos coexistindo naturalmente — NÃO é contradição ilógica!) |
| **Paradoxo (Oxímoro)** *(M-Tec Q4!)* | Junta ideias que **se chocam e se anulam logicamente** numa mesma afirmação para provocar reflexão profunda! | *"É ferida que **dói e não se sente**"* (Camões) / *"Estar **hiperconectado** nos deixa **mais solitários**"* / *"Quanto mais estudo, menos entendo"*. |
| **Comparação (Símile) vs. Metáfora** | **Comparação** usa palavra conectora explícita (**"como"**, *"tal qual"*, *"parece"*). **Metáfora** faz uma comparação **direta, SEM conector**! | Comparação: *"O banco de dados é **como** um cofre."* <br>Metáfora: *"O banco de dados **é** um cofre."* |
| **Metonímia** | Troca uma palavra por outra que tem ligação física/real próxima (autor pela obra, embalagem pelo conteúdo, marca pelo produto). | *"Li **Machado de Assis** ontem"* (os livros dele) / *"Comi **dois pratos**"*. |
| **Ironia** | Dizer o **contrário do que realmente se pensa**, com tom de crítica ou humor. | *"Que maravilha de código — demorou só 4 horas para travar na tela inicial!"* |
| **Hipérbole** | **Exagero** proposital para dar impacto expressivo. | *"Estudei essa matéria **um milhão de vezes**!"* |
| **Hipérbato** | **Inversão brusca da ordem direta** natural da frase (*Sujeito + Verbo + Complemento*). | *"Ouviram do Ipiranga as margens plácidas de um povo heroico o brado retumbante"* (ordem direta seria: *As margens plácidas do Ipiranga ouviram...*). |

#### 2. Semântica: Denotação, Conotação, Polissemia e Hipônimo/Hiperônimo *(M-Tec 2022 Q5)*
- **Denotação (`D` = Dicionário):** Sentido **literal, real, exato** da palavra (*"O muro foi construído com **pedra**"*).
- **Conotação:** Sentido **figurado, poético ou simbólico** (*"Ele tem um coração de **pedra**"* = pessoa fria/insensível).
- **Polissemia:** Uma mesma palavra com **vários sentidos ligados pelo contexto** (*"a **cabeça** do menino"*, *"a **cabeça** do prego"*, *"a **cabeça** da fila"*).
- **Hiperônimo vs. Hipônimo *(caiu literal na M-Tec Q5!)*:**
  ```text
     HIPERÔNIMO (Termo GERAL, guarda-chuva maior) :  "Pensador"   |  "Animal"    |  "Linguagem"
                                                         ↓              ↓              ↓
     HIPÔNIMO   (Termo ESPECÍFICO dentro dele)   :  "Aristóteles" |  "Cachorro"  |  "Python"
  ```
  - Exemplo real de coesão num texto: *"A escola citou **Aristóteles**. O **pensador** grego afirmava..."* → Trocamos o termo específico (**hipônimo** *Aristóteles*) pela categoria ampla (**hiperônimo** *pensador*) para não repetir a palavra!

#### 3. Variações Linguísticas *(M-Tec 2022 Q2)*
A Sociolinguística moderna ensina que **não existe "português certo vs. português burro/errado"** — a língua muda naturalmente e o critério correto é **adequação ao contexto** (você não fala na entrevista de emprego igual fala jogando Discord!):
- **Diatópica (Geográfica / Regional):** Varia de um estado/país para outro (*"aipim" / "macaxeira" / "mandioca"*; *"guri"* no Sul; *"trem"* em MG).
- **Diacrônica (Histórica / Tempo):** Muda ao longo dos séculos (*"Vossa Mercê" → "Vosmicê" → "Você" → "Vc"*).
- **Diastrática (Grupo Social / Profissão):** Jargões de grupos específicos (programador falando *"fazer deploy de um container"*; gírias de skatistas/gamers).
- **Diafásica (Situacional / Grau de Formalidade):** Mesma pessoa muda o falar conforme a situação (falar com o diretor da Etec vs. conversar em casa).

---

### 📚 Parte 3 — Escolas Literárias do 1º Ano EM (Com Contexto e Exemplos Reais!) *(M-Tec Q1 & Q6)*

#### 1. Trovadorismo (Idade Média — sécs. XII a XIV, *M-Tec Q6*)
Primeira literatura em língua galego-portuguesa, nascida nos castelos feudais como **cantigas cantadas** acompanhadas de instrumentos musicais pelos trovadores e jograis:
- **Cantigas Líricas (de Sentimentos / Amor):**
  - **Cantiga de Amor:** Eu lírico **MASCULINO** sofre apaixonado por uma dama nobre distante e superior (*"minha senhor"*). Reflete a **vassalagem amorosa** (traz o ritual do **feudalismo**, em que o vassalo serve humildemente ao seu senhor nobre, agora aplicado ao amor!).
  - **Cantiga de Amigo:** Eu lírico **FEMININO** *(mesmo sendo composta por autores homens!)* expressa saudade do seu namorado (*chamado de "amigo" na época*) conversando com a mãe, amigas, flores ou as ondas do mar! Origem mais popular e rural.
- **Cantigas Satíricas (de Crítica/Zombaria):**
  - **Escárnio:** Crítica **indireta, irônica, com duplo sentido**, **SEM citar o nome** da pessoa ridicularizada.
  - **Maldizer:** Crítica **direta, pesada e explícita**, citando o **nome do alvo** e usando palavras ofensivas.

#### 2. Humanismo (séc. XV), Classicismo (séc. XVI) e Quinhentismo no Brasil
- **Transição Medieval → Renascimento:** Na Idade Média dominava o **Teocentrismo** (Deus no centro de todas as decisões e explicações). No Renascimento nasce o **Antropocentrismo / Humanismo** (valorização da razão humana, ciência e equilíbrio greco-romano).
- **Humanismo (séc. XV):** Fase de transição; destaque absoluto para o teatro crítico de **Gil Vicente** (*Auto da Barca do Inferno*, criticando padres corruptos, nobres e juízes).
- **Classicismo (séc. XVI):** Equilíbrio formal, racionalidade e sonetos medidos (**Luís de Camões** — autor da epopeia *Os Lusíadas*).
- **Quinhentismo no Brasil (1500 — *M-Tec Cards*):** O primeiro século após a chegada dos portugueses teve 2 frentes de escrita aqui:
  1. **Literatura Informativa / de Viagens:** Descrevia a terra, rios, plantas e indígenas para o Rei de Portugal (**Carta de Pero Vaz de Caminha**, 1500).
  2. **Literatura Jesuítica / Catequética:** Poemas e peças teatrais didáticas com objetivo religioso de **catequizar** os indígenas (**Padre José de Anchieta**).

#### 3. Barroco (sécs. XVII–XVIII — *Campeão de Pegadinha: M-Tec Q1!*)
**Contexto histórico:** No século XVI houve a Reforma Protestante e a Igreja Católica reagiu com a **Contrarreforma Católica**, endurecendo dogmas religiosos. O homem do século XVII ficou dividido ao meio entre os prazeres do mundo renascentista e o medo do pecado medieval (**Dualismo Barroco**: corpo × alma, céu × inferno, fugacidade da vida × eternidade)! Por isso a poesia barroca transborda antíteses e paradoxos!

*(Antes da tabela: o que é um **Silogismo**? É um raciocínio lógico encadeado de 3 linhas típico da filosofia: "Todo ser humano é mortal; Sócrates é ser humano; logo, Sócrates é mortal"!)*

| Tendência do Barroco | Foco Principal | Como Aparece no Texto + Exemplo Real | Grande Autor |
| :--- | :--- | :--- | :--- |
| **Cultismo** *(Gongorismo)* | **Jogo de PALAVRAS** e forma exuberante | Vocabulário raro, inversões, metáforas sensoriais (*sol, ouro, cristal, cores*). Ex.: *"Anjo no nome, Angélica na cara, isso é ser flor..."* (Gregório) | **Gregório de Matos** (*"Boca do Inferno"*) na poesia lírica/satírica |
| **Conceptismo** *(Quevedismo)* | **Jogo de IDEIAS** e lógica | Raciocínio lógico rigoroso, argumentação em **silogismos**, perguntas e respostas para provar teses morais/religiosas. Ex.: *"Se a culpa é cega e a paixão é surda, logo..."* | **Padre Antônio Vieira** (nos famosos *Sermões*, como o *Sermão da Sexagésima*) |

> [!CAUTION]
> **Pegadinha clássica da M-Tec Q1:** A banca define certinho o que é cada um e **troca os nomes Cultismo e Conceptismo**! Decore em 2 segundos: **`CON`ceptismo = `CON`ceito (IDEIAS/lógica)**; **`CUL`tismo = `CUL`to à PALAVRA bonita/rebuscada**!

---

### 📚 Parte 4 — História Geral (1º Ano EM) e Movimentos Migratórios *(M-Tec Q24–Q27)*

#### 1. Pré-História Completa: Paleolítico → Revolução Neolítica → Idade dos Metais *(M-Tec Q24–Q25)*

| Período | Estilo de Vida | Como Conseguia Comida & Avanços Tecnológicos |
| :--- | :--- | :--- |
| **Paleolítico** *(Idade da Pedra Lascada)* | **Nomadismo:** mudavam sempre de lugar assim que caça e frutos acabavam na área. | **Caça, pesca e coleta**; ferramentas rústicas de pedra lascada; **descoberta/domínio do fogo**; arte rupestre em cavernas. |
| **Neolítico** *(Pedra Polida — **Revolução Neolítica**)* | **Sedentarismo:** fixaram aldeias permanentes perto de grandes rios férteis! | Descoberta da **agricultura** e **domesticação de animais (pecuária)**! Gerou **excedente de comida**, cerâmica, tecelagem, crescimento da população e nascimento de cidades/Estado. |
| **Idade dos Metais** | Cidades organizadas, comércio e exércitos | Fundição de cobre, bronze e ferro; invenção da roda e criação dos **primeiros sistemas de escrita** (que marcam o fim da Pré-História e início da História!). |

**Os 5 Movimentos Migratórios para Diferenciar *(M-Tec Q24)*:**
- **Nomadismo:** Sem moradia fixa — desloca-se atrás de recursos naturais.
- **Sedentarismo:** Fixação em um território cultivando e morando ali.
- **Êxodo Rural:** Migração definitiva em massa **do campo para as cidades** buscando emprego urbano/industrial.
- **Migração Pendular (*Pendularismo*):** Ir e voltar **todos os dias** entre duas cidades/bairros para trabalhar ou estudar e retornar à noite.
- **Transumância:** Migração **sazonal (temporária por estação do ano)** — ex.: levar gado para áreas úmidas na seca e voltar na época de chuva.

#### 2. Antiguidade Oriental (Primeiras Civilizações) e Clássica *(M-Tec Q26)*
- **Antiguidade Oriental — Crescente Fértil:** Na **Mesopotâmia** (sumérios e babilônios entre os rios **Tigre e Eufrates**) e no **Egito Antigo** (junto ao **Rio Nilo**), a chuva era escassa, mas os rios transbordavam fertilizando as margens. Por isso eram **Sociedades Hidráulicas** (o Estado organizava diques e canais de irrigação), com **Teocracia** (o faraó/rei governava visto como deus ou representante divino), criação das primeiras leis escritas (**Código de Hamurabi** — *"olho por olho, dente por dente"*) e escrita (cuneiforme na argila / hieróglifos egípcios).
- **Antiguidade Clássica — Grécia e Roma:**
  - **Grécia:** Organizada em Cidades-Estado independentes (**Pólis**): **Atenas** criou a **Democracia Direta** *(mas restrita: só votavam homens livres adultos atenienses — excluía mulheres, escravos e estrangeiros!)* e floresceu a Filosofia; **Esparta** focava em sociedade militarista.
  - **Roma:** Passou por Monarquia → República → Império; deixou grande legado no **Direito Romano**, engenharia (aquedutos/estradas), línguas latinas (como o Português!) e difusão do Cristianismo até cair em **476 d.C.** (marco que inicia a Idade Média!).

#### 3. Idade Média Ocidental & Feudalismo (sécs. V ao XV — *M-Tec Q27*)
Com as invasões germânicas e queda de Roma, o comércio urbano encolheu e a população fugiu para o campo:
- **O Feudo (grande propriedade rural autossuficiente) em 3 partes:**
  1. **Manso Senhorial:** Melhores terras exclusivas do Senhor Feudal (tudo produzido ali era 100% dele);
  2. **Manso Servil:** Pequenos lotes entregues aos servos para sobreviverem e tirarem o sustento (pagando pesadas taxas);
  3. **Terras Comunais:** Pastos, bosques e águas usados em comum para lenha e rebanhos.
- **Economia Feudal:** Essencialmente **agrária, rural, de subsistência**, com **escambo (troca direta de produtos) e baixíssima circulação de moedas**!
- **Sociedade Estamental (rígida, quase sem mobilidade: "nasceu servo, morre servo"):**
  1. **Clero** *(oratores — os que rezam/dominam a escrita e escolas)*;
  2. **Nobreza** *(bellatores — os donos das terras/guerreiros)*;
  3. **Servos** *(laboratores — camponeses presos à terra: não podiam ser vendidos como escravos, mas não podiam ir embora e pagavam tributos como **corveia** [dias de trabalho grátis no manso senhorial], **talha** [parte da sua colheita] e **banalidades** [taxa pelo uso do moinho/forno do senhor])*.
- **Política Descentralizada:** O rei perdeu força; cada senhor mandava em seu feudo unido aos outros pelo juramento de **Suserania e Vassalagem** (o **suserano** doava terra/feudo ao **vassalo**, que jurava lealdade militar). A única força unificada em toda a Europa era a **Igreja Católica (Teocentrismo)**.

---

### 🕵️‍♂️ Dissecando Questões Reais da Prova M-Tec

#### Questão Resolvida 1 (Baseada em M-Tec 2022 Q1 — Barroco)
*No Barroco, a tendência marcada pelo jogo lógico de ideias, silogismos e argumentação nos sermões de Padre Antônio Vieira chama-se _____; enquanto a linguagem rebuscada com jogo de palavras e imagens sensoriais chama-se _____.*
- **Gabarito:** **Conceptismo** (conceito/ideias) e **Cultismo** (cultura da palavra/forma).

#### Questão Resolvida 2 (Baseada em M-Tec 2022 Q4 & Q25/27)
*Julgue: I. "Estar hiperconectado nos deixa mais solitários" expressa um Paradoxo por unir ideias logicamente opostas numa mesma afirmação. II. A Revolução Neolítica trouxe a agricultura e o sedentarismo. III. A economia feudal europeia era urbana, industrial e com intenso uso de moedas.*
- **Item I:** VERDADEIRO.
- **Item II:** VERDADEIRO.
- **Item III:** **FALSO!** O feudalismo era agrário, rural, de subsistência e com **redução drástica do uso de moedas**!


---

## Dia 13 — Base Comum M-Tec II: Matemática, Química, Física e Biologia/Ambiental (1º Ano EM)

### 🎯 Por que Essa Aula Pode Garantir Sua Vaga?

Na prova oficial do **M-Tec 2º Ano** *(como vimos nas questões reais M-Tec 2022 Q10–Q23 e Q33)*, muitos candidatos só estudam informática e deixam metade da prova na mesa! A ótima notícia é que os problemas de **Matemática, Química, Física e Biologia** cobrados no 1º Ano seguem **raciocínios diretos e fórmulas bem limpas**. Vamos aprender cada um passo a passo, sem pular nenhuma base!

---

### 📚 Parte 1 — Matemática do 1º Ano Passo a Passo *(M-Tec Q19–Q23)*

#### 1. Os Conjuntos Numéricos (`ℕ, ℤ, ℚ, 𝕀, ℝ`) *(M-Tec Q19)*
Enxergue onde cada número "mora" olhando o esquema das caixinhas uma dentro da outra:

```text
  ┌───────────────────────── ℝ (REAIS = Racionais ∪ Irracionais) ─────────────────────────┐
  │ ┌───────────────────────────────────────────┐  ┌────────────────────────────────────┐ │
  │ │           ℚ (RACIONAIS = Frações!)        │  │         𝕀 (IRRACIONAIS)            │ │
  │ │ ┌───────────────────────────────────────┐ │  │ Decimais infinitos SEM repetição   │ │
  │ │ │       ℤ (INTEIROS): ..., -2, -1       │ │  │ periódica! Nunca viram fração!     │ │
  │ │ │ ┌───────────────────────────────────┐ │ │  │  Ex.: π ≈ 3,141592...              │ │
  │ │ │ │   ℕ (NATURAIS): 0, 1, 2, 3...     │ │ │  │       √2 ≈ 1,41421... , √3 , √5    │ │
  │ │ │ └───────────────────────────────────┘ │ │  └────────────────────────────────────┘ │
  │ │ └───────────────────────────────────────┘ │                                         │
  │ │  Decimais exatos: 0,25 (1/4), -1,5 (-3/2) │  (ATENÇÃO: nenhum número é ℚ e 𝕀 ao    │
  │ │  Dízimas periódicas: 0,333... (1/3)       │   mesmo tempo -> ℚ ∩ 𝕀 = ∅ !)           │
  │ └───────────────────────────────────────────┘                                         │
  └───────────────────────────────────────────────────────────────────────────────────────┘
```
- **Por que toda Dízima Periódica é Racional (`ℚ`)?** Porque **toda dízima com repetição tem uma fração geratriz exata** (ex.: `0,333... = 3/9 = 1/3`; `0,454545... = 45/99 = 5/11`)! Já **`π`** (`3,14159265...`) e **raízes não exatas (`√2, √3, √5`)** nunca repetem padrão nem fecham em fração → são **Irracionais (`𝕀`)**!
- **Armadilha clássica:** **`√9`** é Irracional? **NÃO!** Pois `√9 = 3`, que é Natural/Inteiro/Racional!

#### 2. Operações entre Conjuntos e Diagrama de Venn *(M-Tec Q22)*
- **Interseção (`A ∩ B`):** Pega **APENAS quem está nos dois conjuntos ao mesmo tempo** ("A **e** B").
- **União (`A ∪ B`):** Junta **todos** os elementos de `A` com todos os de `B` num conjunto só, **sem repetir duplicatas**.
- **Diferença (`A - B`):** Pega quem está em `A` e **arranca fora** qualquer um que também esteja em `B`.

**💻 Exemplo Resolvido #1 (Expressão Direta — estilo M-Tec Q22):**
Dados `A = {1, 2, 4, 6}`, `B = {2, 3, 6, 8}` e `C = {3, 9}`, calcule **`(A ∩ B) ∪ C`**:
1. **Parênteses primeiro:** o que aparece em `A` **E** em `B`? Apenas **`{2, 6}`**.
2. **Agora une com `C`:** `{2, 6} ∪ {3, 9}` = **`{2, 3, 6, 9}`**!

**💻 Exemplo Resolvido #2 (Diagrama de Venn com Pesquisa):**
*Numa sala, `80` alunos gostam de Python, `50` de JS e `20` gostam dos dois. Quantos alunos foram entrevistados?*
```text
       Python (80 total)            JS (50 total)
     ┌─────────────────────┬──────┬─────────────────┐
     │   Só Python:        │ Ambos│   Só JS:        │
     │   80 - 20 = 60      │  20  │   50 - 20 = 30  │
     └─────────────────────┴──────┴─────────────────┘
```
**Regra de ouro:** **SEMPRE comece preenchendo o miolo (`20`) e subtraia das pontas** para não somar os 20 alunos duas vezes! Total = `60 + 20 + 30 =` **`110` alunos**!

#### 3. Princípio Fundamental da Contagem (A Pegadinha do Zero!) *(M-Tec Q23)*
*Quantos números naturais de **3 algarismos distintos** podemos formar usando `{0, 1, 2, 3, 4, 5}`?*
Desenhe 3 tracinhos: `[ Centena ] × [ Dezena ] × [ Unidade ]`.
- **Por que começar pela 1ª casa (Centena)?** Porque **um número de 3 dígitos NUNCA pode começar com `0`** (`042` vale `42`, que só tem 2 algarismos!).
  - **1ª casa (Centena):** Tirando o `0` de `{0,1,2,3,4,5}`, sobram **5 opções** (`1,2,3,4,5`).
  - **2ª casa (Dezena):** Já gastamos 1 número na centena (ex.: o `3`), **mas agora o `0` pode entrar!** Dos 6 originais menos o `3` gasto → sobram **5 opções** (`0,1,2,4,5`)!
  - **3ª casa (Unidade):** Dos 6 originais, já gastamos 2 distintos → restam **4 opções**!
- Multiplicando tudo: **`5 × 5 × 4 = 100 números distintos`**!
- *(Dica extra: se a questão pedir número **ÍMPAR** ou **PAR** usando um conjunto com zero, comece preenchendo a restrição mais forte na **Unidade** [última casa] e confira o zero na 1ª casa! Ex.: quantos ímpares de 2 dígitos distintos com `{0,1,2,3}`? Unidade ímpar = `{1,3}` [2 opções]; Dezena sem `0` e sem o dígito usado na unidade = 2 opções → `2 × 2 = 4`!)*

#### 4. Função Afim (1º Grau: `f(x) = ax + b`) — Completa com Exemplo!
- **Cara da função:** **`f(x) = a · x + b`** *(seu gráfico é sempre uma **linha reta**)*.
- **`b` (Coeficiente Linear):** É o **valor fixo inicial** (onde a reta corta o eixo vertical `Y` quando `x = 0`).
- **`a` (Coeficiente Angular / Taxa de Variação):** É o **quanto sobe ou desce a cada 1 passo de `x`**. Se **`a > 0`** a reta é **crescente** (sobe); se **`a < 0`** é **decrescente** (desce).
- **Como achar a Raiz (Zero da função):** Basta igualar **`f(x) = 0`** e isolar o `x`!

**💻 Exemplo Resolvido (Problema Prático de 1º Grau):**
*Um aplicativo cobra **bandeirada fixa de `R$ 6,00`** mais **`R$ 2,50` por quilômetro (`x`)** rodado.*
1. **Qual é a função do preço?** `f(x) = 2,5x + 6` *(note: `a = 2,5` por km; `b = 6` fixo)*.
2. **Quanto custa uma corrida de `10 km`?** `f(10) = 2,5 · 10 + 6 = 25 + 6 =` **`R$ 31,00`**.
3. **E se pagou `R$ 26,00`, quantos km rodou?** `2,5x + 6 = 26` → `2,5x = 20` → `x = 20 / 2,5 =` **`8 km`**!

#### 5. Função Quadrática (2º Grau: `f(x) = ax² + bx + c`, com `a ≠ 0`) *(M-Tec Q20)*
Seu gráfico é uma curva chamada **Parábola** (igual a trajetória de uma bola chutada para cima):
- **Concavidade (boca da curva):**
  - Se **`a > 0`** → boca para **CIMA** (`∪`, sorrindo → tem **ponto de MÍNIMO**).
  - Se **`a < 0`** → boca para **BAIXO** (`∩`, triste → tem **ponto de MÁXIMO**, ex.: altura máxima ou lucro máximo!).
- **Raízes (onde corta o eixo `X`, resolvendo `ax² + bx + c = 0`):**
  1. Calcule o Discriminante: **`Δ = b² - 4 · a · c`**
     - **`Δ > 0`** → **2 raízes reais distintas** (corta o eixo X duas vezes);
     - **`Δ = 0`** → **1 raiz real dupla** (encosta no eixo X num único ponto);
     - **`Δ < 0`** → **NÃO tem raízes reais** (não encosta no eixo X!).
  2. Fórmula de Bhaskara: **`x = (-b ± √Δ) / (2a)`**.
- **Vértice da Parábola (Máximo ou Mínimo exato):** **`x_v = -b / (2a)`** e **`y_v = -Δ / (4a)`** (ou apenas substitua o valor achado de `x_v` dentro da função `f(x)`!).

**💻 Exemplo Resolvido:** Para **`f(x) = x² - 5x + 6`**:
- `a = 1 (> 0 → boca p/ cima)`, `b = -5`, `c = 6`.
- `Δ = (-5)² - 4·(1)·(6) = 25 - 24 =` **`1`** *(como `1 > 0`, tem 2 raízes reais distintas!)*.
- `x = (5 ± √1) / 2` → **`x₁ = 3`** e **`x₂ = 2`**.
- Vértice (ponto mínimo): `x_v = 5 / 2 = 2,5`; `y_v = (2,5)² - 5·(2,5) + 6 = -0,25`.

#### 6. Geometria Plana, Teorema de Pitágoras Desenhado e Macete `3-4-5` *(M-Tec Q21)*
- **Fórmulas de Área para decorar:**
  - **Retângulo:** `A = base × altura` | **Triângulo:** `A = (base × altura) / 2`
  - **Trapézio:** `A = ((Base_maior + base_menor) × altura) / 2` | **Círculo:** `A = π · r²`
- **Teorema de Pitágoras (Só vale em Triângulo Retângulo, que tem um canto reto de `90°`!):**
  ```text
         |\
         | \  Hipotenusa (maior lado, sempre OPOSTO ao canto de 90°!)
   Cateto|  \               h² = cateto₁² + cateto₂²
    (30) |___\  (50)
         90°  Cateto (40)
  ```
  - **Macete Salvador `3-4-5`:** Viu um triângulo retângulo com catetos **`3` e `4`** (ou múltiplos como **`30` e `40`**, ou `6` e `8`)? Sem fazer nenhuma raiz quadrada gigante, a hipotenusa já fecha exata em **`5`** (`50`, ou `10`)! E a área é `(30 × 40) / 2 =` **`600 m²`**!
- **Terreno Composto *(M-Tec Q21)*:** Quebre a figura em um **Retângulo** + um **Triângulo** (ou Trapézio), calcule cada área e **some no final** (ex.: retângulo `40×43 = 1.720 m²` + triângulo `30×40/2 = 600 m²` = **`2.320 m²`**!).

---

### 📚 Parte 2 — Química do 1º Ano DO ZERO: Base Atômica, Ligações, Condutividade e Massa Molar *(M-Tec Q17–Q18)*

#### 1. Primeiro o Básico: Átomo, Metal, Ametal, Íon e Por Que Conduz Eletricidade!
Antes de decorar a tabela, entenda **a física simples por trás dela**:
- Um **átomo** tem núcleo positivo (`+`) e **elétrons** negativos (`-`) girando na casca externa (**camada de valência**). Para ficarem estáveis, os átomos buscam completar a última camada (em geral com 8 elétrons — *Regra do Octeto*):
  - **Metais** (Cobre, Ferro, Sódio, Ouro): têm poucos elétrons soltos na última camada → adoram **DOAR elétrons**!
  - **Ametais** (Cloro, Oxigênio, Carbono, Flúor): faltam poucos elétrons → adoram **RECEBER ou COMPARTILHAR elétrons**!
- **O que é um Íon?** Quando um átomo **perde ou ganha elétrons**, perde o equilíbrio elétrico:
  - Quem perdeu elétron negativo fica **positivo (`+`)** → chama-se **Cátion** (ex.: `Na⁺`).
  - Quem ganhou elétron negativo fica **negativo (`-`)** → chama-se **Ânion** (ex.: `Cl⁻`).
- **Por que algumas coisas conduzem eletricidade e outras não?**
  **Corrente elétrica = movimento livre de cargas elétricas!** Só acende uma lâmpada se existir **elétrons livres circulando** OU **íons positivos/negativos livres conseguindo nadar**!

| Ligação Química | Quem Junta e O Que Faz | Estado Físico & Estrutura | Conduz Eletricidade? *(DECORE PARA A Q18!)* |
| :--- | :--- | :--- | :--- |
| **1. Metálica** *(Metal + Metal)* | Átomos soltam seus elétrons externos criando um **"mar de elétrons móveis"** ligando tudo. | Ex.: Ferro (`Fe`), Cobre (`Cu`), Alumínio (`Al`), Ouro (`Au`) | **CONDUZ no estado SÓLIDO** e no líquido! *(Por isso fios de cobre sólido levam energia!)* |
| **2. Iônica** *(Metal + Ametal)* | Metal **DOA definitivamente** elétrons ao Ametal, formando **íons `+` e `-` presos em uma grade rígida (rede cristalina)**. | Ex.: Sal de cozinha (`NaCl`), Fluoreto (`NaF`), `CaO` | **NÃO conduz SÓLIDO** (os íons estão travados no cristal!), **MAS CONDUZ LÍQUIDO/FUNDIDO (derretido) ou DISSOLVIDO EM ÁGUA** *(pois a água ou calor solta os íons para nadar!)* |
| **3. Covalente / Molecular** *(Ametal + Ametal / H)* | Átomos **COMPARTILHAM pares de elétrons** em moléculas neutras, **SEM criar íons nem elétrons livres**! | Ex.: Açúcar (`C₁₂H₂₂O₁₁`), Álcool (`C₂H₅OH`), Água pura (`H₂O`), Oxigênio (`O₂`) | **NÃO conduz NEM SÓLIDO, NEM LÍQUIDO PURO!** *(Água pura destilada NÃO conduz — o que dá choque na água da torneira são sais minerais dissolvidos nela!)* |

> [!TIP]
> **Resumo em 5 segundos *(M-Tec Q18)*:**
> - Conduz já no estado **SÓLIDO**? → **Metal (Ligação Metálica)**.
> - **NÃO** conduz sólido, **MAS** conduz derretido (líquido) ou em água? → **Composto Iônico**.
> - **NÃO** conduz nem sólido nem líquido? → **Composto Molecular / Covalente**.

#### 2. Cálculo de Massa Molecular (`u`) / Massa Molar (`g/mol`) *(M-Tec Q17)*
Multiplique a massa de cada átomo (a prova sempre dá: **`H = 1`, `C = 12`, `N = 14`, `O = 16`**) pela quantidade de cada letra na fórmula:
1. **Etanol / Álcool Etílico (`C₂H₅OH`):**
   - `C`: `2 × 12 = 24`
   - `H`: `5 + 1 =` **`6` átomos × 1 = 6** *(Armadilha clássica: não esqueça do `H` isolado no final `OH`!)*
   - `O`: `1 × 16 = 16`
   - Total: `24 + 6 + 16 =` **`46 u`** (ou **`46 g/mol`**)!
2. **Ácido Acético / Vinagre (`C₂H₄O₂`):** `2(12) + 4(1) + 2(16) = 24 + 4 + 32 =` **`60 u`**!
3. **Dióxido de Carbono (`CO₂`):** `12 + 2(16) =` **`44 u`** | **Glicose (`C₆H₁₂O₆`):** `6(12) + 12(1) + 6(16) =` **`180 u`**.

---

### 📚 Parte 3 — Física (Óptica das Cores) & Biologia / Meio Ambiente *(M-Tec Q10–Q16 & Q33)*

#### 1. Física — Por que Enxergamos Cores? (Reflexão Seletiva da Luz) *(M-Tec Q33)*
A **luz branca do Sol** é **policromática** — ou seja, dentro dela existem todas as 7 cores juntas (vermelho, laranja, amarelo, verde, azul, anil, violeta). Um objeto opaco não tem "cor própria no escuro": a cor que enxergamos é **APENAS a cor de luz que ele CONSEGUE REFLETIR** de volta para nossos olhos (todas as outras são absorvidas!).

```text
  NO SOL (Luz Branca = todas as cores)        NUMA SALA SÓ COM LUZ VERDE (Monocromática!)
  Sol (V, L, Am, Vd, Az, An, Vi)              Lâmpada (APENAS Luz Verde)
       │                                           │
       ▼                                           ▼
  [ TOMATE VERMELHO ] ──(Reflete Vermelho!)   [ TOMATE VERMELHO ] ──(Absorve o Verde, NÃO reflete NADA!)
  Olho vê: VERMELHO!                          Olho vê: PRETO (ausência de luz refletida)!
```
- **Objeto Branco** (camisa branca): Reflete **TODAS** as cores que baterem nele → no Sol parece branco; sob luz verde pura parece **VERDE**; sob luz azul pura parece **AZUL**!
- **Objeto Preto** (camisa preta): Absorve **praticamente todas** as cores (por isso esquenta tanto no Sol!) e parece preto sob qualquer luz.

#### 2. Método Científico Passo a Passo *(M-Tec Q10)*
Como a ciência descobre a verdade sem "chute": imagine descobrir *por que uma planta da janela murchou*:
1. **Observação & Questionamento:** Olha a planta murcha e pergunta: *"Será falta de água ou falta de sol?"*
2. **Hipótese:** Uma resposta provisória que **possa ser testada** (*"Acho que ela murchou por falta de água"*).
3. **Experimentação Controlada:** Pega duas plantas idênticas: dá água a uma (**Grupo Teste**) e mantém a outra sem água igual estava (**Grupo Controle**) para comparar só aquela variável!
4. **Coleta e Análise de Dados:** Mede quantas folhas reergueram após 3 dias.
5. **Conclusão:** Confirma, ajusta ou rejeita a hipótese original (ciência aceita corrigir erros quando os dados mostram outra resposta!).

#### 3. Sustentabilidade, Aquecimento Global e Chuva Ácida *(M-Tec Q13–Q16)*
- **Desenvolvimento Sustentável:** Crescer atendendo às necessidades da geração atual **sem destruir** os recursos para as gerações futuras (equilíbrio ambiental, social e econômico).
- **Efeito Estufa Natural vs. Aquecimento Global:**
  - O **Efeito Estufa natural** é **BOM e necessário** — gases na atmosfera seguram parte do calor do Sol para a Terra não congelar à noite.
  - O problema é a **intensificação antrópica** (*"antrópica"* = **causada pela ação humana**): queimar gasolina/carvão e desmatar joga excesso de **`CO₂`** (gás carbônico) e **`CH₄`** (metano), prendendo calor demais → gerando o **Aquecimento Global**!
- **Protocolo de Kyoto (1997):** Acordo mundial que criou metas para países ricos reduzirem gases estufa e inventou os **créditos de carbono** (países/empresas que poluem demais podem investir/comprar créditos de projetos limpos que reduzem carbono em países em desenvolvimento).
- **Chuva Ácida & Tabelas CETESB (`SO₂`):** Gás dióxido de enxofre (**`SO₂`**) e óxidos de nitrogênio (`NOₓ`) liberados por indústrias/carros reagem com a água das nuvens gerando chuva ácida (corrói estátuas, solos e rios). Em questões com tabela da **CETESB**, leia sempre o ano, o poluente pedido e confira a unidade (`µg/m³`).

---

### 🕵️‍♂️ Dissecando Questões Reais da Prova M-Tec

#### Questão Resolvida 1 (Baseada em M-Tec 2022 Q18 & Q17 — Química)
*Três sólidos X, Y e Z foram testados: X não conduz sólido, mas conduz muito bem derretido; Y conduz corrente já no estado sólido; Z não conduz nem sólido nem líquido/em água. Classifique X, Y e Z:*
- **X** = Composto **Iônico**; **Y** = **Metálico**; **Z** = **Molecular / Covalente**.

#### Questão Resolvida 2 (Baseada em M-Tec 2022 Q23 & Q33 — Contagem e Óptica)
*1) Quantos números naturais de 3 algarismos distintos existem com `{0, 2, 4, 6, 8}`? 2) Num palco com luz monocromática azul, um cantor veste camisa amarela pura e calça branca: quais cores vemos?*
- **Contagem:** `0` não pode na 1ª casa (`4` opções: `2,4,6,8`); na 2ª casa entra o `0` e sai a usada (`4` opções); na 3ª sobram `3` → `4 × 4 × 3 =` **`48 números`**.
- **Óptica:** Camisa amarela absorve luz azul sem ter amarelo/vermelho/verde para refletir → parece **PRETA**; calça branca reflete tudo o que chega → parece **AZUL**!


---

## Dia 14 — Revisão Integrada Final, as 25 Pegadinhas da Banca FAT e Estratégia para 04/12

### 🎯 Juntando Todas as Peças dos 14 Dias Num Sistema Completo

Agora que você aprendeu cada tijolo do zero — da memória RAM ao HTML/CSS, do Portugol ao Banco de Dados, das Redes à Base Comum — pare 30 segundos para ver **tudo trabalhando junto** quando você abre o portal de estudos pelo navegador:

1. **No Design (Dia 8):** As cores da tela usam **RGB / `#Hexadecimal`**, os ícones nítidos são vetores **`.SVG`**, os rótulos colados nos campos aplicam **Proximidade (Gestalt)** e a interface usa palavras humanas (**Equivalência com o Mundo Real — Nielsen**).
2. **No Front-end Web (Dia 9) & Ecossistema (Dia 4):** A página usa **HTML5 Semântico** (`<header>`, `<main>`, `<form method="POST">` nas senhas!), estilo pelo **CSS3 Box Model** (`padding` interno, `margin` externo), alterada ao vivo pelo JavaScript na árvore **DOM** (empacotada via **Build/Bundling** e versionada no **Git** em equipe), guardando sua sessão num **Cookie local (~4 KB no navegador)**.
3. **Na Rede (Dia 11) & Hardware/SO (Dia 10):** Seu pedido vira pacotes na pilha **TCP/IP**, o **DNS** acha o **IP** do servidor, viaja protegido com cadeado **HTTPS (SSL/TLS)** passando por **Switch (Estrela)** e roteadores até chegar a servidores **Linux** (`/etc`, `/var/log`) rodando dentro de **Contêineres Docker** na nuvem **PaaS/IaaS**.
4. **No Back-end e Banco (Dias 1–7):** O código orientado a objetos (**4 Pilares da POO**, construído em **Scrum/XP**) valida tipos e **Casting** (`(int)` trunca!), consulta um banco relacional normalizado na **1FN** (1 valor por célula!) usando **DQL (`SELECT COUNT(*) WHERE...`)** e **DML (`INSERT`/`UPDATE`)**, e devolve sua resposta!

Você agora não tem dicas soltas — você entende o sistema inteiro de ponta a ponta!

---

### 🎮 Conexão Final: Sua Prova como uma *Speedrun* Estratégica em 3 Fases

Não tente responder da Q1 até a Q30 em linha reta travando 15 minutos na primeira questão de matemática ou matriz difícil! Faça em **3 passadas**:
- **Fase 1 (*Loot Rápido* — 1ª Passada):** Garante primeiro tudo que é rápido e certeiro (E-mail, Cookies, HTML, Frameworks, Licenças, Inglês, Barroco, Paleolítico/Neolítico, Ligação Química). Travou ou pediu tabela longa de cálculo? Circula o número na prova e **pula** — você volta já com pontos garantidos!
- **Fase 2 (*Chefões* — 2ª Passada):** Resolve com calma os Testes de Mesa, Matrizes, Binário/Hex, Contagem e Química **sempre escrevendo o passo a passo no rascunho**, sem "olhômetro".
- **Fase 3 (*Save Final* — 3ª Passada):** Confere questão por questão ao passar para o cartão-resposta e nunca entrega nenhuma bolinha em branco!

---

### 📚 Parte 1 — Dicionário Definitivo das 25 Pegadinhas da Fundação FAT

Releia esta tabela antes de ir para a prova. Quase 100% dos erros em itens I, II e III nascem de uma destas **25 armadilhas verbais**:

| Nº | Assunto | Mentira que a Banca Escreve (FUJA!) | Verdade Oficial da Prova |
| :---: | :--- | :--- | :--- |
| **1** | **Casting** | `(int) 7.99` vira `8` por arredondamento / chama-se *"Conversão Normal"*. | **TRUNCA (passa a tesoura)** na casa decimal → **`7`**! Só existem **Implícita** e **Explícita (*Casting*)**. |
| **2** | **Tipos** | `'A'` ou `12` usa tipo lógico (`bool`). | `'A'` usa **`char`**; `"texto"` usa **`string`**; **`bool`** guarda apenas **`true`/`false`**. |
| **3** | **DIV / MOD** | `17 MOD 5 = 3` e `17 DIV 5 = 2`. | **`DIV`** = quociente inteiro (**`3`**); **`MOD`** = **resto** da divisão (**`2`**). |
| **4** | **Teste de Mesa** | No `enquanto (x <= 6)`, no fim `x` ainda vale `6`. | O último passo acontece dentro da última volta! Só sai quando `x` vira **`7`** e o teste dá Falso! |
| **5** | **Matrizes** | Somar a diagonal secundária achando que é a principal. | Diagonal **Principal** é **`i == j`** (`[0][0], [1][1], [2][2]`). Secundária é `i + j == N - 1`. |
| **6** | **Pilha vs. Fila** | Em Pilha (`LIFO`), `POP` remove o primeiro que chegou. | Pilha = **LIFO** (`POP` tira o **ÚLTIMO** do topo). Fila = **FIFO** (sai o primeiro da frente). |
| **7** | **Frameworks** | *Creative Commons* ou *Adobe Creative Cloud* são frameworks. | Frameworks reais: **Bootstrap, Angular, Laravel (PHP), React Native**. Os outros são licença / suíte design! |
| **8** | **Editores** | Bloco de Notas (Notepad) é uma IDE completa. | Bloco de Notas = texto simples; **VS Code** = editor de código; **Visual Studio/Eclipse** = IDE; **Dreamweaver/Wix** = WYSIWYG. |
| **9** | **Licenças** | Todo Software Livre é obrigatoriamente grátis (`R$ 0`). | **Software Livre** garante **4 liberdades de código aberto** (pode ser vendido!). Grátis e fechado é ***Freeware***! |
| **10** | **Scrum & XP** | Scrum Master chefia tarefas; Pair Programming = 2 salas. | **SM** facilita/remove impedimentos; **PO** prioriza backlog; **Daily** <= 15 min; **Pair Programming** = **2 no mesmo PC**. |
| **11** | **POO** | Classe, Atributo e Método são os pilares da POO. | Os **4 Pilares** oficiais são: **Abstração, Encapsulamento, Herança e Polimorfismo**. |
| **12** | **SQL** | `DROP` é DML; `SELECT` é DDL; `COUNT(*)` vai no `WHERE`. | **DDL** = `CREATE/ALTER/DROP`; **DML** = `INSERT/UPDATE/DELETE`; **DQL** = `SELECT` (`COUNT(*)` vai no **`SELECT`**!). |
| **13** | **1FN & DER** | Dois telefones numa célula (`"111, 222"`) atende à 1FN. | Viola a **1ª Forma Normal (1FN)** (exige **valores atômicos**)! E `idade` calculada é atributo **derivado**. |
| **14** | **Cores** | RGB é para imprimir papel; `"CSS"` ou `"Primária"` é padrão de cor. | **RGB / Hex** = telas (luz); **CMYK** = impressão gráfica (tinta). |
| **15** | **Vetor / Bitmap** | `.JPEG` e `.PNG` são vetoriais que não borram no zoom. | **Vetorial** = **`.SVG` / `.PDF`** (matemática). **Bitmap** = `.JPEG`, `.PNG`, `.BMP` (pixels). |
| **16** | **Gestalt / UX** | Rótulo colado no campo é Fechamento; fonte *Script* serve p/ livro. | Perto = **Proximidade**; parecido = **Semelhança**. **Script** = letra cursiva (só títulos/convites!). |
| **17** | **Cookies** | Cookies são arquivos pesados salvos "na nuvem". | Cookies = **texto pequeno (~4 KB) salvo NO NAVEGADOR LOCAL do usuário** (sessão ou persistente)! |
| **18** | **HTML & CSS** | `<div>` é semântica; `<tr>` é célula; senha vai em `GET`. | **`<div>` é genérica**; **`<tr>`** = linha, **`<td>`** = célula; senha = **`POST`**; **`padding`** = interno, **`margin`** = externo. |
| **19** | **Binário / Hex** | `250` em hexadecimal dá `250` ou `F0`. | `250 ÷ 16` = `15(F)` resto `10(A)` = **`FA₁₆`** (`100` = `64₁₆`; `255` = `11111111₂` = `FF₁₆`). |
| **20** | **Linux Pastas** | `/mkdir`, `/ls`, `/rm`, `/cd` são diretórios do Linux. | São **COMANDOS**, não pastas! Pastas reais FHS: **`/bin, /etc, /home, /lib, /root, /usr, /var, /tmp`**. |
| **21** | **Docker vs. VM** | Contêiner Docker instala um sistema operacional completo novo dentro dele. | Contêiner **compartilha o Kernel** do hospedeiro (leve!); quem virtualiza SO inteiro é **VM + Hypervisor**. |
| **22** | **E-mail** | SMTP recebe/sincroniza e IMAP/POP3 envia. | **SMTP** = **Envia**; **POP3** = Baixa e apaga; **IMAP** = Sincroniza no servidor. |
| **23** | **Topologias** | Romper 1 cabo na Estrela derruba toda a rede. | Na **Estrela (Switch)** cai só aquele PC; quem derruba tudo se romper cabo único é **Barramento (*Bus*)**. |
| **24** | **Port / História** | Cultismo = ideias; Neolítico = nômade sem agricultura; Feudalismo = muita moeda. | **Cultismo** = palavras; **Conceptismo** = ideias; **Neolítico** = agricultura/sedentário; **Feudalismo** = agrário/sem moeda. |
| **25** | **Mat/Quím/Fís** | Dízima periódica é Irracional; Iônico conduz sólido; nº 3 dígitos começa com `0`. | Dízima = **Racional (`ℚ`)**; **Metal** conduz sólido, **Iônico** só líquido/aquoso; `0` proibido na 1ª casa; tomate sob luz verde = **PRETO**! |

---

### 📚 Parte 2 — Como Atacar Questões I, II e III em 15 Segundos + 3 Desafios Finais

#### Técnica Cirúrgica de Eliminação
1. Desconfie de **palavras radicais absolutas**: *"sempre", "nunca", "exclusivamente", "unicamente"* — costumam esconder um erro!
2. Encontre **1 único item com 100% de certeza FALSO** (por exemplo: *"Cookie fica armazenado na nuvem"* → FALSO!) e risque todas as alternativas de A a E que incluem esse número. Quase sempre restam apenas 2 letras!
3. Leia com calma apenas o item restante que decide entre as duas finalistas!

#### 🕵️‍♂️ 3 Questões Finais Dissecadas (Integrando Tudo)

**Desafio Final 1 (Integração SQL + HTML + Redes):**
*Analise: I. `ALTER TABLE usuarios ADD telefone VARCHAR(20)` é DDL. II. `<a href="pagina.html" target="_blank">` abre o link em nova aba mantendo a atual aberta. III. O protocolo IMAP baixa os e-mails e os exclui imediatamente do servidor.*
- **Análise:** I é V (ALTER mexe na estrutura = DDL). II é V (`_blank` = nova aba). **III é F** (quem apaga após baixar por padrão é o **POP3**; IMAP sincroniza mantendo no servidor). **Gabarito: Apenas I e II.**

**Desafio Final 2 (Integração Matriz + Lógica + Casting):**
*Dada `M = [[4, 2], [9, 6]]` e o código: `double media = (M[0][0] + M[1][1]) / 3.0; int final = (int) media;`. Qual o valor de `final` e o nome da conversão?*
- **Passo a passo:** `M[0][0] + M[1][1]` (diagonal principal!) = `4 + 6 = 10`. Divisão: `10 / 3.0 = 3.333...`. `(int) 3.333...` trunca para **`3`**, via **Conversão Explícita (*Type Casting*)**.

**Desafio Final 3 (M-Tec Base Comum — Matemática + Química):**
*Com `H=1, C=12, O=16`, calcule a massa molar de `C₂H₄O₂` e quantos números ímpares de 2 algarismos distintos podemos formar com `{0, 1, 2, 3}`.*
- **Química:** `C₂H₄O₂` = `2(12) + 4(1) + 2(16) = 24 + 4 + 32 =` **`60 g/mol`**.
- **Matemática:** Como pede **ímpar**, começamos pela restrição mais forte (**unidade** precisa ser `1` ou `3` → **2 opções**). Depois na **dezena**, não pode `0` nem o ímpar já usado na unidade (sobram **2 opções**). Total = `2 × 2 =` **`4 números`** (`13, 21, 23, 31`).

---

### 📚 Parte 3 — Plano do Dia da Prova (Sexta-feira, 04/12/2026)

1. **Na Quinta-feira à noite (03/12):**
   - Separe **RG/documento oficial original com foto**, comprovante de inscrição/local de prova, **2 canetas esferográficas pretas/azuis de corpo transparente** e garrafa de água sem rótulo;
   - Releia apenas a **Cola de Bolso** (aba *Apostila & Cola*) por 15 minutos e **durma pelo menos 8 horas** — cérebro descansado pega pegadinha na hora!
2. **Na hora da prova (04/12):**
   - Aplique a **Regra das 3 Passadas**, use **Teste de Mesa no rascunho** para qualquer código/matriz, confira o cartão-resposta número por número com calma e confie no quanto você se preparou! **Boa prova, Henrique!**

