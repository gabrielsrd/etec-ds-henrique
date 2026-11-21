## Dia 2 (22/11) — Programação I: algoritmo, variáveis, operadores e if/else em C#

Hoje você vai escrever seus primeiros programas. A matéria que ensina isso na Etec se chama **Técnicas de Programação e Algoritmos (TPA)** e é a que tem mais aulas no 1º ano (120). Ela aparece na prova escrita **todo ano** (de 3 a 6 questões) e é a base do **laboratório do dia 08/12**, onde você vai ter que programar de verdade.

> [!IMPORTANT]
> **Como estudar esta aula:** leia com o computador ou o celular do lado. Sempre que aparecer um código, **digite** (não copie e cole) no site **dotnetfiddle.net** — no fim da aula tem o passo a passo. Programação se aprende com os dedos, não só com os olhos.

### 1. O que é um algoritmo

Um **algoritmo** é uma **sequência finita de passos bem definidos para resolver um problema**. Você usa algoritmos o tempo todo sem chamar assim:

- **Instalar um jogo:** baixar o instalador → abrir → aceitar os termos → escolher a pasta → esperar → abrir o jogo.
- **Receita de miojo:** ferver 500 ml de água → colocar o macarrão → esperar 3 minutos → desligar o fogo → misturar o tempero.

Repare em três características que a prova adora cobrar:

1. **Finito** — tem começo, meio e **fim**. Uma receita que nunca termina não é algoritmo.
2. **Bem definido / sem ambiguidade** — cada passo só pode ser entendido de um jeito. "Coloque um pouco de sal" é ambíguo para um computador; "coloque 2 g de sal" não é.
3. **Ordem importa** — colocar o macarrão antes de ferver a água dá outro resultado.

**Algoritmo × programa × linguagem**

| Conceito | O que é | Exemplo |
|---|---|---|
| **Algoritmo** | a **ideia**, a sequência de passos | "ler duas notas, somar, dividir por 2, mostrar" |
| **Linguagem de programação** | o **idioma** usado para escrever para o computador | C#, Java, Python, JavaScript |
| **Programa** | o algoritmo **escrito numa linguagem**, pronto para rodar | o arquivo `Program.cs` com o código |

O mesmo algoritmo pode virar programa em qualquer linguagem. Por isso a prova diz que algoritmo **não é** uma linguagem de programação.

> [!WARNING]
> **🔁 Já caiu:** "O que é um algoritmo?" caiu em **2021 (questões 36 e 38)** e em **dez/2025 na prova de Informática para Internet (questão 11)**. A resposta é sempre a definição: *sequência finita de instruções bem definidas e não ambíguas*. Em 2021, a pegadinha era a alternativa "**logaritmo**" (que é uma conta de matemática, não tem nada a ver).

<details class="recall-box">
<summary>🧠 Sua vez — "Mexa bem até ficar bom" é um bom passo de algoritmo?</summary>

Não. É **ambíguo**: quanto é "bem"? Quando está "bom"? Um computador não consegue decidir isso. Um passo bem definido seria "mexa por 2 minutos" ou "mexa até a temperatura chegar a 80 °C".

</details>

### 2. Fluxograma: o algoritmo em desenho

Antes de escrever código, dá para desenhar o algoritmo com formas geométricas. Isso se chama **fluxograma**. Cada forma tem um significado:

| Forma | Nome | Para que serve |
|---|---|---|
| ⬭ oval (retângulo de cantos redondos) | **Terminal** | Início e fim |
| ▱ paralelogramo | **Entrada/Saída** | Ler um dado do teclado ou mostrar na tela |
| ▭ retângulo | **Processamento** | Uma conta ou atribuição (`media = (n1 + n2) / 2`) |
| ◇ losango | **Decisão** | Uma pergunta com resposta **Sim** ou **Não** |
| → seta | **Fluxo** | A ordem dos passos |

Exemplo: o algoritmo que diz se o aluno passou (média 6 ou mais):

```text
        ( Início )
            │
            ▼
   ╱ Ler nota1, nota2 ╱
            │
            ▼
  ┌──────────────────────┐
  │ media = (nota1 + nota2) / 2 │
  └──────────────────────┘
            │
            ▼
       ◇ media >= 6 ? ◇
       Sim │       │ Não
           ▼       ▼
  ╱ "Aprovado" ╱  ╱ "Reprovado" ╱
           │       │
           └───┬───┘
               ▼
           ( Fim )
```

