# Guia Teórico Completo — Vagas Remanescentes Etec (2º Ano M-Tec / Desenvolvimento de Sistemas)

Este manual reúne **explicações completas passo a passo, contexto no mundo real, exemplos comentados linha a linha, quadros comparativos e questões dissecadas** cobrindo 100% do programa técnico (Fundação FAT / CPS) e da Base Comum do 1º ano M-Tec.

---

## Dia 1 — Raio-X da Banca Fundação FAT, Memória RAM, Tipos Primitivos, Casting, DIV/MOD e Lógica Proposicional

### 🎯 Contexto no Mundo Real: Por que você precisa dominar isso?

Imagine que você abre o sistema **NSA da Etec** ou faz um **Pix** no aplicativo do banco. Na tela do Pix aparece: nome do recebedor (`"Maria Oliveira"`), valor (`R$ 150.75`), chave (`11988887777`), tipo de conta (`'C'` para Corrente) e uma pergunta de confirmação (`temSaldoSuficiente = verdadeiro`).

Por trás dos panos, o computador **não enxerga "um recibo de Pix"** como um humano enxerga. Ele enxerga bilhões de interruptores microscópicos (`0` e `1`) na **memória RAM**. Para que o celular não tente "multiplicar o nome da Maria por 2" nem apague os centavos `0.75` na hora de transferir o dinheiro, o programador precisa ensinar à máquina **qual é o formato exato de cada informação** e **como tomar decisões lógicas** com segurança. É exatamente isso que a **Fundação FAT** cobra na abertura das provas de Desenvolvimento de Sistemas!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Se você já jogou algo online, olhou uma HUD no cantinho da tela ou configurou um bot no Discord, você já usou tudo o que cai no Dia 1 sem nem perceber:

- **Os 5 Tipos Primitivos na HUD de um Jogo:**
  - `hp = 100` → **`int`** (vida inteira, sem vírgula).
  - `kda = 2.45` → **`float` / `double`** (taxa de abates/mortes ou precisão com casas decimais).
  - `nick = "Henrique_BR"` → **`string`** (texto completo; se colocar `"100"` entre aspas, vira texto e **não** soma dano!).
  - `rank = 'S'` ou `time = 'A'` → **`char`** (uma única letra/símbolo sozinho).
  - `estaVivo = true` / `mutadoNoDiscord = false` → **`bool`** (liga/desliga: verdadeiro ou falso).
- **Casting no XP / Dano (`(int) 99.9`):** Se o jogo calcula dano crítico `99.9` e faz `(int) dano` para exibir na barra inteira, ele **corta o `.9` fora e mostra `99`** (trunca, não arredonda pra 100!).
- **`DIV` e `MOD` no Minecraft:** Você tem **150 blocos de ferro** e um pack fecha em **64**. Quantos packs cheios dá? `150 DIV 64 =` **`2 packs`**! E quantos blocos ficam soltos no último slot? `150 MOD 64 =` **`22 itens`**!
- **Tabela Verdade na Fila Ranqueada:** Regra do servidor para puxar Ranked: `(nivel >= 20) E (ping < 60 OU servidor == "BR") E NAO estaBanido`. Basta você estar banido (`NAO true = false`) para o **`E`** bloquear sua entrada na partida inteira!

---

### 📚 Parte 1 — Os 4 Moldes Secretos da Banca Fundação FAT

Antes de estudar os conteúdos técnicos, você precisa conhecer o **estilo da banca examinadora** (Fundação FAT / CPS). Analisando provas oficiais anteriores (DS 2025, Info 2025, DS 2019 e M-Tec 2022), praticamente 100% das questões técnicas caem em apenas **4 moldes previsíveis**:

| Molde da Banca | Como a Questão Aparece | Estratégia de Resolução em Segundos |
| :--- | :--- | :--- |
| **Molde 1 — Afirmativas I, II e III** | Apresenta 3 frases (frequentemente ligadas a uma tabela de termos) e pergunta quais estão corretas. | **9 em cada 10 vezes**, a banca pega duas definições e **troca uma pela outra** (ex.: diz que DDL faz `SELECT` e DQL faz `CREATE`, ou diz que Cookie fica na nuvem). Ache uma falsa e elimine 2 ou 3 alternativas (A–E) logo de cara! |
| **Molde 2 — Lista com Intruso** | *"Assinale a alternativa que apresenta APENAS [frameworks / navegadores / pastas Linux / padrões de cores]."* | Todas as 4 alternativas erradas têm **1 único item intruso** escondido no meio de itens verdadeiros (ex.: pôr `Creative Commons` entre frameworks, ou `/mkdir` entre diretórios Linux). |
| **Molde 3 — Definição Direta / Cenário** | Descreve um problema real de projeto e pede o termo oficial da engenharia/SQL/rede. | Busque palavras-gatilho no enunciado: *"sem perder nitidez no zoom"* = SVG/Vetor; *"forçada manualmente pelo dev"* = Casting explícito; *"sincroniza no servidor"* = IMAP. |
| **Molde 4 — Micro-Execução (Na Mão)** | Mostra 5 a 10 linhas de Portugol/JS/SQL/Binário ou uma Matriz 3×3 e pede a saída final. | Nunca tente fazer de cabeça! Desenhe a tabela de **teste de mesa** no rascunho e acompanhe linha por linha até o fim do laço. |

---

### 📚 Parte 2 — Como Variáveis Vivem na Memória RAM e os 5 Tipos Primitivos

Quando um programa está rodando, a **Memória RAM (*Random Access Memory*)** funciona como um armário gigante cheio de gavetas numeradas (endereços de memória). Criar uma **variável** significa **reservar uma gaveta**, dar a ela um **rótulo (identificador)** — por exemplo `idade` — e colar nela uma **etiqueta de tipo**.

**Por que a etiqueta de tipo existe?**
1. **Tamanho em bytes:** Um número inteiro comum costuma ocupar 4 bytes (32 bits), enquanto um número decimal de dupla precisão (`double`) ocupa 8 bytes (64 bits), e um único caractere (`char`) ocupa apenas 1 ou 2 bytes.
2. **Significado dos zeros e uns:** A mesma sequência binária na RAM pode significar o número `65` (se a etiqueta for `int`) ou a letra `'A'` na tabela **ASCII** (se a etiqueta for `char`)!
3. **Operações permitidas:** Só faz sentido calcular raiz quadrada em números, e só faz sentido transformar em maiúsculas em textos.

Conheça os **5 Tipos Primitivos Oficiais** exigidos pela Etec:

| Tipo Técnico | Outros nomes na prova | O que armazena na memória | Exemplos válidos | Armadilha comum |
| :--- | :--- | :--- | :--- | :--- |
| **Inteiro (`int`)** | `integer`, `Inteiro` (Portugol) | Apenas números sem parte fracionária (positivos, negativos ou `0`). | `0`, `16`, `-2026`, `4096` | Divisão inteira entre dois `int` em C/Java (`5 / 2`) resulta em **`2`**, descartando o `.5`! |
| **Real (`float` / `double`)** | Ponto Flutuante, `Real` (Portugol) | Números com casas decimais (precisão simples `float` ou dupla `double`). | `3.14`, `7.5`, `-0.001`, `10.0` | Em programação usa-se **ponto (`.`)**, nunca vírgula (`,`). `10.0` ocupa memória como decimal, mesmo sendo redondo! |
| **Caractere (`char`)** | `Caractere` (um único símbolo) | **Exatamente 1 único caractere** (uma letra, um dígito isolado ou um símbolo de pontuação). | `'A'`, `'m'`, `'7'`, `'@'`, `' '` | Em C/Java vem entre **aspas simples (`'A'`)**. A banca FAT adora perguntar qual tipo guarda uma alternativa `'A'`–`'E'` ou `'M'`/`'F'`! |
| **Texto (`string`)** | `Cadeia`, `Literal`, `varchar` (SQL) | Sequência de **0, 1 ou muitos caracteres** juntos em cadeia. | `"Etec DS"`, `"12345"`, `""` (vazia) | `"123"` entre aspas é **TEXTO (`string`)**, NÃO número! Se somar `"10" + "20"`, vira `"1020"` (**concatenação**). |
| **Booleano (`bool`)** | `Lógico` (Portugol), `boolean` | Exclusivamente dois estados lógicos binários. | `true` (`Verdadeiro`) ou `false` (`Falso`) | Não usa aspas! `"true"` entre aspas é uma `string` de 4 letras, não um booleano! |

> [!WARNING]
> **Pegadinha clássica da FAT (INFO 2025 Q19):** A questão pergunta qual tipo primitivo armazena adequadamente um caractere isolado (como `'S'` ou `'N'`, ou uma letra `'B'`). Resposta oficial: **`char` / Caractere** (e **NUNCA** `boolean`, que só guarda `true`/`false`, nem `float`, que guarda decimais!).

---

### 📚 Parte 3 — Conversão Implícita (*Coerção*) vs. Conversão Explícita (*Type Casting*)

Na vida real de um sistema, frequentemente temos um dado em um tipo e precisamos dele em outro. Por exemplo: o usuário digita a idade no formulário HTML (tudo que vem do teclado na web chega como **texto `string`** `"16"`), mas o sistema precisa somar `+ 1` matematicamente. Como os tipos são convertidos? Existem **dois mecanismos oficiais**:

#### 1. Conversão Implícita (*Coerção Automática*)
Acontece **sozinha nos bastidores**, feita automaticamente pelo compilador ou interpretador **sem que o programador escreva comando de conversão**.
- **Regra em linguagens tipadas (C, Java, C#):** Ocorre na **promoção de um tipo menor para um tipo maior**, onde **não existe risco de perder dados**. Um `int` cabe confortavelmente dentro de um `double`.
  - `int pontos = 10;`
  - `double bonus = pontos;` → O computador converte `10` para `10.0` automaticamente! Ninguém precisou mandar.
- **Em linguagens dinâmicas (JavaScript):** Se você soma número com string (`"Nota: " + 9`), o JS converte `9` em `"9"` implicitamente e junta tudo em `"Nota: 9"`.

#### 2. Conversão Explícita (*Type Casting*)
Acontece quando **o programador escreve explicitamente uma instrução no código forçando a mudança de tipo**. Ela é obrigatória sempre que houver **risco de perda de informação** (por exemplo, transformar um número com casas decimais em inteiro) ou conversão texto ↔ número.
- **Em C / Java / C#:** Coloca-se o tipo desejado entre parênteses antes da variável: `(int) valor`.
- **Em Python / JavaScript:** Usam-se funções de conversão explícita como `int("16")`, `float("7.5")`, `Number("42")`, `parseInt("42")`, `String(100)`.

#### 💻 Exemplo Real Comentado Linha a Linha (O Perigo do Truncamento!)
Veja este trecho clássico estilo prova em C/Java:

```java
double mediaOriginal = 8.95;          // Linha 1: guarda exatamente 8.95 na RAM (8 bytes)
int notaInteira = (int) mediaOriginal;// Linha 2: CASTING EXPLÍCITO! O dev forçou virar int
double notaPromovida = notaInteira;   // Linha 3: CONVERSÃO IMPLÍCITA! int -> double automático

System.out.println(notaInteira);      // Imprime: 8
System.out.println(notaPromovida);    // Imprime: 8.0
```

> [!CAUTION]
> **PEGADINHA MORTAL DA PROVA (DS 2025 Q8):**
> 1. `(int) 8.95` **TRUNCA (corta fora)** a parte decimal `.95`, resultando em **`8`**, e **JAMAIS arredonda para `9`**! Mesmo que seja `9.999`, `(int) 9.999` vira **`9`**.
> 2. A banca inventa nomes falsos como *"Conversão Normal"*, *"Conversão Indireta"* ou *"Conversão Manual Automática"*. Os únicos nomes oficiais são **Implícita** (feita pelo compilador sem perda) e **Explícita / Casting** (forçada pelo programador)!

---

### 📚 Parte 4 — Operadores Aritméticos, `DIV` (Quociente) e `MOD` (Resto)

Além das 4 operações tradicionais (`+`, `-`, `*`, `/`), provas técnicas adoram testar dois irmãos inseparáveis da divisão inteira:

- **`DIV` (em Portugol/Pascal) ou `//` (em Python):** Devolve **apenas a parte inteira do quociente** (quantas vezes o divisor cabe inteiro dentro do dividendo).
- **`MOD` (em Portugol/SQL) ou `%` (em C/Java/JS/Python):** Devolve **apenas o resto inteiro** da divisão que sobrou sem conseguir formar mais um grupo inteiro.

#### 💻 Exemplo Real #1: Caixa Eletrônico Distribuindo Notas
Suponha que um estudante saque **`R$ 137`** e o caixa tenha notas de `R$ 50`, `R$ 20` e moedas de `R$ 1`:

```portugol
valor <- 137
notas50 <- valor DIV 50      // 137 / 50 dá 2 e sobra 37 -> notas50 = 2
sobra   <- valor MOD 50      // O que sobrou após tirar as notas de 50 -> sobra = 37

notas20 <- sobra DIV 20      // 37 / 20 dá 1 e sobra 17 -> notas20 = 1
sobra   <- sobra MOD 20      // O resto agora é 17 -> sobra = 17
```

#### 💻 Exemplo Real #2: Convertendo Segundos em Horas e Minutos (`3665` segundos)
- `horas <- 3665 DIV 3600` → **`1` hora** (`1 × 3600 = 3600`).
- `restoSeg <- 3665 MOD 3600` → sobram **`65` segundos**.
- `minutos <- 65 DIV 60` → **`1` minuto**.
- `segFinais <- 65 MOD 60` → **`5` segundos**! (`01h 01m 05s`).

#### Aplicações Favoritas da Banca FAT com `MOD`:
1. **Teste de Par ou Ímpar:** Todo número par dividido por `2` deixa resto `0` (`N MOD 2 == 0`). Todo ímpar deixa resto `1` (`N MOD 2 == 1`).
2. **Teste de Múltiplo / Ano Bissexto:** `numero MOD 5 == 0` verifica se é múltiplo de 5.
3. **Conversão Decimal → Binário (DS 2019 Q2):** Dividir sucessivamente por `2` pegando `n MOD 2` (o dígito binário `0` ou `1`) e atualizando `n <- n DIV 2` até `n` chegar a `0`!

**Ordem de Precedência Matemática (quem calcula antes de quem):**
1º Parênteses `()` (de dentro para fora) → 2º Potenciação/Raiz → 3º Multiplicação (`*`), Divisão (`/`), `DIV` e `MOD` (da esquerda para a direita) → 4º Soma (`+`) e Subtração (`-`) → 5º Relacionais (`>`, `>=`, `<`, `<=`, `==`, `!=`) → 6º Lógicos (`NÃO` → `E` → `OU`).

---

### 📚 Parte 5 — Lógica Proposicional, Operadores Lógicos e Tabela Verdade

Uma **proposição lógica** é uma afirmação que pode ser julgada exclusivamente como **Verdadeira (`V` / `true`)** ou **Falsa (`F` / `false`)**. Conectamos proposições com 3 operadores fundamentais:

| Operador | Símbolo Matemático | Símbolo em Código (C/Java/JS) | Regra de Funcionamento Real | Analogia Prática |
| :--- | :---: | :---: | :--- | :--- |
| **NÃO (Negação)** | `¬P` | `!P` / `not P` | **Inverte** o valor lógico (`V` vira `F`; `F` vira `V`). | Interruptor inversor |
| **E (Conjunção)** | `P ∧ Q` | `P && Q` / `and` | **Exigente:** Só resulta em **`V`** se **AMBOS** forem **`V`**. Um único `F` derruba tudo para `F`! | **Porta com 2 cadeados em série:** precisa das **2 chaves** para abrir |
| **OU (Disjunção)** | `P ∨ Q` | `P \|\| Q` / `or` | **Flexível:** Resulta em **`V`** se **PELO MENOS UM** for **`V`**. Só dá `F` se **TODOS** forem `F`! | **Casa com 2 portas (frente e fundos):** se pelo menos 1 destrancar, você entra |

#### Tabela Verdade Completa (Memorize visualmente!)

| `P` | `Q` | `¬P` (`NÃO P`) | `P ∧ Q` (`P E Q`) | `P ∨ Q` (`P OU Q`) |
| :---: | :---: | :---: | :---: | :---: |
| **V** | **V** | F | **V** | **V** |
| **V** | **F** | F | **F** | **V** |
| **F** | **V** | V | **F** | **V** |
| **F** | **F** | V | **F** | **F** |

#### 💻 Exemplo Real de Regra de Negócio na Etec
Para passar direto de ano na Etec sem recuperação, o aluno precisa ter **nota maior ou igual a 6** **E** **não** ter mais que 25% de faltas (`faltas <= 25`), **OU** ganhar aprovação especial do conselho (`conselho == true`).
Suponha um aluno com `nota = 7.5`, `faltas = 30`, `conselho = false`:
Expressão: `((nota >= 6) E NAO (faltas > 25)) OU conselho`
1. `nota >= 6` → `7.5 >= 6` → **`V`**
2. `faltas > 25` → `30 > 25` → **`V`**
3. `NAO (faltas > 25)` → `NAO V` → **`F`** *(lembre: `NÃO` executa antes do `E`!)*
4. `V E F` → **`F`** *(reprovou no critério principal por causa das faltas!)*
5. `F OU conselho` → `F OU F` → **`F`** (Reprovado).

> [!TIP]
> **Leis de De Morgan (bônus para pegadinhas de negação):**
> - Negar "`P E Q`" não é "`não P E não Q`"! É **`(não P) OU (não Q)`**! *(Ex.: negar "fui à escola E fiz a prova" significa "NÃO fui à escola OU NÃO fiz a prova")*.
> - Negar "`P OU Q`" resulta em **`(não P) E (não Q)`**.

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q8 — Conversão de Tipos)
*Um desenvolvedor Java escreveu `double preco = 49.99; int inteiro = (int) preco;` e, em seguida, `double copia = inteiro;`. Sobre essas operações, avalie:*
- *I. Na segunda instrução ocorreu uma conversão implícita com arredondamento para 50.*
- *II. Na segunda instrução ocorreu um type casting explícito que truncou o valor para 49.*
- *III. Na terceira instrução (`double copia = inteiro;`) o compilador realizou conversão implícita sem perda de dados.*

**Análise:**
- **Item I é FALSO:** Há duas inverdades! Primeiro, `(int) preco` não é implícita (o dev escreveu `(int)`, logo é explícita/casting); segundo, *casting* **trunca** para `49`, nunca arredonda para `50`.
- **Item II é VERDADEIRO:** `(int) preco` é explícito (*type casting*) e descarta a fração `.99`, deixando `49`.
- **Item III é VERDADEIRO:** Passar `int` para `double` amplia a capacidade sem perda; o compilador converte `49` para `49.0` automaticamente (implícita).
**Resposta:** Apenas **II e III** estão corretas.

#### Questão Resolvida 2 (Baseada em INFO 2025 Q20 & DS 2019 Q1 — Tabela Verdade)
*Considere `P = Verdadeiro`, `Q = Falso` e `R = Verdadeiro`. Qual é o resultado lógico da expressão `(P E Q) OU (NAO Q E R)`?*

**Passo a passo:**
1. Primeiro os parênteses da esquerda: `P E Q` = `V E F` = **`F`**.
2. Agora o parêntese da direita: `NAO Q` = `NAO F` = **`V`**. Em seguida `V E R` = `V E V` = **`V`**.
3. Por último o `OU` externo ligando os dois resultados: `F OU V` = **`V` (Verdadeiro)**!


---

## Dia 2 — Algoritmos, Fluxogramas Oficiais, Decisão Encadeada, Laços de Repetição e Teste de Mesa

### 🎯 Contexto no Mundo Real: O Raciocínio Antes do Código

Antes de um arquiteto erguer um prédio de 20 andares, ele desenha a planta baixa. Na computação, antes de escrever centenas de linhas de Python, JavaScript ou C#, nós desenhamos a lógica da solução usando um **Algoritmo**.

Pense no GPS do celular calculando uma rota até a Etec, ou no aplicativo do iFood conferindo se há entregador disponível, aplicando cupom de desconto, somando o frete e repetindo a verificação de estoque para cada item do carrinho. Tudo isso é formado por **sequência, decisão ("se/senão") e repetição ("enquanto houver itens")**. Se você não dominar a ordem em que a CPU percorre essas linhas, vai cair nas armadilhas do **Teste de Mesa**, que sempre aparece nas provas da Fundação FAT!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Todo jogo que você abre roda um laço de repetição gigante nos bastidores (o famoso ***Game Loop***):

- **Fluxograma = Árvore de Diálogo de RPG / Missão:** O Losango ◇ é aquela encruzilhada de diálogo (*"Você tem a chave da masmorra? Sim → abre o baú / Não → volta para o NPC"*); o Retângulo ▭ é o cálculo de dano; o Paralelogramo ▱ é ler sua tecla `WASD` e desenhar os frames na tela.
- **`while` (Pré-teste) = `while (hp > 0)`:** Enquanto tiver vida, você continua jogando. Se já entrar na arena com `hp == 0`, o laço roda **0 vezes** (nem começa!).
- **`do...while` (Pós-teste) = Tela de *Respawn / Continue?*:** Primeiro você vê o menu *"Jogar Novamente? (S/N)"* **pelo menos 1 vez garantida**, e só no final o programa checa se você clicou em Não para sair.
- **`for` = Varrer os *slots* da mochila:** Quando você sabe que o inventário tem exatamente `10` espaços (`i` de `0` até `9`), usa o `para/for` para checar item por item.
- **Teste de Mesa = Reconstruir uma luta de Boss turno a turno:** Em vez de tentar adivinhar quanto de HP sobrou de cabeça, você anota `turno 1`, `turno 2`, `turno 3` numa tabelinha no papel até o boss cair — impossível errar conta simples assim!

---

### 📚 Parte 1 — O que é um Algoritmo e os Símbolos do Fluxograma

Um **algoritmo** é uma sequência **finita, ordenada e não ambígua** de instruções lógicas para transformar entradas em saídas esperadas. Todo programa segue a tríade clássica **E → P → S**:
1. **Entrada (*Input*):** Receber dados externos (teclado, mouse, sensor, banco de dados).
2. **Processamento (*Processing*):** Calcular, comparar, ordenar e transformar dados na CPU/RAM.
3. **Saída (*Output*):** Devolver o resultado ao usuário ou a outro sistema (tela, impressora, arquivo).

Podemos escrever um algoritmo de três formas: **Descrição Narrativa** (português comum), **Pseudocódigo / Portugol** (parecido com código) e **Fluxograma** (diagrama gráfico padrão ANSI/ISO).

#### Os 4 Símbolos Geométricos que a Banca Cobra Literalmente

| Desenho / Símbolo | Nome Oficial | Função Exata no Fluxograma | Exemplo Real dentro da Caixa |
| :--- | :--- | :--- | :--- |
| **⬭ Oval / Elipse / Cápsula** | **Terminal** | Marca obrigatoriamente apenas o **`Início`** e o **`Fim`** do algoritmo. | `Início` ou `Fim` |
| **▱ Paralelogramo** | **Entrada / Saída (E/S)** | Interação externa: **ler** dados do teclado ou **exibir** resultados na tela. | `Ler nota1, nota2` / `Escrever media` |
| **▭ Retângulo** | **Processamento** | **Contas matemáticas, atribuições de variáveis** e ações internas da máquina. | `media <- (nota1 + nota2) / 2` |
| **◇ Losango** | **Decisão / Condicional** | Avalia uma condição booleana (`V` ou `F`). **Sempre tem 1 seta entrando e 2 setas saindo (`Sim` / `Não`).** | `media >= 6.0?` |

*(Obs.: Pequenos círculos chamam-se **conectores** e setas indicam o **fluxo de execução**).*

#### 💻 Exemplo Real de Fluxograma Completo (Aprovação de Empréstimo)
```text
[ ⬭ Início ]
     ↓
[ ▱ Ler renda, parcela ]
     ↓
[ ▭ limite <- renda * 0.30 ]
     ↓
[ ◇ parcela <= limite? ] ──(NÃO)──→ [ ▱ Escrever "Crédito Negado" ] ──┐
     │ (SIM)                                                           │
     ↓                                                                 ↓
[ ▱ Escrever "Crédito Aprovado" ] ────────────────────────────────→ [ ⬭ Fim ]
```

> [!WARNING]
> **Pegadinha clássica:** Nunca marque que **Retângulo** serve para decidir (`se/senão`), nem que **Losango** faz cálculos (`soma = a + b`). **Processamento/Atribuição = Retângulo**; **Condicional/Decisão = Losango**; **Ler/Imprimir = Paralelogramo**.

---

### 📚 Parte 2 — Estruturas de Decisão: Simples, Composta e Encadeada

#### 1. Decisão Simples (`se`) vs. Composta (`se ... senao`)
- **Simples:** Executa um bloco apenas se for verdadeiro; se falso, não faz nada e segue em frente (`se saldo < 0 entao avisar()`).
- **Composta:** Oferece dois caminhos excludentes: se `V`, executa o bloco do `se`; se `F`, obrigatoriamente executa o bloco do `senao`. **Nunca os dois juntos!**

#### 2. A Pegadinha do Encadeamento (`se ... senao se` vs. Vários `se` Seguidos!)
Compare estes dois códigos reais supondo `nota = 9.0`:

**Código A — Condicional Encadeado (`else if`):**
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
Como `9.0 >= 9.0` dá **Verdadeiro** no primeiro `if`, `conceito` vira **`"MB"`** e o programa **PULA** todos os `else if` abaixo! Mesmo `9.0` sendo `>= 7.0` e `>= 5.0`, eles nem são testados!

**Código B — Múltiplos `if` Independentes (Erro clássico de iniciante!):**
```javascript
if (nota >= 9.0) { conceito = "MB"; }   // Testa -> V! conceito = "MB"
if (nota >= 7.0) { conceito = "B"; }    // Testa de novo -> V! SOBRESCREVE para "B"!
if (nota >= 5.0) { conceito = "R"; }    // Testa de novo -> V! SOBRESCREVE para "R"!
```
No Código B, um aluno nota 9 receberia `"R"` porque os três `if` são independentes e cada um foi apagando a variável! **A banca adora colocar dois ou três `if` sem `else` em questões de saída na tela!**

---

### 📚 Parte 3 — Estruturas de Repetição (Laços / *Loops*) Sem Confusão

Quase todo laço funcional precisa de **3 pilares** (se esquecer o 3º, o programa trava em **loop infinito**!):
1. **Inicialização** da variável de controle antes ou no cabeçalho (`i <- 1`);
2. **Condição de continuação ou parada** (`enquanto i <= 5`);
3. **Atualização / Incremento** dentro do corpo (`i <- i + 1`).

| Estrutura | Momento do Teste | Mínimo de Execuções | Regra Lógica / Idioma | Caso de uso real |
| :--- | :--- | :---: | :--- | :--- |
| **`enquanto ... faca` / `while`** | **Pré-teste** (testa **antes** de entrar) | **0 vezes** (se já começar falsa, nem entra no bloco!) | Repete **ENQUANTO** a condição for **VERDADEIRA**. | Ler registros enquanto não chegar ao fim do arquivo; validar senha. |
| **`do ... while`** (C, Java, JS, PHP) | **Pós-teste** (executa primeiro, testa **no final**) | **Pelo menos 1 vez garantida!** | Repete **ENQUANTO** a condição final for **VERDADEIRA**. | Menu interativo que precisa aparecer ao menos 1 vez na tela. |
| **`repita ... ate`** (Portugol / Pascal) | **Pós-teste** (executa primeiro, testa **no final**) | **Pelo menos 1 vez garantida!** | **Atenção:** Repete **ATÉ QUE** a condição fique **VERDADEIRA** (ou seja, **repete enquanto for FALSA e PARA quando der `V`**!). | Pedir idade até que digite um valor `> 0`. |
| **`para ... de ... ate ... faca` / `for`** | **Pré-teste contado** | **0 ou N vezes** | Contador automático (`inicio`, `fim`, `passo`). | Percorrer vetores e matrizes de tamanho conhecido. |

