# Guia Definitivo — Etec de Taboão da Serra (2ª Série M-Tec-PI Desenvolvimento de Sistemas)

**Calendário Oficial:** 1ª Fase Escrita em **04/12/2026** (40 questões • corte 20/40) • Resultado em **07/12/2026** • 2ª Fase Prática em Laboratório + Entrevista em **08/12/2026** (13h00–15h30).

Este manual foi 100% construído por engenharia reversa das provas reais e do Plano de Curso 612 da Etec de Taboão da Serra.

---

## Dia 1 (21/11) — Raio-X de Taboão da Serra, Regras da Vaga e Guia de Sobrevivência

> [!IMPORTANT]
> **Respira fundo — os números oficiais jogam MUITO a seu favor!**
> Analisando os documentos oficiais da **Etec de Taboão da Serra** dos últimos 3 anos (2023–2025):
> - Apenas **8 a 11 pessoas** fazem a prova escrita para a 2ª série de DS por ano.
> - Você só precisa acertar **20 de 40 questões (50%)** no dia **04/12** para ir à 2ª fase.
> - Nos últimos 3 anos, a maior nota da escrita foi **24/40** — e **NINGUÉM passou na 2ª fase prática** (0 de 7 aprovados na escrita!) porque foram sem treinar código!
> **Resumo:** você não precisa gabaritar nada de literatura pesada nem virar gênio em 14 dias. Precisa bater **25/40 com folga** e chegar no dia **08/12** sabendo fazer o básico de HTML+CSS, C# e Banco de Dados!

---

### 1. Como funciona o Processo Seletivo de Taboão (Edital nº 02)