O **losango** é o coração da aula de hoje: é ali que o programa **toma uma decisão**. Em C#, ele vira o comando `if`.

> [!WARNING]
> **🔁 Já caiu:** em **dez/2025 (questão 34)**, a prova descreveu uma loja que cobra 5% de imposto se o produto custar menos de R$ 100 e 12% caso contrário, e pediu a estrutura certa do fluxograma. A resposta: *ler valor → **se** valor < 100 então imposto = valor × 0,05; **caso contrário** imposto = valor × 0,12 → exibir*. Você vai escrever esse programa daqui a pouco.

### 3. Seu primeiro programa em C#

Todo programa de console em C# tem um "esqueleto". Não precisa decorar tudo agora — entenda a ideia:

```csharp
using System;                       // 1. "Importa" ferramentas prontas, como o Console

class Program                       // 2. Todo código C# fica dentro de uma classe
{
    static void Main()              // 3. Main = a porta de entrada: o programa começa aqui
    {
        Console.WriteLine("Olá, Etec!");   // 4. Mostra um texto na tela e pula de linha
    }                               // 5. Fecha o Main
}                                   // 6. Fecha a classe
```

Saída na tela:

```text
Olá, Etec!
```

Regras de escrita (sintaxe) que **mais causam erro**:

- **Toda instrução termina com `;`** (ponto e vírgula). Esqueceu? O programa **não compila**.
- **Chaves `{ }` sempre aos pares**: cada `{` aberta precisa de um `}` fechando.
- **C# diferencia maiúsculas de minúsculas**: `Console` funciona; `console` dá erro. `idade` e `Idade` seriam duas variáveis diferentes.
- **Texto vai entre aspas duplas**: `"Olá"`. Sem aspas, o C# acha que é nome de variável.
- **Comentários** começam com `//` e são ignorados pelo computador — servem para explicar o código para pessoas.

Duas formas de mostrar coisas na tela:

```csharp
Console.WriteLine("Oi");   // escreve e PULA de linha
Console.Write("Oi");       // escreve e CONTINUA na mesma linha
```

```csharp
Console.Write("A");
Console.Write("B");
Console.WriteLine("C");
Console.WriteLine("D");
```

Saída:

```text
ABC
D
```

<details class="recall-box">
<summary>🧠 Sua vez — o que aparece na tela com Console.Write("1"); Console.WriteLine("2"); Console.Write("3");</summary>

```text
12
3
```

O `Write("1")` não pula linha, então o `2` fica grudado. O `WriteLine("2")` pula a linha depois do 2, então o `3` vai para a linha de baixo.

</details>

### 4. Variáveis: caixinhas com etiqueta

Imagine a memória do computador como um armário cheio de **caixinhas**. Uma **variável** é uma caixinha com:

- um **nome** (a etiqueta): `idade`
- um **tipo** (o que cabe nela): número inteiro
- um **valor** (o que está dentro agora): `16`

Em C#, você cria (**declara**) a variável dizendo o tipo e o nome, e pode já colocar um valor (**atribuir**):

```csharp
int idade = 16;          // cria a caixinha "idade", do tipo inteiro, com 16 dentro
idade = 17;              // troca o conteúdo: agora vale 17 (o 16 foi apagado)
idade = idade + 1;       // pega o valor atual (17), soma 1 e guarda de volta: 18
```

> [!CAUTION]
> **O `=` em programação NÃO é "igual" da matemática.** Ele significa **"recebe"**: o valor da direita é calculado e **guardado** na variável da esquerda. Por isso `idade = idade + 1` faz sentido: "idade **recebe** idade mais 1". Para **comparar** se duas coisas são iguais, usa-se **`==`** (dois iguais).

**Regras para nomes de variáveis:** começa com letra (ou `_`), sem espaço, sem acento (pode, mas evite), sem ser palavra reservada (`int`, `if`, `class`…). Bons nomes: `nota1`, `mediaFinal`, `precoProduto`. Ruins: `1nota` (começa com número), `media final` (tem espaço).

### 5. Tipos de dados

O tipo diz **o que cabe** na caixinha e **quanto de memória** ela ocupa.