> [!CAUTION]
> **Pegadinha de Ouro (Apostas Q9 & Portugol):**
> - No `while (x < 0)`, se `x = 5`, o bloco roda **0 vezes**.
> - No `do { ... } while (x < 0)`, se `x = 5`, o bloco roda **1 vez inteira** antes de testar `5 < 0` e parar!
> - E no Portugol **`repita ... ate (x == 5)`**: ele **continua** quando `x != 5` e **sai** quando `x` vira `5` (exatamente o inverso do `do...while`!).

---

### 📚 Parte 4 — Teste de Mesa Passo a Passo (O Método Anti-Erro)

**Teste de Mesa** (*Trace* ou *Dry Run*) é a técnica de simular o processador manualmente executando cada instrução e preenchendo uma tabela com uma coluna para cada variável e uma coluna para a condição/saída.

**Regras sagradas para fazer no rascunho da prova:**
1. Nunca confie na memória: **risque** o valor antigo quando uma variável for atualizada (`x <- 2` → risca o `2` e escreve `4`).
2. Na troca de valores entre duas variáveis (`A` e `B`), é **obrigatório** usar uma 3ª variável auxiliar:
   - `aux <- A; A <- B; B <- aux;`
   - Se fizer `A <- B; B <- A;` sem `aux`, o valor original de `A` é perdido para sempre e ambos ficam iguais a `B`!
3. Fique atento ao **último incremento** antes de o laço terminar!

#### 💻 Exemplo Real Comentado #1: Acumulador + Filtro + Contador
Veja o algoritmo em Portugol que calcula a soma dos múltiplos de 3 entre 1 e 10 e conta quantos laços foram rodados:

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

**Tabela do Teste de Mesa Linha por Linha:**

| Momento / Passo | Teste `cont <= 7`? | Teste `cont MOD 3 == 0`? | `soma` | `achados` | `cont` (após `cont + 2`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Inicialização** | — | — | `0` | `0` | `1` |
| **Volta 1 (`cont=1`)** | `1 <= 7` (**V** entra) | `1 % 3 = 1` (**F** pula `se`) | `0` | `0` | `1 + 2 = 3` |
| **Volta 2 (`cont=3`)** | `3 <= 7` (**V** entra) | `3 % 3 = 0` (**V** entra `se`!) | `0 + 3 = 3` | `1` | `3 + 2 = 5` |
| **Volta 3 (`cont=5`)** | `5 <= 7` (**V** entra) | `5 % 3 = 2` (**F** pula `se`) | `3` | `1` | `5 + 2 = 7` |
| **Volta 4 (`cont=7`)** | `7 <= 7` (**V** entra) | `7 % 3 = 1` (**F** pula `se`) | `3` | `1` | `7 + 2 = 9` |
| **Volta 5 (`cont=9`)** | `9 <= 7` (**F** SAI!) | *(não executa)* | **`3`** | **`1`** | **`9`** |

**Saída impressa:** `soma = 3`, `achados = 1`, **`cont = 9`**!
Perceba como `cont` virou **`9`** no final da Volta 4 antes de falhar no teste `9 <= 7`. Quem para no `7` cai no distrator clássico da banca!

#### 💻 Exemplo Real Comentado #2: Teste de Mesa com `para` (*for*) + Variável Auxiliar
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
- **`i = 1` (`1 <= 4` V):** `prox = 2`, `a = 1`, `b = 2` → depois `i` vira `2`
- **`i = 2` (`2 <= 4` V):** `prox = 1 + 2 = 3`, `a = 2`, `b = 3` → `i` vira `3`
- **`i = 3` (`3 <= 4` V):** `prox = 2 + 3 = 5`, `a = 3`, `b = 5` → `i` vira `4`
- **`i = 4` (`4 <= 4` V):** `prox = 3 + 5 = 8`, `a = 5`, `b = 8` → `i` vira `5` (sai!)
- **Saída:** `a = 5`, `b = 8` (sequência de Fibonacci!).

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Estilo Molde 4 — Teste de Mesa com `DS 2025 Q9`)
*Analise o algoritmo:* `x <- 10; y <- 4; enquanto (x > y) faca { x <- x - 2; y <- y + 1; } escreva(x, y);` *Quais valores serão impressos?*

**Tabela rápida:**
- Início: `x = 10`, `y = 4`.
- Volta 1: `10 > 4` (V) → `x` vira `8`, `y` vira `5`.
- Volta 2: `8 > 5` (V) → `x` vira `6`, `y` vira `6`.
- Volta 3: `6 > 6` (**F!** Pois é estritamente `>`, não `>=`!) → **SAI DO LAÇO!**
**Gabarito:** Imprime **`x = 6` e `y = 6`**. *(Pegadinha: muita gente acha que `6 > 6` ainda entra e marca `x = 4, y = 7`!).*

#### Questão Resolvida 2 (Estilo Molde 1 — Símbolos de Fluxograma & Laços)
*Julgue os itens:*
- *I. No fluxograma padrão, o retângulo representa entrada e saída de dados via teclado/tela.*
- *II. A estrutura `do...while` garante que o bloco interno será executado pelo menos uma vez, pois o teste ocorre ao final.*
- *III. Se a condição inicial de um laço `while` for falsa desde a primeira leitura, suas instruções internas nunca serão executadas.*

**Análise:**
- **Item I é FALSO:** Entrada e saída usam o **paralelogramo**; o retângulo representa **processamento/atribuições**.
- **Item II é VERDADEIRO:** Pós-teste sempre roda ao menos 1 vez.
- **Item III é VERDADEIRO:** Pré-teste barra na entrada se já nascer falso.
**Gabarito:** Apenas **II e III**.


---

## Dia 3 — Vetores (1D), Matrizes Bidimensionais `[i][j]`, Pilha (LIFO), Fila (FIFO) e Recursividade

### 🎯 Contexto no Mundo Real: Tabuleiros, Carrinhos e a Pilha do "Ctrl+Z"

Imagine fazer um sistema para guardar as 40 notas de uma turma da Etec criando 40 variáveis chamadas `nota1`, `nota2`, ..., `nota40`. Além de trabalhoso, seria impossível usar um laço `for` para calcular a média! Ou imagine representar uma planilha do Excel, uma imagem digital em pixels ou o tabuleiro de um jogo da velha `3 × 3`. Para isso existem as **estruturas de dados indexadas homogêneas** (Vetores e Matrizes), capazes de armazenar dezenas ou milhões de valores sob um único nome na memória.

Além delas, softwares reais dependem de regras rígidas sobre **quem sai primeiro**: quando você aperta **`Ctrl+Z`** no VS Code ou clica em **Voltar** no navegador, o sistema desfaz a **última** ação que você fez (uma **Pilha**). Já quando cinco pessoas mandam imprimir PDFs na impressora da escola, quem enviou **primeiro** imprime **primeiro** (uma **Fila**). Ambas caem com enorme frequência nas provas da FAT!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Você já usa vetores, matrizes, filas e pilhas toda vez que abre o PC:

- **Vetor 1D (Base `0`) = Barra de Atalhos (*Hotbar*) numerada no inventário:** Imagine 5 slots chamados `hotbar`: em programação, o primeiro slot é `hotbar[0]` (Espada), depois `[1]` (Arco), `[2]` (Picareta), `[3]` (Bloco) e o último é `hotbar[4]` (Poção). Se tentar acessar `hotbar[5]`, dá erro porque foi de `0` a `N-1`!
- **Matriz 2D `M[linha][coluna]` = Minimapa / Tabuleiro / Inventário em Grade:** Cada quadradinho tem 2 coordenadas: primeiro qual **fileira de cima pra baixo (`i`)**, depois qual **coluna da esquerda pra direita (`j`)**. Na **Diagonal Principal (`i == j`)**, você anda na diagonal certinha `[0][0] → [1][1] → [2][2]`.
- **Fila (`FIFO`) vs. Pilha (`LIFO`) no Discord e no Matchmaking:**
  - **Fila (`FIFO` — *First In, First Out*):** É a **fila do Matchmaking** no Valorant/LoL/CS2 — o primeiro squad que clicou em "Jogar" é o primeiro que o servidor coloca na sala.
  - **Pilha (`LIFO` — *Last In, First Out*):** É o **`Ctrl+Z`** ou a pilha de *buffs/menus* abertos — se você abriu `Configurações → Áudio → Microfone`, ao apertar `ESC` você fecha **o último menu que abriu (`Microfone`)** primeiro!
- **Recursividade = Boneca Russa / *Call Stack*:** Uma função que chama uma versão menor dela mesma até bater no **Caso Base** (o momento em que ela para de chamar e devolve os resultados de volta!).

---

### 📚 Parte 1 — Vetores (Arrays 1D) e Indexação Base Zero

Um **vetor** (*array* unidimensional) é uma estrutura composta **homogênea** — todas as posições guardam dados do **mesmo tipo** (ex.: só inteiros ou só strings) — disposta em posições contíguas na memória RAM e acessada por um **índice numérico**.

#### A Regra de Ouro dos Índices (Base `0`)
Em C, C++, Java, JavaScript, Python e PHP, a contagem das gavetas **começa no índice `0`**, e **NÃO no `1`!**
Logo, um vetor `notas` de tamanho `N = 5`:
- Possui índices válidos **`0, 1, 2, 3, 4`** (isto é, de **`0` até `N - 1`**!).
- Visualização na memória:

| Índice | `notas[0]` | `notas[1]` | `notas[2]` | `notas[3]` | `notas[4]` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Valor armazenado** | `8.5` | `6.0` | `9.0` | `7.5` | `10.0` |

- Quanto vale `notas[2]`? Vale **`9.0`** (é o **3º** elemento, não o 2º!).
- O que acontece se você tentar acessar `notas[5]`? **Erro fatal (*Index Out of Bounds* / estouro de limite)** porque só vai até `4`!

#### 💻 Exemplo Real Comentado: Varredura com Laço `for` (Apostas Q10)
```javascript
let v = [10, 15, 20, 25];
let soma = 0;
for (let i = 0; i < v.length; i++) {
    if (v[i] % 2 === 0) {
        soma = soma + v[i];
    }
}
// i=0: v[0]=10 (par!) -> soma = 10
// i=1: v[1]=15 (ímpar, ignora)
// i=2: v[2]=20 (par!) -> soma = 30
// i=3: v[3]=25 (ímpar, ignora)
// Resultado final: soma = 30
```

> [!WARNING]
> **Pegadinha de linguagem:** Algumas provas em **Portugol acadêmico (VisuAlg)** declaram explicitamente `vetor[1..5] de inteiro` (começando em `1`). Leia sempre o cabeçalho da questão! Se estiver em JS, C, Java, Python ou PHP — ou se não disser `1..N` — a indexação começa obrigatoriamente em **`0`**.

---

### 📚 Parte 2 — Matrizes Bidimensionais (`M[i][j]`) e Diagonais

Uma **matriz bidimensional** é um "vetor de vetores" organizado como uma tabela de **linhas (`i`)** e **colunas (`j`)**.
Convenção universal em computação: **`M[i][j]`** lê-se **PRIMEIRO a linha `i`**, **DEPOIS a coluna `j`**!

Considere esta **Matriz `M` de ordem `3 × 3`** (3 linhas e 3 colunas, base `0`):

| `Linha (i) \ Coluna (j)` | Coluna `j = 0` | Coluna `j = 1` | Coluna `j = 2` |
| :---: | :---: | :---: | :---: |
| **Linha `i = 0`** | **`5`** (`[0][0]`) | `8` (`[0][1]`) | **`2`** (`[0][2]`) |
| **Linha `i = 1`** | `4` (`[1][0]`) | **`7`** (`[1][1]`) | `9` (`[1][2]`) |
| **Linha `i = 2`** | **`6`** (`[2][0]`) | `1` (`[2][1]`) | **`3`** (`[2][2]`) |

#### As 4 Regiões Clássicas da Matriz Quadrada de Ordem `N` (aqui `N = 3`)

1. **Diagonal Principal:** Formada pelos elementos que descem do **canto superior esquerdo ao canto inferior direito**.
   - **Condição matemática exata:** **`i == j`** (índice da linha igual ao da coluna!).
   - Na matriz acima: `M[0][0] = 5`, `M[1][1] = 7`, `M[2][2] = 3`.
   - **Soma da Diagonal Principal** = `5 + 7 + 3 =` **`15`**.
2. **Diagonal Secundária:** Formada pelos elementos que descem do **canto superior direito ao canto inferior esquerdo**.
   - **Condição matemática exata:** **`i + j == N - 1`** (aqui `i + j == 2`!).
   - Na matriz acima: `M[0][2] = 2` (`0+2=2`), `M[1][1] = 7` (`1+1=2`), `M[2][0] = 6` (`2+0=2`).
   - **Soma da Diagonal Secundária** = `2 + 7 + 6 = 15`. *(Note que em DS 2025 Q10 a matriz tinha diagonais com valores diferentes justamente para pegar quem confundiu principal com secundária!)*
3. **Acima da Diagonal Principal:** `j > i` (`M[0][1], M[0][2], M[1][2]`).
4. **Abaixo da Diagonal Principal:** `i > j` (`M[1][0], M[2][0], M[2][1]`).

#### 💻 Exemplo Real Comentado: Laço Aninhado (`for` dentro de `for`)
Observe como dois laços percorrem uma matriz inteira somando **apenas** a diagonal principal:

```python
M = [
    [1, 3, 5],   # linha i = 0
    [2, 4, 8],   # linha i = 1
    [1, 1, 1]    # linha i = 2
]
soma_dp = 0
for i in range(3):          # i assume 0, 1, 2
    for j in range(3):      # para cada i, j assume 0, 1, 2
        if i == j:          # só entra em [0][0], [1][1], [2][2]
            soma_dp += M[i][j]

print(soma_dp)  # 1 + 4 + 1 = 6!
```

> [!CAUTION]
> **Pegadinha da DS 2025 Q10:** A banca perguntou a soma da **diagonal principal** da matriz `[[1,3,5],[2,4,8],[1,1,1]]` e colocou **`10`** nas alternativas (que é a soma da diagonal **secundária**: `5 + 4 + 1 = 10`). Desenhe sempre os índices `[0][0]`, `[1][1]`, `[2][2]` no rascunho antes de somar!

---

### 📚 Parte 3 — Estruturas Lineares: Pilha (LIFO) vs. Fila (FIFO)

| Critério | Pilha (*Stack*) | Fila (*Queue*) |
| :--- | :--- | :--- |
| **Princípio Oficial** | **LIFO** (*Last In, First Out* — **Último** a entrar, **Primeiro** a sair) ou **FILO** | **FIFO** (*First In, First Out* — **Primeiro** a entrar, **Primeiro** a sair) |
| **Operação de Inserção** | **`PUSH`** (empilha no **topo**) | **`Enqueue`** / Inserir (entra no **fim/cauda**) |
| **Operação de Remoção** | **`POP`** (remove sempre do **topo**) | **`Dequeue`** / Remover (sai sempre da **frente/cabeça**) |
| **Exemplos Reais em TI** | Botão **Voltar** do navegador, **Desfazer (`Ctrl+Z`)**, **Pilha de Chamadas (*Call Stack*)** de funções | **Fila de impressão (*Spooler*)**, **fila de mensagens/tickets**, buffer de teclado |

#### 💻 Rastreamento Completo de Pilha (Baseado em DS 2019 Q3)
Partindo de uma pilha vazia, execute:
1. `push("A")` → Pilha: `["A"]` *(Topo = A)*
2. `push("B")` → Pilha: `["A", "B"]` *(Topo = B)*
3. `push("C")` → Pilha: `["A", "B", "C"]` *(Topo = C)*
4. `pop()` → Remove o **último que entrou (`C`)**! Sobra `["A", "B"]` *(Topo = B)*
5. `push("D")` → Entra no topo: `["A", "B", "D"]` *(Topo = D)*
6. `pop()` → Remove o topo (`D`): Sobra `["A", "B"]` *(Topo = B, Base = A)*.

---

### 📚 Parte 4 — Funções, Parâmetros e Recursividade

Uma **função** (ou sub-rotina) é um bloco de código reutilizável com um nome que recebe **parâmetros** de entrada e devolve um valor (`return`).
Uma função é chamada **recursiva** quando ela **chama a si mesma dentro do próprio corpo**, reduzindo um problema grande a versões menores dele mesmo.

Toda função recursiva bem escrita possui **duas partes obrigatórias**:
1. **Caso Base (Critério de Parada):** A versão mais simples que tem resposta direta sem chamar a função novamente. *(Sem caso base, ocorre recursão infinita até estourar a memória RAM: erro **`Stack Overflow`**!)*
2. **Passo Recursivo:** A função chama a si mesma aproximando o argumento do Caso Base.

#### 💻 Exemplo Real Comentado: Fatorial Recursivo `fatorial(4)` (INFO 2025 Q21)
Definição matemática: **`0! = 1`** e **`n! = n × (n - 1)!`**.

```javascript
function fat(n) {
    if (n <= 1) return 1;        // CASO BASE (0! = 1 e 1! = 1)
    return n * fat(n - 1);       // PASSO RECURSIVO (empilha chamadas na Call Stack!)
}
console.log(fat(4));
```

**Como a Pilha de Chamadas (*Call Stack*) da CPU executa `fat(4)` (LIFO na veia!):**
- **Descida (empilhando *PUSH*):**
  1. `fat(4)` precisa saber `4 * fat(3)` → pausa e chama `fat(3)`
  2. `fat(3)` precisa saber `3 * fat(2)` → pausa e chama `fat(2)`
  3. `fat(2)` precisa saber `2 * fat(1)` → pausa e chama `fat(1)`
  4. `fat(1)` bate no **Caso Base** → retorna **`1`**!
- **Subida (desempilhando *POP* e calculando):**
  5. `fat(2)` calcula `2 * 1 =` **`2`**
  6. `fat(3)` calcula `3 * 2 =` **`6`**
  7. `fat(4)` calcula `4 * 6 =` **`24`**!

> [!TIP]
> **Lembrete matemático importante:** **`0! = 1`** (por definição combinatória, existe 1 forma de organizar zero elementos) e acumulador de multiplicação/fatorial em laço deve começar com **`1`**, nunca `0`!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q3 — Pilha LIFO)
*Em uma estrutura do tipo Pilha vazia, inseriram-se os números 5, 10 e 15 (nessa ordem). Em seguida, aplicou-se uma operação de remoção (POP), inseriu-se o 20 e aplicou-se outro POP. Qual o elemento no TOPO e qual é a BASE restante?*
- Passo a passo: `[]` → `[5]` → `[5,10]` → `[5,10,15]` → `POP` tira `15` (`[5,10]`) → `PUSH 20` (`[5,10,20]`) → `POP` tira `20` (**`[5,10]`**).
- **Resposta:** Base = **`5`**, Topo = **`10`**. *(Se fosse uma **Fila FIFO**, o 1º `Dequeue` teria tirado o `5` em vez do `15`!)*

#### Questão Resolvida 2 (Baseada em Matriz + Índices)
*Considere a matriz quadrada `A` 3×3 preenchida pela regra `se (i + j == 2) entao A[i][j] <- 10 senao A[i][j] <- i * 2`. Qual o valor de `A[2][1]` e qual diagonal recebeu o valor 10?*
- Em `A[2][1]`: `i = 2, j = 1`. Soma `2 + 1 = 3 != 2` (cai no `senao`!). Logo `A[2][1] = 2 * 2 =` **`4`**.
- Como `N = 3`, `i + j == N - 1` (`i + j == 2`) é exatamente a **Diagonal Secundária**!


---

## Dia 4 — Ecossistema de Desenvolvimento: Frameworks, Editores/IDEs/WYSIWYG, Compilação/Build/Bundling, Git e Licenças

### 🎯 Contexto no Mundo Real: Construindo uma Casa sem Fabricar Tijolo por Tijolo

Se uma equipe precisasse inventar toda vez o sistema de rotas URL, autenticação de login, layout responsivo de botões para celular e minificação de scripts do zero, criar um simples site de escola levaria meses. Por isso existem os **frameworks**, as **IDEs**, as ferramentas de **build/bundling**, o controle de versão **Git** e as **licenças legais** que dizem o que uma empresa pode ou não usar comercialmente sem ser processada. Esse módulo é puro **Molde 1 (I, II, III)** e **Molde 2 (Lista com Intruso)** na prova!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Para conectar esse módulo técnico com o mundo de jogos, mods e Discord:

- **Framework vs. Biblioteca = Game Engine / Mod Loader:** Uma biblioteca é igual baixar só um pacote de texturas — você usa se quiser. Um **Framework** (Laravel, Angular, React Native, Bootstrap) é tipo usar uma **Engine** (ou Forge/Fabric no Minecraft): já vem com o esqueleto pronto e você só encaixa o seu código nos lugares certos!
- **Compilação + *Build* + *Bundling*:** Quando você cria mods ou um jogo, são dezenas de arquivos separados `.js`/`.cs` + texturas. O ***Build / Bundling*** empacota tudo num `.exe` ou `.pak` otimizado e minificado para abrir rápido sem fazer 200 carregamentos na internet.
- **Git (`branch`, `diff`, `merge`) = Save Slots antes de testar Mod arriscado:** Em vez de editar o save oficial (`main`) e correr o risco de corromper tudo, você cria uma cópia paralela (**`git branch`**), compara exatamente o que mudou linha por linha (**`git diff`**) e, só quando tiver certeza de que não deu bug, junta de volta no save oficial (**`git merge`**)!
- **Licenças na vida real:**
  - **Discord / Valorant / Spotify:** São ***Freeware*** (grátis para baixar e usar, mas **código-fonte 100% fechado**, NÃO são Software Livre!).
  - **OBS Studio / Godot Engine / Linux:** São **Software Livre / Open Source** — você pode baixar o código no GitHub, estudar, modificar e recompilar legalmente!
  - **EULA:** Aquele textão jurídico de contrato que todo mundo aceita na Steam/Windows dizendo *"não tente piratear, fazer engenharia reversa ou revender este jogo"*.

---

### 📚 Parte 1 — Frameworks Web & Mobile (O que São e Onde Cada Um Atua)

#### Biblioteca vs. Framework (Qual a diferença conceitual?)
- **Biblioteca (*Library*):** Uma caixa de ferramentas — **você chama** a função dela quando quiser (ex.: uma biblioteca de PDF ou matemática).
- **Framework:** Um **esqueleto arquitetural completo** com regras prontas — ele segue a **Inversão de Controle** (o framework organiza o ciclo do app e chama o seu código nos pontos certos).

Os **4 Frameworks campeões** nas provas da Fundação FAT:

| Tecnologia | Linguagem / Stack | Camada / Finalidade Oficial | Arquitetura & Detalhes que Caem |
| :--- | :--- | :--- | :--- |
| **Bootstrap** | HTML + CSS + JS | **Front-end Web Responsivo** (*mobile-first*) | Sistema de **Grid de 12 colunas** (`container`, `row`, `col-md-6`), botões prontos (`btn btn-primary`), alertas (`alert alert-success`), navbar adaptável ao celular. *(DS 2019 Q18)* |
| **Angular** | **TypeScript** / JS (Google) | **Front-end Web SPA** (*Single Page Application*) | Interfaces dinâmicas modulares baseadas em componentes, *data-binding* bidirecional e injeção de dependência. |
| **Laravel** | **PHP** | **Back-end Web (Servidor)** | Segue o padrão **MVC** (*Model-View-Controller*): `Model` cuida dos dados/banco (ORM Eloquent), `View` exibe as telas (Blade), `Controller` recebe requisições HTTP e decide regras de negócio. |
| **React Native** | JavaScript / React (Meta) | **Aplicativos Mobile Nativos (Android + iOS)** | Você escreve uma única base em JS/React e ele **renderiza componentes nativos reais** do Android/iOS (não é só um site dentro de navegador!). |

> [!CAUTION]
> **Pegadinha da DS 2025 Q7 (Molde 2 — Lista com Intruso):** A banca listou frameworks válidos e misturou intrusos como **Creative Commons** (que é uma **licença** de direitos autorais!) e **Adobe Creative Cloud** (suíte de edição de imagem/vídeo como Photoshop/Illustrator). Também costuma inverter **Laravel (back-end PHP)** dizendo que é "para interfaces móveis".

---

### 📚 Parte 2 — Bloco de Notas vs. Editor de Código vs. IDE vs. WYSIWYG

A Fundação FAT cobra literalmente a distinção entre as ferramentas onde programadores digitam e montam interfaces:

| Categoria | Recursos Incluídos | Exemplos Oficiais da Prova | NÃO confunda! |
| :--- | :--- | :--- | :--- |
| **Editor de Texto Simples** | Digita texto puro sem formatação (`UTF-8`), **SEM** destaque de sintaxe, autocompletar ou compilador. | **Bloco de Notas (Notepad)** do Windows, `TextEdit` simples | Embora dê para digitar HTML nele e salvar como `.html`, **ele NÃO é uma IDE nem editor de código avançado**! |
| **Editor de Código-Fonte** | Leve, rápido, oferece **realce de sintaxe** (colorir tags/comandos), numeração de linhas, indentação automática e **extensões/plugins**. | **VS Code** (*Visual Studio Code*), Sublime Text, Notepad++, Atom | VS Code puro, recém-instalado, é oficialmente classificado como **Editor de Código** (embora com plugins chegue perto de uma IDE). |
| **IDE** (*Integrated Development Environment*) | **Ambiente Integrado de Desenvolvimento:** junta em um só software Editor + **Compilador/Interpretador + Depurador (*Debugger* c/ breakpoints) + Gerenciador de Projeto**. | **Visual Studio** (Microsoft), **Eclipse**, **IntelliJ IDEA**, **NetBeans**, **PyCharm**, **Android Studio** | Não confunda *Visual Studio* (IDE completa pesada) com *Visual Studio Code* (editor leve)! |
| **Editor WYSIWYG** (*What You See Is What You Get*) | *"O que você vê é o que você obtém"*: criação visual **arrastar-e-soltar** que mostra o layout pronto ao vivo enquanto gera HTML/CSS nos bastidores. | **Adobe Dreamweaver** (modo Design), **Wix**, **WordPress Gutenberg/Elementor**, Google Sites | Foca em design visual sem precisar digitar toda tag HTML na mão. |

---

### 📚 Parte 3 — Compilação, Interpretação, *Build* e *Bundling* (DS 2025 Q22 & Apostas Q8)

#### 1. Compilador vs. Interpretador vs. Híbrido
- **Compilador (ex.: C, C++, Go, Rust):** Traduz **todo o código-fonte de uma só vez** antes da execução:
  `Código-Fonte (.c)` → **Compilador** → `Código-Objeto (.o/.obj, binário parcial)` → **Linker (Ligador)** (junta bibliotecas do sistema) → `Arquivo Executável (.exe / ELF)`.
  - Resultado: executa muito rápido sem precisar do código-fonte original no PC do cliente.