| Etapa | Data e Horário | O que cai de verdade | Nota / Regra para Passar |
| :--- | :--- | :--- | :--- |
| **1ª Fase — Prova Escrita** | **04/12/2026** (sexta), 13h00 às 17h00 | **40 questões** (A a E): ~16 a 20 de Técnico (1º ano DS) + ~20 a 24 de Base Comum (1º ano EM) | **Eliminatória:** mínimo **20 acertos (50%)**. Nossa meta de segurança: **25+/40**. |
| **Resultado 1ª Fase** | **07/12/2026** (segunda) | Lista dos classificados convocados para o laboratório | Sai no site oficial `etects.cps.sp.gov.br` e na secretaria. |
| **2ª Fase — Prática + Entrevista** | **08/12/2026** (terça), 13h00 às 15h30 | **Avaliação Prática em Laboratório** (VS Code, C#, DER/SQL) + **Entrevista Individual** | **Eliminatória:** menções **MB, B, R** (passa) ou **I** (reprova). A prática é o **1º critério de desempate**! |

---

### 2. O Mapa Exato das 40 Questões da Prova de Taboão

A prova da Etec de Taboão é feita pelos **próprios professores da escola**, seguindo o **Plano de Curso 612 (1ª série M-Tec-PI DS)**. Olha o que **NÃO** existe no 1º ano (e por isso não vale perder noites de sono):
- **NÃO tem no 1º ano:** Biologia, Geografia, Filosofia, Sociologia, Programação Mobile, POO avançada, Redes complexas ou Segurança da Informação.
- **O QUE CAI SEMPRE (seu mapa do tesouro):**

| Bloco na Prova | Qtd. Média | Matérias do 1º Ano (Plano 612) | Por que vale ouro para você |
| :--- | :--- | :--- | :--- |
| **Bloco Técnico (6 matérias)** | **16 a 20 Qs** | TPA (**C#**), Web I (**HTML/CSS/Flexbox/URI**), **BD I**, **APS (UML/Requisitos)**, **Design/UX**, **Fundamentos (Hex/CLI)** | Questões **curtas e diretas**, que se repetem literalmente de um ano para o outro! Meta: **13 a 16 acertos** aqui. |
| **Português + Inglês** | **4 a 6 Qs** | Interpretação de texto, referenciação, adequação, função conativa + `Present Perfect` / `Phrasal Verbs` | Quase tudo é leitura atenta sem decoreba pesada de literatura! Meta: **4 acertos**. |
| **Aprofundamento + Arte/EdF** | **6 a 8 Qs** | Pesquisa Quali/Quanti, Método Científico, Empreendedorismo, Arte (Tema vs Técnica), Ed. Física (Músculos/Invasão) | Questões fáceis de bom senso + 10 min de leitura! Meta: **5 acertos**. |
| **Exatas + História** | **8 a 10 Qs** | Matemática (Venn, Log, PA, Gráficos, Áreas), Física (p×V, Lentes, MRUV), Química (Bohr, Reações), História (Idade Média, Renascimento) | Não precisa acertar todas! Garanta as **4 ou 5 mais diretas** e já bate **26–30/40**! |

> [!TIP]
> **A Matemática da Aprovação:** Se você acertar **14 no Técnico + 4 em Port/Ing + 5 em Pesquisa/Arte/EdF + 4 em Exatas/História = 27/40 (67,5%)** — acima da **maior nota dos últimos 3 anos** da escola!

---

### 3. Estratégia das 3 Passadas (Para Nunca Travar em 4 Horas de Prova)

Você terá **4 horas (240 minutos)** para 40 questões — isso dá **6 minutos por questão**, tempo de sobra se você não emperrar na questão difícil:
1. **1ª Passada — As Fáceis e Técnicas (primeiros 60 min):** Comece pelas questões técnicas (geralmente Q21 a Q40) e as diretas de Português/Pesquisa/Arte. Marque tudo que você já bate o olho e sabe. Isso dá confiança imediata e garante os primeiros ~15–18 pontos!
2. **2ª Passada — As Médias com Conta ou Leitura (próximos 90 min):** Volte nas questões de Matemática (gráficos, Venn, áreas), C# (teste de mesa com papel e caneta) e Física/Química que precisam de calma.
3. **3ª Passada — Difíceis + Eliminação + Gabarito (últimos 60 min):** Nunca deixe nenhuma em branco! Elimine as 2 ou 3 alternativas absurdas e escolha a mais coerente entre as restantes. Reserve **15 minutos finais** só para passar com calma para a folha de respostas.

---

### 4. Como Ler Qualquer Código na Prova (Tradução de 60 Segundos)

Mesmo nunca tendo programado antes, você só precisa traduzir **6 símbolos** que aparecem em C# e JavaScript:

| Símbolo no Código | Tradução em Português Claro | Exemplo Real |
| :--- | :--- | :--- |
| `=` (um sinal só) | **"Recebe / guarda dentro"** (Atribuição) | `x = 10;` → guarda `10` na caixinha `x`. |
| `==` (dois sinais) | **"É igual a?"** (Pergunta Sim/Não) | `if (x == 10)` → pergunta se `x` vale `10`. |
| `!=` | **"É diferente de?"** | `if (nota != 0)` → se `nota` não for zero. |
| `%` | **Resto da divisão** (NÃO é porcentagem!) | `7 % 2` dá **`1`** (7 dividido por 2 dá 3 e sobra 1). |
| `&&` e `\|\|` | **`&&` = E** (tudo V) \| **`\|\|` = OU** (basta 1 V) | `if (idade >= 16 && media >= 6)` |
| `;` e `{ }` | `;` é o **ponto final** \| `{ }` abre e fecha um **bloco** | Tudo dentro de `{ ... }` pertence ao `if` ou `for`. |

<details class="recall-box">
<summary>🧠 Sua vez — tente responder de cabeça e clique para conferir</summary>
<p><strong>Pergunta 1:</strong> Qual é a nota mínima na 1ª Fase (04/12) e qual menção já aprova na 2ª Fase (08/12)?</p>
<p><strong>Resposta:</strong> Na 1ª Fase precisa de <strong>20 acertos em 40 questões (50%)</strong>. Na 2ª Fase (Prática + Entrevista), qualquer menção <strong>R (Regular), B (Bom) ou MB (Muito Bom)</strong> já aprova — só <strong>I (Insatisfatório)</strong> reprova!</p>
<hr>
<p><strong>Pergunta 2:</strong> No código C# <code>if (numero % 2 == 0)</code>, o que esse trecho está testando?</p>
<p><strong>Resposta:</strong> Está testando se o <strong>resto da divisão de <code>numero</code> por 2 é igual a 0</strong> — ou seja, está verificando se o número é <strong>PAR</strong>!</p>
</details>

---

### 5. Missão Obrigatória de Hoje (21/11)

1. Vá na aba **📝 Provas & Simulados** e faça a **Prova Real Etec Taboão 2026 (aplicada em 05/12/2025 — 40Q)** com calma, sem consultar nada.
2. **Não desanime com a nota de hoje!** Esse é o **Diagnóstico Zero** (antes de estudar as aulas). Mesmo que você tire 12, 15 ou 18 hoje, vamos usar o relatório para ver exatamente onde subir +10 pontos em 12 dias!
3. No final da prova, clique no botão **📋 Copiar Diagnóstico p/ WhatsApp** e envie o resultado!


---

## Dia 2 (22/11) — TPA I: Lógica, Fluxograma, Tabela Verdade e `if/else` em C#

> [!NOTE]
> **Por que TPA (Técnicas de Programação e Algoritmos) é a matéria mais forte do 1º ano?**
> No Plano 612 de Taboão da Serra, TPA tem **120 aulas** (mais do que qualquer outra matéria técnica!) e usa a linguagem **C# no Visual Studio**. Ela cai tanto na **Prova Escrita (04/12)** quanto no **Laboratório Prático (08/12)**!

---

### 1. O que é um Algoritmo e os Símbolos de Fluxograma

Um **algoritmo** é simplesmente uma **receita de bolo passo a passo** com começo, meio e fim, sem ambiguidades. Quando desenhamos um algoritmo com caixinhas geométricas, chamamos de **Fluxograma**:

| Símbolo | Nome | Para que serve | Exemplo |
| :--- | :--- | :--- | :--- |
| **Retângulo arredondado (Oval)** | **Terminal** | **Início** e **Fim** do algoritmo | `Início` → ... → `Fim` |
| **Paralelogramo (inclinado)** | **Entrada / Saída** | Ler teclado ou mostrar na tela | `Leia(nota)` / `Escreva(media)` |
| **Retângulo normal** | **Processamento** | Cálculos e atribuições | `media = (n1 + n2) / 2` |
| **Losango (diamante)** | **Decisão (`if`)** | Pergunta com saída **Sim (V)** ou **Não (F)** | `media >= 6?` |

---

### 2. Variáveis e Tipos de Dados em C#

Imagine a memória RAM do computador como uma estante cheia de caixinhas com etiqueta. Cada caixinha é uma **variável**, e em **C#** você precisa avisar qual **tipo** de coisa cabe nela:

| Tipo em C# | O que guarda | Exemplo em C# | Pegadinha Clássica |
| :--- | :--- | :--- | :--- |
| `int` | Números **inteiros** (sem vírgula) | `int idade = 16;` | Se dividir `5 / 2` entre dois `int`, dá **`2`** (corta o `.5`!). |
| `double` | Números **reais** (com casa decimal) | `double media = 7.5;` | Em código usa **ponto** (`7.5`), nunca vírgula! |
| `string` | **Textos** (palavras ou frases) | `string nome = "Henrique";` | Sempre entre **aspas duplas** `"..."`. |
| `char` | **1 único caractere** | `char conceito = 'B';` | Sempre entre **aspas simples** `'...'`. |
| `bool` | **Lógico** (só dois valores!) | `bool aprovado = true;` | Só aceita `true` (verdadeiro) ou `false` (falso). |

---

### 3. Tabela Verdade — As 3 Regras de Ouro (`&&`, `||`, `!`)

Você só precisa memorizar **uma frase** para cada operador lógico:
- **E (`&&` em C# / `AND`):** É **exigente** — só dá **VERDADEIRO** se **TODOS** forem verdadeiros. (`V && F = F`).
- **OU (`||` em C# / `OR`):** É **bonzinho** — dá **VERDADEIRO** se **PELO MENOS UM** for verdadeiro. (`V || F = V`; só dá Falso se ambos forem Falsos).
- **NÃO (`!` em C# / `NOT`):** **Inverte** o resultado (`!true` vira `false`; `!false` vira `true`).

| A | B | `A && B` (E) | `A \|\| B` (OU) | `!A` (NÃO A) |
| :---: | :---: | :---: | :---: | :---: |
| **V** | **V** | **V** | **V** | F |
| **V** | **F** | F | **V** | F |
| **F** | **V** | F | **V** | **V** |
| **F** | **F** | F | F | **V** |

---

### 4. Como Ler Entrada, Saída e `if / else` em C# (Padrão Taboão!)

Olha como a prova de Taboão escreve C# de verdade (veja linha por linha):

```csharp
using System;                           // 1. Importa comandos básicos (como Console)

class Program                           // 2. Bloco principal do programa
{
    static void Main(string[] args)     // 3. Ponto de partida: tudo começa aqui!
    {
        Console.Write("Digite o valor: ");
        double valor = double.Parse(Console.ReadLine()); // Lê texto e converte para número decimal

        if (valor < 100)                // 4. Pergunta: valor é menor que 100?
        {
            Console.WriteLine("Imposto: 5%");
        }
        else if (valor <= 500)          // 5. Senão, testa uma 2ª condição (de 100 até 500)
        {
            Console.WriteLine("Imposto: 10%");
        }
        else                            // 6. Caso contrário (acima de 500)
        {
            Console.WriteLine("Imposto: 15%");
        }
    }
}
```

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO (2025 Q24 e 2026 Q34)!**
> - **Erro de sintaxe** (como esquecer `;` ou `}`) impede o programa de rodar — o compilador **recusa a compilação e mostra a linha do erro** (ele NÃO corrige sozinho!).
> - Na questão do **imposto com faixas** (2026 Q34), o `if / else if / else` escolhe **apenas UM caminho** conforme o valor digitado!

> [!CAUTION]
> **❌ Erros Clássicos de Iniciante em C#**
> 1. Confundir `Console.ReadLine()` (que **lê** do teclado) com `Console.WriteLine()` (que **escreve** na tela).
> 2. Escrever `if (x = 10)` com um igual só — o certo para **comparar** é **`if (x == 10)`**!
> 3. Esquecer o **ponto e vírgula `;`** no fim da linha (NÃO vai `;` depois do `if (...)` nem depois de `}`!).

<details class="recall-box">
<summary>🧠 Sua vez — teste de mesa mental e clique para conferir</summary>
<p><strong>Desafio 1:</strong> No código de imposto acima, se o usuário digitar <code>valor = 100</code>, o que aparece na tela?</p>
<p><strong>Resposta:</strong> Aparece <strong><code>Imposto: 10%</code></strong>! Porque <code>100 &lt; 100</code> é <strong>Falso</strong> (100 não é menor que 100), então ele vai para o <code>else if (valor &lt;= 500)</code>, que é <strong>Verdadeiro</strong>!</p>
<hr>
<p><strong>Desafio 2:</strong> Se <code>nota = 7</code> e <code>faltas = 20</code>, qual o resultado lógico de <code>(nota >= 6) && (faltas <= 15)</code>?</p>
<p><strong>Resposta:</strong> <strong>Falso (<code>false</code>)</strong>! A primeira parte é Verdadeira (<code>7 >= 6</code>), mas a segunda é Falsa (<code>20 <= 15</code>). No operador <strong>E (<code>&&</code>)</strong>, basta um Falso para tudo ficar Falso.</p>
</details>

> [!TIP]
> **🖥️ Teste em 1 Minuto (preparando para 08/12):** Abra `dotnetfiddle.net` no celular ou PC, cole o código acima trocando `Console.ReadLine()` por `double valor = 250;`, clique em **Run** e veja o resultado aparecer na hora!


---

## Dia 3 (23/11) — TPA II: Laços (`while`/`do`/`for`), Vetores, Matrizes `int[,]` e Depuração

> [!IMPORTANT]
> **A aula que mais dá pontos em TPA!**
> Na prova de Taboão 2025 e 2026 caíram **EXATAMENTE** estes 5 assuntos:
> 1. Diferença entre `while`, `do-while` e `for`
> 2. Vetores (`int[]`) e Matrizes (`int[,]`) em C#
> 3. Teste de mesa com operador `%` (resto da divisão)
> 4. **Breakpoints** na depuração (*debugging*)
> 5. **`try / catch`** para impedir que o programa trave quando o usuário digita letras em vez de número!

---

### 1. Os 3 Laços de Repetição (Loops) em C#

Um laço repete um bloco de comandos automaticamente sem você precisar copiar e colar 100 vezes:

| Laço em C# | Quando usar | Quantas vezes roda no mínimo? | Exemplo |
| :--- | :--- | :---: | :--- |
| **`for`** | Quando você **sabe exatamente** quantas voltas quer dar (ex.: de 0 até 4) | **0 vezes** (se já começar falso) | `for (int i = 0; i < 5; i++) { ... }` |
| **`while`** | **Pré-teste:** testa a condição **ANTES** de entrar | **0 vezes** (se já começar falso, nem entra!) | `while (x <= 10) { x++; }` |
| **`do { ... } while`** | **Pós-teste:** executa primeiro e só testa **NO FINAL** | **Pelo menos 1 vez GARANTIDA!** | `do { ... } while (opcao != 0);` |

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO (2025 Q21 e 2025 Q25)!**
> - **`do-while`** é o ÚNICO laço que **garante pelo menos uma execução** mesmo que a condição já comece falsa!
> - **Loop infinito:** acontece quando você esquece de alterar a variável da condição dentro do `while` (ex.: `x` nunca aumenta, então `x < 10` fica sempre verdadeiro e o programa trava!).

---

### 2. Como Fazer Teste de Mesa Sem Errar (Exemplo REAL de Taboão 2025 Q23!)

Veja este trecho real que caiu em Taboão da Serra:
```csharp
for (int i = 0; i < 10; i++)
{
    if (i % 2 == 0)
    {
        Console.WriteLine(i);
    }
}
```
**Passo a passo no papel (faça sempre uma mini-tabela!):**
- `i` começa em `0`, vai aumentando `+1` (`i++`) **enquanto `i < 10`** (logo, `i` passa por `0, 1, 2, 3, 4, 5, 6, 7, 8, 9` — **NÃO chega no 10**, porque `10 < 10` é Falso!).
- A condição `i % 2 == 0` deixa passar só os números **pares** (resto zero na divisão por 2).
- **Saída exata na tela:** **`0, 2, 4, 6, 8`**! *(Atenção: o `0` entra porque `0 % 2 == 0`, e o `10` NÃO entra porque era `< 10`, não `<= 10`!)*

---

### 3. Vetores (`int[]`) e Matrizes (`int[,]`) em C#

- **Vetor (1 dimensão — uma fileira de gavetas):** guarda vários valores do **mesmo tipo** em uma única variável.
  - Em C#, o índice **sempre começa no `0`**!
  - Se `int[] notas = { 7, 8, 10, 6 };`, então: `notas[0]` é `7`, `notas[1]` é `8`, `notas[2]` é `10`, `notas[3]` é `6`.
  - O tamanho é `notas.Length` (= `4`), mas o último índice válido é **`3`** (`Length - 1`). Tentar ler `notas[4]` gera erro (`IndexOutOfRangeException`)!
- **Matriz (2 dimensões — uma tabela com linhas e colunas):**
  - Em C#, declaramos com vírgula dentro dos colchetes: **`int[,] matriz`**!
  - Lemos sempre **`matriz[linha, coluna]`** (primeiro **LINHA**, depois **COLUNA**, começando do **0**!).

**Exemplo REAL de Taboão 2025 Q22:**
```csharp
int[,] matriz = {
    { 1, 2, 3 },   // Linha 0 -> colunas 0, 1, 2
    { 4, 5, 6 },   // Linha 1 -> colunas 0, 1, 2
    { 7, 8, 9 }    // Linha 2 -> colunas 0, 1, 2
};
Console.WriteLine(matriz[1, 2]);
```
- Vá na **Linha 1** (`{ 4, 5, 6 }`) e pegue a **Coluna 2** (`0→4`, `1→5`, `2→6`) → imprime **`6`**!

---

### 4. Depuração (*Breakpoints*) e Tratamento de Erros (`try / catch`)

> [!WARNING]
> **🔁 CAIU DIRETO EM TABOÃO 2026 (Q35 e Q36)!**
> - **Breakpoint (Ponto de Interrupção):** é uma "bolinha vermelha" que você clica ao lado de uma linha no Visual Studio. Quando o programa roda em modo Debug, ele **PAUSA naquela linha** para você olhar o valor de cada variável passo a passo e descobrir onde está o bug! *(Ele NÃO apaga código nem acelera o programa!)*
> - **`try / catch` (Tratamento de Exceções):** protege o programa contra entradas inválidas do usuário (ex.: usuário digita `"abc"` onde o programa esperava um `int`).
>   - Tudo que pode dar erro fica dentro do **`try { ... }`** ("tente fazer isso").
>   - Se der erro, em vez de o programa fechar travado, ele pula para o **`catch { ... }`** ("capture o erro e mostre uma mensagem amigável!").

```csharp
try
{
    int idade = int.Parse(Console.ReadLine());
    Console.WriteLine("Idade válida: " + idade);
}
catch (FormatException)
{
    Console.WriteLine("Ops! Digite apenas números inteiros.");
}
```

<details class="recall-box">
<summary>🧠 Sua vez — resolva de cabeça e clique para conferir</summary>
<p><strong>Desafio 1:</strong> Na matriz <code>{ {10, 20, 30}, {40, 50, 60} }</code>, qual valor está em <code>matriz[0, 2]</code> e em <code>matriz[1, 0]</code>?</p>
<p><strong>Resposta:</strong> <code>matriz[0, 2]</code> = Linha 0, Coluna 2 = <strong><code>30</code></strong>. E <code>matriz[1, 0]</code> = Linha 1, Coluna 0 = <strong><code>40</code></strong>!</p>
<hr>
<p><strong>Desafio 2:</strong> Para que serve um <em>breakpoint</em> no Visual Studio?</p>
<p><strong>Resposta:</strong> Serve para <strong>pausar a execução</strong> do programa em uma linha escolhida para que o programador possa inspecionar variáveis passo a passo e encontrar erros (bugs)!</p>
<hr>
<p><strong>Desafio 3:</strong> Um vetor de 5 posições em C# tem quais índices válidos? Ele pode guardar <code>int</code> e <code>string</code> misturados no mesmo vetor?</p>
<p><strong>Resposta:</strong> Índices válidos são <strong>0, 1, 2, 3 e 4</strong> (sempre começa em 0!). E <strong>NÃO</strong> pode misturar tipos — um vetor é <strong>homogêneo</strong> (todos os elementos têm o mesmo tipo, ex.: todos <code>int</code>)!</p>
</details>


---

## Dia 4 (24/11) — Programação Web I (Parte 1): HTML5, Formulários e Internet (WWW, URI, DNS, HTTP)

> [!IMPORTANT]
> **Programação Web I vale DOBRO:** são **3 a 5 questões garantidas** na prova de 04/12 **E** é o **Desafio Prático #1** no laboratório de 08/12! E a melhor notícia: HTML é super visual e fácil de aprender em 1 tarde!

---

### 1. Como Funciona a Internet (WWW, URI/URL, DNS, HTTP e TCP)

Quando você digita `https://etects.cps.sp.gov.br/vagas` no navegador, 4 peças entram em ação:

| Sigla | Nome Completo | O que faz na vida real | Analogia Simples |
| :--- | :--- | :--- | :--- |
| **WWW** | *World Wide Web* | Sistema de páginas/documentos conectados por **hiperlinks** na Internet | A "biblioteca gigante" de sites |
| **URI** | *Uniform Resource Identifier* | **Identificador único** de um recurso na web (a **URL** é o tipo de URI que diz o *endereço* onde o recurso está!) | O CPF / endereço completo de uma página ou arquivo |
| **DNS** | *Domain Name System* | Traduz nomes humanos (`google.com`) para endereços numéricos **IP** (`142.250.x.x`) | A "agenda telefônica" da Internet |
| **HTTP / HTTPS** | *HyperText Transfer Protocol* | Protocolo de comunicação entre navegador (cliente) e servidor. O **`S`** é de **Seguro (criptografado)**! | O "idioma" que o navegador usa para pedir a página |

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO 2026 (Q25 e Q27)!**
> - **URI** (*Uniform Resource Identifier*): identifica um recurso de forma única na Web! (Cuidado com pegadinhas que dizem que URI só serve para páginas HTML ou que é um tipo de servidor — falso!)
> - **TCP** é protocolo da camada de **Transporte** (garante entrega confiável dos pacotes); **HTTP** é da camada de **Aplicação**!

---

### 2. Anatomia de uma Página HTML5 e as Tags Favoritas de Taboão

**HTML** (*HyperText Markup Language*) **NÃO é linguagem de programação** — é uma **linguagem de marcação** que cria o esqueleto (estrutura) da página usando etiquetas chamadas **tags** (`<tag>...</tag>`).

```html
<!DOCTYPE html>                    <!-- Avisa o navegador: isso é HTML5! -->
<html lang="pt-BR">                <!-- Início da página em português -->
<head>                             <!-- CABEÇA: configurações INVISÍVEIS (título da aba, CSS, charset) -->
  <meta charset="UTF-8">
  <title>Site do Henrique</title>
  <link rel="stylesheet" href="style.css">  <!-- Liga o arquivo CSS externo -->
</head>
<body>                             <!-- CORPO: TUDO QUE APARECE VISÍVEL NA TELA! -->
  <header>
    <h1>Título Principal</h1>      <!-- h1 é o maior título; vai até h6 (o menor) -->
    <h2>Subtítulo</h2>
  </header>

  <main>
    <p>Este é um parágrafo.<br>E aqui pulou uma linha!</p>
    <hr>                           <!-- Linha horizontal divisória! -->
    <img src="foto.jpg" alt="Foto da escola Etec Taboão">
    <a href="https://etects.cps.sp.gov.br" target="_blank">Abrir em nova aba</a>
  </main>

  <script src="app.js"></script>   <!-- Liga um arquivo JavaScript externo! -->
</body>
</html>
```

> [!WARNING]
> **🔁 CAIU LITERAL EM TABOÃO 2025 (Q32, Q35) E TABOÃO 2026 (Q26)!**
> Decore estas **7 tags/atributos** porque caíram quase palavra por palavra:
> 1. **`<p>`** → cria um **parágrafo**.
> 2. **`<hr>`** → cria uma **linha horizontal** divisória (*Horizontal Rule*).
> 3. **`<h2>`** → cria um **subtítulo** (título nível 2; `<h1>` é o maior e `<h6>` o menor).
> 4. **`<br>`** → força uma **quebra de linha** (*Break*) sem fechar o parágrafo.
> 5. **`<body>`** → engloba **todo o conteúdo visível** da página.
> 6. **`<img src="..." alt="...">`** → o atributo **`alt`** exibe um **texto alternativo** se a imagem não carregar **E** garante **acessibilidade** para leitores de tela (pessoas com deficiência visual)!
> 7. **`<script src="arquivo.js"></script>`** → forma correta de ligar um arquivo **JavaScript externo** no HTML! *(NÃO confundir com `<link rel="stylesheet" href="style.css">`, que é para **CSS**!)*

---

### 3. Tags Semânticas, Listas, Tabelas e Formulários (`GET` vs `POST`)

| Grupo | Tags Essenciais | Como não confundir |
| :--- | :--- | :--- |
| **Semânticas HTML5** | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` | Dão **significado** ao bloco (bom para Google/SEO e acessibilidade). **`<div>` e `<span>` NÃO são semânticas** (são caixas genéricas)! |
| **Listas** | `<ol>` (ordenada: 1, 2, 3), `<ul>` (bolinhas), `<li>` (cada item) | `O` = Ordenada; `U` = *Unordered* (sem ordem). |
| **Tabelas** | `<table>`, `<tr>` (linha), `<th>` (título), `<td>` (célula de dado) | **`tr`** = *Table Row* (linha); **`td`** = *Table Data* (célula!). |
| **Formulários** | `<form action="..." method="POST">`, `<label>`, `<input type="password">`, `<button>` | **`GET`** manda os dados visíveis na **URL** (bom para pesquisas). **`POST`** manda escondido no **corpo da requisição** (OBRIGATÓRIO para **senhas** e cadastros!). |

> [!CAUTION]
> **❌ Erros Clássicos de Iniciante em HTML**
> - Achar que `<title>` aparece gigante no meio da página → **Errado!** `<title>` aparece lá em cima na **aba do navegador**; o título grande da página é `<h1>`!
> - Usar `<link>` para puxar JavaScript → **Errado!** CSS usa `<link rel="stylesheet" href="...">`; JavaScript usa `<script src="..."></script>`!
> - Esquecer `target="_blank"` quando a questão pede para abrir link em **nova aba**.

<details class="recall-box">
<summary>🧠 Sua vez — teste rápido e clique para conferir</summary>
<p><strong>Pergunta 1:</strong> Qual a diferença entre <code>&lt;br&gt;</code> e <code>&lt;hr&gt;</code>?</p>
<p><strong>Resposta:</strong> <code>&lt;br&gt;</code> faz uma <strong>quebra de linha</strong> (pula para a linha de baixo). <code>&lt;hr&gt;</code> desenha uma <strong>linha horizontal</strong> visível para separar seções!</p>
<hr>
<p><strong>Pergunta 2:</strong> Por que o atributo <code>alt</code> na tag <code>&lt;img&gt;</code> é obrigatório nas boas práticas?</p>
<p><strong>Resposta:</strong> Porque mostra um <strong>texto alternativo</strong> caso a imagem falhe ao carregar e permite que <strong>leitores de tela</strong> descrevam a imagem para pessoas com deficiência visual (acessibilidade)!</p>
<hr>
<p><strong>Pergunta 3:</strong> Em um formulário de login com senha, devo usar <code>method="GET"</code> ou <code>method="POST"</code>?</p>
<p><strong>Resposta:</strong> Sempre <strong><code>method="POST"</code></strong> (e <code>type="password"</code> no input), porque o <code>GET</code> expõe a senha visível na barra de endereço (URL)!</p>
</details>


---

## Dia 5 (25/11) — Programação Web I (Parte 2): CSS3, Box Model, Flexbox, `@media` e JavaScript

> [!NOTE]
> Se o **HTML** é o esqueleto (paredes e tijolos da casa), o **CSS** (*Cascading Style Sheets*) é a **pintura, decoração e posição dos móveis**, e o **JavaScript (JS)** é a **parte elétrica** (faz botões reagirem e coisas acontecerem)!

---

### 1. Como Escrever e Ler CSS (Seletores)

Toda regra CSS escolhe **quem** vai estilizar (seletor) e abre `{ propriedade: valor; }`:

| Seletor CSS | O que ele seleciona | Exemplo |
| :--- | :--- | :--- |
| `p` (nome da tag) | **Todas** as tags `<p>` da página | `p { color: blue; }` |
| **`.cartao`** (com **ponto `.`**) | Todos os elementos com `class="cartao"` (pode repetir várias vezes!) | `.cartao { padding: 16px; }` |
| **`#topo`** (com **cerquilha `#`**) | O elemento **único** com `id="topo"` | `#topo { background: navy; }` |

---

### 2. CSS Box Model — A Caixa que Todo Elemento Tem!

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO 2025 (Q34)!**
> No CSS, **todo elemento HTML é tratado como uma caixa retangular** composta por **4 camadas** (de dentro para fora):

```text
+----------------- MARGIN (espaço EXTERNO, afasta outras caixas) -----------------+
|  +--------------- BORDER (a moldura / borda da caixa) -----------------------+  |
|  |  +------------ PADDING (espaço INTERNO, acolchoamento) ----------------+  |  |
|  |  |                                                                     |  |  |
|  |  |                CONTENT (texto ou imagem de verdade)                 |  |  |
|  |  |                                                                     |  |  |
|  |  +---------------------------------------------------------------------+  |  |
|  +---------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------+
```
- **Dica para nunca inverter `padding` e `margin`:**
  - **`padding`** = *almofada **P**or dentro* (espaço entre o texto e a borda).
  - **`margin`** = ***M**argem de fora* (espaço externo entre esta caixa e a caixa vizinha).

---

### 3. Flexbox — O Queridinho de Taboão (Caiu na Escrita E Cai na Prática!)

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO 2025 (Q36) — E É A PROPRIEDADE #1 DO LAB 08/12!**
> O **Flexbox** (`display: flex;`) é o jeito moderno do CSS alinhar elementos em linha ou coluna e centralizar qualquer cartão sem sofrer!

Decore estas **4 propriedades mágicas** colocadas no **container (elemento pai)**:

```css
.container {
  display: flex;              /* 1. Liga o modo Flexbox! */
  flex-direction: row;        /* 2. Direção: row (lado a lado) ou column (empilhado) */
  justify-content: center;    /* 3. Alinha no EIXO PRINCIPAL (horizontal se for row) */
  align-items: center;        /* 4. Alinha no EIXO CRUZADO (vertical se for row) */
}
```
- Quer **centralizar perfeitamente** um cartão no meio da tela? Basta os 3 comandos:
  `display: flex; justify-content: center; align-items: center;`!
- Quer empurrar um logo para a esquerda e o menu para a direita? Use `justify-content: space-between;`!

---

### 4. Design Responsivo (`@media`) e Transformações CSS3

- **Media Queries (`@media`):** permitem mudar o layout conforme o tamanho da tela (celular vs. computador)!
  ```css
  /* Só aplica quando a largura da tela for até 600px (celular!) */
  @media (max-width: 600px) {
    .menu { flex-direction: column; }
  }
  ```
- **CSS3 `transform` (cai muito em provas Etec):**
  - `scale(1.2)` → aumenta proporcionalmente o tamanho;
  - `rotate(45deg)` → gira o elemento;
  - `translate(20px, 10px)` → move de lugar;
  - `skew(15deg)` → inclina/entorta o elemento.

---

### 5. JavaScript Básico: Tipos Primitivos e Interatividade

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO 2025 (Q33)!**
> No **JavaScript**, quais são os **tipos de dados primitivos**?
> - **`String`** (texto: `"Olá"`)
> - **`Number`** (números inteiros ou decimais: `10`, `7.5`)
> - **`Boolean`** (`true` ou `false`)
> - **`Undefined`** (variável criada sem valor ainda) e **`Null`** (vazio intencional)
> - *(Também existem `Symbol` e `BigInt`)*
> **Pegadinha clássica:** `Array` (lista) e `Object` (objeto) **NÃO são primitivos** — são objetos compostos!

```javascript
let nome = "Henrique";       // String (primitivo)
const nota = 8.5;            // Number (primitivo)
let passou = true;           // Boolean (primitivo)
```
- **`let`** → cria variável que pode mudar de valor depois.
- **`const`** → cria constante (não muda depois).
- **DOM** (*Document Object Model*): é a árvore de elementos HTML que o JavaScript manipula (ex.: `document.getElementById("titulo").innerText = "Oi!";`).

<details class="recall-box">
<summary>🧠 Sua vez — teste de Flexbox, Box Model e JS</summary>
<p><strong>Pergunta 1:</strong> Qual propriedade CSS cria espaço <strong>por dentro</strong> da borda de um botão e qual cria espaço <strong>por fora</strong>?</p>
<p><strong>Resposta:</strong> Por dentro = <strong><code>padding</code></strong>; por fora = <strong><code>margin</code></strong>!</p>
<hr>
<p><strong>Pergunta 2:</strong> Quais 3 linhas de CSS você escreve no elemento pai para centralizar um card tanto na horizontal quanto na vertical?</p>
<p><strong>Resposta:</strong> <code>display: flex; justify-content: center; align-items: center;</code></p>
<hr>
<p><strong>Pergunta 3:</strong> Entre <code>String</code>, <code>Array</code>, <code>Object</code> e <code>Function</code>, qual é um tipo de dado <strong>primitivo</strong> em JavaScript?</p>
<p><strong>Resposta:</strong> <strong><code>String</code></strong>! (<code>Array</code>, <code>Object</code> e <code>Function</code> são tipos compostos/objetos).</p>
</details>


---

## Dia 6 (26/11) — Banco de Dados I: Tabelas, Chaves (PK/FK), DER, Normalização e SQL

> [!IMPORTANT]
> **Banco de Dados I é uma mina de ouro na prova de Taboão!**
> Em 2025 caíram **4 questões seguidas** (Q37–Q40) e em 2026 caíram **3 questões super fáceis** (Q38–Q40) — além de ser o **Desafio Prático #3** do laboratório de 08/12!

---

### 1. A Analogia da Planilha (Que Resolve 3 Questões de Taboão 2026!)

Pense em um **Banco de Dados Relacional** como uma pasta com várias **planilhas organizadas** ligadas entre si:

| Termo de Banco de Dados | Analogia do Dia a Dia | Exemplo na Tabela `ALUNOS` |
| :--- | :--- | :--- |
| **Tabela (Entidade)** | Uma planilha / agenda inteira de um mesmo assunto | `ALUNOS` (ou `CONTATOS`, `LIVROS`) |
| **Coluna / Campo (Atributo)** | Cada característica armazenada | `id_aluno`, `nome`, `telefone`, `email` |
| **Linha / Registro (Tupla)** | **Todos os dados de UMA única pessoa/item** | `(1, "Henrique", "11-99999-0000", "h@etec.sp.gov.br")` |
| **Consulta (`SELECT` / Busca)** | Procurar um contato específico pelo nome na agenda do celular | `SELECT * FROM alunos WHERE nome = 'Henrique';` |

> [!WARNING]
> **🔁 CAIU LITERAL EM TABOÃO 2026 (Q38, Q39 e Q40)!**
> - **Tabela** = lista de alunos com colunas para nome, idade e nota.
> - **Registro** = **uma linha** com todas as informações sobre um único aluno (ou ficha individual).
> - Procurar um contato específico na agenda pelo nome = fazer uma **consulta / busca** no banco de dados!

---

### 2. Chave Primária (PK) vs. Chave Estrangeira (FK)

- **Chave Primária (`PK` — *Primary Key*):** é o **"CPF"** de cada linha da tabela.
  - **2 Regras sagradas:** **NUNCA pode repetir** (é única!) e **NUNCA pode ficar vazia** (`NOT NULL`)!
  - Ex.: `id_aluno` na tabela `ALUNOS`.
- **Chave Estrangeira (`FK` — *Foreign Key*):** é a Chave Primária de uma tabela colocada **dentro de outra tabela** para ligá-las com segurança (*Integridade Referencial*)!
  - Ex.: Um `ALUNO` pertence a uma `TURMA` (`1:N` — 1 turma tem muitos alunos). Então colocamos **`id_turma` (FK)** dentro da tabela `ALUNOS`!
  - **Regra de ouro:** em um relacionamento **`1:N`**, a **FK sempre vai para o lado `N`** (muitos)! Em **`N:N`** (ex.: Aluno ↔ Livro), criamos uma **3ª tabela associativa** (ex.: `EMPRESTIMO`) recebendo as duas FKs!

---

### 3. As 3 Etapas da Modelagem + Dicionário de Dados

> [!WARNING]
> **🔁 JÁ REPETIU EM TABOÃO (2022, 2025 Q38, Q39 e Q40)!**

| Etapa / Artefato | O que é (Definição Oficial de Prova) | Ferramenta / Cara |
| :--- | :--- | :--- |
| **1. Modelo Conceitual (DER)** | Visão de alto nível **independente do SGBD**; desenha **Entidades** (retângulos), **Relacionamentos** (losangos) e **Atributos** (elipses). | Diagrama Entidade-Relacionamento (DER / Peter Chen) |
| **2. Modelo Lógico** | Traduz o DER para **Tabelas, Colunas, PKs e FKs** (resolve `N:N` criando a 3ª tabela). | Esquema relacional de tabelas |
| **3. Modelo Físico** | Código **SQL real** (`CREATE TABLE ...`) rodando no SGBD (MySQL, SQL Server, PostgreSQL). | Script `.sql` |
| **Dicionário de Dados** | Documento que cataloga **nomes das tabelas/campos, tipos de dados, tamanhos, PK/FK e descrições** de tudo no banco. | Planilha/catálogo de metadados |

---

### 4. Normalização (1FN, 2FN, 3FN) — Por que Existe?

> [!WARNING]
> **🔁 JÁ CAIU EM TABOÃO 2025 (Q37)!**
> **Objetivo da Normalização:** **eliminar redundâncias (dados repetidos)** e evitar inconsistências/anomalias (ao inserir, atualizar ou apagar dados), garantindo integridade!
- **1ª Forma Normal (1FN):** **Valores atômicos (indivisíveis)** — nada de colocar dois telefones na mesma célula (`"9999-1111, 8888-2222"`) nem colunas repetidas (`tel1, tel2, tel3`).
- **2ª Forma Normal (2FN):** Estar na 1FN + sem dependência parcial (todo campo depende da PK **inteira**).
- **3ª Forma Normal (3FN):** Estar na 2FN + sem dependência transitiva (nenhum campo comum depende de outro campo comum que não é chave).

---

### 5. SQL em 60 Segundos (Para a 1ª e a 2ª Fase!)

Olhe sempre para a **primeira palavra**:
- **DDL (Estrutura — mexe no esqueleto da tabela):** `CREATE` (cria), `ALTER` (altera coluna), `DROP` (apaga a tabela inteira!).
- **DML (Dados — mexe nas linhas):** `INSERT` (insere linha), `UPDATE` (atualiza linha), `DELETE` (apaga linha).
- **DQL (Consulta — lê dados):** `SELECT coluna FROM tabela WHERE condicao;`

```sql
CREATE TABLE aluno (
    id_aluno INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES turma(id_turma)
);

INSERT INTO aluno (id_aluno, nome, id_turma) VALUES (1, 'Henrique', 2);
SELECT nome FROM aluno WHERE id_turma = 2;
```

<details class="recall-box">
<summary>🧠 Sua vez — teste de Banco de Dados e clique para conferir</summary>
<p><strong>Pergunta 1:</strong> Uma tabela <code>PRODUTO</code> tem 50 linhas e 4 colunas (<code>id, nome, preco, estoque</code>). Quantos <strong>registros</strong> e quantos <strong>campos</strong> ela tem?</p>
<p><strong>Resposta:</strong> Tem <strong>50 registros</strong> (linhas) e <strong>4 campos/atributos</strong> (colunas)!</p>
<hr>
<p><strong>Pergunta 2:</strong> Em uma escola, 1 <code>PROFESSOR</code> dá aula para N <code>TURMAS</code> (1:N). Onde vai a Chave Estrangeira (FK)?</p>
<p><strong>Resposta:</strong> A FK (<code>id_professor</code>) sempre vai na tabela do lado <strong>N</strong> → dentro da tabela <strong><code>TURMA</code></strong>!</p>
<hr>
<p><strong>Pergunta 3:</strong> Qual é o objetivo principal da <strong>Normalização</strong> de um banco de dados?</p>
<p><strong>Resposta:</strong> <strong>Eliminar redundâncias</strong> (repetição desnecessária de dados) e evitar anomalias/inconsistências, mantendo os dados íntegros e organizados!</p>
</details>


---

## Dia 7 (27/11) — APS (Requisitos, Ágil, UML) + Design Digital & UX

> [!IMPORTANT]
> **Dois assuntos de leitura rápida que rendem 4 a 6 questões fáceis na prova!**
> Em Taboão 2026 caíram **3 questões só de UML e UX** (Q28, Q29, Q30 — inclusive Q28 e Q31 repetiram o mesmo tema de Diagrama de Classes!), e em 2025 caíram **Requisitos, Metodologias Ágeis e UML** (Q26, Q27, Q28)!

---

### 1. APS — Requisitos Funcionais vs. Não Funcionais

Antes de programar qualquer aplicativo, o analista entrevista o cliente e escreve os **Requisitos** (o contrato do que será feito):

| Tipo | Pergunta que Responde | Exemplos Clássicos |
| :--- | :--- | :--- |
| **Requisito Funcional (RF)** | **O QUE** o sistema deve fazer? (funções, telas, cadastros, cálculos) | *"O sistema deve cadastrar alunos"*, *"O sistema deve emitir boletim em PDF"*, *"Calcular média final"*. |
| **Requisito Não Funcional (RNF)** | **COMO** o sistema se comporta? (qualidade, velocidade, segurança, visual, plataforma) | *"A página deve abrir em menos de 2 segundos"*, *"Senhas criptografadas"*, *"Funcionar em celular e PC"*. |

> [!WARNING]
> **🔁 JÁ REPETIU EM TABOÃO (2022 e 2025 Q26)!**
> Frase de prova: *"Os **requisitos funcionais** descrevem **o que** o sistema deve fazer (suas funcionalidades), enquanto os **requisitos não funcionais** especificam critérios de qualidade como desempenho, segurança e usabilidade."*

---

### 2. Cascata vs. Metodologias Ágeis (Scrum, XP, Kanban)

- **Modelo Cascata (*Waterfall*):** etapas **rígidas e sequenciais** (Análise → Projeto → Código → Teste). Só avança quando termina a fase anterior; difícil mudar algo no meio.
- **Metodologias Ágeis:** entregas **rápidas e iterativas** em ciclos curtos, feedback constante do cliente e adaptação a mudanças!
  - **Exemplos que caem na prova (Taboão 2025 Q27):** **Scrum**, **XP (*Extreme Programming*)** e **Kanban**!
  - **Scrum em 3 peças:** **Product Owner (PO)** (define o que vale mais negócio / *Backlog*), **Scrum Master** (ajuda o time e remove obstáculos), **Sprint** (ciclo curto de 1–4 semanas) e **Daily Scrum** (reunião diária de 15 min).
  - **Pegadinha:** *Cascata*, *Espiral* e *RUP* são modelos tradicionais — **NÃO são ágeis**!

---

### 3. UML — Os 2 Diagramas Favoritos de Taboão!

**UML** (*Unified Modeling Language*) é a linguagem padrão mundial para desenhar diagramas de software (como a planta baixa de um arquiteto). Em Taboão, 90% das questões cobram estes **2 diagramas**:

| Diagrama UML | Para que serve | Elementos Visuais |
| :--- | :--- | :--- |
| **Diagrama de Casos de Uso** *(Use Case)* | Mostra **O QUE** o sistema faz sob o ponto de vista do usuário (**interação entre atores e funcionalidades**) | **Ator** (bonequinho palito = usuário ou sistema externo) + **Caso de Uso** (oval com verbo: *"Fazer Login"*) |
| **Diagrama de Classes** | Mostra a **estrutura estática** do sistema: classes, **atributos**, **métodos** e as **associações/relacionamentos** entre elas! | Caixas com 3 divisórias (Nome / Atributos / Métodos) ligadas por linhas de **associação** (com multiplicidade `1..*`) |

> [!WARNING]
> **🔁 CAIU EM TABOÃO 2026 (Q28, Q29 e Q31)!**
> - **Diagrama de Casos de Uso:** representa as **funcionalidades do sistema e como os atores (usuários) interagem com elas**!
> - **Associações no Diagrama de Classes:** representam **como objetos de diferentes classes se relacionam/conectam entre si** (ex.: um `Aluno` está associado a uma `Turma`)!

---

### 4. Design Digital & UX (Usabilidade, Cores, Vetor vs. Bitmap, Gestalt)

| Tópico | O que você precisa saber na ponta da língua | Pegadinha para fugir |
| :--- | :--- | :--- |
| **UX & Usabilidade** *(Taboão 2026 Q30!)* | **Usabilidade** = facilidade, eficiência e satisfação com que o usuário aprende e usa a interface para concluir suas tarefas! | NÃO é só "ficar bonito/cheio de animações" — interface bonita difícil de usar tem **péssima usabilidade**! |
| **Cores: RGB vs. CMYK** | **RGB** (*Red, Green, Blue*): **luz / telas** (monitor, celular, TV).<br>**CMYK** (*Cyan, Magenta, Yellow, Key/Black*): **tinta / impressão gráfica** (folhetos, livros). | Inverter RGB com CMYK! Dica: **C**MYK tem **K** de tinta preta de cartucho! |
| **Vetor vs. Bitmap** | **Vetor** (`SVG`, `AI`, `EPS`, `PDF`): feito por fórmulas matemáticas — **pode ampliar infinito sem pixelar** (ideal para **logotipos**!).<br>**Bitmap/Raster** (`JPEG`, `PNG`, `BMP`, `GIF`): feito de grade de **pixels** — se ampliar muito, serrilha! (`PNG` aceita fundo transparente!). | Dizer que `JPEG` ou `PNG` é vetorial! |
| **Leis da Gestalt** | **Proximidade** (itens perto parecem do mesmo grupo), **Semelhança** (mesma cor/forma parecem grupo), **Fechamento** (cérebro completa figuras abertas), **Continuidade** (olho segue linhas suaves). | Esquecer que colocar rótulo **perto** do campo de texto é **Proximidade**! |

<details class="recall-box">
<summary>🧠 Sua vez — 3 perguntas diretas de APS e UX</summary>
<p><strong>Pergunta 1:</strong> "O aplicativo deve carregar a tela inicial em até 2 segundos" é Requisito Funcional ou Não Funcional?</p>
<p><strong>Resposta:</strong> <strong>Requisito Não Funcional</strong> (desempenho/velocidade = diz <em>como</em> o sistema se comporta, não uma nova função)!</p>
<hr>
<p><strong>Pergunta 2:</strong> Qual diagrama UML usa bonequinhos (atores) e ovais para mostrar como o usuário interage com as funções do sistema?</p>
<p><strong>Resposta:</strong> <strong>Diagrama de Casos de Uso</strong>!</p>
<hr>
<p><strong>Pergunta 3:</strong> Você vai criar um logotipo que vai aparecer num ícone pequeno e num outdoor gigante de 5 metros. Qual tipo de imagem escolher?</p>
<p><strong>Resposta:</strong> <strong>Imagem Vetorial (ex.: SVG)</strong>, pois é baseada em equações matemáticas e nunca perde qualidade/pixela ao ampliar!</p>
</details>


---

## Dia 8 (28/11) — Fundamentos da Informática: Hexadecimal (`187=BB`), Binário, CLI, Hardware e SO

> [!IMPORTANT]
> **A aula com o MAIOR índice de repetição literal de Taboão da Serra!**
> Olha que absurdo: em **2024 (Q29 e Q30)** e de novo em **2025 (Q32 e Q33)**, a escola colocou **AS MESMAS DUAS QUESTÕES** (Hexadecimal do número `187` e definição de `CLI`)! Se você dominar esta aula, são **2 a 4 pontos praticamente garantidos no bolso**!

---

### 1. Conversão Decimal → Hexadecimal (O Clássico `187 = BB`!)

> [!WARNING]
> **🔁 REPETIU IDÊNTICO EM TABOÃO 2025 (Q29) E TABOÃO 2026 (Q33)!**

O sistema **Hexadecimal (base 16)** usa **16 símbolos**: os números de `0` a `9`, e depois as letras **`A` até `F`** para valer de 10 a 15:

| Decimal | 0–9 | **10** | **11** | **12** | **13** | **14** | **15** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hexadecimal** | 0–9 | **`A`** | **`B`** | **`C`** | **`D`** | **`E`** | **`F`** |

**Receita Infalível (Divisões Sucessivas por 16):**
Vamos converter **`187`** (decimal) para Hexadecimal passo a passo:
1. Divida `187 ÷ 16`:
   - `16 × 10 = 160`
   - `16 × 11 = 176` (o mais perto sem passar!)
   - **Quociente = `11`** e **Resto = `187 - 176 = 11`**!
2. Como o quociente (`11`) já é menor que `16`, acabou!
3. Leia **do último quociente para o resto** trocando 10–15 pelas letras:
   - Quociente `11` = **`B`**
   - Resto `11` = **`B`**
   - Resultado: **`187 (decimal) = BB (hexadecimal)`**!

**Outro exemplo para treinar (`250` → Hex):**
- `250 ÷ 16`: `16 × 15 = 240` → Quociente = **`15` (`F`)**, Resto = `250 - 240 =` **`10` (`A`)** → **`250 = FA`**!

---

### 2. Binário ↔ Decimal em 30 Segundos (Tabela das Potências de 2)

Um **bit** vale `0` ou `1`. Um **Byte** são **8 bits**. Para converter qualquer binário em decimal, basta somar os pesos onde tem **`1`**:

| Posição (da dir. p/ esq.) | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Exemplo: `01100100` | 0 | **1** | **1** | 0 | 0 | **1** | 0 | 0 |
| **Soma onde tem `1`:** | — | **64** | **+32** | — | — | **+4** | — | — |

`64 + 32 + 4 = 100`! E se todos os 8 bits forem `1` (`11111111`) = `128+64+32+16+8+4+2+1` = **`255`**!
- **Macete de ouro:** Se o último bit (da direita) for **`1`**, o número é **ÍMPAR**. Se for **`0`**, é **PAR**!

---

### 3. Interface CLI vs. GUI e Sistemas Multiusuário

> [!WARNING]
> **🔁 REPETIU IDÊNTICO EM TABOÃO 2025 (Q30) E TABOÃO 2026 (Q32)!**

| Conceito | Definição Exata de Prova (Taboão) | Exemplo |
| :--- | :--- | :--- |
| **CLI** (*Command Line Interface*) | **Interface por linha de comando** (somente texto digitado, sem janelas gráficas/ícones; tradicionalmente chamada na questão de *"interface monotarefa/textual por linha de comando"*) | Prompt de Comando (CMD), PowerShell, Terminal Linux |
| **GUI** (*Graphical User Interface*) | **Interface Gráfica do Usuário** — janelas, ícones, botões e ponteiro de mouse | Windows 11, macOS, Android |
| **Sistema Multiusuário** *(Taboão 2025 Q31!)* | Permite que **vários usuários utilizem o sistema simultaneamente** (ou com contas isoladas), cada um com suas próprias permissões e arquivos! | Linux, Windows Server |

---

### 4. Hardware, Memórias, Sistema Operacional e Software Livre

| Componente | O que faz na prática | Detalhe que cai em prova |
| :--- | :--- | :--- |
| **CPU (Processador)** | O "cérebro" que executa cálculos e instruções (ULA + Unidade de Controle + Registradores) | Medida em GHz (clock) e núcleos (cores) |
| **Memória RAM** | Memória principal de trabalho **VOLÁTIL** (apaga tudo quando desliga a energia!) | Mais rápida que HD/SSD, guarda programas abertos agora |
| **HD vs. SSD** | Armazenamento **NÃO-VOLÁTIL** (guarda arquivos mesmo desligado). **SSD** usa memória flash (sem partes móveis) → muito **mais rápido e resistente a impactos** que o HD (disco magnético giratório)! | Pegadinha: achar que SSD é volátil (NÃO é! RAM é volátil!) |
| **Sistema Operacional (SO)** | Software base que faz a **interface (ponte) entre o usuário (*peopleware*) e o hardware**, gerenciando CPU, memória e arquivos | Windows, Linux, Android, iOS |
| **Software Livre** | Software que garante a liberdade de **usar, estudar, modificar e redistribuir o código-fonte** (ex.: Linux, VS Code open-source) | **Pegadinha clássica:** Software Livre **NÃO** significa necessariamente gratuito (pode ser vendido!) — e Freeware gratuito NÃO é software livre se o código for fechado! |
| **Git (Controle de Versão)** | Guarda histórico do código em equipe: `commit` (salva ponto), `branch` (ramo paralelo), `diff` (compara diferenças), `merge` (junta ramos) | Muito útil também na vida real de DS! |

<details class="recall-box">
<summary>🧠 Sua vez — 3 exercícios rápidos de Fundamentos (clique para conferir)</summary>
<p><strong>Desafio 1:</strong> Converta o número decimal <strong><code>205</code></strong> para Hexadecimal!</p>
<p><strong>Resposta:</strong> Divida <code>205 ÷ 16</code>: <code>16 × 12 = 192</code> → Quociente = <strong><code>12</code> (letra <code>C</code>)</strong>, Resto = <code>205 - 192 = 13</code> (letra <strong><code>D</code></strong>). Logo, <strong><code>205 = CD</code></strong>!</p>
<hr>
<p><strong>Desafio 2:</strong> O que significa a sigla <strong>CLI</strong>?</p>
<p><strong>Resposta:</strong> <em>Command Line Interface</em> — <strong>Interface por Linha de Comando</strong> (onde o usuário digita comandos de texto no terminal em vez de clicar em ícones gráficos)!</p>
<hr>
<p><strong>Desafio 3:</strong> Qual memória perde todos os dados quando falta luz: <strong>RAM</strong> ou <strong>SSD</strong>?</p>
<p><strong>Resposta:</strong> A <strong>Memória RAM</strong> (porque é <strong>volátil</strong>)! O SSD (e o HD) é memória secundária <strong>não-volátil</strong> e mantém os arquivos salvos.</p>
</details>


---

## Dia 9 (29/11) — Base Comum I: Português Prático & Inglês Técnico (Sem Travar em Literatura!)

> [!IMPORTANT]
> **Alívio real para quem trava em Português:**
> Nas provas oficiais de **Taboão da Serra (2024 e 2025)**, das 4 questões de Português, **quase tudo é leitura e interpretação inteligente** (coesão, adequação ao contexto, função da linguagem e concordância). Você **não** precisa decorar 50 livros antigos!

---

### 1. Os 5 Temas de Português que Realmente Caem em Taboão

| Tema | Explicação Direta em 1 Frase | Exemplo Real de Taboão |
| :--- | :--- | :--- |
| **1. Interpretação de Texto** | Leia o enunciado **antes** do texto; a resposta certa **NUNCA** exagera (*"sempre", "nunca", "única causa"*) e sempre respeita o que o autor escreveu! | Taboão 2026 Q01–Q02: texto sobre plataformas digitais e *fake news* — exige **leitura crítica** das fontes! |
| **2. Referenciação (Coesão)** | Usar pronomes (`ele, esse, cujo, onde`) ou sinônimos para **retomar algo já dito** sem deixar dúvida de quem está falando! | **Cuidado com ambiguidade:** *"Pedro falou com João sobre **seu** projeto"* (de quem é o projeto? Ambiguidade!). Forma certa (Taboão 2026 Q03): *"O livro **cujo** autor..."* ou retomar claramente com *"esse estudo"*. |
| **3. Adequação Linguística** | Não existe "falar errado" — existe falar **adequado ou inadequado à situação**! Gíria com amigos = adequado; gíria numa entrevista de emprego = inadequado. | Taboão 2026 Q04: adaptar a fala ao contexto, público e objetivo comunicativo! |
| **4. Funções da Linguagem** | **Conativa/Apelativa** = tenta **convencer o leitor** usando verbos no imperativo (*"Compre já!", "Inscreva-se!"*). **Referencial** = informa dados objetivos (jornal). **Emotiva** = focada no "eu" (sentimentos). | Taboão 2025 Q03: anúncio *"Compre já! Esta é a melhor oferta!"* → **Função Conativa (Apelativa)**! |
| **5. Concordância & Figuras** | **Concordância:** adjetivos concordam com o substantivo (*"Os alunos estavam ansiosos e **atentos**"* — e não *"atento"*!). **Figuras:** **Metáfora** (comparação escondida), **Antítese** (opostos: *dia/noite*), **Paradoxo** (contradição ilógica). | Taboão 2025 Q01 (erro de concordância em *"atento"*) e Q02 (poema *Morte e Vida Severina*). |

> [!TIP]
> **Bônus relâmpago (se cair Literatura Clássica da 1ª série):**
> - **Quinhentismo (séc. XVI):** Carta de Pero Vaz de Caminha (informativa) + textos jesuíticos de Anchieta.
> - **Barroco:** contrastes (vida/morte). **Cultismo** = jogo de **palavras**; **Conceptismo** = jogo de **ideias**!

---

### 2. Inglês em Taboão — 2 Pontos Fáceis que Quase Ninguém Estuda!

> [!WARNING]
> **🔁 CAIU DIRETO EM TABOÃO 2025 (Q04) E TABOÃO 2026 (Q05 e Q06)!**

#### A. Present Perfect (`have / has + Particípio`) — Caiu em 2 questões seguidas em 2026!
Usamos **Present Perfect** para falar de ações que **começaram no passado e continuam agora** OU ações passadas **sem data exata marcada** (muito comum com `already`, `yet`, `just`, `since`, `for`, `ever`):
- **Fórmula de ouro:**
  - `I / You / We / They` → **`have` + verbo no 3º tempo (Particípio)**
  - `He / She / It` → **`has` + verbo no 3º tempo (Particípio)**
- **Verbos regulares:** só coloca **`-ed`** (`finished`, `studied`, `worked`).
- **Verbos irregulares favoritos de prova:** `go → gone`, `see → seen`, `do → done`, `write → written`, `read → read`, `make → made`.
- **Exemplo certo:** *"She **has finished** her homework."* / *"The students **have read** the chapter."*
- **Pegadinha clássica:** Nunca misture `has` com plural (*"They has"* = ERRADO!), nem `have` com passado simples irregular (*"She has went"* = ERRADO! O certo é *"She has **gone**"*!).

#### B. Phrasal Verbs (Verbo + Preposição que Muda o Sentido!) — Caiu em Taboão 2025 Q04!
| Phrasal Verb | Significado Real | Exemplo |
| :--- | :--- | :--- |
| **`give up`** | **Desistir** | *Never give up!* (Nunca desista!) |
| **`look for`** | **Procurar** | *I'm looking for a job.* |
| **`find out`** | **Descobrir** | *We need to find out the bug.* |
| **`turn on` / `turn off`** | **Ligar / Desligar** | *Turn off the computer.* |
| **`carry on` / `go on`** | **Continuar** | *Carry on studying!* |
| **`put off`** | **Adiar** | *Don't put off your tasks.* |

#### C. Falsos Cognatos (Palavras que Parecem Português, Mas Enganam!)
- `actually` = **na verdade** (NÃO é "atualmente"!)
- `data` = **dados** (NÃO é "data de calendário"!)
- `pretend` = **fingir** (NÃO é "pretender"!)
- `push` = **empurrar** (NÃO é "puxar" — puxar é `pull`!)

<details class="recall-box">
<summary>🧠 Sua vez — 3 questões rápidas de Português e Inglês</summary>
<p><strong>Pergunta 1:</strong> A frase publicitária <em>"Clique agora e garanta sua vaga!"</em> usa qual Função da Linguagem?</p>
<p><strong>Resposta:</strong> <strong>Função Conativa (ou Apelativa)</strong>, pois usa verbos no imperativo (<em>Clique, garanta</em>) para convencer o leitor a agir!</p>
<hr>
<p><strong>Pergunta 2:</strong> Complete corretamente no <em>Present Perfect</em>: <code>"Maria _____ (finish) the project."</code></p>
<p><strong>Resposta:</strong> <strong><code>has finished</code></strong>! (Maria = <em>She</em> → usa <strong><code>has</code></strong> + particípio <code>finished</code>!)</p>
<hr>
<p><strong>Pergunta 3:</strong> O que significa o <em>phrasal verb</em> <strong><code>give up</code></strong> e o que significa <strong><code>find out</code></strong>?</p>
<p><strong>Resposta:</strong> <code>give up</code> = <strong>desistir</strong>; <code>find out</code> = <strong>descobrir</strong>!</p>
</details>


---

## Dia 10 (30/11) — Aprofundamento (Pesquisa & Empreendedorismo) + Arte & Educação Física

> [!IMPORTANT]
> **Os 6 pontos mais "de graça" da prova de Taboão!**
> Em Taboão 2026 caíram **8 questões** desses 4 blocos (Q07–Q10 de Arte/Ed. Física e Q21–Q24 de Ciência/Pesquisa). Quase todo mundo ignora isso porque acha que "não cai" — e você vai acertar quase todas com 20 minutos de leitura!

---

### 1. Laboratório de Investigação Científica (Método + Qualitativa vs. Quantitativa)

> [!WARNING]
> **🔁 CAIU EM TABOÃO 2025 (Q15) E TABOÃO 2026 (Q23 e Q24)!**

- **Ordem Oficial do Método Científico:**
  `1. Observação` → `2. Problema / Pergunta` → `3. Hipótese` → `4. Experimentação (Testes)` → `5. Análise de Dados` → `6. Conclusão`!
- **Pesquisa Qualitativa vs. Quantitativa (Caiu em 2026 Q24!):**

| Tipo de Pesquisa | Foco Principal | Como Coleta Dados | Exemplo |
| :--- | :--- | :--- | :--- |
| **Quantitativa** *(de **QUANTO**)* | **Números, estatísticas, gráficos, porcentagens** | Questionários fechados, medições, censos | *"72% dos alunos usam celular para estudar."* |
| **Qualitativa** *(de **QUALIDADE / SENTIDO**)* | **Opiniões, sentimentos, significados, profundidade** | Entrevistas abertas, observação, análise de falas | *"Por que os estudantes se sentem inseguros antes da prova?"* |

> **Pegadinha:** Uma pesquisa científica pode usar **as duas juntas** (pesquisa mista / quali-quanti) — elas se complementam!

---

### 2. Práticas de Empreendedorismo (Análise SWOT + Perfil Empreendedor)

- **Empreendedorismo (Taboão 2025 Q16):** empreendedores bem-sucedidos combinam **planejamento, resiliência (aprender com erros), inovação e visão de oportunidades** — NÃO é "apostar na sorte sem planejar"!
- **Análise SWOT (ou FOFA em português):** divide o diagnóstico do negócio em **Ambiente Interno** (você controla!) vs. **Ambiente Externo** (mercado, você não controla!):
  - **S — *Strengths* (Forças):** Interno + Positivo (ex.: equipe qualificada, bom preço).
  - **W — *Weaknesses* (Fraquezas):** Interno + Negativo (ex.: pouco dinheiro em caixa, site lento).
  - **O — *Opportunities* (Oportunidades):** Externo + Positivo (ex.: crescimento da demanda de TI).
  - **T — *Threats* (Ameaças):** Externo + Negativo (ex.: novo concorrente forte, crise econômica).

---

### 3. Arte — Tema vs. Técnica em Processos Criativos (Caiu em 2026 Q07 e Q08!)

> [!WARNING]
> **🔁 CAIU DUAS QUESTÕES SEGUIDAS EM TABOÃO 2026 (Q07 e Q08)!**

Não confunda nunca **O QUE** a obra fala com **COMO** ela foi feita:
- **TEMA (Assunto / Ideia):** é a **mensagem ou questão** que o artista quer abordar!
  - *Exemplos de Tema:* preservação ambiental, identidade cultural, desigualdade social, amizade, memória urbana.
- **TÉCNICA (Modo de Fazer / Procedimento):** é o **método prático e os materiais** usados para criar a obra!
  - *Exemplos de Técnica:* pintura a óleo, aquarela, colagem, gravura, escultura em argila, grafite com spray, fotografia digital.
- **Arte Urbana / Grafite (Taboão 2025 Q20):** o grafite (como os murais do paulistano **Speto** inspirados em xilogravura/cordel) é uma forma legítima de **arte visual contemporânea**, democratizando o espaço público!

---

### 4. Educação Física — Músculos, Aparelho Locomotor e Esportes de Invasão

> [!WARNING]
> **🔁 CAIU EM TABOÃO 2025 (Q19) E TABOÃO 2026 (Q09 e Q10)!**

- **Os 3 Tipos de Contração Muscular (Caiu em 2026 Q09!):**
  1. **Isométrica:** o músculo faz força **SEM mudar de tamanho / sem movimento articular** (ex.: segurar uma **prancha abdominal** parada ou empurrar uma parede!).
  2. **Isotônica Concêntrica:** o músculo **encurta** vencendo a carga (ex.: **subir** o haltere na rosca bíceps).
  3. **Isotônica Excêntrica:** o músculo **alonga controladamente** freando a carga (ex.: **descer** o haltere devagar).
- **Aparelho Locomotor (Caiu em 2026 Q10!):** formado por **ossos (esqueleto) + articulações + músculos**. Função principal: **sustentação do corpo, proteção de órgãos vitais e movimentação (locomoção)**!
- **Esportes de Invasão (Caiu em 2025 Q19!):** esportes coletivos em que o time precisa **invadir o campo adversário** para fazer ponto/gol e defender a própria meta!
  - **SÃO de Invasão:** Futebol, Futsal, Basquete, Handebol, Rugby, Hóquei, Polo Aquático.
  - **NÃO são de Invasão:** Vôlei e Tênis (são de **rede/parede** — ninguém invade o outro lado!), Natação e Atletismo (esportes de **marca**), Ginástica (técnico-combinatório).

<details class="recall-box">
<summary>🧠 Sua vez — 4 perguntas relâmpago (clique para conferir)</summary>
<p><strong>1.</strong> Um questionário com 500 respostas de "Sim/Não" gerando gráficos de porcentagem é pesquisa <strong>Qualitativa</strong> ou <strong>Quantitativa</strong>?</p>
<p><strong>Resposta:</strong> <strong>Quantitativa</strong> (trabalha com quantidade, números e estatísticas)!</p>
<hr>
<p><strong>2.</strong> "Aquarela sobre papel" é <strong>Tema</strong> ou <strong>Técnica</strong> artística?</p>
<p><strong>Resposta:</strong> <strong>Técnica</strong> (é o <em>como</em> foi feita)! "Sustentabilidade nas cidades" seria um <strong>Tema</strong>!</p>
<hr>
<p><strong>3.</strong> Segurar uma prancha abdominal parada sem se mexer é qual tipo de contração muscular?</p>
<p><strong>Resposta:</strong> Contração <strong>Isométrica</strong> (gera tensão sem encurtar nem alongar o músculo)!</p>
<hr>
<p><strong>4.</strong> Qual destes NÃO é esporte de invasão: Basquete, Handebol, Vôlei ou Futsal?</p>
<p><strong>Resposta:</strong> <strong>Vôlei</strong> (é esporte de <strong>rede/quadra dividida</strong> — os times não invadem o campo adversário)!</p>
</details>


---

## Dia 11 (01/12) — Base Comum II: Matemática de Taboão (Sem Trauma — Só os 7 Moldes que Caem!)

> [!TIP]
> **Segredo para não travar em Matemática:** Você **NÃO** precisa estudar a apostila inteira do Ensino Médio! Nos últimos anos de Taboão (2021, 2024 e 2025), caíram **4 questões por prova**, e quase todas repetem estes **7 moldes exatos**!

---

### Molde 1: Gráficos e Porcentagem (Os 2 Pontos Mais Fáceis de 2026 Q13–Q14!)

- **Porcentagem sem fórmula complicada:**
  - `10%` → divide por `10` (anda 1 casa com a vírgula!). Ex.: 10% de `250 = 25`.
  - `1%` → divide por `100`. Ex.: 1% de `250 = 2,5`.
  - Para achar `35%` de `200`: faça `(35 × 200) ÷ 100 = 70`!
- **Receita vs. Despesa (Taboão 2026 Q14):**
  - **Lucro** = `Receita - Despesa` (quando a barra de Receita é **maior** que a de Despesa!).
  - **Prejuízo** = quando a Despesa é maior que a Receita.
  - Sempre leia os **eixos** e a **legenda** do gráfico antes de fazer qualquer conta!

---

### Molde 2: Conjuntos e Diagrama de Venn (Repetiu em 2021 e 2025 Q08!)

> **Exemplo clássico de Taboão:** *"Numa pesquisa com 170 pessoas, 92 leem o jornal A, 88 leem o jornal B e 20 não leem nenhum. Quantos leem OS DOIS (interseção)?"*
- **Receita de 3 passos (nunca erra!):**
  1. Tire quem não gosta de nenhum: `170 - 20 = 150` pessoas leem pelo menos um jornal.
  2. Some os dois grupos inteiros: `92 + 88 = 180`.
  3. O que **passou** de `150` é exatamente quem foi contado duas vezes (**a interseção**!): `180 - 150 =` **`30` pessoas leem os dois**!

---

### Molde 3: Logaritmo com Propriedades (Repetiu em 2021 e 2025 Q09!)

Parece assustador, mas é **100% conta de somar e multiplicar** usando só **2 regrinhas**:
1. **Produto vira SOMA:** `log_a(m · n) = log_a(m) + log_a(n)`
2. **Expoente cai multiplicando na frente (Regra do Tombamento):** `log_a(mᵏ) = k · log_a(m)`

**Exemplo real de Taboão 2025 Q09:**
Dados `log_a(m) = 11` e `log_a(n) = 6`, quanto vale `log_a(m² · n²)`?
- Separa o produto em soma: `log_a(m²) + log_a(n²)`
- Tomba os expoentes: `2 · log_a(m) + 2 · log_a(n)`
- Substitui os valores: `2(11) + 2(6) = 22 + 12 =` **`34`**! *(Viu como demorou 10 segundos?!)*

---

### Molde 4: Progressão Aritmética — PA (Repetiu em 2021 e 2025 Q10!)

**PA** é uma sequência que sobe sempre somando a mesma razão `r` (ex.: `10, 15, 20, 25...` onde `a₁ = 10` e `r = 5`).
- **Termo geral:** `aₙ = a₁ + (n - 1) · r`
- **Exemplo real (Marta na poupança — Taboão 2025 Q10):**
  - 1º mês: `a₁ = 10`, sobe `r = 5` todo mês. Em qual mês deposita `250`?
  - `250 = 10 + (n - 1) · 5` → `240 = (n - 1) · 5` → `240 / 5 = 48` → `n - 1 = 48` → **`n = 49` meses**!

---

### Molde 5: Inequação de 1º Grau (Taboão 2025 Q07)

Resolva igual a uma equação normal (`x` de um lado, número do outro).
- **Única regra especial:** se multiplicar ou dividir por número **NEGATIVO**, **inverte o sinal** (`<` vira `>`, `≤` vira `≥`)!
- Ex.: `1 - 2x > 7` → `-2x > 6` → divide por `-2` e **vira o sinal**: **`x < -3`**!

---

### Molde 6: Geometria — Teorema de Pitágoras, Semelhança e Áreas (Taboão 2026 Q11–Q12!)

| Fórmula | Quando usar | Exemplo rápido |
| :--- | :--- | :--- |
| **Retângulo:** `A = base × altura` | Terrenos, chapas retangulares | `20 × 15 = 300 m²` |
| **Triângulo:** `A = (base × altura) / 2` | Telhados, cortes diagonais | `(10 × 6) / 2 = 30 m²` |
| **Trapézio:** `A = [(B + b) × h] / 2` | Terreno com 2 lados paralelos | `[(20 + 10) × 8] / 2 = 120 m²` |
| **Pitágoras:** `a² = b² + c²` | Triângulo retângulo (macete **3-4-5** e seus múltiplos: 30-40-50, 330-440-550!) | `330² + 440² = 550²`! |
| **Semelhança / Tales:** proporção direta | Triângulos encaixados / retas paralelas (Taboão 2026 Q11!) | `lado maior / lado menor = outro maior / outro menor` |

---

### Molde 7: Conjuntos Numéricos & Princípio da Contagem (M-Tec 2022)

- **Dízima periódica** (`0,333...`) é **Racional (`ℚ`)**, porque vira fração (`1/3`)! **Irracionais (`𝕀`)** são `π` e raízes não exatas (`√2`).
- **Contagem com zero:** quantos números de 3 dígitos distintos com `{0,1,2,3,4,5}`? O **0 não pode ir na 1ª casa!** Logo: `5 × 5 × 4 = 100`!

<details class="recall-box">
<summary>🧠 Sua vez — 3 continhas rápidas de Taboão (clique para conferir)</summary>
<p><strong>1.</strong> Se <code>log_a(m) = 8</code> e <code>log_a(n) = 5</code>, quanto vale <code>log_a(m³ · n)</code>?</p>
<p><strong>Resposta:</strong> <code>3 · log_a(m) + log_a(n) = 3(8) + 5 = 24 + 5 =</code> <strong><code>29</code></strong>!</p>
<hr>
<p><strong>2.</strong> Numa turma de 50 alunos, 30 jogam futebol, 25 jogam basquete e 5 não jogam nenhum. Quantos jogam os dois?</p>
<p><strong>Resposta:</strong> <code>50 - 5 = 45</code> jogam algo. Soma: <code>30 + 25 = 55</code>. Excesso = <code>55 - 45 =</code> <strong><code>10</code> alunos</strong>!</p>
<hr>
<p><strong>3.</strong> Um triângulo retângulo tem hipotenusa <code>50 m</code> e um cateto <code>30 m</code>. Quanto mede o outro cateto?</p>
<p><strong>Resposta:</strong> Pelo triângulo mágico <strong>3-4-5</strong> multiplicado por 10 → o outro cateto mede <strong><code>40 m</code></strong>!</p>
</details>


---

## Dia 12 (02/12) — Base Comum III: Física, Química e História (Só os Alvos Certos de Taboão!)

> [!NOTE]
> Em Taboão da Serra caem cerca de **2 questões de Física, 2 de Química e 2 de História** (6 no total). Acertando **3 ou 4** com estes macetes diretos, você voa acima da nota de corte!

---

### 1. Física — Os 4 Clássicos que Taboão Repete!

#### A. Lei Geral dos Gases Ideais (🔁 REPETIU em 2021 Q18 e 2026 Q15!)
**Fórmula simples:** `(P₁ · V₁) / T₁ = (P₂ · V₂) / T₂` *(com temperatura **T sempre em Kelvin (K)**!)*
- **Macete do gráfico `p × V` (Taboão 2026 Q15):**
  - Se a pressão **fica igual** e o volume **dobra** (`V` → `2V`), então a temperatura `T` também **DOBRA** (`300 K → 600 K`)!
  - Se o volume fica igual e a pressão dobra (`p` → `2p`), a temperatura também **DOBRA**!
  - **Em 1 linha:** temperatura `T` é diretamente proporcional a **`p × V`**!

#### B. Lentes Convergentes & Óptica das Cores (Taboão 2026 Q16 e M-Tec 2022)
- **Por que o tomate parece vermelho?** Porque ele absorve todas as outras cores da luz branca e **REFLETE a cor vermelha**!
- **Lente Convergente (lupa):**
  - Objeto **entre o Foco (`F`) e o Centro Óptico (`O`)** (como na lupa de relojeiro — Taboão 2026 Q16!): forma imagem **Virtual, Direita e MAIOR**!
  - Objeto **além do foco**: imagem **Real e Invertida**.

#### C. Cinemática (MRUV) e Leis de Newton (Taboão 2025 Q13 e Q14)
- **Velocidade média:** `v = ΔS / Δt` (para converter `m/s` ↔ `km/h`, **multiplique ou divida por `3,6`**!).
- **MRUV (aceleração constante `a`):**
  - `v = v₀ + a · t`
  - `ΔS = v₀ · t + (a · t²) / 2` *(Se parte do repouso, `v₀ = 0` → `ΔS = (a · t²) / 2`!)*
- **2ª Lei de Newton:** **`F_R = m · a`** (Força Resultante = massa × aceleração).

---

### 2. Química — Os 4 Clássicos do 1º Ano em Taboão!

| Tema | Verdade Direta para Marcar na Prova | Caiu em |
| :--- | :--- | :--- |
| **Modelo Atômico de Bohr (Cores dos Fogos)** | Quando um elétron absorve energia, salta para uma camada mais externa; ao **retornar para uma camada mais interna**, ele **emite luz (fóton)** com cor característica de cada elemento! | **Taboão 2026 Q17!** |
| **Reações Exotérmicas vs. Endotérmicas** | **Exotérmica** (*EXO* = fora): **libera calor** (ex.: combustão/queima de gás, explosão). **Endotérmica** (*ENDO* = dentro): **absorve calor** (ex.: gelo derretendo, cozinhar). | **Taboão 2025 Q17!** |
| **Tabela Periódica (Famílias)** | Elementos na **mesma coluna (família/grupo)** têm o mesmo nº de elétrons na camada de valência → **propriedades químicas semelhantes**! Ex.: Sódio (`Na`) e Césio (`Cs`) são ambos da **Família 1A (Metais Alcalinos)**. | **Taboão 2025 Q18!** |
| **Condutividade Elétrica & Massa Molar** | **Metal:** conduz eletricidade no estado **SÓLIDO**. **Iônico (sal):** só conduz **LÍQUIDO/fundido** ou dissolvido em água. **Molecular:** **NÃO** conduz! Massa Molar: some `C=12, H=1, O=16`. | **M-Tec 2022!** |

---

### 3. História — Os 4 Marcos do 1º Ano (Sem Decoreba de Datas!)

| Período | Palavras-Chave que Entregam a Resposta | Caiu em |
| :--- | :--- | :--- |
| **Pré-História** | **Paleolítico:** nômade, caça/coleta, pedra lascada, domínio do fogo. **Neolítico:** sedentarismo, agricultura e domesticação de animais! | M-Tec 2022 |
| **Democracia Ateniense (Grécia Antiga)** | **Democracia DIRETA**, porém **excludente**: só homens livres, maiores e filhos de atenienses votavam (**mulheres, escravos e estrangeiros/metecos ficavam de fora!**). | **Taboão 2025 Q05!** |
| **Idade Média & Feudalismo** | Poder descentralizado nos feudos, economia agrária e **sociedade estamental dividida em 3 ordens**: **Clero** (os que rezam), **Nobreza** (os que guerreiam) e **Servos/Camponeses** (os que trabalham)! **Ciência Árabe:** médicos e sábios árabes preservaram e ampliaram obras clássicas greco-romanas! | **Taboão 2026 Q19 e Q20!** |
| **Renascimento Cultural (sécs. XIV–XVI)** | Transição para a Idade Moderna: **Antropocentrismo** (ser humano no centro, sem eliminar a religião, mas valorizando a **razão, ciência e cultura greco-romana clássica** — *Humanismo*!). | **Taboão 2025 Q06!** |

<details class="recall-box">
<summary>🧠 Sua vez — 4 perguntas rápidas de Física, Química e História</summary>
<p><strong>1. (Física)</strong> Um gás ideal a <code>300 K</code> tem seu volume dobrado mantendo a pressão constante. Qual a nova temperatura?</p>
<p><strong>Resposta:</strong> <strong><code>600 K</code></strong> (como <code>p</code> ficou igual e <code>V</code> dobrou, <code>T</code> também dobra)!</p>
<hr>
<p><strong>2. (Química)</strong> Segundo o modelo de Bohr, por que fogos de artifício emitem cores diferentes?</p>
<p><strong>Resposta:</strong> Porque os elétrons dos diferentes elementos químicos, ao <strong>retornarem para níveis de menor energia</strong>, emitem luz com frequências (cores) específicas!</p>
<hr>
<p><strong>3. (Química)</strong> A queima da gasolina no motor de um carro é uma reação <strong>Exotérmica</strong> ou <strong>Endotérmica</strong>?</p>
<p><strong>Resposta:</strong> <strong>Exotérmica</strong> (toda combustão/queima <strong>libera calor</strong>)!</p>
<hr>
<p><strong>4. (História)</strong> Quais eram as 3 ordens da sociedade feudal na Idade Média e quem NÃO podia votar na Democracia Ateniense?</p>
<p><strong>Resposta:</strong> As 3 ordens eram <strong>Clero, Nobreza e Servos/Camponeses</strong>. Em Atenas, <strong>mulheres, escravos e estrangeiros</strong> eram excluídos da cidadania!</p>
</details>


---

## Dia 13 (03/12 — Véspera da Prova Escrita!) — Simulado Final, Cola de Bolso & Checklist 04/12

> [!IMPORTANT]
> **Você chegou à véspera da 1ª Fase!**
> Hoje a regra é **clareza mental, ZERO desespero e dormir bem**. Você já estudou 100% do que realmente cai em Taboão da Serra!

---

### 1. Sua Rotina de Hoje (03/12 — Véspera)

1. **Faça 1 Simulado Final cronometrado:** escolha a **Prova Real Taboão 2025** (ou o **Simulado Inédito Premonição Taboão 2027**) na aba **📝 Provas & Simulados**.
2. **Revise só o que errou** lendo a explicação de cada questão errada.
3. **Passe o olho na Cola de Bolso (abaixo e na aba 📚 Apostila)** por 10 minutos — sem virar a madrugada!
4. **Durma pelo menos 8 horas!** Cérebro descansado ganha facilmente +4 a +6 questões de atenção em provas de 4 horas.

---

### 2. Os 15 Pontos de Ouro de Taboão da Serra (Revisão Turbo de 5 Minutos)

| # | Matéria | Ponto de Ouro para Marcar sem Medo |
| :-: | :--- | :--- |
| 1 | **Fundamentos** | `187 (decimal) = BB (hexadecimal)` (`187 ÷ 16 = 11`, resto `11`; `10=A, 11=B, 12=C, 13=D, 14=E, 15=F`) |
| 2 | **Fundamentos** | **CLI** = Interface por linha de comando (texto); **Multiusuário** = vários usuários com permissões próprias |
| 3 | **TPA (C#)** | **`do-while`** executa pelo menos **1 vez** garantida; **`while`** testa antes (pode rodar 0 vezes) |
| 4 | **TPA (C#)** | Vetores/Matrizes começam no índice **`0`**; `matriz[linha, coluna]`; `%` é **resto da divisão**! |
| 5 | **TPA (C#)** | **`breakpoint`** pausa o código para depurar; **`try/catch`** trata erros sem travar o programa |
| 6 | **Web I (HTML)** | `<p>` parágrafo, `<hr>` linha horizontal, `<h2>` subtítulo, `<br>` quebra de linha, `<body>` conteúdo visível |
| 7 | **Web I (HTML)** | `<img alt="...">` = texto alternativo + acessibilidade; `<script src="..."></script>` = JS externo; `method="POST"` = senhas |
| 8 | **Web I (CSS/JS)** | **Box Model:** `padding` (interno) vs `margin` (externo); **Flexbox:** `display: flex; justify-content: center; align-items: center;`; JS primitivos: `String, Number, Boolean` |
| 9 | **Web I (Net)** | **URI** identifica um recurso de forma única na Web; **DNS** traduz nome → IP; **HTTPS** é seguro |
| 10 | **BD I** | **Tabela** = conjunto; **Registro** = 1 linha individual; **PK** = única e `NOT NULL`; **FK** = liga tabelas (lado `N`!) |
| 11 | **BD I** | **Normalização** elimina redundâncias e anomalias (**1FN** = valores atômicos); **DDL** (`CREATE/ALTER/DROP`), **DML** (`INSERT/UPDATE/DELETE`), **DQL** (`SELECT`) |
| 12 | **APS & UX** | **RF** = O QUE faz; **RNF** = COMO se comporta; **Ágeis** = Scrum, XP, Kanban; **Casos de Uso** = atores × funções; **Usabilidade** = facilidade e eficiência de uso |
| 13 | **Port & Ing** | **Adequação linguística** depende do contexto; **Conativa** usa imperativo; **Present Perfect** = `have/has + particípio` |
| 14 | **Pesq/Arte/EdF** | **Quantitativa** (números) vs **Qualitativa** (opiniões); **Tema** (ideia) vs **Técnica** (como faz); **Isométrica** (parada) |
| 15 | **Exatas & Hist** | `log_a(mᵏ·nᵖ) = k·log_a(m) + p·log_a(n)`; Gases: `T` proporcional a `p·V`; Bohr: elétron retorna e emite luz; Idade Média: 3 ordens (Clero, Nobreza, Servos) |

---

### 3. Checklist para o Dia da Prova (Sexta, 04/12/2026)

- **Horário:** Chegue às **12h30** na Etec de Taboão da Serra (a prova começa às **13h00** e vai até **17h00** — portões fecham pontualmente!).
- **Levar na mochila:**
  - Documento oficial original com foto (RG / CIN);
  - Caneta esferográfica **azul ou preta** (leve 2 para garantir!), lápis e borracha;
  - Garrafa d'água transparente e um lanchinho leve (chocolate/barrinha).
- **Na hora da prova:** Faça a **Estratégia das 3 Passadas** (Técnico + Fáceis primeiro → Médias → Difíceis por eliminação → 15 min finais no gabarito). **Nenhuma questão em branco!**

<details class="recall-box">
<summary>🧠 Sua vez — 1 minuto de confiança antes da prova</summary>
<p><strong>Qual é a sua meta amanhã (04/12)?</strong></p>
<p><strong>Resposta:</strong> Passar com tranquilidade dos <strong>20/40 (50%)</strong> mirando <strong>25+/40</strong>! E assim que sair da prova, descansar no sábado de manhã e já começar o <strong>Sprint da 2ª Fase (Dias 14 a 16)</strong> para garantir a vaga no laboratório em <strong>08/12</strong>!</p>
</details>


---

## Dia 14 (05/12 — Sprint 2ª Fase!) — Laboratório Prático #1: Web I (HTML5 + CSS3 + Flexbox)

> [!IMPORTANT]
> **PARABÉNS por encarar a 1ª Fase! Agora começa o diferencial que decide a sua vaga!**
> Lembra do dado oficial de Taboão? Nos últimos 3 anos, **0 de 7 candidatos passaram na prova prática**. Por quê? Porque nunca abriram o VS Code nem escreveram 30 linhas de HTML/CSS/C# de verdade!
> Hoje (**05/12**), amanhã (**06/12**) e segunda (**07/12**), você vai **colocar a mão na massa no computador** e chegar no dia **08/12 (13h00–15h30)** pronto para tirar **B ou MB**!

---

### 1. O que Pode Cair no Laboratório de Web I (08/12)

Na prova prática de Programação Web I (VS Code + navegador), o professor costuma pedir:
- Criar uma pasta de projeto com `index.html` e `style.css`;
- Montar uma página limpa com **cabeçalho (`<header>`), conteúdo (`<main>`), rodapé (`<footer>`)**;
- Inserir título (`<h1>`, `<h2>`), parágrafo (`<p>`), linha (`<hr>`), imagem com `alt` (`<img src="..." alt="...">`) e/ou **formulário** (`<form method="POST">`);
- Estilizar no `style.css` usando **Box Model** (`padding`, `margin`, `border`), **cores/fontes**, **Flexbox** para alinhar cartões lado a lado ou centralizados, e **`@media`** para celular!

---

### 2. Passo a Passo no VS Code (Faça Junto Agora!)

1. Crie na Área de Trabalho uma pasta chamada **`treino_web_henrique`**.
2. Abra o **VS Code** → `Arquivo` → `Abrir Pasta` → escolha `treino_web_henrique`. *(Sem VS Code? Pode usar o Bloco de Notas salvando como `index.html`, ou online em **codepen.io**!)*
3. Crie dois arquivos na mesma pasta: **`index.html`** e **`style.css`**.
4. No `index.html`, digite **`!`** e aperte **`Tab`** — o VS Code gera o esqueleto HTML5 inteiro automaticamente!
5. Mude `<html lang="en">` para `<html lang="pt-BR">` e ligue o CSS dentro do `<head>`:
   `<link rel="stylesheet" href="style.css">`

---

### 3. Projeto Completo para Digitar (NÃO Copie e Cole — Digite Para Ganhar Memória Muscular!)

> [!TIP]
> **Vá na aba `🛠️ 2ª Fase (08/12)`** → clique em **Desafio Prático #1 (Web I)** para ver o código completo colorido com botão de copiar e o **checklist interativo** para marcar cada item!

**As 5 peças que você precisa saber digitar de cabeça na hora H:**
```html
<!-- 1. Ligar CSS no <head> -->
<link rel="stylesheet" href="style.css">

<!-- 2. Imagem com acessibilidade -->
<img src="logo.png" alt="Logo da Etec Taboão">

<!-- 3. Formulário seguro -->
<form action="#" method="POST">
  <label for="nome">Nome:</label>
  <input id="nome" type="text" required>
  <button type="submit">Enviar</button>
</form>
```

```css
/* 4. Centralizar tudo com Flexbox */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
}

/* 5. Adaptar para celular */
@media (max-width: 600px) {
  .container { flex-direction: column; }
}
```

---

### 4. Como Testar e Corrigir Erros na Prova Prática (F12!)

- Dê **duplo clique** em `index.html` para abrir no Chrome ou Edge.
- Salvou mudança no código? Aperte **`Ctrl + S`** no VS Code e **`F5`** no navegador!
- Algo não ficou do jeito que você queria? Aperte **`F12`** no navegador (DevTools) → clique na aba **Elements / Estilos** para ver o Box Model (azul = conteúdo, verde = `padding`, laranja = `margin`)!

<details class="recall-box">
<summary>🧠 Sua vez — checklist rápido de laboratório Web</summary>
<p><strong>O CSS não aplicou na página quando abri o <code>index.html</code>! Quais as 3 primeiras coisas para checar?</strong></p>
<p><strong>Resposta:</strong> 1) Esqueci de salvar (<code>Ctrl + S</code>) o arquivo <code>style.css</code> ou <code>index.html</code>; 2) Esqueci a tag <code>&lt;link rel="stylesheet" href="style.css"&gt;</code> dentro do <code>&lt;head&gt;</code>; 3) O nome do arquivo ou o nome da classe (<code>.cartao</code>) está escrito diferente no HTML e no CSS!</p>
</details>


---

## Dia 15 (06/12 — Sprint 2ª Fase!) — Laboratório Prático #2: C# Console (3 Programas Reais + Debug)

> [!IMPORTANT]
> **Este é o dia que tira você do zero absoluto e coloca na frente de 100% dos concorrentes!**
> Em Taboão da Serra, TPA do 1º ano é em **C# (Visual Studio)**. Se você souber abrir um **Aplicativo de Console C#**, ler 2 números, fazer um `if/else`, um `for` e um vetor sem travar, você já garante no mínimo **R ou B** na parte de programação!

---

### 1. Como Criar um Projeto C# no Laboratório (Visual Studio) ou em Casa

- **No Laboratório da Etec (Visual Studio):**
  `Criar um projeto` → filtre por **C#** → escolha **Aplicativo de Console (Console App)** → dê um nome (`Exercicio1`) → `Criar`. Aperte **`F5`** para rodar!
- **Em casa hoje (sem instalar nada!):**
  Abra **[dotnetfiddle.net](https://dotnetfiddle.net)** no navegador, escolha linguagem **C#**, digite seu código e clique em **Run**!

---

### 2. O Kit de Sobrevivência em C# (6 Comandos que Resolvem 90% das Provas!)

| O que você quer fazer | Comando exato em C# |
| :--- | :--- |
| Mostrar texto na tela | `Console.WriteLine("Olá!");` |
| Ler texto do teclado | `string nome = Console.ReadLine();` |
| Ler número inteiro | `int n = int.Parse(Console.ReadLine());` |
| Ler número decimal | `double nota = double.Parse(Console.ReadLine());` |
| Decisão (`se / senão`) | `if (nota >= 6.0) { ... } else { ... }` |
| Repetição contada (`para`) | `for (int i = 0; i < 4; i++) { ... }` |

---

### 3. Os 3 Mini-Desafios Obrigatórios de Hoje (Digite e Rode Todos!)

Vá na aba **`🛠️ 2ª Fase (08/12)` → Desafio Prático #2 (C# Console)** para ver os códigos completos e testar passo a passo:
1. **Programa 1 — Calculadora de Média com Aprovação (`if/else` + `try/catch`):** lê duas notas, calcula a média `(n1 + n2) / 2`, diz se foi `APROVADO` (`>= 6`) ou `RECUPERAÇÃO` e não trava se o usuário digitar letra!
2. **Programa 2 — Tabuada ou Pares com `for` e `%`:** lê um número `n` e mostra os números pares de `0` até `n` (usando `if (i % 2 == 0)`).
3. **Programa 3 — Vetor de 4 Notas (`double[]` + `for`):** guarda 4 notas em um vetor, soma todas dentro de um `for` e mostra a média final com `ToString("F1")`!

---

### 4. Kit de Emergência: Deu Sublinhado Vermelho? Não Entre em Pânico!

Os **5 erros de compilação** que mais acontecem no laboratório (e como corrigir em 10 segundos):
1. **`CS1002: ; expected`** → Faltou um **ponto e vírgula `;`** no final da linha acima!
2. **`CS1513: } expected`** → Faltou fechar uma **chave `}`** (conte quantas `{` abriu e quantas `}` fechou).
3. **Maiúscula/minúscula errada** → Em C#, `console.writeline` dá erro! O certo é **`Console.WriteLine`** (`C`, `W` e `L` maiúsculos!).
4. **Vírgula vs. Ponto no código** → No código fonte use **ponto** (`double x = 7.5;`), mas ao digitar no console em Windows em português, pode testar com vírgula (`7,5`) se `double.Parse` reclamar!
5. **Acabou o tempo e faltou 1 detalhe?** **Escreva comentários `//`** explicando a sua lógica! O professor avalia seu **raciocínio lógico** mesmo se um detalhe de sintaxe falhar!

<details class="recall-box">
<summary>🧠 Sua vez — ache os 2 erros propositais neste código C#!</summary>
<pre><code>int idade = int.Parse(Console.ReadLine())
if (idade = 18)
{
    Console.WriteLine("Tem 18 anos!");
}</code></pre>
<p><strong>Resposta:</strong><br>
1) Faltou o ponto e vírgula <strong><code>;</code></strong> no final da linha 1 (<code>Console.ReadLine());</code>)!<br>
2) Dentro do <code>if</code> está <code>idade = 18</code> (atribuição) em vez de <strong><code>idade == 18</code></strong> (comparação de igualdade)!</p>
</details>


---

## Dia 16 (07/12 — Véspera da 2ª Fase!) — Lab BD I (DER + SQL) + Simulação da Entrevista Individual

> [!IMPORTANT]
> **Hoje sai o resultado da 1ª Fase (07/12) e amanhã (08/12, 13h00–15h30) é o grande dia no Laboratório!**
> Hoje você fecha a preparação prática de **Banco de Dados I** e ensaia em voz alta a **Entrevista Individual** com os professores!

---

### 1. Laboratório Prático #3: Como Montar Qualquer DER + SQL em 15 Minutos

Se o avaliador entregar um mini-cenário (ex.: *Biblioteca*, *Clínica Médica*, *Loja* ou *Sistema Escolar*), siga sempre esta **Receita em 5 Passos**:
1. **Circule os substantivos principais** → viram **Entidades (Tabelas)** (ex.: `ALUNO`, `LIVRO`).
2. **Dê uma Chave Primária (PK)** para cada tabela (`id_aluno`, `id_livro`) — nunca repete, nunca é nula!
3. **Liste os campos simples** de cada tabela (ex.: `nome`, `ra`, `titulo`, `autor`), respeitando a **1FN** (nada de dois dados na mesma coluna!).
4. **Defina a cardinalidade** entre elas:
   - Se for **`1:N`** (1 Turma tem N Alunos) → coloque a **FK (`id_turma`)** dentro da tabela do lado **`N`** (`ALUNO`)!
   - Se for **`N:N`** (N Alunos pegam N Livros) → crie uma **3ª tabela associativa** (`EMPRESTIMO`) com as duas FKs (`id_aluno`, `id_livro`) + `data_retirada`!
5. **Escreva os 3 comandos SQL essenciais** (treine agora na aba **`🛠️ 2ª Fase (08/12)` → Desafio Prático #3**):
   - `CREATE TABLE ...` (DDL)
   - `INSERT INTO ... VALUES (...)` (DML)
   - `SELECT ... FROM ... WHERE ...` (DQL)

---

### 2. Como Brilhar na Entrevista Individual (08/12)

Na entrevista, 2 ou 3 professores da banca vão conversar com você por cerca de **5 a 10 minutos** sobre:
1. **Sua motivação:** Por que você quer vir para o 2º ano M-Tec-PI em DS na Etec de Taboão?
2. **Sua dedicação e adaptação:** Você sabe que é período integral e que terá atividades de adaptação do 1º ano? Como estudou até aqui?
3. **2 ou 3 perguntas técnicas sobre o que você acabou de fazer no computador!** (Ex.: *"Para que serve essa PK/FK?"*, *"O que faz esse `justify-content: center`?"*, *"Qual a diferença de `while` e `do-while`?"*).

> [!TIP]
> **Regra de Ouro na Entrevista:**
> - **Olhe nos olhos**, fale com calma e **nunca invente resposta se não souber algo**!
> - Se der um branco numa pergunta técnica, diga com maturidade: *"Na prática agora eu não lembro o comando exato de cabeça, mas eu sei o conceito e sei consultar a documentação para resolver!"* — professores adoram honestidade e vontade de aprender!
> - **Treine em voz alta agora mesmo:** abra a aba **`🛠️ 2ª Fase (08/12)` → 🎤 Simulador de Entrevista** e responda em voz alta às **8 perguntas reais** antes de conferir as respostas-modelo!

---

### 3. Checklist Final para Terça-feira (08/12/2026)

- **Horário:** Chegue às **12h30** na Etec de Taboão da Serra (prova prática + entrevista das **13h00 às 15h30**).
- **Documentos:** RG/CIN original com foto + caneta azul/preta e lápis (para rascunhar DER e teste de mesa no papel antes de digitar!).
- **Mentalidade de Campeão:** Lembre que nos últimos 3 anos ninguém passou na prática porque foram despreparados. Você treinou **HTML5+CSS3+Flexbox**, **C# Console com `if/for/vetor/try-catch`**, **DER+PK/FK+SQL** e a **Entrevista**. **Basta entregar com calma, organizado e comentado — a vaga é sua!**

<details class="recall-box">
<summary>🧠 Sua vez — simulação relâmpago da pergunta final da entrevista</summary>
<p><strong>Banca:</strong> <em>"Henrique, por que devemos escolher você para esta vaga no 2º ano de Desenvolvimento de Sistemas?"</em></p>
<p><strong>Modelo de resposta segura:</strong> <em>"Porque eu realmente quero construir minha formação em tecnologia aqui na Etec. Mesmo vindo do ensino médio regular, eu estudei o Plano de Curso de vocês do 1º ano, treinei HTML/CSS, C# e Banco de Dados na prática, e estou 100% comprometido com o período integral e com as atividades de adaptação."</em></p>
</details>


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