| Tipo C# | Guarda | Exemplo | Cuidado |
|---|---|---|---|
| `int` | número **inteiro** | `int idade = 16;` | não guarda vírgula |
| `double` | número **real** (com casas decimais) | `double nota = 7.5;` | no código, o decimal usa **ponto**: `7.5` |
| `string` | **texto** | `string nome = "Henrique";` | entre aspas **duplas** |
| `char` | **um** caractere | `char turma = 'B';` | entre aspas **simples** |
| `bool` | **lógico**: só `true` ou `false` | `bool aprovado = true;` | não tem aspas |

Esses tipos simples se chamam **tipos primitivos**. Em JavaScript (Web) os nomes mudam (`number`, `string`, `boolean`), mas a ideia é a mesma — você vê isso no Dia 5.

**A pegadinha da divisão inteira** (cai muito em teste de mesa):

```csharp
int a = 7;
int b = 2;
Console.WriteLine(a / b);     // 3   ← inteiro dividido por inteiro dá INTEIRO (corta o ,5)
Console.WriteLine(7.0 / 2);   // 3.5 ← se um dos lados é double, o resultado é double
```

<details class="recall-box">
<summary>🧠 Sua vez — qual tipo você usaria para: nome de um jogo, número de vidas, preço de um skin, se o jogador está online?</summary>

- nome do jogo → `string` (texto)
- número de vidas → `int` (inteiro)
- preço do skin → `double` (tem centavos)
- está online → `bool` (`true` ou `false`)

</details>

### 6. Lendo dados do teclado

Para o programa conversar com o usuário, usamos `Console.ReadLine()`, que **espera a pessoa digitar e apertar Enter**. Só que ele sempre devolve um **texto** (`string`). Se você quer fazer contas, precisa **converter** o texto em número:

```csharp in=16
Console.Write("Digite sua idade: ");
string texto = Console.ReadLine();     // a pessoa digitou "16" → é TEXTO
int idade = int.Parse(texto);          // int.Parse transforma "16" no número 16
Console.WriteLine("Ano que vem você terá " + (idade + 1) + " anos.");
```

O jeito curto, que aparece nas provas e no laboratório:

```csharp in=16|7.5
int idade = int.Parse(Console.ReadLine());
double nota = double.Parse(Console.ReadLine());
```

Leia de **dentro para fora**: primeiro o `Console.ReadLine()` pega o texto; depois o `int.Parse(...)` converte para número; por fim, o número é guardado em `idade`.

> [!CAUTION]
> **A pegadinha do `+`:** com **números**, `+` soma; com **textos**, `+` **junta** (concatena). `"5" + "3"` dá `"53"`, não `8`! É por isso que precisa do `int.Parse` antes de somar o que foi digitado.

> [!NOTE]
> **Vírgula ou ponto?** No **código**, número decimal sempre usa **ponto** (`7.5`). Mas, quando o programa roda num Windows em português e você **digita** um número, o `double.Parse` espera **vírgula** (`7,5`). No dotnetfiddle.net (que é configurado em inglês), digite com ponto. Se der erro ao digitar um decimal, troque o ponto pela vírgula.

**Mostrando textos com variáveis** — duas formas:

```csharp
string nome = "Henrique";
int idade = 16;
Console.WriteLine("Olá, " + nome + "! Você tem " + idade + " anos.");   // concatenação
Console.WriteLine($"Olá, {nome}! Você tem {idade} anos.");              // interpolação (o $ antes das aspas)
```

As duas mostram: `Olá, Henrique! Você tem 16 anos.`

### 7. Operadores aritméticos (as contas)

| Operador | Faz | Exemplo | Resultado |
|---|---|---|---|
| `+` | soma | `7 + 2` | 9 |
| `-` | subtração | `7 - 2` | 5 |
| `*` | **multiplicação** (não é `x`!) | `7 * 2` | 14 |
| `/` | divisão | `7 / 2` | **3** (inteiros) |
| `%` | **resto** da divisão | `7 % 2` | **1** |

O **`%` (módulo)** é o operador que mais aparece em prova. **Não tem nada a ver com porcentagem**: ele dá o **resto** da divisão inteira. Lembra da conta armada do fundamental?

```text
  7 │ 2
 -6   3   ← quociente: 7 / 2 = 3
  1       ← resto:     7 % 2 = 1
```