- **Interpretador (ex.: Python, JavaScript, PHP):** Lê, traduz e executa o código **linha por linha em tempo de execução**. Mais portável e rápido de testar, porém exige o interpretador instalado.
- **Modelo Híbrido (Java / C#):** Compila o fonte para um código intermediário chamado ***Bytecode*** (`.class` em Java), que depois roda na **JVM (*Java Virtual Machine*)**, garantindo alta portabilidade (*"Write Once, Run Anywhere"*).

#### 2. O que são *Build*, *Bundling*, *Minificação* e *Tree Shaking* na Web Moderna?
Quando você faz um site grande em React ou Angular, você tem **150 arquivos `.js` e `.css` separados**. Se o navegador do usuário tivesse que fazer 150 downloads separados ao abrir a página, o site ficaria lentíssimo!
- ***Build* (Construção):** Processo automatizado completo que prepara o projeto para entrar no ar (produção): compila/transpila código moderno (ex.: TypeScript → JS), roda testes, otimiza imagens e gera a pasta final de distribuição (`dist/`).
- ***Bundling* (Empacotamento):** Realizado por *bundlers* (**Webpack, Vite, Parcel**). Consiste em **agrupar dezenas de módulos/arquivos JS e CSS espalhados em poucos arquivos consolidados (*bundles*)** para reduzir requisições HTTP na rede.
- **Minificação (*Minification*):** Remove comentários, espaços em branco, quebras de linha e encurta nomes de variáveis internas (`contadorDeAlunos` vira `a`) apenas para o arquivo pesar menos KB na internet.
- ***Tree Shaking*:** Técnica em que o *bundler* detecta funções importadas que **nunca foram usadas** no projeto e as **exclui do bundle final** para economizar tamanho.

---

### 📚 Parte 4 — Controle de Versão Git em Equipe (DS 2019 Q26)

Imagine dois desenvolvedores editando `sistema.js` ao mesmo tempo: sem controle de versão, um sobrescreve o trabalho do outro ou perde tudo num erro! O **Git** é um **sistema de controle de versão distribuído** (cada dev tem o histórico completo na sua máquina; o **GitHub/GitLab/Azure DevOps** é a nuvem que hospeda repositórios Git).

**Ciclo real e comandos obrigatórios para a prova:**
- `git init` / `git clone <url>`: Inicia repositório novo na pasta / Baixa cópia completa de um remoto.
- `git status`: Mostra em tempo real quais arquivos foram modificados ou estão aguardando *commit*.
- `git add arquivo.js` (ou `git add .`): Envia as mudanças selecionadas para a **Staging Area** (área de preparação).
- `git commit -m "Corrige cálculo de média"`: Grava um ponto definitivo no histórico (**snapshot**) com identificador único (hash).
- **`git branch nova-tela`**: Cria uma **ramificação paralela e isolada** do código principal (`main`) para desenvolver uma novidade sem quebrar o sistema em produção! *(DS 2019 Q26)*
- **`git diff`**: **Compara** e exibe linha por linha as **diferenças** entre arquivos, commits ou branches.
- **`git merge nova-tela`**: **Funde (mescla)** o trabalho pronto de uma *branch* dentro de outra (ex.: traz `nova-tela` para dentro da `main`).
- `git push` / `git pull`: **Envia** seus commits para o servidor remoto / **Baixa e mescla** commits dos colegas do remoto para o seu PC.

---

### 📚 Parte 5 — Licenças de Software (Software Livre, Open Source, Proprietário, Freeware, EULA)

A Fundação FAT e o M-Tec cobram esse tema quase todo ano (**DS 2025 Q23**, **M-Tec 2022 Q36**)! Entenda a diferença jurídica real:

| Licença / Modelo | Código-Fonte é Aberto? | Pode Alterar e Redistribuir? | Precisa ser Grátis (`R$ 0`)? | Essência e Exemplos |
| :--- | :---: | :---: | :---: | :--- |
| **Software Livre (*Free Software* — FSF)** | **SIM** | **SIM** | **NÃO obrigatoriamente!** (*"Free as in freedom, not free beer"*) | Defende **4 Liberdades Fundamentais** (usar p/ qualquer fim, estudar/modificar, redistribuir cópias, distribuir modificações). Pode ser vendido por mídia ou suporte! Ex.: Linux (GPL), LibreOffice, GIMP. |
| **Open Source (Código Aberto — OSI)** | **SIM** | **SIM** | Geralmente sim (alguns com modelo comercial em cima) | Foco prático/empresarial em desenvolvimento colaborativo, transparência e qualidade técnica. Principais licenças: **MIT, Apache 2.0, BSD** (permissivas) e **GPL** (*copyleft* — exige que derivados continuem livres). |
| **Proprietário / Comercial** | **NÃO (Fechado)** | **PROIBIDO** (restringido por lei) | Pago (ou assinatura) | O dono retém todos os direitos autorais e entrega só o binário executável. O usuário aceita um **EULA (*End User License Agreement*)** proibindo engenharia reversa e cópia. Ex.: Windows, Photoshop, MS Office. |
| ***Freeware*** | **NÃO (Fechado)** | **PROIBIDO modificar** | **SIM (`R$ 0`)** | Distribui gratuitamente o executável, **mas esconde o código-fonte**! Ex.: Skype, WinRAR antigo/Adobe Reader. **NÃO é Software Livre!** |
| ***Shareware* / Trial** | **NÃO** | **PROIBIDO** | Grátis por tempo limitado (ex.: 30 dias) | Teste temporário antes de exigir compra da licença. |
| **Assinatura / SaaS** | Geralmente fechado | **PROIBIDO** | Mensalidade/anuidade contínua | Acesso ao software e atualizações enquanto pagar (ex.: Microsoft 365, Adobe Creative Cloud, Netflix). |

> [!CAUTION]
> **Pegadinha clássica (DS 2025 Q23 & M-Tec 2022 Q36):**
> 1. *"Todo Software Livre é necessariamente gratuito e nunca pode ser comercializado."* → **FALSO!** Você pode vender distribuição ou suporte de Software Livre; a liberdade é sobre **acessar e modificar o código-fonte**.
> 2. *"Todo software gratuito (Freeware) é Open Source."* → **FALSO!** Se o código é fechado, é proprietário gratuito (*Freeware*), jamais Open Source ou Software Livre!
> 3. **EULA** (*End User License Agreement*) é o contrato de usuário final típico de software **proprietário**, definindo limites de instalação e proibindo redistribuição.

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q26 & DS 2025 Q19 — Git e Editores)
*Analise: I. O Bloco de Notas (Notepad) é classificado como IDE por permitir salvar arquivos `.html`. II. No Git, `git branch` cria linha paralela de desenvolvimento, `git diff` mostra diferenças entre versões e `git merge` une ramificações. III. Bundlers como Webpack agrupam vários módulos JS/CSS para diminuir requisições HTTP.*
- **Item I é FALSO:** Bloco de Notas é editor de texto simples (não possui compilador/depurador integrados).
- **Item II é VERDADEIRO:** Definições exatas dos três comandos Git.
- **Item III é VERDADEIRO:** Função exata de *bundling*.
**Gabarito:** **II e III corretas**.

#### Questão Resolvida 2 (Baseada em DS 2025 Q23 — Licenças)
*Qual alternativa está INCORRETA sobre licenciamento de software?*
- *A) Open Source exige acesso ao código-fonte para inspeção e melhoria.* (Verdadeira)
- *B) Um software proprietário costuma ser distribuído sob um EULA restringindo cópia e modificação.* (Verdadeira)
- *C) Software Livre proíbe cobrança financeira e exige distribuição de binários sem código-fonte.* (**FALSA!** Tanto permite venda quanto **exige** acesso ao código-fonte!).
**Gabarito:** **C**.


---

## Dia 5 — Engenharia de Software, Ciclos de Vida, Requisitos, SWOT, UML, Scrum/XP, Testes e POO

### 🎯 Contexto no Mundo Real: Por que "Só Sair Digitando Código" Quebra Empresas?

Imagine construir um prédio de 15 andares sem engenheiro: você começa a empilhar tijolos no primeiro dia e, no quinto andar, descobre que esqueceu o poço do elevador e que o solo não aguenta o peso. Na década de 1960 ocorreu a chamada **Crise do Software** — projetos estouravam orçamentos em 300%, entregavam atrasados e cheios de falhas críticas porque programadores escreviam código direto sem planejar requisitos, arquitetura ou testes.

É daí que nasce a **Engenharia de Software**: um conjunto sistemático de métodos, processos e boas práticas para entregar sistemas como **Spotify, Nubank ou o NSA da Etec** no prazo, dentro do orçamento, fáceis de manter e fiéis ao que o cliente realmente precisa.

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Você já viu na prática por que grandes estúdios de games falham ou acertam dependendo do jeito que desenvolvem o software:

- **Cascata vs. Ágil/Scrum (Atualizações de Jogos):**
  - Fazer um jogo em **Cascata** é passar 5 anos desenvolvendo escondido sem testar com ninguém e lançar tudo de uma vez (e se os jogadores odiarem a mecânica, já era!).
  - Usar **Scrum (Ágil)** é lançar uma base jogável rápido e ir soltando *Patches / Seasons* a cada **Sprint** de 2 semanas, fazendo a **Daily de 15 min** na call do Discord só para alinhar quem tá fazendo o quê e tirar bloqueios (*Scrum Master*) enquanto o *Product Owner* prioriza o que dá mais valor pro jogador!
- **Requisitos Funcionais (RF) vs. Não Funcionais (RNF) num Jogo Online:**
  - **RF ("O QUÊ faz"):** *"O personagem pula, atira, recarrega e abre loja de skins."*
  - **RNF ("COMO se comporta"):** *"Rodar a **120 FPS**, ping abaixo de **30 ms**, anti-cheat ativo e ter **Portabilidade** para rodar tanto no Windows 11 quanto no Steam Deck (Linux)!"*
- **Os 4 Pilares da POO na Prática:** Você cria um molde geral chamado classe **`Personagem` (Abstração)**. Dele nascem `Mago` e `Guerreiro` aproveitando vida/nome/mover (**Herança**). A variável interna `hp` fica bloqueada como `private` pra ninguém editar com cheat (**Encapsulamento**). E quando os dois apertam `Q` (`usarHabilidade()`), cada classe solta um poder diferente com o mesmo comando (**Polimorfismo**)!

---

### 📚 Parte 1 — Modelos de Ciclo de Vida: Cascata vs. Prototipação vs. Espiral vs. Ágil

Todo software passa por fases: **Levantamento de Requisitos → Projeto/Arquitetura → Implementação (Código) → Testes/Validação → Implantação → Manutenção**. A forma como organizamos essas fases define o **Modelo de Processo**:

| Modelo | Como funciona passo a passo | Quando brilha | Onde costuma falhar |
| :--- | :--- | :--- | :--- |
| **Cascata (*Waterfall*)** *(DS 2019 Q8)* | **Sequencial e rígido:** uma fase só inicia quando a anterior for 100% encerrada e assinada (*Requisitos → Design → Código → Testes → Uso*). | Requisitos totalmente estáveis desde o dia 1 (ex.: software médico/aviação regulado). | Se o cliente mudar de ideia na metade, voltar fases é caríssimo; **cliente só vê software pronto no final!** |
| **Prototipação** | Constrói rapidamente um **protótipo** (tela simulada ou rascunho) para o cliente testar, validar a ideia e corrigir cedo. | Quando o cliente não sabe explicar direito o que quer. | Risco de o cliente achar que o rascunho já é o sistema pronto. |
| **Espiral (Boehm)** | Ciclos repetidos (*espiral*) onde **cada volta começa com Análise de Riscos**, protótipo, engenharia e avaliação. | Sistemas gigantes de alto risco financeiro ou técnico. | Complexo e caro gerenciar a análise de riscos em projetos pequenos. |
| **Metodologias Ágeis** *(Scrum, Kanban, XP)* | Desenvolvimento **iterativo e incremental** em ciclos curtos (*Sprints* de 1–4 semanas). Entrega software funcionando rápido e **abraça mudanças**. | 90% dos projetos modernos (apps, web, startups) onde o mercado muda toda hora. | Exige participação próxima do cliente e equipe madura/auto-organizável. |

> [!WARNING]
> **Pegadinha clássica (DS 2019 Q8):** No **Modelo em Cascata**, as fases avançam de forma **sequencial descendente** e cada etapa deve ser concluída antes de passar para a próxima — o erro nas alternativas é afirmar que *"o modelo Cascata entrega incrementos semanais ao cliente sem documentação prévia"* (isso é Ágil!).

---

### 📚 Parte 2 — Engenharia de Requisitos, Estudo de Viabilidade e Análise SWOT

Antes de escrever código, o Analista de Sistemas conversa com os *stakeholders* (partes interessadas: clientes, usuários, diretoria) para levantar os **Requisitos** e realizar o **Estudo de Viabilidade**.

#### 1. Estudo de Viabilidade (*INFO 2025 Q23 & Apostas Q12*)
Responde à pergunta: *"Vale a pena e é possível fazer este sistema?"* Analisa 3 frentes:
- **Viabilidade Técnica:** Temos tecnologia, servidores, APIs e equipe capaz de construir?
- **Viabilidade Econômica / Financeira:** O benefício/lucro (*ROI*) compensa o custo de desenvolvimento e manutenção?
- **Viabilidade Operacional:** Os funcionários e usuários reais vão conseguir e querer operar o sistema no dia a dia?

#### 2. Requisitos Funcionais (RF) vs. Requisitos Não Funcionais (RNF)
Vamos aplicar ao exemplo real de um **aplicativo de delivery (tipo iFood)**:

| Tipo | O que descreve | Exemplos reais no App de Delivery |
| :--- | :--- | :--- |
| **Requisito Funcional (RF)** | **O QUE** o sistema faz — ações, serviços, regras de cálculo e telas visíveis. | **RF01:** Permitir cadastro de cliente com CPF.<br>**RF02:** Calcular taxa de entrega por distância.<br>**RF03:** Permitir pagamento via Pix ou cartão.<br>**RF04:** Cancelar pedido em até 2 minutos. |
| **Requisito Não Funcional (RNF)** | **COMO** o sistema se comporta — restrições de qualidade, desempenho, segurança, **portabilidade**, usabilidade e normas. | **RNF01 (Desempenho):** Carregar cardápio em **menos de 2 segundos**.<br>**RNF02 (Segurança):** Senhas criptografadas com BCrypt e tráfego **HTTPS**.<br>**RNF03 (Disponibilidade):** Funcionar 99,9% do tempo na Black Friday.<br>**RNF04 (Portabilidade):** *(DS 2019 Q10)* Poder ser instalado/transferido entre **Android, iOS e Windows/Linux** facilmente! |

**Critérios de um Bom Requisito *(INFO 2025 Q22)*:** Um requisito bem escrito nunca pode dizer *"O sistema deve ser rápido e bonito"* (vago!). Ele deve ser **Claro, Não Ambíguo, Verificável/Testável** (*"responder em até 2 segundos"*), **Consistente** (não contradizer outro RF) e **Rastreável**.

#### 3. Análise SWOT / FOFA *(M-Tec 2022 Q29 & Sim2 Q30)*
Ferramenta de planejamento estratégico para avaliar negócios/projetos em 4 quadrantes:
- **Ambiente Interno (controlável pela empresa):**
  - **S — *Strengths* (Forças):** Vantagens internas (ex.: equipe sênior experiente, marca forte).
  - **W — *Weaknesses* (Fraquezas):** Pontos fracos internos (ex.: servidor antigo, falta de suporte 24h).
- **Ambiente Externo (mercado/governo — fora do controle direto):**
  - **O — *Opportunities* (Oportunidades):** Cenários externos favoráveis (ex.: lei incentivando digitalização, concorrente faliu).
  - **T — *Threats* (Ameaças):** Riscos externos (ex.: entrada de gigante estrangeiro no mercado, alta do dólar).

---

### 📚 Parte 3 — UML (Linguagem de Modelagem Unificada) e Dicionário de Dados

A **UML** não é uma linguagem de programação — é a **notação visual padrão** usada mundialmente para desenhar sistemas orientados a objetos *(M-Tec 2022 Q30 & INFO 2025 Q24)*.

1. **Diagrama de Casos de Uso (*Use Case Diagram* — Comportamental):**
   - Mostra **quem** usa o sistema e **o que** faz, visto pelo olhar do usuário externo.
   - **Elementos principais:** **Ator** (bonequinho — pode ser humano *Aluno* ou outro sistema externo *Banco*), **Caso de Uso** (elipse com verbo no infinitivo: *"Realizar Matrícula"*) e linhas de associação.
   - **Relacionamentos especiais:** `<<include>>` (obrigatório sempre, ex.: *Fazer Transferência* sempre inclui *Validar Senha*) e `<<extend>>` (opcional sob condição, ex.: *Solicitar Comprovante PDF*).
2. **Diagrama de Classes (Estrutural / Estático):**
   - Cada classe é um retângulo com 3 partes: **Nome da Classe** (ex.: `Aluno`), **Atributos** (`- nome: string`, `+ ra: int`) e **Métodos** (`+ calcularMedia(): float`).
   - Símbolos de visibilidade: **`+` Público (`public`)**, **`-` Privado (`private`)**, **`#` Protegido (`protected`)**.
3. **Dicionário de Dados *(M-Tec 2022 Q32)*:**
   - Documento/catálogo complementar onde cada dado do sistema é detalhado com precisão:

| Nome do Campo | Tipo & Tamanho | Obrigatório? | Domínio / Regra de Validação | Descrição |
| :--- | :--- | :---: | :--- | :--- |
| `cpf_aluno` | `CHAR(11)` | Sim (`NOT NULL`) | Apenas dígitos `0–9`, único (`UNIQUE`) | CPF do estudante sem pontos/traços |
| `nota_final` | `DECIMAL(4,2)` | Não | De `0.00` até `10.00` | Média calculada do módulo |

---

### 📚 Parte 4 — Scrum, Kanban, XP (*Extreme Programming*) e Pirâmide de Testes

| Framework / Prática | Componentes e Definições Exatas para a Prova |
| :--- | :--- |
| **Scrum — Os 3 Papéis** | **Product Owner (PO):** Representa cliente/negócio; **dono do *Product Backlog***; define **O QUÊ** construir e em que ordem de prioridade de valor.<br>**Scrum Master (SM):** **Líder servidor/facilitador**; garante o uso correto do Scrum e **remove impedimentos** do time. *(NÃO é chefe tradicional que distribui ordens nem arquiteto de código!)*<br>**Time de Desenvolvimento (*Developers*):** Equipe técnica multidisciplinar e **auto-organizável** que decide **COMO** implementar e estima as tarefas. |
| **Scrum — Eventos (*Timeboxes*)** | **Sprint:** Ciclo curto e fixo (geralmente 1 a 4 semanas) que entrega Incremento pronto.<br>**Daily Scrum:** Reunião diária curta de **no máximo 15 minutos**, em pé, para sincronizar o trabalho das próximas 24h e apontar impedimentos. *(DS 2019 Q12)*<br>**Sprint Review** (mostra software funcionando aos clientes) e **Sprint Retrospective** (melhoria interna do processo do time). |
| **Kanban** | Sistema visual com **quadro de cartões e colunas** (*Backlog → Fazendo → Em Teste → Feito*) focado em fluxo contínuo e **limitação do trabalho em progresso (WIP — *Work In Progress*)** para evitar gargalos. |
| **XP — *Pair Programming*** *(DS 2019 Q24)* | **Programação em Par:** **Dois programadores compartilham o mesmo computador** — o **Piloto (*Driver*)** digita o código focado na linha atual, enquanto o **Copiloto (*Navigator*)** revisa erros em tempo real e pensa na estratégia/arquitetura, alternando papéis! |

#### Os 4 Níveis Oficiais de Teste de Software *(DS 2019 Q25)*
1. **Teste de Unidade (Unitário):** Verifica a **menor unidade isolada** do software (uma única função ou método, ex.: testar `calcularFrete(10)` sem acessar banco de dados real).
2. **Teste de Integração:** Verifica se **módulos combinados** conversam corretamente (ex.: Controller + Banco MySQL + Gateway de pagamento).
3. **Teste de Sistema:** Testa a aplicação inteira integrada de ponta a ponta simulando um ambiente de produção.
4. **Teste de Aceitação (UAT):** Validação final junto ao cliente/PO confirmando se os requisitos do contrato foram atendidos.

---

### 📚 Parte 5 — Programação Orientada a Objetos (POO): Classes, Objetos e os 4 Pilares

Na POO, trazemos coisas do mundo real para dentro do código usando dois conceitos base:
- **Classe:** É o **molde / projeto** (ex.: a planta de um carro ou o formulário em branco de `ContaBancaria`, definindo **Atributos** = características/dados e **Métodos** = ações/comportamentos).
- **Objeto:** É uma **instância concreta criada em memória RAM** a partir da classe (ex.: a conta real nº `1020-5` da `Ana`, com saldo `R$ 500`, e outra conta `9988-1` do `João`, com saldo `R$ 1200`).

#### 💻 Exemplo Real Comentado com os 4 Pilares da POO *(DS 2019 Q27)*

```python
class Animal:                           # ABSTRAÇÃO: só atributos/métodos essenciais ao sistema
    def __init__(self, nome, peso):
        self.__nome = nome              # ENCAPSULAMENTO: __ privado! Protegido de acesso direto externo
        self.__peso = peso

    def get_nome(self):                 # Interface pública segura para leitura controlada
        return self.__nome

    def emitir_som(self):               # Método base
        return "..."

class Cachorro(Animal):                 # HERANÇA: Cachorro herda nome, peso e get_nome() de Animal!
    def emitir_som(self):               # POLIMORFISMO: sobrescreve emitir_som() com comportamento próprio!
        return "Au au!"

class Gato(Animal):                     # HERANÇA
    def emitir_som(self):               # POLIMORFISMO: mesmo nome de método, resposta diferente!
        return "Miau!"
```

| Os 4 Pilares Oficiais da POO | Significado exato que cai na prova |
| :--- | :--- |
| **1. Abstração** | Focar apenas nos atributos e comportamentos essenciais do problema real, ignorando detalhes irrelevantes. |
| **2. Encapsulamento** | **Ocultar e proteger dados internos** (`private`) para evitar alterações inválidas (ex.: `saldo = -99999`), liberando acesso controlado via métodos públicos (`depositar()`, `getSaldo()`). |
| **3. Herança** | Uma classe filha (**subclasse**) reaproveita atributos e métodos de uma classe mãe (**superclasse**), criando especializações (`Gerente` herda de `Funcionario`). |
| **4. Polimorfismo** | *"Muitas formas"*: objetos de classes diferentes respondem de maneira própria à mesma chamada de método (`emitir_som()` ou `calcularSalario()`). |

> [!CAUTION]
> **Pegadinha clássica (DS 2019 Q27):** A banca pergunta quais são os **4 Pilares da POO** e coloca no meio palavras como *"Atributo, Método, Classe, Compilação, Recursividade"*. **Classe, Objeto, Atributo e Método são ELEMENTOS básicos**, mas os **4 PILARES** são exclusivamente **Abstração, Encapsulamento, Herança e Polimorfismo**!

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q12 & Apostas Q13 — Scrum)
*Sobre o framework Scrum, julgue:*
- *I. O Scrum Master atua como gerente tradicional que atribui linhas de código e impõe prazos diários ao time.*
- *II. O Product Owner é o responsável por maximizar o valor do produto e priorizar o Product Backlog.*
- *III. A Daily Scrum é uma reunião diária de sincronização limitada a no máximo 15 minutos.*
**Análise:** **I é FALSO** (Scrum Master é facilitador que remove impedimentos; o time é auto-organizável). **II e III são VERDADEIROS**.

#### Questão Resolvida 2 (Baseada em DS 2019 Q10 & INFO 2025 Q22 — Requisitos)
*Um cliente exige que o sistema funcione sem modificações nos navegadores Chrome, Edge e Safari, e que responda em até 1,5 segundo com 1.000 usuários simultâneos. Essas exigências classificam-se, respectivamente, como:*
**Análise:** Compatibilidade entre diferentes ambientes/plataformas é **Portabilidade**; limite de 1,5s é **Desempenho**. Ambos descrevem *como* o sistema se comporta, portanto são **Requisitos Não Funcionais**!


---

## Dia 6 — Banco de Dados Relacional, SGBDs, as 5 Sublinguagens SQL e Bancos NoSQL

### 🎯 Contexto no Mundo Real: Por que Sistemas Sérios Não Salvam Dados em Arquivos de Texto ou Planilhas?

Imagine uma loja virtual vendendo o **último iPhone do estoque** para duas pessoas clicando em "Comprar" no mesmo milissegundo em São Paulo e em Campinas. Se os dados ficassem numa planilha do Excel compartilhada, os dois pedidos poderiam gravar "estoque = 0" vendendo 2 aparelhos onde só havia 1, sem falar na lentidão com 5 milhões de clientes cadastrados ou no risco de alguém abrir o arquivo e apagar tudo!

Para resolver concorrência, velocidade de busca, permissões de usuários e integridade financeira, usamos um **SGBD (*Sistema Gerenciador de Banco de Dados*)** — como **MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server ou SQLite** — conversando através da linguagem padrão **SQL (*Structured Query Language*)**. E quando precisamos armazenar catálogos gigantes e flexíveis estilo JSON de redes sociais ou cache em milissegundos, entra em cena o universo **NoSQL**.

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Onde ficam salvas todas as mensagens de um servidor do Discord, sua lista de amigos da Steam ou o ranking mundial do Fortnite? Dentro de **Bancos de Dados (SQL e NoSQL)**! Olha como as **5 sublinguagens SQL** aparecem nisso:

- **DDL (`CREATE`, `ALTER`, `DROP`):** Mexe na **estrutura** — cria a tabela `jogadores`, adiciona a coluna `elo`, ou apaga a tabela inteira!
- **DML (`INSERT`, `UPDATE`, `DELETE`):** Mexe nos **registros dentro da tabela** — grava uma nova partida (`INSERT`), sobe seu XP (`UPDATE`) ou apaga uma mensagem enviada no chat (`DELETE`).
- **DQL (`SELECT` + `COUNT(*)`):** Faz a **consulta** — *"Quantos jogadores têm elo Diamante (`SELECT COUNT(*) WHERE elo = 'Diamante'`)?"*.
- **DCL (`GRANT`, `REVOKE`):** É exatamente **dar ou tirar cargo de Admin / Moderador** no Discord para um usuário poder ler ou mexer nos registros!
- **TCL (`COMMIT`, `ROLLBACK`):** É o sistema anti-golpe de **Trade de Skins na Steam**! Quando você troca uma faca por 3 skins com outro player, ou os dois itens trocam de dono ao mesmo tempo (**`COMMIT`**), ou se a internet cair no meio o banco desfaz tudo e ninguém é roubado (**`ROLLBACK`**)!
- **NoSQL (MongoDB / Redis):** Guarda coisas flexíveis em JSON (cada personagem tem atributos diferentes no inventário sem coluna fixa) e status instantâneo na RAM (*"Fulano está online jogando Valorant"*).

---

### 📚 Parte 1 — O Papel do SGBD e Transações ACID

Um **SGBD** fica entre o seu programa (back-end PHP/Node/Java/Python) e os arquivos físicos no SSD/HD. Ele garante as propriedades **ACID** em transações bancárias e comerciais:
- **A — Atomicidade:** "Tudo ou nada" (num Pix, ou tira do saldo de João **e** entra no saldo de Maria, ou desfaz ambos — nunca some no meio!).
- **C — Consistência:** O banco nunca viola regras/chaves (`NOT NULL`, chaves estrangeiras).
- **I — Isolamento:** Milhares de usuários consultando e comprando simultaneamente não corrompem uns aos outros.
- **D — Durabilidade:** Confirmado com `COMMIT`, os dados sobrevivem mesmo se faltar energia elétrica 1 segundo depois.

---

### 📚 Parte 2 — As 5 Sublinguagens Oficiais da SQL (Questão Garantida na Prova!)