Usos clássicos do `%`:

- **Par ou ímpar:** `numero % 2 == 0` → par (resto zero ao dividir por 2). Se der 1, é ímpar.
- **Múltiplo de 5:** `numero % 5 == 0`.
- **Último dígito:** `numero % 10` (o resto ao dividir por 10). Ex.: `187 % 10` = 7.

**Ordem das contas (precedência):** igual à matemática — primeiro `*`, `/` e `%`, depois `+` e `-`. Parênteses mudam a ordem.

```csharp
Console.WriteLine(2 + 3 * 4);     // 14 (primeiro 3*4 = 12, depois 2 + 12)
Console.WriteLine((2 + 3) * 4);   // 20
Console.WriteLine(10 - 6 / 2);    // 7  (primeiro 6/2 = 3)
Console.WriteLine(17 % 5);        // 2  (17 = 3*5 + 2)
```

**Atalhos que aparecem em código:**

```csharp nocheck
x = x + 1;   // é o mesmo que:  x++;    (soma 1)
x = x - 1;   // é o mesmo que:  x--;    (tira 1)
x = x + 3;   // é o mesmo que:  x += 3;
```

<details class="recall-box">
<summary>🧠 Sua vez — calcule: 23 % 4, 20 % 4, 9 / 2 (inteiros) e 5 + 10 % 3</summary>

- `23 % 4` = **3** (4 × 5 = 20, sobra 3)
- `20 % 4` = **0** (20 é múltiplo de 4)
- `9 / 2` = **4** (divisão inteira corta o 0,5)
- `5 + 10 % 3` = 5 + **1** = **6** (o `%` vem antes do `+`; 10 % 3 = 1)

</details>

### 8. Operadores relacionais (as comparações)

Comparam dois valores e respondem **verdadeiro (`true`)** ou **falso (`false`)**:

| Operador | Significa | Exemplo com `nota = 7` | Resultado |
|---|---|---|---|
| `==` | igual a | `nota == 7` | true |
| `!=` | diferente de | `nota != 7` | false |
| `>` | maior que | `nota > 7` | false |
| `<` | menor que | `nota < 7` | false |
| `>=` | maior **ou igual** | `nota >= 7` | **true** |
| `<=` | menor **ou igual** | `nota <= 7` | **true** |

A pegadinha de prova: **`>=` inclui o próprio valor**. `7 >= 7` é verdadeiro; `7 > 7` é falso.

### 9. Operadores lógicos e a tabela verdade

Às vezes a decisão depende de **duas condições ao mesmo tempo**: "passa se a nota for 7 ou mais **E** a frequência for 75% ou mais". Para juntar condições, usamos os **operadores lógicos**:

| Em português | Em C# | Regra de ouro |
|---|---|---|
| **E** (AND) | `&&` | É **exigente**: só dá verdadeiro se **as duas** forem verdadeiras |
| **OU** (OR) | `\|\|` | É **tranquilo**: dá verdadeiro se **pelo menos uma** for verdadeira |
| **NÃO** (NOT) | `!` | **Inverte**: verdadeiro vira falso, falso vira verdadeiro |

A **tabela verdade** mostra todas as combinações possíveis (V = verdadeiro, F = falso):

| A | B | A **E** B (`A && B`) | A **OU** B (`A \|\| B`) | **NÃO** A (`!A`) |
|---|---|---|---|---|
| V | V | **V** | V | F |
| V | F | F | **V** | F |
| F | V | F | **V** | V |
| F | F | F | **F** | V |

Como lembrar sem decorar a tabela inteira:

- **E** só tem **um** V (quando tudo é V). Basta **um F** para o resultado ser F.
- **OU** só tem **um** F (quando tudo é F). Basta **um V** para o resultado ser V.

Pense no Discord: para entrar num canal privado você precisa **estar no servidor E ter o cargo** (`&&`). Para receber notificação basta **ser mencionado OU ter ativado alertas do canal** (`||`).

```csharp
double nota = 8.0;
int frequencia = 70;
bool passou = nota >= 7 && frequencia >= 75;   // true && false → false
Console.WriteLine(passou);                      // False
```