A **SQL** é dividida em **5 subconjuntos especializados de comandos**. A Fundação FAT adora criar tabelas misturando **DDL**, **DML** e **DQL** para confundir o candidato (**DS 2025 Q11**, **DS 2019 Q7**, **Apostas Q16**):

| Sublinguagem | Sigla em Inglês | Comandos Principais | Onde atua? (Macete definitivo) | Analogia de uma Pasta/Tabela Excel |
| :---: | :--- | :--- | :--- | :--- |
| **DDL** | *Data Definition Language* (Definição) | **`CREATE`**, **`ALTER`**, **`DROP`**, `TRUNCATE` | Atua na **ESTRUTURA (esqueleto)** do banco: cria tabela, adiciona coluna, muda tipo de coluna, apaga a tabela inteira! | **Construir, reformar ou demolir** a estante de aço. |
| **DML** | *Data Manipulation Language* (Manipulação) | **`INSERT`**, **`UPDATE`**, **`DELETE`** | Atua nos **DADOS (linhas/registros)** dentro da tabela já existente. | **Colocar, trocar ou retirar** pastas de dentro da estante. |
| **DQL** | *Data Query Language* (Consulta) | **`SELECT`** *(com `FROM`, `WHERE`, `JOIN`, `ORDER BY`)* | Apenas **CONSULTA / LÊ** os dados sem alterá-los. *(Nota: alguns autores antigos põem dentro de DML, mas a **FAT cobra separadamente como DQL**!)* | **Procurar e ler** uma pasta sem modificá-la. |
| **DCL** | *Data Control Language* (Controle) | **`GRANT`**, **`REVOKE`** | Gerencia **PERMISSÕES e SEGURANÇA** de acesso de usuários. | **Dar ou tomar a chave** do arquivo de um funcionário. |
| **TCL** | *Transaction Control Language* (Transação) | **`BEGIN`**, **`COMMIT`**, **`ROLLBACK`**, `SAVEPOINT` | Controla **TRANSAÇÕES**: confirma definitivamente (`COMMIT`) ou desfaz alterações (`ROLLBACK`) em caso de erro. | **Carimbar "Aprovado"** no Pix ou **cancelar tudo** se falhou. |

#### 💻 Script SQL Completo Comentado Linha por Linha (Do Zero até Consultas e Transações)

```sql
-- ==================== 1. DDL (ESTRUTURA) ====================
CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,   -- Identificador único obrigatório
    nome VARCHAR(100) NOT NULL,          -- Texto variável até 100 letras
    turma VARCHAR(10),
    nota DECIMAL(4,2)
);

-- Esqueci a coluna de email! Uso ALTER TABLE (DDL) para modificar a estrutura:
ALTER TABLE alunos ADD email VARCHAR(120);

-- ==================== 2. DML (REGISTROS / LINHAS) ====================
INSERT INTO alunos (nome, turma, nota, email)
VALUES
    ('Lucas Ferreira', '2MTEC', 8.50, 'lucas@etec.sp.gov.br'),
    ('Ana Beatriz',    '2MTEC', 9.20, 'ana@etec.sp.gov.br'),
    ('Bruno Costa',    '1MTEC', 5.80, 'bruno@etec.sp.gov.br'),
    ('Carla Dias',     '2MTEC', 7.00, 'carla@etec.sp.gov.br');

-- Bruno fez recuperação e foi para 6.50. ATENÇÃO AO WHERE!!
UPDATE alunos SET nota = 6.50 WHERE id = 3;

-- Se quiser remover apenas o aluno de id = 3 (tabela continua existindo!):
DELETE FROM alunos WHERE id = 3;

-- ==================== 3. DQL (CONSULTAS / LEITURA) ====================
-- Listar nome e nota dos aprovados do 2MTEC ordenados da maior nota para a menor:
SELECT nome, nota
FROM alunos
WHERE turma = '2MTEC' AND nota >= 6.0
ORDER BY nota DESC;

-- ==================== 4. DCL & 5. TCL ====================
GRANT SELECT ON alunos TO professor_estagiario;  -- DCL: dá permissão apenas de leitura
REVOKE SELECT ON alunos FROM professor_estagiario; -- DCL: retira a permissão

BEGIN;                                           -- TCL: inicia bloco transacional seguro
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;                                          -- TCL: grava os dois juntos! (Se desse erro, usaria ROLLBACK)
```

> [!CAUTION]
> **PEGADINHA Nº 1 (`DROP` vs `DELETE` — DS 2025 Q11):**
> - `DROP TABLE alunos;` é **DDL**: **destrói a tabela inteira e seu desenho**. Se rodar `SELECT * FROM alunos` depois, dá erro *"Tabela não existe"*.
> - `DELETE FROM alunos WHERE ...;` é **DML**: apaga **linhas/registros**, mas a estrutura da tabela continua viva!
> - E **esquecer o `WHERE`** num `UPDATE` ou `DELETE` altera ou apaga **TODAS as linhas da tabela**!

---

### 📚 Parte 3 — Dominando `WHERE`, Operadores Lógicos e Funções de Agregação (`COUNT(*)`)

#### 1. Ordem Mental de Execução do `SELECT` *(INFO 2025 Q28)*
A cláusula **`WHERE`** serve exclusivamente para **filtrar registros** segundo condições verdadeiras ou falsas:
- `WHERE cidade = 'São Paulo' AND idade >= 18`: só traz se **ambas** forem verdadeiras.
- `WHERE turma = 'A' OR turma = 'B'`: basta **uma** ser verdadeira.
- `WHERE nome LIKE 'An%'`: começa com `"An"` (`%` substitui qualquer sequência de caracteres).
- `WHERE nota BETWEEN 6 AND 10`: intervalo fechado de 6 a 10.
- `ORDER BY nome ASC` (crescente A–Z, padrão) ou `DESC` (decrescente Z–A / maior para menor).

#### 2. `COUNT(*)`, `SUM()`, `AVG()`, `MAX()` e `MIN()` *(DS 2025 Q14)*
Observe a diferença entre **contar linhas** e **somar valores** na tabela `vendas`:

| `id_venda` | `vendedor` | `cidade` | `valor` |
| :---: | :--- | :--- | :---: |
| `1` | João | São Paulo | `200` |
| `2` | Maria | Campinas | `500` |
| `3` | Pedro | São Paulo | `150` |

- `SELECT COUNT(*) FROM vendas WHERE cidade = 'São Paulo';` → Retorna **`2`**! *(Existem **2 linhas/vendas** em São Paulo — `COUNT(*)` conta linhas, **NÃO** soma `200 + 150`!)*
- `SELECT SUM(valor) FROM vendas WHERE cidade = 'São Paulo';` → Retorna **`350`** (`200 + 150`, soma valores numéricos).
- `SELECT AVG(valor) FROM vendas WHERE cidade = 'São Paulo';` → Retorna **`175`** (média aritmética: `350 / 2`).
- `SELECT MAX(valor) FROM vendas;` → Retorna **`500`** | `MIN(valor)` → **`150`**.

> [!CAUTION]
> **Pegadinha clássica da DS 2025 Q14:** A banca escreve comandos SQL errados como `SELECT * FROM clientes WHERE COUNT(cidade) = 'São Paulo';` ou coloca `FROM` depois do `WHERE`. **Regra inviolável da sintaxe SQL:** **`COUNT(*)` fica SEMPRE na cláusula `SELECT`** (entre `SELECT` e `FROM`), e **JAMAIS** dentro do `WHERE`! A ordem fixa sempre é **`SELECT ... FROM ... WHERE ... ORDER BY ...`**.

---

### 📚 Parte 4 — Bancos NoSQL (*Not Only SQL* — INFO 2025 Q29 & Apostas Q18)

O modelo relacional (SQL) exige tabelas rígidas com colunas pré-definidas (*schema* fixo) e cresce principalmente **verticalmente** (colocando um servidor mais caro/potente). Quando empresas como Netflix, Instagram e Amazon passaram a lidar com **terabytes por dia de dados variados (Big Data)** espalhados em milhares de servidores comuns (**escalabilidade horizontal**), popularizaram-se os bancos **NoSQL** (*"Não Apenas SQL"*).

#### Características Centrais do NoSQL
1. **Esquema Flexível (*Schema-less*):** Na mesma coleção de produtos, o tênis pode ter campo `numeracao: 41` e o notebook pode ter `ram_gb: 16`, sem precisar de `ALTER TABLE` nem deixar colunas cheias de `NULL`!
2. **Escalabilidade Horizontal (*Sharding*):** Fácil de dividir os dados entre dezenas/centenas de máquinas em rede.
3. **Sem JOINs complexos:** Prioriza velocidade de leitura armazenando objetos relacionados já aninhados juntos.

#### As 4 Famílias Famosas de NoSQL

| Família NoSQL | Como guarda os dados | Exemplos famosos | Caso de uso real |
| :--- | :--- | :--- | :--- |
| **1. Documentos** | Objetos **JSON / BSON** flexíveis agrupados em coleções | **MongoDB**, CouchDB, Firebase Firestore | Catálogos de e-commerce, perfis de usuários, apps móveis |
| **2. Chave-Valor (*Key-Value*)** | Dicionário gigante ultrarrápido na memória RAM (`chave -> valor`) | **Redis**, Amazon DynamoDB | Cache de páginas, carrinhos temporários, tokens de sessão |
| **3. Colunar (*Wide-Column*)** | Famílias de colunas esparsas otimizadas para escrita massiva | Apache **Cassandra**, HBase | Telemetria IoT de milhões de sensores, histórico de logs |
| **4. Grafos (*Graph*)** | Nós (entidades) e arestas (conexões diretas) | **Neo4j** | Redes sociais (*"amigos de amigos"*), detecção de fraudes, recomendações |

**Exemplo real de Documento JSON no MongoDB (note como telefones e endereço moram aninhados sem precisar de JOIN!):**
```json
{
  "_id": "user_901",
  "nome": "Henrique Silva",
  "curso": "DS M-Tec",
  "telefones": ["1199999-0001", "1198888-0002"],
  "endereco": { "cidade": "São Paulo", "uf": "SP" }
}
```

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q11 & DS 2019 Q7 — Sublinguagens SQL)
*Considere as afirmações: I. Os comandos `CREATE`, `ALTER` e `DROP` fazem parte da DDL, responsável pela estrutura do banco. II. `SELECT` pertence à DQL, permitindo consultar registros sem modificar tabelas. III. `INSERT`, `UPDATE` e `DELETE` pertencem à TCL, pois salvam ou desfazem transações.*
- **Item I:** VERDADEIRO.
- **Item II:** VERDADEIRO.
- **Item III:** **FALSO**! `INSERT`, `UPDATE` e `DELETE` são **DML** (manipulação de dados). Quem pertence à **TCL** são `COMMIT`, `ROLLBACK` e `SAVEPOINT`.

#### Questão Resolvida 2 (Baseada em DS 2025 Q14 & INFO 2025 Q28)
*Para descobrir quantos alunos têm nota maior ou igual a 7 na tabela `notas`, qual comando SQL é sintaticamente e logicamente correto?*
- `A) SELECT COUNT(*) FROM notas WHERE nota >= 7;` → **CORRETA!** Ordem exata `SELECT ... FROM ... WHERE ...` e `COUNT(*)` contando as linhas filtradas.
- *B) SELECT * FROM notas WHERE COUNT(nota) >= 7;* → **ERRADA!** `COUNT` jamais entra direto dentro do `WHERE`.


---

## Dia 7 — Modelagem de Dados (Conceitual, Lógico, Físico), DER, Chaves, Cardinalidades e Normalização (1FN–3FN)

### 🎯 Contexto no Mundo Real: Por que Bancos Mal Projetados Perdem Dados?

Imagine uma escola que cria uma única planilhona gigante chamada `MATRICULAS` onde cada linha repete: nome do aluno, CPF, três telefones colados juntos na mesma célula (`"11999-1111, 11888-2222"`), nome do curso e telefone da coordenação do curso.
Veja os **3 pesadelos** que acontecem nessa tabela não normalizada:
1. Se 500 alunos cursarem *Desenvolvimento de Sistemas* e o telefone da coordenação mudar, você terá que atualizar 500 linhas (e se esquecer 1 linha, o banco fica inconsistente!).
2. Se um professor criar um curso novo que ainda não tem nenhum aluno matriculado, você **nem consegue cadastrar o curso** porque precisa inventar um aluno para preencher a linha (**anomalia de inserção**)!
3. Se o único aluno de um curso trancar a matrícula e for deletado, você **perde para sempre o cadastro do curso** (**anomalia de exclusão**)!

Para evitar esses desastres reais, usamos a **Modelagem em 3 Níveis** e a **Normalização (1FN, 2FN e 3FN)**!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Pensa no **Discord**: você pode mudar seu *username* e apelido no servidor toda semana, mas por trás existe um **`User ID` numérico único** (`18 dígitos`) que **nunca muda e nunca se repete** — essa é sua **Chave Primária (PK)**!

- **Chave Estrangeira (FK) e `1:N`:** Um servidor tem **muitos** canais de texto, mas cada canal pertence a **um único** servidor. A FK `id_servidor` sempre vai dentro da tabela `CANAIS` (lado `N`!).
- **`N:N` (Muitos para Muitos):** Um usuário entra em **vários** servidores do Discord, e um servidor tem **vários** usuários. Para ligar os dois no banco relacional, cria-se a **3ª Tabela Associativa `MEMBROS_SERVIDOR`** (guardando `id_usuario FK` + `id_servidor FK` + cargos!).
- **Atributo Derivado:** O texto *"Conta criada há 3 anos"* ou *"Winrate: 58%"* não precisa ficar salvo fixo — o sistema calcula na hora usando `data_criacao` ou `vitorias / partidas`!
- **1ª Forma Normal (1FN):** Imagina salvar o inventário inteiro num texto só: `itens = "Espada, Escudo, Poção"`! Fica horrível para buscar ou dropar só a poção. Colocar na **1FN** significa ter **apenas 1 valor atômico por célula** (uma tabela separada `INVENTARIO` com 1 linha para cada item)!

---

### 📚 Parte 1 — As 3 Etapas da Modelagem de Dados *(Apostas Q14)*

| Etapa | Nível de Abstração | Como é representada e para que serve | Exemplo na Etec |
| :--- | :--- | :--- | :--- |
| **1. Modelo Conceitual** | Mais alto nível (próximo ao usuário/negócio) | Feito com **DER (Diagrama Entidade-Relacionamento, notação de Peter Chen)**. Mostra entidades, relacionamentos e atributos principais, **100% independente de software/SGBD**. | Retângulo `ALUNO` conectado pelo losango `CURSA` ao retângulo `DISCIPLINA` (`N:N`). |
| **2. Modelo Lógico** | Intermediário (estrutural) | Converte o DER em **Tabelas do Modelo Relacional**, define **Chaves Primárias (PK)**, **Chaves Estrangeiras (FK)** e resolve relacionamentos `N:N` criando tabelas intermediárias. Ainda independe do fornecedor específico. | `ALUNO(id_aluno PK, nome)` / `DISCIPLINA(id_disc PK, titulo)` / `MATRICULA(id_aluno FK, id_disc FK, ano)`. |
| **3. Modelo Físico** | Mais próximo da máquina (implementação real) | Script **`CREATE TABLE`** escrito no dialeto exato do SGBD escolhido (MySQL, PostgreSQL, SQL Server), definindo tipos exatos (`INT`, `VARCHAR(80)`), índices, *constraints* e armazenamento. | `CREATE TABLE aluno (id_aluno INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(80) NOT NULL);` |

---

### 📚 Parte 2 — Vocabulário Formal Relacional & Tipos de Atributos no DER

Na prova teórica, a Fundação FAT exige a correspondência entre os nomes acadêmicos do **Modelo Relacional (Edgar Codd)** e os nomes práticos *(DS 2025 Q12)*:

| Nome Formal na Prova | Equivalente Prático | Exemplo |
| :--- | :--- | :--- |
| **Relação (*Relation*)** | **Tabela** | A grade inteira `ALUNOS` |
| **Tupla (*Tuple*)** | **Linha / Registro** | `(1, 'Henrique', '2DS', '2010-05-14')` — representa um objeto/aluno completo |
| **Atributo (*Attribute*)** | **Coluna / Campo** | A coluna `nome` ou `data_nascimento` |
| **Domínio (*Domain*)** | **Tipo e faixa de valores válidos** | Para `nota`, apenas decimais de `0.0` a `10.0` |

#### Os 4 Tipos de Atributos no DER *(Apostas Q15)*
- **Atributo Simples (Atômico):** Indivisível em partes menores com sentido próprio (ex.: `cpf`, `sexo`, `nota`).
- **Atributo Composto:** Pode ser subdividido em vários sub-atributos menores (ex.: `Endereco` se divide em `logradouro`, `numero`, `bairro`, `cidade`, `cep`).
- **Atributo Multivalorado:** Pode armazenar **vários valores para uma mesma ocorrência** da entidade (ex.: uma pessoa pode ter vários `telefones` ou vários `idiomas`; desenhado com elipse dupla no DER — na hora de ir para a 1FN no banco relacional, vira uma nova tabela!).
- **Atributo Derivado (Calculado):** Seu valor **não precisa ser armazenado fisicamente**, pois é **calculado em tempo real** a partir de outros atributos guardados (ex.: **`idade`** calculada a partir da `data_nascimento`; **`valor_total`** = `quantidade * preco_unitario`; **`tempo_de_casa`** a partir de `data_admissao`). Desenhado com **elipse pontilhada/tracejada** no DER!

---

### 📚 Parte 3 — Chaves (`PK`, `FK`, Candidata/Alternativa) e Cardinalidades (`DS 2019 Q5 e Q9`)

#### 1. Os Tipos de Chaves
- **Chave Primária (*Primary Key* — `PK`):** Atributo (ou conjunto mínimo de atributos — *PK Composta*) escolhido para **identificar de forma única cada linha** da tabela.
  - **Duas regras sagradas da PK:** **NUNCA pode ter valor repetido** e **NUNCA pode ser nula (`NULL`)**!
- **Chave Candidata & Chave Alternativa *(DS 2019 Q9)*:** Suponha a tabela `FUNCIONARIO(id_func, cpf, rg, email, nome)`. Tanto `id_func`, quanto `cpf` e `email` identificam uma pessoa sem repetir — logo, todos são **Chaves Candidatas**. Escolhemos `id_func` como **Chave Primária (PK)**. Os outros candidatos únicos que sobraram (`cpf`, `email`) chamam-se **Chaves Alternativas (*Alternate Keys*)**!
- **Chave Estrangeira (*Foreign Key* — `FK`):** É uma coluna em uma tabela B que armazena o valor da **Chave Primária da tabela A**, criando o vínculo entre as duas.
  - **Integridade Referencial:** O SGBD impede gravar um `id_aluno = 999` numa tabela de `NOTAS` se não existir aluno `999` na tabela `ALUNOS`, e impede apagar um curso que ainda tenha alunos vinculados sem antes tratar as FKs!

#### 2. Cardinalidades e Como Viram Tabelas Reais
Representam quantos registros de uma tabela podem se ligar a quantos da outra:
1. **`1:1` (Um para Um):** Ex.: `PAIS` — `PRESIDENTE` ou `FUNCIONARIO` — `CRACHA`. Cada lado liga a no máximo 1 do outro. A FK é colocada em um dos lados (geralmente no lado opcional).
2. **`1:N` (Um para Muitos):** Ex.: Uma `TURMA` tem **vários** `ALUNOS`, e cada `ALUNO` pertence a **1** `TURMA`.
   - **Regra de ouro absoluta:** Na modelagem lógica/SQL, **a Chave Estrangeira (FK) SEMPRE vai para a tabela do lado `N` (Muitos)**!
   - Ou seja: `id_turma` fica dentro de **`ALUNO`** (nunca colocamos 40 colunas `id_aluno1, id_aluno2...` dentro de `TURMA`!).
3. **`N:N` (Muitos para Muitos):** Ex.: Um `ALUNO` cursa **várias** `DISCIPLINAS` e uma `DISCIPLINA` tem **vários** `ALUNOS`.
   - **Como resolver em bancos relacionais?** Como `N:N` não cabe diretamente com uma única FK de cada lado, **criamos obrigatoriamente uma 3ª Tabela Associativa (Intermediária)** — ex.: `MATRICULA(id_matricula PK, id_aluno FK, id_disciplina FK, media)` — que recebe as FKs das duas entidades originais!
4. **Auto-relacionamento (Relacionamento Unário / Recursivo — *DS 2019 Q5*):** Quando uma **tabela se relaciona com ela mesma**!
   - Exemplo clássico: Na tabela `FUNCIONARIO(id_func, nome, cargo, id_supervisor)`, alguns funcionários são supervisores de outros funcionários! Então a coluna `id_supervisor` é uma **FK dentro da tabela `FUNCIONARIO` que aponta para a PK `id_func` da própria tabela `FUNCIONARIO`**!

---

### 📚 Parte 4 — Normalização Passo a Passo: 1FN, 2FN e 3FN na Prática!

**Normalizar** é aplicar regras progressivas (Formas Normais) para eliminar redundâncias e anomalias de inserção/atualização/exclusão. Veja uma tabela caótica passar pelas **3 Formas Normais**:

#### Tabela Original Fora das Formas Normais (`PEDIDOS_BAGUNCADOS`)

| `id_pedido` | `id_cliente` | `nome_cliente` | `telefones_cliente` *(vários juntos!)* | `id_produto` | `nome_produto` | `qtd` |
| :---: | :---: | :--- | :--- | :---: | :--- | :---: |
| `101` | `5` | Lucas | `119999-1111, 118888-2222` | `10` | Teclado | `2` |

#### 🔹 Passo 1: Primeira Forma Normal (1FN) — *A CAMPEÃ DE PROVAS (DS 2025 Q13 & DS 2019 Q4)*
- **Regra da 1FN:** Todo atributo deve conter apenas **valores atômicos (indivisíveis)** — é proibido armazenar múltiplos valores separados por vírgula numa célula (atributos multivalorados) ou tabelas aninhadas (*grupos repetitivos*).
- **Como corrigimos na prática:** Retiramos `telefones_cliente` da tabela e criamos uma nova tabela ligada por FK (`CLIENTES_TELEFONES`) com **1 único número por linha**:

`PEDIDOS_1FN`: `(id_pedido, id_produto [PK composta], id_cliente, nome_cliente, nome_produto, qtd)` *(agora todas as células são atômicas!)*
`CLIENTES_TELEFONES`:
- `(id_tel=1, id_cliente=5, numero='119999-1111')`
- `(id_tel=2, id_cliente=5, numero='118888-2222')`

#### 🔹 Passo 2: Segunda Forma Normal (2FN) — *Elimina Dependência Parcial*
- **Regra da 2FN:** Já estar na **1FN** **+** quando a Chave Primária for **composta** (`id_pedido + id_produto`), nenhuma coluna não-chave pode depender de **apenas metade** da chave!
- Olhe `PEDIDOS_1FN`: `qtd` depende do pedido **e** do produto (OK!). Mas **`nome_produto`** depende **APENAS de `id_produto`** (não importa qual pedido seja!), e `id_cliente/nome_cliente` dependem só de **`id_pedido`**! Isso é **dependência parcial**!
- **Correção para 2FN:** Separamos em 3 tabelas coerentes:
  - `PEDIDO(id_pedido PK, id_cliente, nome_cliente)`
  - `PRODUTO(id_produto PK, nome_produto)`
  - `ITEM_PEDIDO(id_pedido FK, id_produto FK, qtd)` *(agora sim na 2FN!)*

#### 🔹 Passo 3: Terceira Forma Normal (3FN) — *Elimina Dependência Transitiva*
- **Regra da 3FN:** Já estar na **2FN** **+** nenhuma coluna não-chave pode depender de **outra coluna não-chave** (tudo depende *"da chave, apenas da chave e nada além da chave"*).
- Olhe `PEDIDO(id_pedido PK, id_cliente, nome_cliente)`: `id_cliente` depende de `id_pedido`, mas **`nome_cliente` depende de `id_cliente`**, que NÃO é a chave primária da tabela `PEDIDO`! (Se Lucas casar e mudar de nome, teríamos que atualizar 50 pedidos dele!).
- **Correção para 3FN:** Criamos a tabela `CLIENTE(id_cliente PK, nome_cliente)` e deixamos em `PEDIDO(id_pedido PK, id_cliente FK)`! **Banco 100% normalizado, limpo e sem redundâncias!**

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q13 & DS 2019 Q4 — 1FN)
*Uma tabela `FORNECEDORES(cnpj, razao_social, telefones_contato)` armazena na coluna `telefones_contato` o texto `"(11) 3333-1111; (11) 99999-2222"`. Qual forma normal foi diretamente violada e como corrigir?*
**Análise:** Uma célula contém dois valores (atributo multivalorado/não atômico). Isso viola diretamente a **1ª Forma Normal (1FN)**. Correção: criar tabela separada `TELEFONES_FORNECEDOR` referenciando `cnpj` por Chave Estrangeira, com apenas 1 telefone por registro/linha.

#### Questão Resolvida 2 (Baseada em DS 2019 Q5 & Apostas Q15 — Auto-relacionamento e Atributo Derivado)
*I. Em uma tabela `COLABORADOR`, o campo `id_lider` aponta para `id_colaborador` da própria tabela, configurando auto-relacionamento. II. O campo `valor_total` calculado multiplicando `quantidade * preco` no momento da consulta é um atributo derivado.*
**Análise:** Ambos os itens são **VERDADEIROS**! Esse é o exemplo clássico de auto-relacionamento `1:N` e atributo derivado no DER.


---

## Dia 8 — Design Digital, Teoria das Cores, Vetor vs. Bitmap, Bancos de Imagens, Gestalt, Tipografia e UX

### 🎯 Contexto no Mundo Real: Por que Sistemas Técnicos Precisam de Bom Design?

Você já entrou em um site onde a letra cinza clara quase some no fundo branco, os botões ficam todos espremidos sem saber qual confirma a compra, ou a logomarca da empresa aparece toda quadriculada ("pixelada") quando você dá zoom no celular? Mesmo que o back-end SQL e o código JavaScript funcionem perfeitamente, um design errado faz o usuário abandonar o sistema em segundos — e pior, se mandar uma arte digital em **RGB** para a gráfica imprimir um banner, as cores saem escuras e erradas porque impressoras usam **CMYK**!

A Fundação FAT dedica cerca de **4 a 5 questões por prova** diretamente a **Design Digital, Cores, Gestalt, Tipografia e Experiência do Usuário (UX)**.

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Todo setup de PC e todo jogo que você abre ilustra perfeitamente o módulo de Design Digital:

- **RGB vs. CMYK:** Os LEDs do seu teclado/gabinete **RGB** e o monitor do seu PC funcionam emitindo **LUZ** (`Red, Green, Blue` de `0` a `255` — somou tudo dá luz **branca**!). Já se você imprimir um pôster físico do seu jogo favorito numa gráfica, a impressora usa cartuchos de **TINTA CMYK** (*Ciano, Magenta, Amarelo e Preto*).
- **Hexadecimal `#RRGGBB`:** Sabe quando você escolhe a cor do cargo no Discord digitando `#5865F2` (Blurple do Discord) ou `#FF0000`? Aquilo é literalmente o **RGB escrito em Hexadecimal**!
- **Vetor (`.SVG`) vs. Bitmap (`.PNG`, `.JPG`):** Já chegou com a câmera bem colada numa parede ou placa num jogo e percebeu os **quadradinhos borrados (pixels)**? Isso é imagem **Bitmap / Raster**! Já o ícone de mira, logos em **`.SVG`** ou fontes do jogo continuam **100% lisos e nítidos** seja em 720p ou dando zoom de 800% em 4K porque são feitos por **fórmulas matemáticas (Vetor)**!
- **Gestalt e Nielsen na HUD:** No Discord, todos os canais de texto têm `#` e os de voz têm um alto-falante (Lei da **Semelhança**); os canais ficam agrupados debaixo da categoria certa (Lei da **Proximidade**); e o ícone de lixeira para deletar mensagem é **Equivalência com o Mundo Real (Nielsen)**!