> [!WARNING]
> **🔁 Já caiu:**
> - **Informática para Internet, dez/2024 (questão 38):** "Segundo a tabela verdade" — a certa era **F ou V = V**. As erradas tinham "V e F = V" (no **E**, um F já derruba tudo).
> - **Informática para Internet, dez/2025 (questão 13):** `SE (nota >= 7) E (frequencia >= 75)` — qual entrada dá "Aprovado"? Só a que tem **as duas** condições verdadeiras (nota 8, frequência 85). Nota 7 com frequência 74 **reprova**.
> - O operador `&&` como "E" do C# aparece também nas provas de DS. Lembre: `&&` = E, `||` = OU, `!` = NÃO, e **`%` não é operador lógico** (é o resto).

<details class="recall-box">
<summary>🧠 Sua vez — com idade = 15 e temAutorizacao = true, quanto vale (idade >= 16) || temAutorizacao? E (idade >= 16) && temAutorizacao?</summary>

- `idade >= 16` → 15 ≥ 16 → **false**
- `false || true` → **true** (no OU, basta um verdadeiro)
- `false && true` → **false** (no E, basta um falso)

</details>

### 10. Tomando decisões: if, else e else if

O losango do fluxograma vira **`if`** ("se") em C#:

```csharp nocheck
if (condição)
{
    // roda SÓ se a condição for verdadeira
}
else
{
    // roda SÓ se a condição for falsa
}
```

O programa **escolhe um dos caminhos** — nunca os dois. O `else` é opcional.

**Exemplo 1 — aprovado ou reprovado:**

```csharp in=7|8
using System;

class Program
{
    static void Main()
    {
        Console.Write("Nota 1: ");
        double n1 = double.Parse(Console.ReadLine());
        Console.Write("Nota 2: ");
        double n2 = double.Parse(Console.ReadLine());

        double media = (n1 + n2) / 2;      // parênteses: soma ANTES de dividir

        if (media >= 6)
        {
            Console.WriteLine("Aprovado com média " + media);
        }
        else
        {
            Console.WriteLine("Reprovado com média " + media);
        }
    }
}
```

Por que os parênteses em `(n1 + n2) / 2`? Sem eles, o C# faria `n1 + (n2 / 2)` — a divisão vem antes da soma. Esse é um dos erros mais comuns em média.

**Exemplo 2 — mais de dois caminhos com `else if`** (o imposto da prova de dez/2025):

```csharp in=250
Console.Write("Valor do produto: ");
double valor = double.Parse(Console.ReadLine());
double imposto;

if (valor < 100)
{
    imposto = valor * 0.05;        // 5% = 0.05
}
else
{
    imposto = valor * 0.12;        // 12% = 0.12
}
Console.WriteLine("Imposto: R$ " + imposto);
```

Se a loja tivesse três faixas, usaríamos `else if`:

```csharp nocheck
if (valor < 100)
    imposto = valor * 0.05;
else if (valor <= 500)             // só testa se a primeira deu falso
    imposto = valor * 0.10;
else                                // nenhuma das anteriores
    imposto = valor * 0.15;
```

O C# testa **de cima para baixo** e para no **primeiro** verdadeiro. Para `valor = 300`: `300 < 100`? não → `300 <= 500`? **sim** → 10%. O último `else` nem é olhado.

(Quando o bloco tem **uma linha só**, as chaves `{ }` podem ser omitidas, como acima. Na dúvida, use sempre as chaves.)

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2025 (questão 14):**
>
> ```csharp
> int idade = 17;
> string status;
> if (idade >= 18) { status = "Adulto"; } else { status = "Menor de idade"; }
> Console.WriteLine(status);
> ```
>
> Saída: **Menor de idade** (17 ≥ 18 é falso, vai para o `else`). A pegadinha era a alternativa "status": o `WriteLine` mostra o **valor** da variável, não o nome dela.

### 11. Teste de mesa: rodando o programa no papel

Na prova não tem computador. Para saber o que um código mostra, você faz o **teste de mesa**: uma tabela com uma coluna para cada variável, e você executa **linha por linha**, anotando cada mudança.

**Exemplo A — caiu em Informática para Internet, dez/2024 (questão 36):**

```text
var x, y, r : inteiro
início
   x = 8
   y = x - 1
   r = x * y
fim
```

| Linha | x | y | r |
|---|---|---|---|
| `x = 8` | 8 | | |
| `y = x - 1` | 8 | 7 | |
| `r = x * y` | 8 | 7 | **56** |

Resposta: `r` vale **56**. Quem soma em vez de multiplicar marca 15 (pegadinha).

**Exemplo B — com decisão e resto:**

```csharp
int n = 14;
int r = n % 4;
if (r == 0 && n > 10)
    Console.WriteLine("A");
else if (r == 2 || n < 5)
    Console.WriteLine("B");
else
    Console.WriteLine("C");
```

| Passo | n | r | Teste | Resultado |
|---|---|---|---|---|
| 1 | 14 | | | |
| 2 | 14 | 2 (14 = 3·4 + 2) | | |
| 3 | | | `r == 0 && n > 10` → `false && true` | **false** |
| 4 | | | `r == 2 \|\| n < 5` → `true \|\| false` | **true** → mostra **B** |

Saída: **B**.

> [!TIP]
> **Método de prova para código:** (1) desenhe a tabela com as variáveis; (2) execute uma linha por vez, **sem pular**; (3) quando aparecer uma condição, escreva V ou F antes de decidir o caminho; (4) só olhe as alternativas no fim. Quem tenta "adivinhar de cabeça" cai nas pegadinhas.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Esquecer o `;`** no fim da linha → o programa não compila (o Visual Studio sublinha de vermelho). Mas **não** vai `;` depois do `if (...)` — `if (x > 5);` faz o if não controlar nada.
> - **Usar `=` para comparar:** `if (nota = 7)` está errado; o certo é `if (nota == 7)`.
> - **Esquecer de converter** o `Console.ReadLine()`: `int idade = Console.ReadLine();` dá erro (texto não cabe em int).
> - **Média sem parênteses:** `n1 + n2 / 2` não é a média.
> - **Achar que `%` é porcentagem:** é o **resto** da divisão.
> - **Escrever `console`, `writeline`, `If`** com letra errada — C# diferencia maiúsculas.
> - **Esquecer as aspas** em textos: `Console.WriteLine(Olá);` dá erro; o certo é `Console.WriteLine("Olá");`.

### Exercícios resolvidos

Tente cada um **no papel** antes de abrir a resposta.

<details class="recall-box">
<summary>🧠 Exercício 1 — Qual alternativa NÃO é característica de um algoritmo? (A) ter fim (B) passos sem ambiguidade (C) ordem definida (D) depender da opinião de quem executa (E) resolver um problema</summary>

**D.** Se cada pessoa executa de um jeito, os passos são ambíguos. Algoritmo é **finito, ordenado, sem ambiguidade** e resolve um problema.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — No fluxograma, qual símbolo representa "Ler o salário do funcionário"? (A) oval (B) losango (C) paralelogramo (D) retângulo (E) círculo</summary>

**C — paralelogramo** (entrada/saída de dados). Oval = início/fim; losango = decisão; retângulo = cálculo.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — O que o código mostra? int a = 10; int b = 3; Console.WriteLine(a / b + a % b);</summary>

`a / b` = 10 / 3 = **3** (inteiros). `a % b` = resto de 10 ÷ 3 = **1**. 3 + 1 = **4**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Com x = 4 e y = 9, avalie: (x > 5) && (y > 5); (x > 5) || (y > 5); !(x > 5)</summary>

- `x > 5` → false; `y > 5` → true.
- `false && true` → **false**
- `false || true` → **true**
- `!false` → **true**

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — O que aparece? int n = 7; if (n % 2 == 0) Console.WriteLine("par"); else Console.WriteLine("ímpar");</summary>

7 % 2 = 1, e 1 == 0 é **falso** → vai para o else → mostra **ímpar**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Ache os 3 erros: int idade = Console.ReadLine() / if (idade = 18) / Console.WriteLine("Maior de idade")</summary>

1. `Console.ReadLine()` devolve texto: precisa de `int.Parse(Console.ReadLine())`.
2. `idade = 18` atribui; para comparar é `idade == 18` (e para "maior de idade" o certo seria `idade >= 18`).
3. Falta o `;` no fim do `Console.WriteLine(...)` (e no fim da primeira linha).

Corrigido:

```csharp in=20
int idade = int.Parse(Console.ReadLine());
if (idade >= 18)
    Console.WriteLine("Maior de idade");
```

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Teste de mesa: int a = 5; int b = 2; a = a + b; b = a * b; a = a - b; Console.WriteLine(a + " " + b);</summary>