---

### 📚 Parte 1 — Teoria das Cores: RGB, Hexadecimal, CMYK e Círculo Cromático

#### 1. Síntese Aditiva (RGB) vs. Síntese Subtrativa (CMYK)
Por que existem dois sistemas principais de cores? Porque **emissores de luz (telas)** funcionam de forma oposta a **pigmentos em papel (tintas)**!

| Sistema | Nome e Canais | Natureza Física | Onde é usado | Mistura Máxima vs. Zero |
| :--- | :--- | :--- | :--- | :--- |
| **RGB** | **R**ed (Vermelho), **G**reen (Verde), **B**lue (Azul)<br>Valores de **`0` a `255`** por canal (256³ = 16,7 milhões de cores) | **Síntese Aditiva (LUZ)** — quanto mais luz soma, mais claro fica! | **Telas digitais** (monitores, TVs, celulares, Web, Photoshop web) | `rgb(255, 255, 255)` = **BRANCO** (luz total)<br>`rgb(0, 0, 0)` = **PRETO** (ausência de luz) |
| **Hexadecimal** | `#RRGGBB` — usando base 16 (`0–9` e `A–F`) | É o **mesmo RGB traduzido para Hexadecimal!** | **Código CSS / HTML** e seletores de cor de UI | `#FFFFFF` = **BRANCO** (`255,255,255`)<br>`#000000` = **PRETO** (`0,0,0`)<br>`#FF0000` = Vermelho puro; `#2563EB` = Azul |
| **CMYK** | **C**yan (Ciano), **M**agenta, **Y**ellow (Amarelo), blac**K** (Preto)<br>Valores de **`0%` a `100%`** | **Síntese Subtrativa (TINTA)** — a tinta absorve luz refletida do papel branco. | **Impressão gráfica** (revistas, cartões de visita, banners, apostilas) | `0%, 0%, 0%, 0%` = papel branco<br>O **K (Preto)** existe porque misturar só C+M+Y gera marrom escuro impuro e gasta muita tinta. |

**Como ler qualquer código Hexadecimal em 3 segundos:**
Divida `#RRGGBB` em 3 pares: os 2 primeiros dígitos são **Vermelho (`RR`)**, os 2 do meio são **Verde (`GG`)**, os 2 últimos são **Azul (`BB`)**. Como `00` = zero e `FF` = `255` (máximo):
- `#00FF00` → zero vermelho, máximo verde, zero azul = **Verde puro**.
- `#FFFF00` → máximo vermelho + máximo verde = na luz RGB dá **Amarelo**!
- `#CCCCCC` ou `#808080` → os três canais com valor igual produzem sempre **tons de Cinza**!

#### 2. Círculo Cromático e Harmonias *(INFO 2025 Q9 & DS 2019 Q13)*
- **Cores Primárias (Modelo RBY tradicional / arte):** **Vermelho, Amarelo e Azul**. (Misturando duas primárias nascem as **Secundárias**: Laranja, Verde e Roxo; misturando primária + secundária nascem as **Terciárias**).
- **Cores Análogas:** Ficam **lado a lado** no círculo cromático (ex.: verde + verde-amarelado + amarelo) → visual calmo e harmônico.
- **Cores Complementares:** Ficam em **lados diretamente opostos** (180°) no círculo (ex.: azul × laranja; roxo × amarelo; vermelho × verde) → geram **máximo contraste** para chamar atenção em botões *Call-to-Action*!
- **Harmonia em Tríade *(DS 2019 Q13)*:** Conjunto de **3 cores equidistantes** no círculo cromático (formam um triângulo equilátero de 120°, como Vermelho + Amarelo + Azul).

> [!CAUTION]
> **Pegadinha da DS 2025 Q15 (Molde 2):** A banca pede a alternativa com *"exclusivamente padrões de representação de cores"* e coloca como intrusos palavras como **"CSS"**, **"HTML"**, **"Primária"** ou **"Bitmap"** no meio de `RGB`, `CMYK` e `Hexadecimal`! Só são sistemas de cores: **`RGB`**, **`CMYK`**, **`Hexadecimal`** (e eventualmente `HSL`/`HSB`).

---

### 📚 Parte 2 — Imagem Vetorial vs. Bitmap (Raster), Rasterização e Bancos de Imagens

Essa é uma das diferenças técnicas mais fáceis de visualizar e mais cobradas pela banca (**DS 2025 Q18** & **INFO 2025 Q10**):

| Característica | Imagem Vetorial | Imagem Bitmap (Matricial / Raster) |
| :--- | :--- | :--- |
| **Como é formada** | **Fórmulas e equações matemáticas** (coordenadas de pontos, linhas, polígonos e curvas de Bézier) | **Grade (matriz) fixa de pixels** (milhares de quadradinhos coloridos) |
| **Quando dá zoom (800%)** | **Recalcula a matemática na hora:** bordas permanecem **100% nítidas e lisas**, sem jamais perder qualidade! | **Pixela / serrilha:** os quadrados individuais aumentam e a imagem fica **borrada / quadriculada**! |
| **Para que serve** | **Logotipos, ícones, tipografia, ilustrações planas, gráficos técnicos** | **Fotografias reais** (onde milhões de variações de luz/pele não cabem em formas geométricas simples) |
| **Formatos na prova** | **`.SVG`** (web/HTML), **`.PDF`** (quando salva vetores), **`.AI`** (Illustrator), **`.CDR`** (CorelDraw), **`.EPS`** | **`.JPEG`/`.JPG`** (compressão c/ perda para fotos, **sem transparência**), **`.PNG`** (compressão sem perda + **suporta fundo transparente**), **`.BMP`**, **`.GIF`**, **`.WEBP`** |

- **O que é Rasterização? *(INFO 2025 Q10)*:** É o processo de **converter uma imagem vetorial em bitmap (grade de pixels)** para ser exibida numa tela ou impressa (ex.: exportar um logo `.SVG` para `.PNG` em `1024×1024 px`).
- **Resolução: PPI vs. DPI:** **PPI** (*Pixels Per Inch*) refere-se à densidade da tela digital; **DPI** (*Dots Per Inch*) refere-se aos pontos de tinta da impressora (`300 DPI` é o padrão de alta qualidade para impressão gráfica, enquanto `72–96 PPI` bastava para monitores antigos).

#### Bancos de Imagens e Direitos Autorais *(DS 2025 Q16)*
Achar uma imagem no Google Imagens **NÃO** dá direito de uso comercial nem escolar livre!
- **Domínio Público / `CC0`:** Autor liberou direitos ou prazo legal expirou — uso 100% livre até comercialmente.
- ***Creative Commons* (`CC`):** Licença padronizada gratuita onde o autor escolhe condições: **`BY`** (exige dar crédito ao autor), **`NC`** (proíbe uso comercial), **`ND`** (proíbe modificar/derivar).
- ***Royalty-Free* (Livre de Royalties):** Significa que você paga **uma única vez** (ou assina um banco como Shutterstock/Adobe Stock) e pode usar a foto várias vezes sem pagar taxa adicional por cada cópia impressa ou visualização. (**Atenção:** *"Royalty-Free"* NÃO significa necessariamente *"de graça"*, e sim *"sem royalties recorrentes por tiragem"*!).

---

### 📚 Parte 3 — Princípios da Gestalt na Design & Interfaces *(DS 2025 Q17)*

A **Gestalt** é uma escola da psicologia alemã que mostra como o cérebro humano **organiza visualmente o todo antes das partes**. Designers usam essas leis para deixar telas intuitivas:

| Lei da Gestalt | O que o cérebro faz | Exemplo real em Aplicativos / Interfaces Web |
| :--- | :--- | :--- |
| **1. Proximidade** | Elementos **fisicamente próximos** são percebidos como pertencentes ao **mesmo grupo**. | Num formulário de cadastro, o texto *"CPF:"* fica bem colado à sua caixinha e mais afastado do campo *"Senha:"* abaixo — você não precisa de linha separando para saber qual rótulo pertence a qual caixa! *(Apostas Q21)* |
| **2. Semelhança** | Elementos com **mesma cor, forma ou tamanho** são interpretados como tendo a mesma função. | Todos os links clicáveis num texto são sublinhados e azuis; todos os botões principais do site têm o mesmo formato arredondado verde. |
| **3. Fechamento** | Quando uma figura tem traços interrompidos ou falhas, o cérebro **completa os espaços vazios mentalmente** para enxergar a forma fechada inteira. | Logotipo do panda da **WWF**, logo da **IBM** feito só com listras horizontais ou ícone de carregamento tracejado. |
| **4. Continuidade** | O olhar segue naturalmente o alinhamento contínuo de curvas ou linhas retas sem quebras bruscas. | Barra de progresso horizontal, carrossel de cards ou alinhamento de ícones em coluna numa barra lateral. |
| **5. Figura e Fundo** | O cérebro separa o **objeto de foco (figura)** do **cenário (fundo)**. | Modal de alerta escurecendo o resto do site atrás; alto contraste entre texto escuro e fundo claro garante legibilidade rápida. |

---

### 📚 Parte 4 — Tipografia, Google Fonts e Heurísticas de Nielsen (UX)

#### 1. Classificação Tipográfica *(DS 2019 Q14 & INFO 2025 Q15)*
- **Fontes Serifadas** (*Times New Roman*, *Georgia*): Possuem pequenos traços de acabamento ("pezinhos"/serifas) nas pontas das hastes, ajudando a guiar o olho em **textos impressos longos** (livros, jornais).
- **Fontes Sem Serifa (*Sans-Serif*)** (*Arial*, *Roboto*, *Inter*, *Helvetica*): Hastes limpas e geométricas sem enfeites — padrão ouro para **telas digitais, menus e apps** pela nitidez mesmo em pixels pequenos.
- **Fontes *Script* / Caligráficas *(DS 2019 Q14)*:** Imitam **escrita à mão / letra cursiva fluida**. São excelentes para convites elegantes, logotipos ou títulos decorativos, mas **péssimas para parágrafos longos** por cansarem a leitura!
- **Fontes Monoespaçadas** (*Consolas*, *Fira Code*, *Courier New*): Cada letra ocupa exatamente a mesma largura — padrão em **editores de código-fonte e terminais** para alinhar indentação!
- **Google Fonts *(INFO 2025 Q15)*:** Biblioteca online gratuita de fontes web que você importa com `<link>` no `<head>` do HTML (e usa no CSS via `font-family`), garantindo que o site exiba exatamente aquela fonte em qualquer PC/celular sem depender das fontes já instaladas no Windows do usuário!

#### 2. UX & Heurísticas de Usabilidade de Jakob Nielsen *(DS 2019 Q15)*
**UI (*User Interface*)** cuida da aparência visual (botões, cores, fontes); **UX (*User Experience*)** cuida de toda a jornada de satisfação, facilidade e eficiência do usuário ao resolver seu problema. As heurísticas de Nielsen mais cobradas:
1. **Equivalência entre o sistema e o mundo real *(DS 2019 Q15)*:** O sistema deve **falar a linguagem e usar conceitos familiares do usuário**, com metáforas reais e ordem lógica natural — ex.: usar o ícone de **lixeira** para apagar, **carrinho de compras** no e-commerce e texto *"Sem conexão com a internet"* em vez de `"ERR_NETWORK_RESET_0x8004"`.
2. **Visibilidade do status do sistema:** Manter o usuário informado do que está acontecendo em tempo hábil (barra de carregamento `%`, mensagem *"Salvando..."*, alerta *"E-mail enviado!"*).
3. **Prevenção de erros:** Mais vale impedir o erro do que exibir mensagem bonita depois — ex.: pedir confirmação *"Tem certeza que deseja excluir sua conta permanentemente?"* antes de apagar.
4. **Consistência e padrões:** Não mudar o significado de cores/ícones (botão vermelho normalmente é cancelar/excluir; disquete/nuvem é salvar).

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q17 & Q18 — Vetor e Gestalt)
*Um designer criou um logotipo em SVG e precisou aplicá-lo tanto no ícone do app (48px) quanto num painel de 4 metros de altura sem serrilhamento. No layout da tela de login, colocou cada rótulo encostado em seu respectivo campo de texto e usou ícones vermelhos em todas as mensagens de erro. Identifique os conceitos aplicados:*
**Análise:**
- Logo em **`.SVG`** ampliado sem serrilhar = **Imagem Vetorial** (baseada em equações matemáticas, não pixels).
- Rótulo próximo ao campo formando unidade visual = Lei da **Proximidade** (Gestalt).
- Todos os erros com a mesma cor vermelha agrupados visualmente = Lei da **Semelhança** (Gestalt).

#### Questão Resolvida 2 (Baseada em DS 2019 Q15 & INFO 2025 Q9)
*Sobre Harmonia Cromática e UX: I. Cores análogas ficam frente a frente no círculo cromático buscando contraste máximo. II. Usar um ícone de carrinho de supermercado num site de vendas exemplifica a heurística de "equivalência entre o sistema e o mundo real" de Nielsen.*
**Análise:** **Item I é FALSO** — quem fica em lados opostos buscando máximo contraste são as **Complementares** (Análogas ficam *lado a lado*). **Item II é VERDADEIRO**.


---

## Dia 9 — Desenvolvimento Web Front-end: HTML5 Semântico, Links, Tabelas, Formulários, CSS Box Model, DOM e Cookies

### 🎯 Contexto no Mundo Real: O que Acontece Quando Você Abre um Site no Navegador?

Quando você digita `www.etec.sp.gov.br` ou abre sua conta na Shopee pelo Chrome/Edge, seu navegador recebe arquivos de texto puro vindos de um servidor e precisa transformá-los em milissegundos numa tela interativa. Para fazer isso sem virar bagunça, toda página web moderna trabalha em **3 camadas separadas** (a **Tríade da Web**), além de contar com pequenos arquivos locais no navegador (**Cookies**) para lembrar que você já fez login ou que há 2 produtos no seu carrinho!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Já apertou **`F12` (Inspecionar Elemento)** no Chrome para ver ou zoar o texto de uma página no navegador (só na sua tela!)? Aquilo funciona porque você está manipulando o **DOM** ao vivo na sua memória!

- **HTML / CSS / JS no Discord Web / Twitch:** O **HTML** monta as caixinhas de chat e lista de membros; o **CSS Box Model** dá o espaçamento interno dos balões de mensagem (`padding`), borda e distância entre usuários (`margin`); e o **JavaScript + DOM** faz aparecer uma mensagem nova no chat instantaneamente sem recarregar a aba inteira (`F5`)!
- **Cookies (~4 KB) no seu PC:** Como o **Discord Web**, o YouTube e a Twitch lembram que você já está logado com autenticação em 2 fatores sem pedir senha toda vez que abre o Chrome? Através de um **Cookie** — um arquivinho de texto minúsculo (**~4 KB**) salvo **LOCALMENTE dentro da pasta do navegador no SEU PC Windows 11** (e **NUNCA "na nuvem"**!). Se você apagar os cookies do navegador, desloga na hora!
- **`GET` vs. `POST`:** Quando você pesquisa `?search_query=minecraft` no YouTube, vai pela URL (**`GET`**); quando digita senha para logar na Steam, vai escondido no corpo da requisição (**`POST`**)!

---

### 📚 Parte 1 — A Tríade da Web & Anatomia Completa de uma Página HTML5

| Camada | Papel Exato | Analogia da Construção de uma Casa |
| :--- | :--- | :--- |
| **HTML5** (*HyperText Markup Language*) | **Estrutura e Conteúdo Semântico** — diz o que cada elemento *é* (título, menu, parágrafo, tabela, botão). *(**Atenção:** HTML **NÃO** é linguagem de programação, é linguagem de **marcação**!)* | **Paredes, colunas, portas e janelas** (estrutura bruta) |
| **CSS3** (*Cascading Style Sheets*) | **Estilo Visual e Layout** — cores, fontes, tamanhos, espaçamentos, grid, responsividade e animações. | **Pintura, iluminação, decoração e móveis** |
| **JavaScript (JS)** | **Comportamento e Interatividade** — validar senhas no clique, abrir menus, calcular carrinho e manipular o **DOM** sem recarregar a página. | **Eletricidade, portão automático e automação** |

#### 💻 Código Real Comentado: Página HTML5 Semântica Completa *(M-Tec Q38–40 & DS 2019 Q16)*

```html
<!DOCTYPE html>                    <!-- Declara ao navegador que o documento segue o padrão HTML5 -->
<html lang="pt-BR">                <!-- Tag raiz: document.documentElement no DOM! -->
<head>                             <!-- Cabeçalho INVISÍVEL: metadados, encoding, título da aba e links CSS -->
    <meta charset="UTF-8">         <!-- Garante acentos (ç, ã, é) corretos -->
    <title>Portal Etec DS</title>  <!-- Texto exibido na aba do navegador -->
    <link rel="stylesheet" href="estilos.css">
</head>
<body>                             <!-- CORPO VISÍVEL: tudo que o usuário enxerga na janela -->
    <header>                       <!-- Tag semântica: cabeçalho do site ou seção -->
        <h1>Desenvolvimento de Sistemas</h1>
        <nav>                      <!-- Tag semântica: barra de menu com links de navegação -->
            <a href="horarios.html">Mesma Aba (_self padrão)</a>
            <a href="https://cps.sp.gov.br" target="_blank" rel="noopener">Site CPS (Nova Aba)</a>
        </nav>
    </header>

    <main>                         <!-- Tag semântica: conteúdo principal único da página -->
        <section>                  <!-- Seção temática dentro do conteúdo -->
            <article>              <!-- Conteúdo independente reutilizável (notícia, post, card) -->
                <h2>Edital de Vagas Remanescentes</h2>
                <p>Prova em <span class="destaque">04 de dezembro</span>.</p>
            </article>
        </section>
        <div class="caixa-visual"> <!-- DIV: contêiner GENÉRICO em bloco SEM valor semântico! -->
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
> 1. **`<div>` e `<span>` NÃO são tags semânticas!** Elas servem apenas como caixas genéricas (`<div>` ocupa a largura inteira em bloco; `<span>` fica na mesma linha) quando nenhuma tag semântica faz sentido *(M-Tec 2022 Q38)*. Tags semânticas reais introduzidas no HTML5 incluem `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` e `<footer>` *(DS 2019 Q16)*.
> 2. **Tag `<a>` e `target="_blank"` *(DS 2025 Q20)*:** O atributo `href` define o endereço de destino e **`target="_blank"` força o link a abrir em uma NOVA ABA (ou nova janela)**. O comportamento padrão (`target="_self"`) abre na mesma aba atual.
> 3. **Visível x Metadados:** Tudo o que aparece na tela vai dentro de **`<body>`**, nunca dentro de `<head>` *(M-Tec 2022 Q40)*.

---

### 📚 Parte 2 — Listas, Tabelas HTML e Formulários HTTP (`GET` vs. `POST`)

#### 1. Listas (`<ol>` vs. `<ul>`) *(M-Tec 2022 Q39)*
- **`<ol>` (*Ordered List*):** Lista **ordenada / numerada** (`1., 2., 3.` ou `a., b., c.`) — usada quando a sequência importa (ex.: receita passo a passo).
- **`<ul>` (*Unordered List*):** Lista **não ordenada** (marcadores `•`, quadradinhos) — usada para itens sem ordem fixa (ex.: menu de links, lista de compras).
- Dentro de **ambas**, cada item individual é envolvido pela tag **`<li>`** (*List Item*).

#### 2. Tabelas HTML (`<table>`, `<tr>`, `<th>`, `<td>`) *(Apostas Q24)*
```html
<table>
    <thead>
        <tr>                        <!-- TR = Table Row: representa UMA LINHA inteira! -->
            <th>Matéria</th>        <!-- TH = Table Header: célula de cabeçalho (negrito/centralizada) -->
            <th>Nota</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Banco de Dados</td> <!-- TD = Table Data: célula comum com dado -->
            <td>9.5</td>
        </tr>
    </tbody>
</table>
```
**Pegadinha fatal:** **`<tr>` cria uma LINHA**; **`<td>` cria a CÉLULA (dado)**! Nunca confunda `<tr>` com célula nem `<td>` com título!

#### 3. Formulários HTML: `method="GET"` vs. `method="POST"` *(Apostas Q24)*

| Critério | `method="GET"` | `method="POST"` |
| :--- | :--- | :--- |
| **Onde os dados viajam?** | Anexados diretamente ao **final da URL** após `?` (ex.: `busca.php?termo=sql&pag=2`). | Enviados ocultos no **corpo (*body*) da requisição HTTP**. |
| **Segurança e Limite** | Expostos na barra de endereços e no histórico do navegador! Tamanho limitado pelo navegador. | **Não ficam expostos na URL!** Suporta grandes volumes e upload de arquivos/imagens. |
| **Quando usar na prática** | Pesquisas, filtros de busca, links compartilháveis. | **Login (usuário e senha!), cadastros, pagamentos, envio de dados sensíveis.** |

---

### 📚 Parte 3 — CSS3: Seletores, Anatomia da Regra, Box Model e `transform`

#### 1. Anatomia da Regra CSS e Seletores *(INFO 2025 Q14)*
```css
/* Seletor { propriedade: valor; } */
p { color: #1e293b; }           /* Seletor de TAG/ELEMENTO: atinge todos os <p> */
.cartao { padding: 16px; }      /* Seletor de CLASSE (.): pode repetir em vários elementos */
#menu-topo { height: 60px; }    /* Seletor de ID (#): identificador ÚNICO na página! */
```
*(Lembre da especificidade: um seletor `#id` é mais forte que uma `.classe`, que é mais forte que uma `tag`!).*

#### 2. CSS Box Model (*Modelo de Caixa* — *Apostas Q25*)
Para o CSS, **todo elemento HTML é uma caixa retangular** formada por **4 camadas concêntricas (de dentro para fora)**:
```text
┌─────────────── MARGIN (espaço EXTERNO entre caixas vizinhas) ───────────────┐
│ ┌───────────── BORDER (linha/borda visível da caixa) ───────────────────────┐ │
│ │ ┌─────────── PADDING (acolchoamento INTERNO entre conteúdo e borda) ────┐ │ │
│ │ │           CONTENT (texto, imagem: width x height)                     │ │ │
│ │ └───────────────────────────────────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────────┘
```
- **Troca clássica na prova:** Confundir **`padding`** (espaço **entre o texto/conteúdo e a borda**, dentro do fundo colorido do botão) com **`margin`** (espaço **para fora da borda**, empurrando outros elementos distantes).

#### 3. Propriedade CSS3 `transform` *(DS 2019 Q17)*
Permite mover, girar, inclinar e redimensionar elementos 2D/3D sem quebrar o fluxo da página:
- `transform: scale(1.3);` → **Aumenta ou diminui proporcionalmente** o tamanho (`1.3` = 130%).
- `transform: rotate(45deg);` → **Gira/rotaciona** o elemento em graus.
- `transform: translate(20px, -10px);` → **Desloca/move** horizontal e verticalmente.
- `transform: skew(15deg, 5deg);` → **Inclina/distorce** o ângulo dos eixos.

---

### 📚 Parte 4 — A Árvore DOM no JavaScript e Cookies HTTP

#### 1. Como o JavaScript Enxerga a Página: DOM *(Document Object Model — DS 2019 Q19)*
Quando o navegador lê o HTML, ele transforma cada tag em um **nó de uma árvore hierárquica na memória RAM** chamada **DOM**:
- Raiz da árvore: `document.documentElement` (o elemento `<html>`).
- Métodos clássicos cobrados pela banca FAT:
  - `document.getElementById("aviso")` → Captura o elemento que possui `id="aviso"`.
  - `document.querySelector(".card")` → Captura usando qualquer seletor CSS.
  - `document.createElement("li")` / `document.createTextNode("Novo item")` → Cria novos nós HTML ou de texto em memória.
  - `pai.appendChild(filho)` → Encaixa o novo nó dentro da página viva.
  - `elemento.parentNode` → Sobe um degrau acessando o **nó pai** daquele elemento na árvore!

#### 2. Cookies no Navegador: A Verdade Contra a Pegadinha! *(DS 2025 Q21)*
O protocolo HTTP é *stateless* (sem memória): por padrão, a cada clique num link, o servidor esquece quem você é! Para resolver isso, quando você faz login, o servidor pede ao seu navegador para gravar um **Cookie**.

**Fatos oficiais sobre Cookies (decore cada um deles):**
1. **O que são?** Pequenos **arquivos de texto simples** (par `chave=valor`, ex.: `tema=escuro`).
2. **Onde ficam armazenados?** **EXCLUSIVAMENTE NO NAVEGADOR / COMPUTADOR LOCAL DO USUÁRIO (CLIENTE)**! Eles trafegam nos cabeçalhos HTTP entre cliente e servidor, mas **NUNCA moram "na nuvem"** como um banco remoto!
3. **Qual o limite tradicional?** Cerca de **4 KB (~4.096 bytes)** por cookie! Não servem para guardar vídeos, fotos ou bancos pesados.
4. **Os 2 tipos quanto à validade:**
   - **Cookie de Sessão (*Session Cookie*):** Não define prazo de expiração (`Expires` / `Max-Age`). **Apaga-se automaticamente assim que o navegador é fechado**.
   - **Cookie Persistente / Permanente:** Tem data/tempo de expiração (`max-age=604800` para 7 dias). Continua salvo no disco do seu navegador mesmo após desligar e religar o PC!
5. **Manipulação:** Em JS lê/escreve via `document.cookie` (exceto quando o servidor ativa a flag de segurança **`HttpOnly`**, impedindo scripts maliciosos XSS de roubarem o cookie de sessão!).
6. **Comparação rápida com Web Storage:** Diferente de cookies (~4 KB enviados em toda requisição HTTP), **`localStorage`** e **`sessionStorage`** permitem guardar ~5–10 MB apenas localmente no navegador sem viajar em todo cabeçalho HTTP.

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q21 — Cookies)
*Analise as afirmativas sobre Cookies Web: I. Cookies são grandes arquivos multimídia armazenados diretamente nos servidores em nuvem da hospedagem. II. Cookies possuem tamanho pequeno (~4 KB) e ficam armazenados no navegador do usuário. III. Cookies podem ser temporários (de sessão, apagados ao fechar o browser) ou permanentes (com data de validade).*
- **Item I é FALSO:** Cookies são arquivos de **texto pequenos (~4 KB)** e ficam **no navegador local do cliente**, jamais na nuvem!
- **Itens II e III são VERDADEIROS.**

#### Questão Resolvida 2 (Baseada em M-Tec Q38–39 & Apostas Q24–25)
*Sobre HTML5 e CSS3: I. A tag `<tr>` representa uma célula de conteúdo na tabela e `<td>` cria uma linha. II. Formulários com senha devem usar `method="POST"` em vez de `GET` para não expor os campos na URL. III. No CSS Box Model, `padding` é o espaçamento interno entre conteúdo e borda.*
- **Item I é FALSO:** É exatamente o contrário (`<tr>` = linha / *table row*; `<td>` = célula / *table data*).
- **Itens II e III são VERDADEIROS.**


---

## Dia 10 — Sistemas Numéricos (Binário/Hexadecimal), Hardware, Memórias, SO, VMs/Docker e Linux

### 🎯 Contexto no Mundo Real: De Bits `0 e 1` até Servidores Linux na Nuvem

Dentro do chip do seu celular ou notebook não existem letras `'A'`, números `255` nem cores azuis `#2563EB` flutuando soltos. Tudo — cada pixel da tela, cada música MP3 e cada comando Python — é convertido para sequências elétricas binárias (**`0`** sem tensão / **`1`** com tensão). Para economizar espaço ao exibir longas sequências de 8, 16 ou 32 bits em endereços de memória e cores CSS, engenheiros agrupam bits em **Hexadecimal**.

Ao mesmo tempo, quando você abre o Windows ou roda servidores **Linux** usando **Máquinas Virtuais** ou **Contêineres Docker**, o **Sistema Operacional** precisa decidir o que fica na rápida **Memória RAM**, o que vai para o **SSD** e como organizar pastas do sistema sem deixar programas invadirem a memória uns dos outros.

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Se você já comparou placas/memórias, mexeu em pasta de jogo no Windows ou tentou hospedar um servidor de Minecraft/bot de Discord, você já conhece na prática o Dia 10:

- **SSD (Flash NAND) vs. HDD vs. RAM:** Por que instalar GTA/Valorant no **SSD** carrega o mapa em 3 segundos enquanto no **HD antigo (disco girando com agulha)** trava por 1 minuto? Porque o SSD usa chips **Flash NAND sem partes móveis**. E a **RAM** guarda só o que está **rodando aberto agora** (desligou o PC da tomada, zera na hora!).
- **Por que o jogo dá *stuttering* quando falta RAM?** Você abre Jogo pesado + Discord + 15 abas do Chrome numa máquina com pouca RAM. A RAM lota! Aí o **Sistema Operacional** usa **Memória Virtual (Arquivo de Paginação / *Swap*)**: pega partes da RAM e joga no **SSD/HD** para o PC não fechar os programas à força — como o SSD é bem mais lento que a RAM, o FPS cai na hora!
- **VM vs. Contêiner Docker:** Subir um servidor dedicado de Minecraft ou bot de Discord dentro de uma **VM** (VirtualBox) é instalar um Windows/Linux inteiro virtualizado só pra isso (come GBs de RAM!). Subir via **Contêiner Docker** isola só o app e suas libs **compartilhando o mesmo Kernel** do servidor — inicia em segundos!
- **Binário & Hex:** Aquele clássico código de erro/cor **`255`** (ex.: `255.255.255.0` no roteador ou `rgb(255,0,0)`) existe porque `255` é exatamente **1 Byte inteiro ligado (`11111111₂ = FF₁₆`)**!

---

### 📚 Parte 1 — Conversão Passo a Passo: Decimal ↔ Binário (Base 2) ↔ Hexadecimal (Base 16)

#### Vocabulário de Capacidade
- **1 Bit (*Binary Digit*):** Menor unidade de informação (`0` ou `1`).
- **1 Byte = 8 bits:** Consegue representar **`2⁸ = 256` valores diferentes** — em inteiros sem sinal, vai de **`0` (`00000000`) até `255` (`11111111`)**! *(É por isso que IPs `192.168.0.255` e cores RGB `rgb(255, 255, 255)` param exatamente em `255`!)*

#### A. Como Converter Decimal → Binário (2 Métodos para Conferir na Prova!)

**Método 1 — Régua das 8 Potências de 2 (o mais rápido na hora da prova!):**
Escreva as potências de 2 da direita para a esquerda em 8 casas:
`128 | 64 | 32 | 16 | 8 | 4 | 2 | 1`

Vamos converter **`100₁₀`** *(DS 2019 Q20)*:
- `128` cabe em 100? Não → bit `0`
- **`64`** cabe em 100? **Sim** → bit **`1`** (sobra `100 - 64 = 36`)
- **`32`** cabe em 36? **Sim** → bit **`1`** (sobra `36 - 32 = 4`)
- `16` cabe em 4? Não → bit `0`
- `8` cabe em 4? Não → bit `0`
- **`4`** cabe em 4? **Sim** → bit **`1`** (sobra `4 - 4 = 0`)
- `2` → `0`, `1` → `0`.
Resultado: **`01100100₂`** (ou `1100100₂`). Conferência: `64 + 32 + 4 = 100`!

**Método 2 — Divisões Sucessivas por 2 (`DIV 2` e `MOD 2`):**
Para **`250₁₀`**:
- `250 ÷ 2 = 125`, resto **`0`**
- `125 ÷ 2 = 62`, resto **`1`**
- `62 ÷ 2 = 31`, resto **`0`**
- `31 ÷ 2 = 15`, resto **`1`**
- `15 ÷ 2 = 7`, resto **`1`**
- `7 ÷ 2 = 3`, resto **`1`**
- `3 ÷ 2 = 1`, resto **`1`**
- `1 ÷ 2 = 0`, resto **`1`**
Lendo os restos **de baixo para cima**: **`11111010₂`** (`128+64+32+16+8+2 = 250`)!

#### B. Como Converter Decimal / Binário ↔ Hexadecimal (Base 16)
Como só temos 10 algarismos (`0` a `9`), a Base 16 usa **letras para representar de 10 a 15**:
`0..9` normal | **`A = 10`** | **`B = 11`** | **`C = 12`** | **`D = 13`** | **`E = 14`** | **`F = 15`**.

**Regra direta:** Divida por **`16`** ou separe o byte binário em **dois blocos de 4 bits** (cada grupo de 4 bits vale exatamente 1 dígito Hexadecimal, de `0` a `15`!):

Veja dois exemplos reais da **DS 2019 Q20**:
1. **Converter `100₁₀` para Hexadecimal:**
   - Divisão por 16: `100 ÷ 16` = quociente **`6`** (`6 × 16 = 96`), resto **`4`**. Logo, **`64₁₆`**!
   - *(Conferindo pelos 4 bits: `0110 | 0100` → esquerda `4+2 = 6`, direita `4` → `64₁₆`!)*
2. **Converter `250₁₀` para Hexadecimal:**
   - Divisão por 16: `250 ÷ 16` = quociente **`15`** (`15 × 16 = 240`), resto **`10`**.
   - Troca números $\ge 10$ pelas letras: `15 = F`, `10 = A`. Logo, **`FA₁₆`**!
   - *(Conferindo pelos 4 bits: `1111 | 1010` → esquerda `8+4+2+1 = 15 (F)`, direita `8+2 = 10 (A)` → `FA₁₆`!)*
3. **E `255₁₀` *(INFO 2025 Q4)*?** `1111 1111₂` = **`FF₁₆`** (o máximo de `#RRGGBB` no CSS!).

---

### 📚 Parte 2 — Arquitetura de Hardware & Hierarquia de Memórias

Na arquitetura clássica de **Von Neumann**, o computador integra **CPU** (Processador: **ULA** faz cálculos/lógica, **UC** coordena o fluxo e **Registradores** guardam dados imediatos), **Memória** e **Dispositivos de Entrada/Saída (E/S)** interligados por barramentos.

#### Hierarquia de Memórias (Quanto mais perto da CPU → Mais rápida, Menor capacidade, Maior custo/GB)

| Memória | Volátil? (Apaga sem energia?) | Tecnologia / Papel Oficial | Detalhe Cobrado pela FAT |
| :--- | :---: | :--- | :--- |
| **Registradores & Cache (L1/L2/L3)** | **Sim (Volátil)** | Estática (`SRAM`) dentro do próprio chip do processador. | Velocidade máxima; evita que a CPU espere a RAM ler dados repetidos. |
| **Memória RAM** *(Principal)* | **Sim (Volátil)** | Dinâmica (`DRAM` / DDR4, DDR5). | Carrega o Sistema Operacional e todos os programas/dados **em execução no momento**. Desligou o PC, zera! |
| **Memória ROM** *(BIOS / UEFI)* | **Não (Não volátil)** | Chips de leitura gravados com firmware de inicialização. | Executa o **POST** (autoteste de hardware ao ligar) e encontra o SSD/HD para iniciar o *boot*. |
| **SSD** *(Solid State Drive)* | **Não (Não volátil)** | Armazenamento secundário sólido usando **chips de memória Flash NAND**. | **Sem partes mecânicas móveis!** Muito mais rápido, silencioso e resistente a quedas/vibrações do que HDD. *(DS 2019 Q21)* |
| **HDD** *(Hard Disk Drive)* | **Não (Não volátil)** | Discos magnéticos giratórios com cabeça mecânica de leitura/escrita. | Barato por TB para guardar arquivos grandes/backups, porém mais lento e sensível a choques físicos. |

---

### 📚 Parte 3 — Sistema Operacional: Gerenciamento de Memória, VMs vs. Contêineres (Docker)

Um **Sistema Operacional (SO)** — como Windows, Linux, macOS ou Android — atua como o **intermediário** entre o hardware físico e o usuário/softwares (*M-Tec 2022 Q35*). Sua parte central chama-se **Kernel (Núcleo)**.

#### 1. Gerenciamento de Memória e Memória Virtual (*DS 2025 Q27*)
Quando você abre o Chrome (com 20 abas), VS Code e Spotify ao mesmo tempo, o SO é o gerente que garante que:
- **Proteção/Isolamento:** Um programa travado não consiga ler ou sobrescrever a memória RAM de outro processo nem do Kernel.
- **Alocação e Desalocação:** Entrega blocos de RAM para quem abre e recolhe de volta ao fechar (evitando vazamentos globais).
- **Memória Virtual (*Paginação / Swap*):** Se a RAM física de 8 GB encher, o SO pega blocos ("páginas") pouco usados no momento e move temporariamente para uma área reservada no **SSD/HD** (*arquivo de paginação / partição swap*). Isso impede o computador de fechar apps à força, **mas deixa o sistema lento** porque SSD/HDD é muito mais lento que a RAM!

#### 2. Virtualização Tradicional (VM) vs. Contêineres (Docker) *(INFO 2025 Q5 e Q16)*

| Critério | Máquina Virtual (VM — VirtualBox, VMware) | Contêiner (Docker / Podman) |
| :--- | :--- | :--- |
| **Como isola** | Um **Hypervisor** virtualiza hardware completo e roda **um Sistema Operacional convidado (*Guest OS*) inteiro** para cada VM. | Isola processos, arquivos e rede usando recursos nativos do kernel (*namespaces* e *cgroups*), **COMPARTILHANDO o mesmo Kernel do SO hospedeiro**! |
| **Peso e Velocidade** | **Pesada** (gigabytes por VM; demora minutos para ligar porque dá *boot* completo em outro Windows/Linux). | **Ultraleve** (megabytes; inicia em frações de segundo porque não carrega outro kernel!). |
| **Ideal para** | Rodar um Windows completo dentro de um Mac/Linux, isolamento máximo de hardware. | Empacotar aplicações web + dependências (*"funciona igual na minha máquina e no servidor"*). *(INFO 2025 Q16)* |

---

### 📚 Parte 4 — Sistema de Arquivos Linux (FHS), Comandos e Produtividade Windows/Word

#### 1. Diretórios Oficiais do Linux (FHS — *Filesystem Hierarchy Standard*) *(INFO 2025 Q18)*
No Linux não existem unidades `C:\` ou `D:\`! Tudo nasce de uma única árvore começando na **raiz `/`**. Memorize os 7 diretórios campeões de prova:
- **`/`**: Raiz absoluta do sistema de arquivos.
- **`/bin`** (e `/usr/bin`): Arquivos **binários executáveis** dos comandos essenciais do sistema (`ls`, `cp`, `cat`).
- **`/etc`**: Arquivos de **configuração** do sistema e servidores (`passwd`, `hosts`, configs do Apache/Nginx).
- **`/home`**: Pastas pessoais dos **usuários comuns** (ex.: `/home/lucas`).
- **`/root`**: Pasta pessoal exclusiva do **superusuário administrador (`root`)**. **Pegadinha:** `/root` NÃO é a raiz `/`, é apenas a pasta home do admin!
- **`/lib`**: **Bibliotecas** compartilhadas necessárias pelos binários.
- **`/usr`**: Softwares e utilitários instalados para uso dos usuários.
- **`/var`**: Dados **variáveis** que crescem com o tempo (especialmente **logs** em `/var/log`, filas de impressão/e-mail e caches).
- **`/tmp`**: Arquivos **temporários** (frequentemente apagados ao reiniciar).

> [!CAUTION]
> **Pegadinha famosa (INFO 2025 Q18 — Lista com Intruso):** A banca pergunta qual alternativa contém **APENAS diretórios padrão Linux** e enfia no meio `/mkdir`, `/ls`, `/rm`, `/cd`, `/cat` ou `/apt`! **`mkdir`, `ls`, `rm`, `cd`, `cat` são COMANDOS executados no terminal**, **NÃO são pastas do sistema!**

#### 2. Comandos Essenciais de Terminal Linux *(DS 2019 Q22)*
| Comando | Significado e Ação | Exemplo prático |
| :--- | :--- | :--- |
| **`pwd`** | *Print Working Directory*: mostra em qual pasta você está agora | `pwd` → `/home/lucas/projeto` |
| **`ls`** | *List*: lista arquivos e subpastas (`ls -la` mostra detalhado + ocultos iniciados por `.`) | `ls -l` |
| **`cd`** | *Change Directory*: entra ou volta de pasta (`cd ..` sobe um nível) | `cd /etc` |
| **`mkdir`** | *Make Directory*: cria uma nova pasta vazia | `mkdir fotos` |
| **`cp` / `mv`** | **`cp`** copia arquivo/pasta (`cp -r`); **`mv`** **move OU renomeia** arquivo! | `mv antigo.txt novo.txt` |
| **`rm`** | *Remove*: apaga arquivos (`rm -rf` apaga pastas recursivamente — cuidado!) | `rm teste.txt` |
| **`chmod`** | *Change Mode*: altera **permissões** de leitura (`r=4`), escrita (`w=2`), execução (`x=1`) | `chmod 755 script.sh` |

*(No ambiente Microsoft Office / Windows — INFO 2025 Q6 & Apostas Q30: no Word, listas com marcadores/numeração ficam na guia **Página Inicial**, e **Mala Direta** automatiza cartas personalizadas a partir de uma lista Excel; no Windows, `Ctrl+C`/`Ctrl+V`/`Ctrl+Z` e Gerenciador de Tarefas `Ctrl+Shift+Esc` encerram travamentos).*

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2019 Q20 & INFO 2025 Q4 — Conversões)
*Converta os valores decimais `255`, `100` e `250` para binário (8 bits) e hexadecimal.*
- `255` = `128+64+32+16+8+4+2+1` = **`11111111₂`** = **`FF₁₆`**.
- `100` = `64+32+4` = **`01100100₂`**; `100 ÷ 16` = `6` resto `4` = **`64₁₆`**.
- `250` = `128+64+32+16+8+2` = **`11111010₂`**; `250 ÷ 16` = `15(F)` resto `10(A)` = **`FA₁₆`**.

#### Questão Resolvida 2 (Baseada em INFO 2025 Q16 & Q18 — Contêineres e Linux)
*I. Contêineres Docker são idênticos a Máquinas Virtuais porque cada contêiner emula um hardware separado e instala um kernel Linux completo dentro dele. II. No Linux, `/etc` armazena configurações do sistema e `/var` guarda logs variáveis.*
- **Item I é FALSO:** Contêineres **compartilham o mesmo kernel** do SO hospedeiro (não instalam kernel/SO inteiro por dentro como VMs).
- **Item II é VERDADEIRO.**


---

## Dia 11 — Redes de Computadores (TCP/IP, E-mail, Topologias), Cloud, IoT, Inglês Técnico e Ética CPS

### 🎯 Contexto no Mundo Real: A Viagem de um Clique até Outro Continente

Quando você envia uma mensagem pelo WhatsApp, lê um e-mail no celular ou acessa um site seguro com cadeado (`https://`), seus dados não viajam "por mágica" em um único bloco gigante. Eles são picotados em **pacotes**, endereçados por **IP**, protegidos por criptografia **SSL/TLS**, atravessam **cabos submarinos ou Wi-Fi** ligados por switches e roteadores, chegam a servidores na **Nuvem (Cloud)** e retornam reconstruídos na sua tela! Além disso, esse módulo fecha **Inglês Técnico e Ética/LGPD**, garantindo **10 a 12 questões certeiras** numa prova de 30!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Tudo sobre **Ping, Redes, Discord e Cloud** fica muito mais claro pensando num PC Gamer conectado à internet:

- **TCP vs. UDP na Call do Discord e nos Jogos Online:**
  - Quando você baixa um jogo na Steam, cada byte precisa chegar inteirinho sem arquivo corrompido (mesmo que espere reenvio) → usa **TCP (confiável)**.
  - Quando você está em **call de voz no Discord** ou dando flick no CS2/Valorant, **velocidade em tempo real importa mais que recuperar pacote velho de 2 segundos atrás!** Por isso voz e movimento usam **UDP (rápido, sem confirmação)**.
- **DNS e DHCP do seu Roteador:** O **DHCP** entrega seu IP local (`192.168.1.X`) automaticamente quando o PC ou celular conecta no Wi-Fi. Já o **DNS** traduz `discord.com` no IP real do servidor (*colocar DNS `1.1.1.1` ou `8.8.8.8` às vezes melhora rotas exatamente por isso!*).
- **Topologia Estrela vs. Barramento em LAN House:** Numa **LAN House moderna (Estrela)**, todos os PCs ligam por cabo próprio num **Switch** no rack: se o cabo do PC-3 arrebentar, só o PC-3 cai; já numa rede antiga em **Barramento (*Bus*)**, se o cabo central partir, a LAN inteira cai junto!
- **Cloud nos Games (IaaS / PaaS / SaaS):**
  - **SaaS:** Discord Web, **GeForce NOW / Xbox Cloud Gaming** — você só entra e usa/joga pronto no navegador!
  - **PaaS:** Subir o código JS/Python do **seu Bot de Discord** na nuvem sem configurar sistema operacional.
  - **IaaS:** Alugar uma máquina virtual Linux crua (VPS) para configurar servidor de jogos/site do zero.

---

### 📚 Parte 1 — Arquitetura TCP/IP e Principais Protocolos da Internet *(DS 2025 Q25 & INFO 2025 Q25)*

Um **protocolo** é um conjunto formal de regras e formatos para que máquinas diferentes (um iPhone e um servidor Linux) consigam conversar no mesmo idioma. A Internet opera sobre a pilha **TCP/IP**, organizada classicamente em **4 camadas** (da mais próxima do usuário até o cabo/onda):

| Camada TCP/IP | Função Principal | Protocolos & Equipamentos Típicos |
| :--- | :--- | :--- |
| **4. Aplicação** | Onde os aplicativos conversam na rede (web, e-mail, arquivos, nomes). | **HTTP, HTTPS, FTP, SFTP, SMTP, POP3, IMAP, DNS, DHCP, SSH, RDP** |
| **3. Transporte** | Garante a comunicação ponta a ponta entre processos (portas), controle de fluxo e integridade. | **TCP** (confiável, exige confirmação/ACK — Web, E-mail, Bancos) vs. **UDP** (rápido sem confirmação — Vídeos ao vivo, Jogos online, VoIP, DNS) |
| **2. Internet (Rede)** | Endereçamento lógico global (**IP**) e escolha da melhor rota entre redes diferentes (**Roteamento**). | **IP (IPv4 32 bits / IPv6 128 bits)**, ICMP (`ping`), **Roteadores** |
| **1. Acesso à Rede (Enlace + Física)** | Transforma pacotes em quadros locais (endereço físico **MAC**) e transmite em sinais elétricos/luz/rádio. | **Ethernet** (cabos UTP/fibra), **Wi-Fi**, Placa de Rede, **Switch** (Camada 2) |

*(Atenção: Alguns materiais acadêmicos detalham o **Modelo OSI de 7 camadas** — Física, Enlace, Rede, Transporte, Sessão, Apresentação, Aplicação — mas na prova prática da FAT o padrão da Internet cobrado é o **TCP/IP em 4 camadas**!)*

#### Protocolos que Mais Caem na FAT:
- **HTTP vs. HTTPS *(INFO 2025 Q27)*:** HTTP (*HyperText Transfer Protocol*) trafega páginas web em texto aberto; **HTTPS** encapsula o HTTP dentro de criptografia **SSL/TLS** (cadeado no navegador), garantindo **confidencialidade e autenticidade** contra interceptação!
- **DNS (*Domain Name System*):** A "agenda telefônica" da internet — traduz nomes legíveis (`www.google.com`) em **endereços IP** numéricos (`142.250...`).
- **DHCP:** Atribui **endereços IP automaticamente** aos dispositivos que entram na rede Wi-Fi/cabo (sem precisar digitar IP manual).
- **FTP / SFTP:** Protocolos específicos para **transferência de arquivos** cliente ↔ servidor (`SFTP` com segurança SSH).
- **SSH vs. RDP *(INFO 2025 Q17)*:** Acesso remoto! **SSH** abre terminal de comandos criptografado (padrão Linux/servidores); **RDP (*Remote Desktop Protocol*)** da Microsoft acessa a **área de trabalho gráfica** remota do Windows.

---

### 📚 Parte 2 — Protocolos de E-mail: A Trinca de Ouro (SMTP, POP3, IMAP) + Webmail

Esse assunto caiu literalmente igual na **DS 2025 Q28** e na **INFO 2025 Q7 e Q26**! Nunca confunda os 3 papéis:

| Ferramenta / Protocolo | Direção | O que acontece na prática passo a passo | Cenário real |
| :--- | :---: | :--- | :--- |
| **SMTP** *(Simple Mail Transfer Protocol)* | **ENVIO / SAÍDA** | Envia a mensagem do seu aplicativo até seu servidor e transporta entre servidores de e-mail (`@etec` → `@gmail`). | Você clica em **Enviar** e a carta sai da sua caixa de saída. **SMTP NÃO serve para ler sua caixa de entrada!** |
| **POP3** *(Post Office Protocol v3)* | **RECEBIMENTO (Baixa)** | Conecta ao servidor, **faz o download das mensagens para o dispositivo local e, por padrão, APAGA do servidor**. | Se você baixar no notebook de casa via POP3, ao abrir o celular na rua os e-mails antigos **não estarão mais lá**! |
| **IMAP** *(Internet Message Access Protocol)* | **RECEBIMENTO (Sincroniza)** | **Mantém todos os e-mails e pastas no servidor remoto**, sincronizando o status (*lido/não lido/apagado*) em tempo real em todos os aparelhos. | Você lê um e-mail no celular e, quando abre o PC ou tablet, ele já aparece sincronizado como lido! |
| **Webmail** | Acesso via **Browser** | Interface acessada diretamente pelo navegador via **HTTP/HTTPS** (ex.: Gmail Web, Outlook.com), sem instalar cliente desktop (como Mozilla Thunderbird). | Abrir seu e-mail no Chrome em qualquer computador. |

> [!CAUTION]
> **Pegadinha clássica da DS 2025 Q28:** A banca cria uma tabela de itens I, II e III dizendo que *"SMTP sincroniza mensagens no servidor"* e *"IMAP apenas envia e-mails"*. Lembre sempre do macete: **S**MTP = **S**ubir / **S**air (Envio); **POP3** = **P**uxa para o PC e apaga; **IMAP** = espelho sincronizado no servidor!

---

### 📚 Parte 3 — Topologias de Rede, Cloud Computing, IoT e Navegadores

#### 1. Topologias de Rede *(DS 2025 Q26 & DS 2019 Q23)*

| Topologia | Desenho Físico / Como Liga | Ponto Forte | Ponto Fraco / Pegadinha de Prova |
| :--- | :--- | :--- | :--- |
| **Barramento (*Bus*)** *(DS 2025 Q26)* | Todos os computadores compartilham **UM ÚNICO cabo central (*backbone*)** com terminadores nas duas pontas. | Barata e usa pouco cabo. | **Ponto único de falha no cabo:** se o cabo principal romper em qualquer lugar, **A REDE INTEIRA CAI!** Além disso, só um transmite por vez (colisões). |
| **Estrela (*Star*)** *(DS 2019 Q23)* | Cada PC tem um cabo exclusivo indo até um **nó central concentrador (Switch ou Hub)**. | Se **o cabo de 1 PC romper, só ele para** — o resto da rede continua intacto! Fácil de dar manutenção. | Depende do nó central: se o **Switch** queimar ou desligar, a rede para. (Padrão moderno das redes cabeadas). |
| **Anel (*Ring*)** | Cada computador liga-se ao vizinho formando um circuito fechado; um sinal (*Token*) dá a volta dando vez de falar. | Fluxo ordenado sem colisões aleatórias. | Em anel simples sem redundância, se um nó falha, interrompe o ciclo. |
| **Malha (*Mesh*)** | Cada nó se conecta diretamente a **vários ou todos os outros nós** (múltiplos caminhos alternativos). | **Tolerância máxima a falhas!** Se um cabo cair, o tráfego desvia por outra rota. | Caríssima e complexa em cabeamento se tiver muitas máquinas. |
| **Híbrida** | Combina duas ou mais topologias (ex.: várias Estrelas ligadas em Barramento ou Malha). | Flexibilidade para grandes prédios e campi. | Maior complexidade de projeto e gerenciamento. |

#### 2. Computação em Nuvem (*Cloud Computing*) — Analogia da Pizzaria *(Apostas Q26)*
Imagine a diferença entre fazer tudo em casa e pedir delivery pronto para entender os **3 Modelos de Serviço Cloud**:
- **IaaS (*Infraestrutura como Serviço* — ex.: AWS EC2, Azure VMs, Google Compute Engine):** Você aluga hardware virtual na nuvem (CPU, RAM, disco, rede). É como **alugar a cozinha e o forno** — você mesmo instala o Sistema Operacional, banco, patches e sobe seu app!
- **PaaS (*Plataforma como Serviço* — ex.: Heroku, Vercel, Azure App Service):** O provedor já gerencia hardware, SO, firewall e runtime (Node/Python/Java). É como **comprar a massa e os ingredientes prontos** — o desenvolvedor só faz o deploy do **próprio código**!
- **SaaS (*Software como Serviço* — ex.: Google Docs, Gmail, Microsoft 365, Canva, Figma):** Software 100% pronto usado no navegador/app por assinatura ou grátis. É como **sentar na pizzaria e comer a pizza pronta** — você não instala nem programa nada!

#### 3. Internet das Coisas (IoT), Navegadores e Suítes *(DS 2025 Q24, Q29 e Q30)*
- **IoT (*Internet of Things*):** Conecta objetos físicos do cotidiano à rede usando **sensores** (leem temperatura, umidade, batimentos), **atuadores** e conectividade para trocar dados e agir automaticamente (ex.: semáforos inteligentes, sensores agrícolas, fechaduras e relógios smart).
- **Navegadores (*Browsers*)** *(DS 2025 Q29)*: Softwares clientes que interpretam HTML/CSS/JS — **Google Chrome, Mozilla Firefox, Microsoft Edge, Apple Safari, Opera, Brave**. **Intrusos clássicos da prova:** *Google Search* (é **buscador**, não navegador!), *Outlook*, *Excel* e *VS Code*.
- **Suítes de Produtividade** *(DS 2025 Q30)*: Conjuntos integrados de escritório (Editor de Texto + Planilha + Apresentações) como **Microsoft 365 / Office** (Word, Excel, PowerPoint), **LibreOffice** (Writer, Calc, Impress) e **Google Workspace** (Docs, Sheets, Slides).

---

### 📚 Parte 4 — Inglês Técnico & Ética Socioambiental CPS

Quase toda prova DS/Info começa com **Q1 a Q3 de Inglês** e **Q4 a Q6 de Ética/Cidadania**!