| Linha | a | b |
|---|---|---|
| início | 5 | 2 |
| `a = a + b` | 7 | 2 |
| `b = a * b` | 7 | 14 |
| `a = a - b` | −7 | 14 |

Mostra **`-7 14`**. Atenção: cada linha usa o valor **atual**, já modificado pelas linhas de cima.

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — Um cinema dá meia-entrada para quem tem menos de 18 OU mais de 60 anos. Qual condição está certa? (A) idade < 18 && idade > 60 (B) idade < 18 || idade > 60 (C) idade > 18 || idade < 60 (D) !(idade < 18)</summary>

**B.** Basta **uma** das situações → **OU** (`||`). A alternativa A nunca é verdadeira: ninguém tem menos de 18 **e** mais de 60 ao mesmo tempo.

</details>

### 🖥️ Mão na massa (30 minutos)

Você vai rodar C# de verdade, sem instalar nada:

1. Abra **dotnetfiddle.net** (no PC ou no celular).
2. Confira no menu da esquerda: **Language: C#**, **Project Type: Console**.
3. Apague o código que vem pronto e **digite** (não copie) o programa abaixo.
4. Clique em **Run**. Quando o programa pedir dados, digite na caixa de saída embaixo e aperte Enter.

**Programa 1 — par ou ímpar:**

```csharp in=7
using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite um número inteiro: ");
        int n = int.Parse(Console.ReadLine());

        if (n % 2 == 0)
            Console.WriteLine(n + " é par");
        else
            Console.WriteLine(n + " é ímpar");
    }
}
```

**Programa 2 — sozinho:** escreva um programa que lê a **idade** e diz "Pode votar" se a idade for **16 ou mais**, e "Ainda não pode votar" caso contrário.

**Programa 3 — desafio:** leia **nota** e **frequência**. Mostre "Aprovado" se nota ≥ 6 **e** frequência ≥ 75; senão, "Reprovado". Teste com: (7, 80), (7, 70) e (5, 90).

**Programa 4 — erro de propósito:** no Programa 1, apague um `;` e clique em Run. Leia a mensagem de erro (ela diz a linha e que "**; expected**", ou seja, "esperava um ponto e vírgula"). Coloque de volta. Aprender a ler erro é metade do laboratório do dia 08/12.

<details class="recall-box">
<summary>✅ Uma resposta possível para os Programas 2 e 3</summary>

```csharp in=16|7|80
// Programa 2
Console.Write("Idade: ");
int idade = int.Parse(Console.ReadLine());
if (idade >= 16)
    Console.WriteLine("Pode votar");
else
    Console.WriteLine("Ainda não pode votar");

// Programa 3
Console.Write("Nota: ");
double nota = double.Parse(Console.ReadLine());
Console.Write("Frequência: ");
int freq = int.Parse(Console.ReadLine());
if (nota >= 6 && freq >= 75)
    Console.WriteLine("Aprovado");
else
    Console.WriteLine("Reprovado");
```

Resultados esperados do Programa 3: (7, 80) → Aprovado; (7, 70) → Reprovado; (5, 90) → Reprovado.

(Lembre de colocar esses trechos **dentro** do `static void Main() { ... }`.)

</details>

### ✅ Resumo de 1 minuto

- **Algoritmo** = passos **finitos, ordenados e sem ambiguidade**. Programa = algoritmo escrito numa linguagem.
- **Fluxograma**: oval (início/fim), paralelogramo (entrada/saída), retângulo (cálculo), **losango (decisão)**.
- **Variável** = caixinha com nome, tipo e valor. `=` **atribui**; `==` **compara**.
- **Tipos**: `int` (inteiro), `double` (decimal, com ponto no código), `string` (texto entre aspas), `char`, `bool`.
- `Console.ReadLine()` lê **texto** → use `int.Parse` / `double.Parse`.
- **`%` = resto** da divisão. Inteiro ÷ inteiro = inteiro (`7 / 2` = 3).
- **`&&` = E** (precisa das duas), **`||` = OU** (basta uma), **`!` = NÃO**.
- **`if / else if / else`**: escolhe **um** caminho, testando de cima para baixo.
- **Teste de mesa**: tabela de variáveis, uma linha por vez, sem pular.