#### 1. Técnicas Rápidas e Vocabulário Obrigatório de Inglês Técnico *(DS 2025 Q1–Q3 & M-Tec Q7–Q9)*
- **Técnicas de leitura:**
  - *Skimming:* leitura panorâmica rápida no título e primeira frase de cada parágrafo para pegar a **ideia central**.
  - *Scanning:* busca dirigida de datas, números, siglas ou palavras específicas pedidas na questão.
- **Gramática que já caiu:**
  - **Comparativo / Superlativo irregular *(M-Tec 2022 Q7)*:** `bad → worse (pior que) → the worst (o pior)`; `good → better → the best`.
  - **Formação de palavras com prefixos/sufixos *(M-Tec 2022 Q9)*:** `-able / -ible` formam **adjetivos** indicando possibilidade (*debatable*, *scalable*, *readable*); `-ive` forma **adjetivos** (*positive*, *interactive*); `-tion / -ment / -ness` formam **substantivos**; `-ly` forma **advérbios**.
- **Falsos Cognatos (parecem português, mas significam outra coisa!):**
  - `data` = **dados** (NÃO é "datas" — data de calendário é *date*!).
  - `actually` = **na verdade** (NÃO é "atualmente" = *currently*).
  - `pretend` = **fingir** (NÃO é "pretender" = *intend*).
  - `library` = **biblioteca / biblioteca de código** (NÃO é "livraria" = *bookstore*).
  - `support` = **apoiar / dar suporte** (NÃO é "aguentar/suportar dor" = *bear/stand*).
- **Termos recorrentes de Soft Skills & TI:**
  `outcomes` (resultados/desfechos) • `troubleshooting` (diagnóstico e solução de falhas) • `critical thinking` (pensamento crítico) • `inference` (inferência/dedução implícita nas entrelinhas) • `daunting` (intimidante/assustador) • `bias` (viés/parcialidade algorítmica) • `awareness` (consciência).

#### 2. Ética em TI, Direitos Trabalhistas, Lixo Eletrônico e LGPD *(DS 2025 Q4–Q6)*
- **Ética para o Bem Comum:** Ações verdadeiramente éticas visam o impacto coletivo, transparência e respeito aos direitos humanos — rejeitando alternativas baseadas em *vaidade pessoal, autopromoção em redes sociais ou lucro acima da segurança*.
- **Sustentabilidade & Lixo Eletrônico (*e-waste*):** Baterias, placas e monitores contêm metais pesados (chumbo, mercúrio, cádmio). Nunca devem ir para o lixo comum! A postura ética correta exige **logística reversa / descarte em pontos de coleta recicladora certificados** e desenvolvimento de sistemas eficientes (TI Verde) sem induzir **obsolescência programada**.
- **LGPD (Lei Geral de Proteção de Dados):** Coleta mínima necessária de dados pessoais, finalidade explícita, consentimento do titular e proteção contra vazamentos.

---

### 🕵️‍♂️ Dissecando Questões no Estilo Exato da Prova

#### Questão Resolvida 1 (Baseada em DS 2025 Q26 & Q28 — Topologias e E-mail)
*Analise: I. Na topologia em Barramento, o rompimento do cabo backbone interrompe a comunicação de toda a rede. II. O protocolo POP3 envia mensagens do aplicativo cliente para o servidor de saída. III. O protocolo IMAP mantém os e-mails sincronizados no servidor para acesso em vários aparelhos.*
- **Item I:** VERDADEIRO.
- **Item II:** **FALSO** (quem envia é o **SMTP**; POP3 baixa e apaga).
- **Item III:** VERDADEIRO.

#### Questão Resolvida 2 (Baseada em DS 2025 Q1 & M-Tec Q7 — Inglês Técnico)
*No trecho "Effective troubleshooting produces reliable outcomes, even when legacy bugs feel daunting and represent the worst scenario", as palavras destacadas significam respectivamente:*
- `troubleshooting` = **solução/diagnóstico de problemas**; `outcomes` = **resultados**; `daunting` = **intimidante**; `worst` = **pior** (superlativo de *bad*).


---

## Dia 12 — Base Comum M-Tec I: Português, Interpretação, Literatura e História (1º Ano EM)

### 🎯 Contexto no Mundo Real: Por que Português e História Decidem Vagas no M-Tec?

Na prova de **Vagas Remanescentes do 2º Ano M-Tec (Ensino Médio Integrado ao Técnico)**, você não disputa apenas com quem decorou tags HTML: cerca de metade da prova oficial (*como vimos na prova real M-Tec 2022, questões Q1–Q6 e Q24–Q27*) cobra matérias da **Base Nacional Comum da 1ª Série do Ensino Médio**!

E tem mais um detalhe estratégico: saber **interpretar textos com precisão**, distinguir um **Paradoxo** de uma **Antítese**, separar **Cultismo** de **Conceptismo** e dominar a passagem do **Paleolítico ao Neolítico** também afia diretamente seu olhar para as pegadinhas verbais das questões de programação e engenharia!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Português, Literatura e História ficam mil vezes mais fáceis quando comparamos com jogos e internet:

- **Tipos Textuais nos Games:**
  - **Narração:** A *lore* / cutscene contando a história do personagem (*"Kratos atravessou os reinos buscando..."*).
  - **Descrição:** O texto da ficha de um item (*"Armadura pesada de aço escovado, escura e rachada nas bordas"*).
  - **Injunção (Instrucional):** O **tutorial** no começo do jogo (*"Pressione `Espaço` para pular; aperte `R` para recarregar"* — verbos no **imperativo**!).
  - **Exposição vs. Argumentação:** A **wiki** explica neutro como o item funciona (Expositivo); um vídeo/artigo dizendo *"Por que tal arma deveria ser nerfada"* defende opinião com provas (Argumentativo).
- **Variação Linguística:** Falar *"Mano, dropa a spike no B e dá call no Disc"* com seu duo é perfeito para a partida (**Diafásica/Situacional** e **Diastrática/Jargão**); já numa redação ou entrevista de estágio você muda para a norma padrão — não existe "falar errado", existe **adequação ao contexto**!
- **História Estilo *Age of Empires / Civilization*:**
  - **Paleolítico:** Fase inicial **nômade** — você anda pelo mapa caçando cervo e colhendo fruta até acabar o recurso da área.
  - **Revolução Neolítica:** Desbloqueou a tecnologia de **Fazenda (Agricultura) e Pecuária** → você para de andar, funda uma aldeia fixa perto do rio (**Sedentarismo**), estoca comida e cresce a cidade!
  - **Feudalismo:** Mapa cheio de **castelos isolados (feudos)**, quase sem comércio/ouro circulando, **servos** plantando na terra do senhor em troca de proteção e contratos de lealdade (**Suserania e Vassalagem**).

---

### 📚 Parte 1 — Tipologia Textual vs. Gêneros Textuais *(M-Tec 2022 Q3)*

**Atenção à distinção conceitual:**
- **Gênero Textual** é o formato concreto que circula na sociedade (são dezenas: *notícia, crônica, receita de bolo, bula de remédio, contrato, e-mail, artigo de opinião, tutorial*).
- **Tipo Textual (Tipologia)** refere-se à **estrutura e objetivo predominante** dentro do texto — são apenas **5 tipos oficiais**:

| Tipo Textual | Objetivo Central | Pistas Gramaticais na Prova | Exemplo Real de Trecho |
| :--- | :--- | :--- | :--- |
| **1. Narração** | Contar fatos/ações vividos por personagens em **tempo e espaço** | Verbos de ação no pretérito (*chegou, programou*), marcadores temporais (*ontem, depois*). | *"Ontem à noite, Lucas abriu o notebook, corrigiu o bug do login e enviou o código antes do prazo."* |
| **2. Descrição** | Retratar características físicas ou psicológicas (**"fotografia em palavras"**, sem avanço temporal) | Adjetivos, verbos de estado/ligação (*é, estava, parecia*), detalhes sensoriais. | *"O laboratório tinha vinte monitores largos, cadeiras ergonômicas pretas e iluminação fria e silenciosa."* |
| **3. Exposição (Dissertativo-Expositivo)** | **Explicar, informar e esclarecer** um assunto de forma clara e **impessoal**, sem tentar convencer de uma opinião polêmica | Linguagem objetiva, 3ª pessoa, definições e exemplos didáticos (apostilas, enciclopédias, notícias neutras). | *"O protocolo HTTPS adiciona a camada criptográfica SSL/TLS sobre o HTTP para proteger os dados em trânsito."* |
| **4. Dissertação Argumentativa** | **Defender uma tese / ponto de vista** usando provas, dados e argumentos para **persuadir** o leitor | Tese clara, conectivos lógicos (*portanto, contudo, logo*), juízo de valor fundamentado (editoriais, redação ENEM). | *"O ensino técnico integrado é indispensável pois une formação cidadã e prática profissional real."* |
| **5. Injunção / Instrucional** | **Instruir, orientar, dar ordens ou conselhos** passo a passo sobre como fazer algo | Verbos no **imperativo** (*clique, abra, adicione*) ou infinitivo instrucional (*manter em local seco*). | *"1. Extraia o arquivo ZIP. 2. Clique duas vezes em COMECE_AQUI.html. 3. Responda ao simulado."* |

---

### 📚 Parte 2 — Figuras de Linguagem, Semântica e Variações Linguísticas

#### 1. Figuras de Linguagem Campeãs de Prova *(M-Tec 2022 Q4)*

| Figura | Como funciona na prática | Exemplo Real Comentado |
| :--- | :--- | :--- |
| **Antítese** | Apenas **aproxima palavras ou ideias de sentidos opostos** na frase, **SEM contradição lógica impossível**. | *"Entre o **claro** e o **escuro**, entre a **alegria** e a **tristeza**, o dia seguiu."* (Dia e noite existem naturalmente, apenas estão contrastando!) |
| **Paradoxo (Oxímoro)** | Une ideias contraditórias que **se anulam logicamente numa mesma afirmação** para causar reflexão profunda! *(M-Tec Q4)* | *"É ferida que **dói e não se sente**"* (Camões) / *"Quanto mais estudo, menos entendo"* / *"Silêncio ensurdecedor"*. |
| **Metáfora vs. Comparação** | **Comparação (Símile)** usa conectivo explícito (*"como, tal qual"*). **Metáfora** transfere o sentido **diretamente, sem conectivo**. | Comparação: *"O banco de dados é **como** um cofre."* <br>Metáfora: *"O banco de dados **é** um cofre."* |
| **Metonímia** | Substitui uma palavra por outra com relação lógica real (autor pela obra, continente pelo conteúdo, parte pelo todo). | *"Passei a tarde lendo **Machado de Assis**"* (os livros dele) / *"Comi **dois pratos** hoje."* |
| **Ironia** | Dizer exatamente o **oposto** do que se pensa, com intenção crítica ou humorística. | *"Que código maravilhoso e limpo — levou só 4 horas para travar na tela de login!"* |
| **Hipérbole** | **Exagero** intencional para dar ênfase expressiva. | *"Já compilei esse projeto **um milhão de vezes** hoje!"* |
| **Hipérbato** | **Inversão brusca da ordem natural** da frase (sujeito + verbo + complemento), muito comum no Barroco e no Hino Nacional. | *"Ouviram do Ipiranga as margens plácidas de um povo heroico o brado retumbante..."* |

#### 2. Semântica: Denotação, Conotação, Polissemia e Hipônimo/Hiperônimo *(M-Tec 2022 Q5)*
- **Denotação (D = Dicionário):** Sentido **literal, exato** da palavra (*"O servidor usa memória física de **pedra** de silício"* / *"Quebrou a **pedra**"*).
- **Conotação:** Sentido **figurado, poético ou contextual** (*"Ele tem um coração de **pedra**"* = insensível).
- **Polissemia:** Quando uma única palavra possui **vários significados diferentes** dependendo da frase (*"a **cabeça** do aluno"*, *"a **cabeça** do prego"*, *"a **cabeça** da fila"*).
- **Hiperônimo vs. Hipônimo *(caiu em M-Tec Q5!)*:**
  - **Hiperônimo** = termo **mais amplo / categoria geral** (*"pensador"*, *"animal"*, *"linguagem de programação"*).
  - **Hipônimo** = termo **mais específico** contido dentro da categoria (*"Aristóteles"*, *"cachorro"*, *"Python"*).
  - Exemplo real de coesão num texto: *"A França convocou **Aristóteles** na homenagem. O **pensador** grego..."* → substituir *Aristóteles* (hipônimo) por *pensador* (hiperônimo) evita repetição!

#### 3. Variações Linguísticas *(M-Tec 2022 Q2)*
A Sociolinguística moderna ensina que a língua é viva e não existe *"falar errado"* de modo absoluto — o que existe é **adequação ou inadequação ao contexto comunicativo** (ninguém fala igual numa entrevista de emprego e num grupo de WhatsApp com amigos!).
- **Variação Diatópica (Geográfica/Regional):** Muda conforme o lugar (*"aipim" / "macaxeira" / "mandioca"*; *"trem"* em MG; *"guri"* no RS).
- **Variação Diacrônica (Histórica):** Muda com o passar do tempo (*"Vossa Mercê" → "Vosmicê" → "Você" → "Vc"*).
- **Variação Diastrática (Social / Profissional):** Muda conforme grupo social ou profissão (jargão de TI: *"fazer deploy de um container"*; gírias juvenis).
- **Variação Diafásica (Situacional / Registro):** Grau de formalidade entre falar com um juiz vs. conversar em casa.

---

### 📚 Parte 3 — Escolas Literárias do 1º Ano do Ensino Médio *(M-Tec Q1 & Q6)*

#### 1. Trovadorismo (Idade Média — sécs. XII a XIV, *M-Tec Q6*)
Primeira manifestação literária em língua galego-portuguesa, nascida nos castelos feudais como **cantigas** acompanhadas de música (trovadores + jograis):
- **Cantigas Líricas (Amorosas):**
  - **Cantiga de Amor:** Eu lírico **MASCULINO** sofre por uma dama nobre distante e inatingível (*"minha senhor"*). Reflete a **vassalagem feudal** trazida para o amor (o homem serve humildemente à mulher superior).
  - **Cantiga de Amigo:** Eu lírico **FEMININO** (mesmo tendo sido escrita por homens!) expressa saudade do seu namorado (*"amigo"*) conversando com a mãe, amigas ou elementos da natureza (mar, ondas, pinheiros). Origem popular/rural.
- **Cantigas Satíricas (Críticas):**
  - **Escárnio:** Crítica **indireta, irônica, ambígua**, **sem** citar o nome da pessoa diretamente.
  - **Maldizer:** Crítica **direta, agressiva, explícita**, citando o nome do alvo e usando palavras de baixo calão.

#### 2. Humanismo (séc. XV), Classicismo (séc. XVI) e Quinhentismo no Brasil
- **Humanismo:** Transição da Idade Média para o Renascimento (**Gil Vicente**, teatro crítico em *O Auto da Barca do Inferno*).
- **Classicismo:** Renascimento pleno, equilíbrio, razão, imitação dos clássicos greco-romanos (**Luís de Camões** — *Os Lusíadas* e sonetos equilibrados).
- **Quinhentismo no Brasil (1500 — *M-Tec Cards*):** Duas frentes no primeiro século após 1500:
  1. **Literatura Informativa / de Viagens:** Descrevia e catalogava a nova terra, fauna, flora e indígenas para a Coroa Portuguesa (**Carta de Pero Vaz de Caminha**, 1500).
  2. **Literatura Jesuítica / Catequética:** Textos, poesias e autos teatrais de caráter religioso e pedagógico para **catequizar** os indígenas e educar colonos (**Padre José de Anchieta**).

#### 3. Barroco (sécs. XVII–XVIII — *Campeão de Pegadinha: M-Tec Q1!*)
Nascido no clima tenso da **Contrarreforma Católica**, o Barroco expressa o **conflito dramático humano (dualismo)**: espírito × carne, céu × inferno, efemeridade da vida × busca pelo eterno. Usa muitas antíteses e paradoxos!

| Estilo Barroco | Foco Principal | Características & Recursos | Grande Autor |
| :--- | :--- | :--- | :--- |
| **Cultismo (Gongorismo)** | **Jogo de PALAVRAS** e forma | Linguagem rebuscada, exuberante, vocabulário raro, metáforas complexas, hipérboles e imagens sensoriais (*cores, brilho, sons*). | **Gregório de Matos** (*"Boca do Inferno"*) na poesia ornamentada |
| **Conceptismo (Quevedismo)** | **Jogo de IDEIAS** e lógica | Raciocínio lógico rigoroso, argumentação persuasiva, **silogismos** e encadeamento intelectual para provar teses morais/religiosas. | **Padre Antônio Vieira** (nos *Sermões*, ex.: *Sermão da Sexagésima*) |

> [!CAUTION]
> **Pegadinha clássica da M-Tec Q1:** A banca define perfeitamente o que é **Cultismo** (jogo de palavras/linguagem sensorial rebuscada) e **Conceptismo** (jogo de ideias/raciocínio lógico), e simplesmente **troca um nome pelo outro** nas alternativas! Associe sempre: **Con**ceptismo = **Con**ceito / **Ideia**; **Cul**tismo = **Cul**tura da palavra / **Forma**!

---

### 📚 Parte 4 — História Geral do 1º Ano: Pré-História, Antiguidade e Feudalismo *(M-Tec Q24–Q27)*

#### 1. Pré-História: Paleolítico vs. Revolução Neolítica *(M-Tec Q24–Q25)*

| Período | Estilo de Vida | Como Conseguia Alimento e Tecnologia |
| :--- | :--- | :--- |
| **Paleolítico** *(Idade da Pedra Lascada)* | **Nomadismo:** bandos mudavam constantemente de região assim que caça/frutos esgotavam-se. | **Caça, pesca e coleta**; ferramentas rústicas de pedra lascada e ossos; **domínio do fogo**; arte rupestre nas cavernas. |
| **Neolítico** *(Idade da Pedra Polida — Revolução Neolítica)* | **Sedentarismo:** fixaram moradia permanente em aldeias próximas a grandes rios. | Descoberta da **agricultura** e **domesticação de animais**! Produção de **excedentes**, cerâmica, tecelagem, crescimento populacional e surgimento da propriedade privada/Estado. |
| **Idade dos Metais** | Cidades organizadas e comércio | Fundição de cobre, bronze e ferro; invenção da roda e dos primeiros sistemas de escrita (fim da Pré-História!). |

- **Conceitos de Migração *(M-Tec Q24)*:** **Nomadismo** (deslocamento constante sem residência fixa para sobreviver); **Sedentarismo** (fixação num território por meio da agricultura/moradia); **Êxodo Rural** (migração em massa de trabalhadores do campo para as cidades em busca de emprego urbano/industrial).

#### 2. Antiguidade Oriental (Primeiras Civilizações) e Clássica *(M-Tec Q26)*
As primeiras civilizações urbanas surgiram no **Crescente Fértil** (*Mesopotâmia* — sumérios, babilônios entre os rios **Tigre e Eufrates**; *Egito* no **Rio Nilo**), caracterizadas como **sociedades hidráulicas** (agricultura de irrigação controlada pelo Estado), governo **teocrático** (rei visto como deus ou representante divino), leis escritas (**Código de Hamurabi** — *"olho por olho, dente por dente"*) e sistemas de escrita (cuneiforme/hieróglifos). Na sequência, **Grécia** (democracia ateniense, filosofia) e **Roma** (direito romano, república, império, cristianismo).

#### 3. Idade Média Ocidental & Feudalismo (sécs. V ao XV — *M-Tec Q27*)
Após a queda de Roma Ocidental (476 d.C.) e invasões germânicas, a Europa ruralizou-se:
- **Economia Feudal:** Essencialmente **agrária, rural, autossuficiente (de subsistência)**, com escambo e baixíssima circulação monetária dentro do feudo (*manso senhorial, manso servil e terras comunais*).
- **Sociedade Estamental (sem mobilidade social — "nasceu servo, morre servo"):**
  1. **Clero** (*oratores* — os que rezam/dominam o saber);
  2. **Nobreza** (*bellatores* — os senhores feudais guerreiros donos das terras);
  3. **Servos** (*laboratores* — camponeses presos à terra, não eram escravos comprados/vendidos, mas pagavam pesados tributos como **corveia** [trabalho gratuito nas terras do senhor], **talha** [parte da produção] e **banalidades** [uso de forno/moinho]).
- **Política Descentralizada:** O poder real enfraqueceu e pulverizou-se entre os senhores locais ligados pelo contrato de **Suserania e Vassalagem** (o **suserano** doava um **feudo/terra** ao **vassalo**, que jurava lealdade e apoio militar). A única instituição centralizadora unindo a Europa era a **Igreja Católica (Teocentrismo)**.

---

### 🕵️‍♂️ Dissecando Questões Reais da Prova M-Tec

#### Questão Resolvida 1 (Baseada em M-Tec 2022 Q1 — Barroco)
*No Barroco brasileiro e português, a tendência marcada pelo jogo lógico de ideias, silogismos e raciocínio argumentativo, presente nos sermões de Padre Antônio Vieira, denomina-se _____; enquanto o rebuscamento formal com jogo de palavras e metáforas sensoriais denomina-se _____.*
- **Gabarito:** **Conceptismo** (ideias/lógica) e **Cultismo** (palavras/forma).

#### Questão Resolvida 2 (Baseada em M-Tec 2022 Q4 — Figuras de Linguagem)
*"Vivemos em uma época em que estar hiperconectado no celular nos deixa cada vez mais solitários." A figura de linguagem dominante na contradição lógica entre estar "hiperconectado" e "mais solitário" numa mesma ideia é:*
- **Gabarito:** **Paradoxo** (ideias logicamente excludentes unidas numa mesma afirmação crítica).

#### Questão Resolvida 3 (Baseada em M-Tec 2022 Q25 & Q27 — Neolítico e Feudalismo)
*Sobre a Revolução Neolítica e o Feudalismo: I. A domesticação de plantas e animais no Neolítico permitiu a sedentarização humana. II. A economia feudal europeia era predominantemente industrial e centrada no comércio marítimo assalariado.*
- **Item I:** VERDADEIRO.
- **Item II:** **FALSO!** O feudalismo era agrário, rural, de subsistência e baseado no trabalho **servil** (não assalariado industrial!).


---

## Dia 13 — Base Comum M-Tec II: Matemática, Química, Física e Biologia/Meio Ambiente (1º Ano EM)

### 🎯 Contexto no Mundo Real: Pontos Decisivos que Diferenciam Quem Passa

Em provas do **M-Tec 2º Ano** (como vimos nas questões reais **M-Tec 2022 Q10–Q23 e Q33**), quem estuda só informática costuma deixar pontos valiosos na mesa em **Conjuntos Numéricos, Contagem, Função Quadrática, Áreas com Pitágoras, Massa Molar, Condutividade de Ligações Químicas e Óptica das Cores**. A excelente notícia é que os problemas cobrados pela banca seguem **fórmulas diretas e limpas**, fáceis de dominar quando entendemos o raciocínio por trás de cada conta!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Você encontra Matemática, Química e Física do 1º ano funcionando dentro dos próprios jogos e do seu PC:

- **Contagem (Combinações de PIN / Senha / Tag):** Quer criar uma senha/código numérico de 3 dígitos distintos sem começar com `0`? Você calcula passo a passo quantas opções existem em cada slot — começando sempre pela casa que tem restrição (`0` proibido na frente!).
- **Função do 2º Grau (`ax² + bx + c`) = Trajetória de Granada / Flecha / Bola:** Quando você joga uma granada para cima, ela sobe até o **ponto máximo (Vértice `y_v`)** e cai formando uma **parábola com concavidade para baixo (`a < 0`)**! E quando cai numa conta de lucro mínimo, `a > 0`.
- **Geometria `3-4-5` = Distância em Diagonal / Hitbox no Mapa:** Se um player andou `30m` para o Norte e `40m` para o Leste, a distância em linha reta (*Pitágoras*) fecha exatamente **`50m`** sem precisar sofrer na raiz quadrada!
- **Química nos Cabos e Bateria do PC:**
  - Os fios de **Cobre (`Cu`)** dentro do seu PC e USB conduzem eletricidade direto no **estado SÓLIDO** porque são **Metais** (mar de elétrons livres).
  - Água pura (destilada) ou plástico isolante da capa do fio é **Molecular/Covalente** (não conduz!), mas se cair sal (`NaCl`, **Iônico**) dissolvido na água, libera íons e **conduz corrente na hora**!
- **Óptica das Cores na Tela/Iluminação:** Quando uma lâmpada RGB verde ilumina um objeto vermelho opaco, ele não tem luz vermelha para refletir de volta — absorve o verde e fica **PRETO**!

---

### 📚 Parte 1 — Matemática do 1º Ano Passo a Passo *(M-Tec Q19–Q23)*

#### 1. Os Conjuntos Numéricos (`ℕ, ℤ, ℚ, 𝕀, ℝ`) *(M-Tec Q19)*
Entenda onde cada número "mora" para nunca errar dízimas periódicas nem raízes:
- **`ℕ` (Naturais):** Inteiros de contagem não negativos `{0, 1, 2, 3, 4, ...}`.
- **`ℤ` (Inteiros):** Acrescenta os negativos exatos `{..., -3, -2, -1, 0, 1, 2, ...}`. Logo, todo Natural é Inteiro (`ℕ ⊂ ℤ`).
- **`ℚ` (Racionais):** Qualquer número que **pode ser escrito em forma de fração `a / b`** (`b ≠ 0`). Isso inclui:
  - Todos os inteiros (`5 = 5/1`);
  - Decimais exatos/finitos (`0,25 = 1/4`; `1,75 = 7/4`);
  - **Todas as DÍZIMAS PERIÓDICAS (infinitas com repetição padrão)!** Ex.: `0,333... = 1/3`, `0,454545... = 45/99 = 5/11` → Logo, **dízima periódica é RACIONAL (`ℚ`)!**
- **`𝕀` (Irracionais):** Números decimais **infinitos e NÃO periódicos** que **jamais viram fração exata**: `π ≈ 3,14159265...`, `e ≈ 2,71828...`, raízes não exatas (`√2 ≈ 1,41421...`, `√3`, `√5`). *(Atenção: `√9 = 3`, logo `√9` é Natural/Racional, NÃO irracional!)*
- **`ℝ` (Reais):** A união dos Racionais + Irracionais (`ℝ = ℚ ∪ 𝕀`). Importante: `ℚ ∩ 𝕀 = ∅` (nenhum número pertence aos dois ao mesmo tempo!).

#### 2. Operações entre Conjuntos e Diagrama de Venn *(M-Tec Q22)*
Dados dois ou três conjuntos finitos:
- **Interseção (`A ∩ B`):** Pega **apenas os elementos em comum** (que aparecem dentro de `A` **E** dentro de `B`).
- **União (`A ∪ B`):** Junta **todos** os elementos de `A` e de `B` num conjunto só, **sem repetir duplicatas**.
- **Diferença (`A - B`):** Pega os elementos de `A`, **removendo** qualquer um que também pertença a `B`.

**💻 Exemplo Resolvido Passo a Passo (estilo M-Tec Q22):**
Se `A = {1, 2, 4, 6}`, `B = {2, 3, 6, 8}` e `C = {3, 9}`, quanto vale **`(A ∩ B) ∪ C`**?
1. **Regra dos parênteses primeiro:** `A ∩ B` = o que existe em `A` e em `B` ao mesmo tempo → **`{2, 6}`**.
2. Agora fazemos a união com `C`: `{2, 6} ∪ {3, 9}` → juntando e ordenando: **`{2, 3, 6, 9}`**!
*(Nota: em problemas de pesquisa — "80 gostam de Python, 50 de JS e 20 de ambos" — lembre-se sempre de **começar preenchendo o centro da interseção (`20`)** no diagrama e descontar `80 - 20 = 60 só Python` e `50 - 20 = 30 só JS`, evitando contar os 20 alunos duas vezes!)*

#### 3. Princípio Fundamental da Contagem com o Dígito Zero *(M-Tec Q23)*
**Pergunta clássica:** *Quantos números naturais de **3 algarismos distintos** podemos formar usando o conjunto `{0, 1, 2, 3, 4, 5}`?*
1. Desenhe 3 tracinhos para as casas: `[ Centena ] × [ Dezena ] × [ Unidade ]`.
2. **A Pegadinha Fatal do Zero:** Um número natural de 3 algarismos **NUNCA pode começar com `0`** (pois `045` equivale a `45`, que só tem 2 algarismos!).
3. Preenchendo **da esquerda para a direita (começando pela restrição!)**:
   - **1ª casa (Centena):** Dos 6 dígitos `{0,1,2,3,4,5}`, o `0` está proibido! Sobram **5 opções** (`1, 2, 3, 4` ou `5`).
   - **2ª casa (Dezena):** Já usamos 1 dígito na centena (digamos o `3`), mas **agora o `0` está liberado**! Dos 6 originais menos o `3` já gasto, restam **5 opções** (`0, 1, 2, 4, 5`)!
   - **3ª casa (Unidade):** Dos 6 dígitos, já gastamos 2 distintos. Restam **4 opções**!
4. Multiplicamos tudo: **`5 × 5 × 4 = 100 números distintos`**! *(E se permitisse repetição? Seria `5 × 6 × 6 = 180`!).*

#### 4. Função Afim (1º Grau) e Função Quadrática (2º Grau) *(M-Tec Q20)*
- **Função Afim (`f(x) = ax + b`):** Gráfico é uma reta. `a` é a taxa de variação (inclinação: se `a > 0` crescente; `a < 0` decrescente); `b` é o valor fixo inicial onde a reta corta o eixo Y (`x = 0`).
- **Função Quadrática (`f(x) = ax² + bx + c`, com `a ≠ 0`):** Gráfico é uma **parábola**:
  - Se **`a > 0`**: concavidade voltada para **CIMA** (tem **ponto de MÍNIMO**).
  - Se **`a < 0`**: concavidade voltada para **BAIXO** (tem **ponto de MÁXIMO** — ótimo para lucro/altura máxima!).
  - **Raízes (zeros da função, `ax² + bx + c = 0`):**
    1. Discriminante: **`Δ = b² - 4 · a · c`**
       - `Δ > 0` → **duas raízes reais distintas**;
       - `Δ = 0` → **uma única raiz real dupla** (toca o eixo X num ponto);
       - `Δ < 0` → **não possui raízes reais** (não toca o eixo X).
    2. Bhaskara: **`x = (-b ± √Δ) / (2a)`**.
  - **Vértice da Parábola (Máximo ou Mínimo):** **`x_v = -b / (2a)`** e **`y_v = -Δ / (4a)`** (ou apenas substitua o valor achado de `x_v` na própria função `f(x)`!).

**💻 Exemplo Resolvido:** Para `f(x) = x² - 5x + 6`:
- `a = 1 (> 0 → concavidade p/ cima)`, `b = -5`, `c = 6`.
- `Δ = (-5)² - 4(1)(6) = 25 - 24 = 1 (> 0 → 2 raízes reais distintas!)`.
- `x = (5 ± √1) / 2` → **`x₁ = 3`** e **`x₂ = 2`**. Vértice: `x_v = 5/2 = 2,5` e `y_v = (2,5)² - 5(2,5) + 6 = -0,25`.

#### 5. Geometria Plana, Triângulo 3-4-5 e Decomposição de Áreas *(M-Tec Q21)*
- **Fórmulas essenciais:**
  - Retângulo / Paralelogramo: `A = base × altura`
  - Triângulo: `A = (base × altura) / 2`
  - Trapézio: `A = ((B + b) × h) / 2`
  - Círculo: `A = π · r²` e Comprimento: `C = 2 · π · r`
- **Teorema de Pitágoras & Triângulo 3-4-5:** Num triângulo retângulo, `hipotenusa² = cateto₁² + cateto₂²`.
  - Sempre que você vir catetos múltiplos de **3 e 4**, a hipotenusa é múltiplo de **5** sem precisar fazer conta gigante! Ex.: **`30m` e `40m` → hipotenusa `50m`** (`30² + 40² = 900 + 1600 = 2500 = 50²`), e área = `(30 × 40) / 2 = 600 m²`!
- **Resolvendo terreno composto *(M-Tec Q21)*:** Divida figuras em L ou chanfradas em um retângulo + um triângulo retângulo (ou trapézio + retângulo) e **some as áreas individuais**. Exemplo da prova: terreno composto formado por retângulo + trapézio/triângulo totalizando **`2.320 m²`** (como `40m × 58m = 2.320 m²` ou retângulo `40 × 43 = 1.720 m²` + triângulo `30×40/2 = 600 m²` → **`1.720 + 600 = 2.320 m²`**!).

---

### 📚 Parte 2 — Química do 1º Ano: Ligações, Condutividade e Massa Molar *(M-Tec Q17–Q18)*

#### 1. Ligações Químicas & Condutividade Elétrica *(M-Tec Q18 — Quase 100% de chance na prova!)*
Para haver corrente elétrica, é obrigatório existir **cargas elétricas livres para se movimentar** (elétrons livres ou íons soltos):

| Tipo de Ligação | Como os átomos se unem | Exemplos Reais | Conduz Eletricidade? (DECORE ISSO!) |
| :--- | :--- | :--- | :--- |
| **1. Ligação Metálica** *(Metal + Metal)* | Átomos doam elétrons externos formando um **"mar de elétrons" móveis** ao redor dos cátions. | Ferro (`Fe`), Cobre (`Cu`), Alumínio (`Al`), Ouro (`Au`) | **CONDUZ no estado SÓLIDO** e no líquido! (Por isso fios elétricos são de cobre sólido!). |
| **2. Ligação Iônica** *(Metal + Ametal/H)* | **Transferência definitiva** de elétrons formando **íons** positivos (`+`) e negativos (`-`) presos num cristal rígido. | Sal de cozinha (`NaCl`), Fluoreto (`NaF`), Óxidos metálicos (`CaO`) | **NÃO conduz no estado SÓLIDO** (íons presos na rede cristalina), mas **CONDUZ quando LÍQUIDO/FUNDIDO (derretido) ou DISSOLVIDO EM ÁGUA** (pois os íons ficam livres!). |
| **3. Ligação Covalente (Molecular)** *(Ametal + Ametal / Hidrogênio)* | Átomos **compartilham pares de elétrons** formando moléculas eletricamente neutras, sem íons! | Açúcar (`C₁₂H₂₂O₁₁`), Álcool (`C₂H₅OH`), Água pura (`H₂O`), Oxigênio (`O₂`) | **NÃO conduz eletricidade NEM no estado SÓLIDO, NEM puro/líquido!** |

> [!TIP]
> **Resumo instantâneo da Tabela de Condutividade *(M-Tec Q18)*:**
> - Conduz sólido **E** líquido? → **Metal (Ligação Metálica)**.
> - Não conduz sólido, mas conduz líquido/aquoso? → **Composto Iônico**.
> - Não conduz em nenhum estado? → **Composto Molecular / Covalente**.

#### 2. Cálculo de Massa Molecular (`u`) / Massa Molar (`g/mol`) *(M-Tec Q17)*
Basta multiplicar a massa atômica de cada elemento (dada no enunciado: geralmente **`H = 1`, `C = 12`, `N = 14`, `O = 16`**) pela quantidade de átomos que aparecem na fórmula:

1. **Etanol / Álcool Etílico (`C₂H₅OH` ou `C₂H₆O`):**
   - `C`: `2 átomos × 12 = 24`
   - `H`: `5 + 1 = 6 átomos × 1 = 6` *(Cuidado para não esquecer o `H` que fica depois do `O`!)*
   - `O`: `1 átomo × 16 = 16`
   - **Total:** `24 + 6 + 16 =` **`46 u` (`46 g/mol`)**!
2. **Ácido Acético / Vinagre (`C₂H₄O₂`):**
   - `C`: `2 × 12 = 24` | `H`: `4 × 1 = 4` | `O`: `2 × 16 = 32`
   - **Total:** `24 + 4 + 32 =` **`60 u` (`60 g/mol`)**!
3. **Dióxido de Carbono (`CO₂`):** `12 + 2×16 =` **`44 u`** | **Glicose (`C₆H₁₂O₆`):** `6×12 + 12×1 + 6×16 = 72 + 12 + 96 =` **`180 u`**.

---

### 📚 Parte 3 — Física (Óptica das Cores) & Biologia / Meio Ambiente *(M-Tec Q10–Q16 & Q33)*

#### 1. Física — Óptica das Cores por Reflexão Seletiva *(M-Tec Q33)*
A luz solar (branca) é **policromática**, contendo todas as cores do espectro visível juntas (vermelho, laranja, amarelo, verde, azul, anil, violeta). A cor que enxergamos em um objeto opaco depende exclusivamente de **qual cor da luz ele REFLETE** até os nossos olhos (as demais são absorvidas em forma de calor):
- **Tomate maduro sob luz branca (Sol):** Absorve azul, verde, amarelo etc., e **REFLETE a luz vermelha** → vemos **vermelho**!
- **Tomate vermelho dentro de uma sala iluminada APENAS com luz VERDE pura (monocromática):** Como só chega luz verde, e o pigmento vermelho do tomate **absorve** a luz verde sem ter nenhuma luz vermelha para refletir, não volta luz alguma para nossos olhos → **enxergamos o tomate PRETO!**
- **Camisa branca sob luz verde:** O branco reflete **todas** as cores que chegam — se só chega luz verde, ele reflete verde → vemos **verde**!
- **Objeto preto:** Absorve praticamente **todas** as cores (por isso esquenta rápido no Sol).

#### 2. Método Científico *(M-Tec Q10)*
Ordem lógica rigorosa da investigação científica:
1. **Observação** cuidadosa do fenômeno natural + **Questionamento**;
2. Formulação de **Hipótese** (uma explicação provisória e **testável**);
3. **Experimentação controlada** (grupo teste × grupo controle) para testar a hipótese;
4. **Coleta e Análise de Dados**;
5. **Conclusão** (confirma, ajusta ou refuta a hipótese — conhecimento científico não é dogma imutável!).

#### 3. Sustentabilidade, Poluentes e Protocolo de Kyoto *(M-Tec Q13–Q16)*
- **Desenvolvimento Sustentável:** Atender às necessidades da geração atual **sem comprometer** a capacidade das gerações futuras (equilíbrio ambiental, social e econômico).
- **Efeito Estufa vs. Aquecimento Global:** O Efeito Estufa *natural* é vital (retém calor na Terra evitando congelamento). O problema atual é a **intensificação antrópica** pelo excesso de gases como **`CO₂`** (queima de combustíveis fósseis, desmatamento) e **`CH₄` (metano)**, gerando **Aquecimento Global** e derretimento de geleiras/eventos extremos.
- **Protocolo de Kyoto (1997):** Tratado internacional pioneiro que estabeleceu metas obrigatórias para países desenvolvidos **reduzirem emissões de gases do efeito estufa**, criando o mecanismo de **créditos de carbono** (Mecanismo de Desenvolvimento Limpo).
- **Chuva Ácida & Tabelas CETESB (`SO₂`):** O dióxido de enxofre (**`SO₂`**) e óxidos de nitrogênio (`NOₓ`) liberados por indústrias/escapamentos reagem com a umidade do ar formando **chuva ácida** (danifica solos, lagos e monumentos). Em questões com tabela da **CETESB**, leia atentamente o cabeçalho da coluna, o ano pedido e confira a unidade (`µg/m³`).

---

### 🕵️‍♂️ Dissecando Questões Reais da Prova M-Tec

#### Questão Resolvida 1 (Baseada em M-Tec 2022 Q18 & Q17 — Química)
*Três substâncias sólidas desconhecidas X, Y e Z foram testadas no laboratório:*
- *X não conduz corrente sólido, mas conduz muito bem quando fundido/líquido.*
- *Y conduz corrente elétrica já no estado sólido.*
- *Z não conduz nem sólido nem dissolvido em água.*
*Classifique as ligações de X, Y e Z:*
- **X** = Composto **Iônico**; **Y** = **Metálico**; **Z** = **Covalente / Molecular**.

#### Questão Resolvida 2 (Baseada em M-Tec 2022 Q23 — Contagem)
*Quantos números de 3 algarismos distintos podem ser formados com `{0, 2, 4, 6, 8}`?*
- Cuidado com o `0` na centena!
- 1ª casa (sem `0`): **4 opções** (`2, 4, 6, 8`).
- 2ª casa (entra o `0`, sai a usada na 1ª): **4 opções**.
- 3ª casa: **3 opções**.
- Total: `4 × 4 × 3 =` **`48 números`**!

#### Questão Resolvida 3 (Baseada em M-Tec 2022 Q33 — Física Óptica)
*Num palco iluminado exclusivamente por refletores monocromáticos azuis, um artista entra vestindo uma camisa amarela pura e uma calça branca. Como o público enxergará a camisa e a calça?*
- **Camisa amarela** absorve luz azul (só refletiria amarelo/vermelho/verde) → parece **PRETA**.
- **Calça branca** reflete todas as cores incidentes → parece **AZUL**!


---

## Dia 14 — Revisão Integrada Final, as 25 Pegadinhas da Banca FAT e Estratégia para a Prova de 04/12

### 🎯 Contexto no Mundo Real: Juntando Todas as Peças no Sistema Completo

Pare por 30 segundos e enxergue como tudo o que você estudou nestes **14 dias** trabalha junto num único sistema real — por exemplo, quando você abre o navegador no PC da Etec para responder a uma prova online:

1. No **Design (Dia 8)**, a interface usou cores **RGB / `#Hexadecimal`**, logo vetorial **`.SVG`**, fonte sem serifa do **Google Fonts**, espaçamento por **Proximidade (Gestalt)** e respeitou a **Equivalência com o Mundo Real (Nielsen)**.
2. No **Front-end Web (Dia 9)**, a tela foi montada com **HTML5 Semântico** (`<header>`, `<main>`, `<form method="POST">`), estilizada com **CSS3 Box Model** (`padding`/`margin`), alterada dinamicamente via árvore **DOM** em JavaScript (construído com **Frameworks** e empacotado por **Build/Bundling** do **Dia 4** sob **Git** e licença **MIT/GPL**) e manteve sua sessão em um **Cookie local (~4 KB)**.
3. Na **Rede (Dia 11)**, seu pedido viajou pela pilha **TCP/IP**, traduzido pelo **DNS**, criptografado via **HTTPS (SSL/TLS)**, através da rede local **Estrela (Switch)** até servidores **Linux** (`/etc`, `/var/log` — **Dia 10**) rodando em **Contêineres Docker** na nuvem **PaaS/IaaS**.
4. No **Back-end e Banco de Dados (Dias 1–7)**, o servidor recebeu dados tipados/convertidos (**Casting**, **POO**, **Scrum**), consultou um banco relacional normalizado na **1FN** (sem múltiplos telefones na célula!) usando **DQL (`SELECT COUNT(*) WHERE...`)** e **DML (`INSERT`/`UPDATE`)**, e devolveu sua nota!

Você agora não sabe só "dicas soltas" — você entende a arquitetura completa de sistemas!

---

### 🎮 Conexão Gamer & Discord (Pra Entender de Primeira!)

Encare a prova de **04/12** como uma **Speedrun estratégica em 3 fases**, igual zerar um jogo no modo ranqueado sem tiltar numa fase difícil no meio:

- **Fase 1 (1ª Passada — *Loot Rápido*):** Garante primeiro todas as questões fáceis e diretas (E-mail, Cookies, Tags HTML, Frameworks, Licenças, Inglês, Barroco, Paleolítico/Neolítico). Questão grande que pede conta? Dá *skip* marcado e volta já com pontos garantidos no bolso!
- **Fase 2 (2ª Passada — *Chefões de Cálculo e I-II-III*):** Resolve com calma os Testes de Mesa, Matrizes, Binário/Hex, Matemática e Química desenhando passo a passo no rascunho — sem "olhômetro".
- **Fase 3 (3ª Passada — *Save Final / Gabarito*):** Confere cada marcação no cartão-resposta sem pressa e nunca entrega bolinha em branco.

---

### 📚 Parte 1 — Dicionário das 25 Pegadinhas Mais Recorrentes da Fundação FAT

Leia com muita atenção esta tabela antes da prova. Quase todo erro em questões I, II e III acontece exatamente por uma destas **25 armadilhas verbais**:

| Nº | Assunto | Frase FALSA que a banca inventa (NÃO CAIA!) | Verdade Oficial da Prova |
| :---: | :--- | :--- | :--- |
| **1** | **Casting** | `(int) 7.99` converte para `8` arredondando. | **TRUNCA (corta)** a parte decimal → **`7`**! E só se chama **explícita/casting** (nunca "conversão normal"). |
| **2** | **Tipos** | `'A'` ou `12` usa tipo booleano (`bool`). | `'A'` usa **`char`**; `"texto"` usa **`string`**; `bool` guarda **exclusivamente `true`/`false`**. |
| **3** | **DIV / MOD** | `17 MOD 5` vale `3` e `17 DIV 5` vale `2`. | **`DIV`** = quociente inteiro (**`3`**); **`MOD`** = **resto** da divisão (**`2`**). |
| **4** | **Teste de Mesa** | No `enquanto (x <= 6)`, ao sair `x` ainda vale `6`. | O último incremento ainda acontece na última volta! Confira a tabela até a condição dar **Falso**. |
| **5** | **Matrizes** | Somar diagonal secundária achando que é a principal. | Diagonal **Principal** é **`i == j`** (`[0][0], [1][1], [2][2]`). Secundária é `i + j == N - 1`. |
| **6** | **Pilha vs Fila** | Em Pilha (`LIFO`), `POP` remove o primeiro que entrou. | Pilha = **LIFO** (`POP` remove o **ÚLTIMO** que entrou, do topo). Fila = **FIFO** (sai o primeiro). |
| **7** | **Frameworks** | *Creative Commons* ou *Adobe Creative Cloud* são frameworks. | **Frameworks reais:** Bootstrap, Angular, Laravel (PHP), React Native (Mobile). Os outros são licença/suíte design! |
| **8** | **Editores** | Bloco de Notas (Notepad) é uma IDE completa. | Bloco de Notas = **editor de texto puro**; **VS Code** = editor de código; **Visual Studio / Eclipse** = IDE; **Dreamweaver/Wix** = WYSIWYG. |
| **9** | **Licenças** | Software Livre significa necessariamente gratuito (`R$ 0`). | **Software Livre** garante **4 liberdades de código aberto** (pode ser vendido!). Já **Freeware** é grátis, mas de **código fechado**! |
| **10** | **Scrum & XP** | Scrum Master chefia tarefas; Pair Programming = cada dev em uma sala. | **SM** facilita/remove impedimentos; **PO** prioriza backlog; **Daily** <= 15 min; **Pair Programming** = **2 devs no mesmo PC**. |
| **11** | **POO** | Classe, Atributo e Método são os pilares da POO. | Os **4 Pilares** oficiais são: **Abstração, Encapsulamento, Herança e Polimorfismo**. |
| **12** | **SQL DDL/DML/DQL** | `DROP` é DML; `SELECT` é DDL; `COUNT(*)` vai no `WHERE`. | **DDL** = `CREATE/ALTER/DROP` (estrutura); **DML** = `INSERT/UPDATE/DELETE` (dados); **DQL** = `SELECT` (`COUNT(*)` vai no `SELECT`!). |
| **13** | **1FN & DER** | Vários telefones na mesma célula (`"111, 222"`) atende à 1FN. | Viola a **1ª Forma Normal (1FN)** (exige valores **atômicos**)! E **`idade`** via `data_nasc` é atributo **derivado**. |
| **14** | **Cores** | RGB é para gráfica/papel; "CSS" ou "Primária" é padrão de cor. | **RGB** / **Hex** = telas (luz aditiva); **CMYK** = impressão (tinta). |
| **15** | **Vetor vs Bitmap** | `.JPEG` e `.PNG` são formatos vetoriais sem pixelação. | **Vetorial** = **`.SVG` / `.PDF`** (equações matemáticas, zoom sem perda). **Bitmap** = `.JPEG`, `.PNG`, `.BMP`. |
| **16** | **Gestalt & UX** | Rótulo colado ao campo é Fechamento; fonte *Script* serve para texto longo. | Perto = **Proximidade**; mesmo estilo = **Semelhança**. Fonte **Script** imita letra cursiva (só títulos/convites!). |
| **17** | **Cookies** | Cookies são pesados e armazenados nos servidores em nuvem. | Cookies são **texto pequeno (~4 KB) salvos LOCALMENTE no navegador do cliente** (sessão ou persistente)! |
| **18** | **HTML & CSS** | `<div>` é tag semântica; `<tr>` é célula; `GET` esconde senha. | **`<div>` é genérica** (`<header>/<nav>/<main>/<article>/<footer>` são semânticas); `<tr>` = linha, `<td>` = célula; senha vai no **`POST`**; `padding` = interno, `margin` = externo. |
| **19** | **Binário & Hex** | `250` em hexadecimal é `250` ou `F0`. | `250 ÷ 16` = `15(F)` resto `10(A)` = **`FA₁₆`** (`100` = `64₁₆`; `255` = `11111111₂` = `FF₁₆`). |
| **20** | **Linux Pastas** | `/mkdir`, `/ls`, `/rm`, `/cd` são diretórios do Linux. | São **COMANDOS**, não pastas! Pastas reais FHS: **`/bin, /etc, /home, /lib, /root, /usr, /var, /tmp`**. |
| **21** | **Contêiner vs VM** | Contêiner Docker instala um Kernel completo novo por dentro. | Contêiner **compartilha o Kernel** do hospedeiro (leve); quem virtualiza SO inteiro é **VM + Hypervisor**. |
| **22** | **E-mail** | SMTP recebe/sincroniza e IMAP ou POP3 envia. | **SMTP** = **Envia**; **POP3** = Baixa e apaga do servidor; **IMAP** = Sincroniza no servidor. |
| **23** | **Topologias** | Na topologia Estrela, romper 1 cabo derruba toda a rede. | Na **Estrela (Switch)** cai só aquele PC; quem derruba tudo ao romper cabo único é **Barramento (*Bus*)**. |
| **24** | **Português/História** | Cultismo = jogo de ideias; Neolítico = nômade sem agricultura. | **Cultismo** = palavras/forma; **Conceptismo** = ideias/lógica; **Neolítico** = agricultura + sedentário; **Paleolítico** = nômade. |
| **25** | **Mat/Quím/Física** | Dízima periódica é Irracional; composto iônico conduz sólido; nº de 3 dígitos começa com `0`. | Dízima é **Racional (`ℚ`)**; **Metal** conduz sólido, **Iônico** só líquido/aquoso; `0` proibido na 1ª casa; tomate vermelho sob luz verde parece **PRETO**! |

---

### 📚 Parte 2 — Método Cirúrgico para Questões I, II e III + Revisão Comentada

#### Técnica de Eliminação em 15 Segundos
Quando enfrentar qualquer questão longa com afirmativas **I, II e III**:
1. Leia buscando **palavras absolutas perigosas**: *"sempre", "nunca", "exclusivamente", "unicamente"* — costumam esconder erro!
2. Ache **1 único item que você tem 100% de certeza que é FALSO** e risque todas as letras (A–E) que contenham esse número. Na maioria das provas da FAT, eliminar 1 item errado já elimina **3 alternativas de uma vez**, deixando você entre duas!
3. Compare apenas o item restante que desempata as duas opções!

#### 🕵️‍♂️ 3 Questões Finais Dissecadas (Integrando Tudo)

**Desafio Final 1 (Estilo Molde 1 — Integração SQL + Web + Redes):**
*Analise: I. `ALTER TABLE usuarios ADD telefone VARCHAR(20)` pertence à DDL. II. `<a href="pagina.html" target="_blank">` abre o link em uma nova aba, mantendo a atual aberta. III. O protocolo IMAP baixa os e-mails e os apaga imediatamente do servidor remoto para economizar espaço.*
- **Análise:** I é V (ALTER é estrutura = DDL). II é V (`_blank` = nova aba). **III é F** (quem apaga por padrão após baixar é o **POP3**; IMAP mantém sincronizado no servidor). **Gabarito: I e II corretas.**

**Desafio Final 2 (Estilo Molde 4 — Integração Matriz + Lógica + Casting):**
*Dada `M = [[4, 2], [9, 6]]` e o código: `double media = (M[0][0] + M[1][1]) / 3.0; int final = (int) media;`. Qual o valor de `final` e o nome do processo que gerou `final`?*
- **Passo a passo:** `M[0][0] + M[1][1]` (diagonal principal!) = `4 + 6 = 10`. Divisão real: `10 / 3.0 = 3.333...`. `(int) 3.333...` trunca para **`3`**, através de **Conversão Explícita (*Type Casting*)**.

**Desafio Final 3 (Estilo M-Tec Base Comum — Matemática + Química):**
*Considerando `H=1, C=12, O=16`, calcule a massa molar de `CH₃COOH` (`C₂H₄O₂`) e determine quantos números ímpares de 2 algarismos distintos existem usando `{0, 1, 2, 3}`.*
- **Química:** `C₂H₄O₂` = `2(12) + 4(1) + 2(16) = 24 + 4 + 32 =` **`60 g/mol`**.
- **Matemática:** Queremos número **ímpar** de 2 dígitos distintos com `{0, 1, 2, 3}`. Começamos pela restrição mais forte (**unidade** tem que ser ímpar → `1` ou `3` = **2 opções**). Depois na **dezena**, não pode `0` nem o ímpar já gasto na unidade (ex.: se gastou `1`, sobram `{2, 3}` = **2 opções**). Total = `2 × 2 =` **`4 números`** (`13, 21, 23, 31` — batendo exatamente!).

---

### 📚 Parte 3 — Estratégia de Execução no Dia da Prova (Sexta, 04/12/2026)

1. **Regra das 3 Passadas (Gestão de Tempo):**
   - **1ª Passada (45–60 min) — "Colheita Rápida":** Responda primeiro tudo que for definição direta e reconhecimento rápido (Inglês, Ética, SQL sublinguagens, E-mail, Cookies, Cores/Vetor, História/Literatura). Viu teste de mesa grande ou conta longa de geometria? Faça um círculo no número e **pule temporariamente** — todas as questões têm o mesmo peso!
   - **2ª Passada (60 min) — "Contas & I-II-III":** Resolva com calma os **Testes de Mesa**, **Matrizes**, **Binário/Hex**, **Conjuntos**, **Contagem** e **Química**, **sempre escrevendo o passo a passo no rascunho da prova**!
   - **3ª Passada (últimos 30 min) — "Conferência & Gabarito":** Ataque as 2 ou 3 difíceis restantes, preencha o **cartão-resposta** conferindo questão por questão em voz mental baixa (*"Questão 14... letra C!"*) e **nunca deixe nenhuma questão em branco**.
2. **Checklist de Véspera (Quinta, 03/12):**
   - Separe **RG/documento oficial original com foto**, comprovante/local de prova, **2 canetas esferográficas pretas/azuis de corpo transparente** e garrafa de água sem rótulo;
   - Releia apenas a **Cola de Bolso** (aba *Apostila & Cola*) por 15 minutos e **durma pelo menos 8 horas** — o cérebro consolida memórias e fica afiado contra pegadinhas quando está descansado. **Você cobriu 100% da prova — confie no seu preparo e arrebente!**

