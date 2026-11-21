## Dia 3 (23/11) — Programação II: laços, vetores, matrizes, erros e depuração

Ontem o programa aprendeu a **decidir** (`if`). Hoje ele aprende a **repetir** (laços) e a **guardar vários valores** (vetores e matrizes). Também vamos ver o que acontece quando o programa dá erro e como achar o defeito. Essas quatro coisas aparecem juntas em quase toda prova técnica de Taboão — e no laboratório você vai precisar de pelo menos um laço.

> [!IMPORTANT]
> Hoje o **teste de mesa** é obrigatório. Questão de laço sem tabela é chute. Tenha papel e caneta do lado e faça cada tabela antes de abrir a resposta.

### 1. Por que repetir?

Imagine mostrar os números de 1 a 100. Sem laço, seriam 100 linhas de `Console.WriteLine`. Com laço, são 3:

```csharp
for (int i = 1; i <= 100; i++)
{
    Console.WriteLine(i);
}
```

Um **laço** (ou *loop*, ou **estrutura de repetição**) executa um bloco **várias vezes** enquanto uma condição for verdadeira. Em C# existem três: **`while`**, **`do … while`** e **`for`**. Em português estruturado eles se chamam **ENQUANTO**, **REPITA** e **PARA**.

> [!WARNING]
> **🔁 Já caiu — 2021 (questão 39):** "A instrução PARA é uma: …" → **estrutura de repetição**. As três famílias de comandos: **sequência/atribuição** (`x = 5`), **condição/decisão** (`if`, `switch`) e **repetição** (`for`, `while`, `do-while`).

### 2. while: "enquanto"

```csharp nocheck
while (condição)
{
    // repete enquanto a condição for verdadeira
}
```

O `while` **testa a condição antes** de cada volta (é um laço **pré-testado**). Se a condição já começar falsa, o bloco roda **zero vezes**.

```csharp
int contador = 1;
while (contador <= 3)
{
    Console.WriteLine("Volta " + contador);
    contador++;                 // sem isto, o laço nunca acaba!
}
Console.WriteLine("Fim");
```

Teste de mesa:

| Antes da volta | contador | contador <= 3? | Mostra |
|---|---|---|---|
| 1ª | 1 | V | Volta 1 |
| 2ª | 2 | V | Volta 2 |
| 3ª | 3 | V | Volta 3 |
| — | 4 | **F** → sai | Fim |

> [!CAUTION]
> **Laço infinito:** se nada dentro do laço muda a variável da condição, ela nunca fica falsa e o programa trava repetindo para sempre. Sempre confira: *"o que faz esse laço parar?"*

**Quando usar o while:** quando você **não sabe quantas vezes** vai repetir. Exemplo: ler números até o usuário digitar 0.

```csharp in=5|3|0
int soma = 0;
Console.Write("Número (0 para parar): ");
int n = int.Parse(Console.ReadLine());
while (n != 0)
{
    soma = soma + n;
    Console.Write("Número (0 para parar): ");
    n = int.Parse(Console.ReadLine());
}
Console.WriteLine("Soma: " + soma);
```

Digitando 5, 3 e 0, a saída final é `Soma: 8`.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2025 (questão 12):** "repetir um número **indefinido** de vezes, até que uma condição seja atendida (como ler dados até o usuário digitar 'sair')" → **while ou do-while**. O `for` é para quando a quantidade de voltas é **conhecida**.

### 3. do … while: "faça, depois teste"

```csharp nocheck
do
{
    // roda PELO MENOS UMA VEZ
} while (condição);     // ← repare no ; no final
```

O `do … while` executa o bloco **primeiro** e testa **depois** (laço **pós-testado**). Por isso ele **sempre roda pelo menos uma vez**, mesmo se a condição for falsa desde o início.

```csharp
int x = 10;
while (x < 5)
{
    Console.WriteLine("while: " + x);     // nunca roda: 10 < 5 é falso logo de cara
}

do
{
    Console.WriteLine("do-while: " + x);  // roda uma vez antes de testar
} while (x < 5);
```

Saída:

```text
do-while: 10
```

| | `while` | `do … while` |
|---|---|---|
| Testa a condição | **antes** de cada volta | **depois** de cada volta |
| Mínimo de execuções | **0** | **1** |
| Uso típico | ler até aparecer um valor de parada | **menu** ("deseja continuar?"), validar entrada |

O uso clássico do `do … while` é o **menu**, que precisa aparecer pelo menos uma vez:

```csharp in=1|2|0
int opcao;
do
{
    Console.WriteLine("1 - Jogar  2 - Ranking  0 - Sair");
    opcao = int.Parse(Console.ReadLine());
    Console.WriteLine("Você escolheu " + opcao);
} while (opcao != 0);
```

> [!TIP]
> Essa diferença (do-while executa **ao menos uma vez** porque testa **no final**) é cobrada em prova de várias formas. Se uma alternativa diz que o do-while "pode não executar nenhuma vez", ela está **errada**.

### 4. for: o laço com contador

Quando você **sabe quantas vezes** quer repetir, o `for` é o mais prático. Ele junta três coisas numa linha só:

```csharp
for (int i = 1; i <= 5; i++)
//   ───┬────   ───┬──   ─┬─
//   início   condição   passo
{
    Console.WriteLine(i);
}
```

A ordem exata em que o C# executa:

1. **Início** (`int i = 1`) — roda **uma vez só**, no começo.
2. **Condição** (`i <= 5`) — testa. Se falsa, **sai** do laço.
3. **Bloco** — executa o que está entre `{ }`.
4. **Passo** (`i++`) — atualiza o contador.
5. Volta para o passo **2**.

O detalhe que derruba gente em prova: o **passo acontece depois do bloco**. Então o **primeiro valor mostrado é o inicial**.

**Exemplo — caiu em dez/2023 (questão 36):**

```csharp
for (int i = -5; i <= 7; i += 3)
{
    Console.WriteLine(i);
}
```

| Volta | i | i <= 7? | Mostra |
|---|---|---|---|
| 1 | −5 | V | −5 |
| 2 | −2 | V | −2 |
| 3 | 1 | V | 1 |
| 4 | 4 | V | 4 |
| 5 | 7 | V (7 ≤ 7) | 7 |
| — | 10 | **F** → sai | |

Saída: **−5, −2, 1, 4, 7**. As alternativas erradas da prova esqueciam o −5 (achando que o passo vem antes) ou o 7 (esquecendo que `<=` inclui o igual).

**Contando para trás e pulando:**

```csharp
for (int i = 10; i >= 0; i -= 5)
    Console.Write(i + " ");      // 10 5 0
Console.WriteLine();
for (int i = 0; i < 10; i += 2)
    Console.Write(i + " ");      // 0 2 4 6 8
```

<details class="recall-box">
<summary>🧠 Sua vez — quantas vezes roda e o que mostra: for (int i = 2; i < 11; i += 4) Console.Write(i + " ");</summary>

i = 2 (2 < 11 ✔) → 6 (✔) → 10 (✔) → 14 (✘ sai). Roda **3 vezes** e mostra **`2 6 10`**.

</details>

**Qual laço usar?**

| Situação | Laço |
|---|---|
| Sei quantas vezes (de 1 a 10, cada aluno da turma, cada posição do vetor) | **`for`** |
| Não sei quantas vezes; para quando uma condição mudar | **`while`** |
| Igual ao while, mas precisa rodar **ao menos uma vez** (menu, validação) | **`do … while`** |

### 5. Contadores e acumuladores

Dois "truques" aparecem em quase todo programa com laço:

- **Contador:** conta quantas vezes algo aconteceu → `cont = cont + 1` (ou `cont++`).
- **Acumulador:** vai somando valores → `soma = soma + valor` (ou `soma += valor`).

Os dois precisam **começar com zero antes** do laço.

```csharp
int soma = 0;
int pares = 0;
for (int i = 1; i <= 6; i++)
{
    soma += i;               // acumula 1+2+3+4+5+6
    if (i % 2 == 0)
        pares++;             // conta quantos são pares
}
Console.WriteLine("Soma: " + soma + " | Pares: " + pares);
```

| i | soma | i % 2 == 0? | pares |
|---|---|---|---|
| (antes) | 0 | | 0 |
| 1 | 1 | não | 0 |
| 2 | 3 | sim | 1 |
| 3 | 6 | não | 1 |
| 4 | 10 | sim | 2 |
| 5 | 15 | não | 2 |
| 6 | 21 | sim | 3 |

Saída: `Soma: 21 | Pares: 3`.

**Laço com `if` e `%` dentro** — o formato preferido das provas: "o que este laço imprime?". Exemplo:

```csharp
int n = 12;
while (n <= 20)
{
    if (n % 4 == 0)
        Console.Write(n + " ");
    n++;
}
```

| n | n <= 20? | n % 4 == 0? | Mostra |
|---|---|---|---|
| 12 | V | V | 12 |
| 13, 14, 15 | V | F | — |
| 16 | V | V | 16 |
| 17, 18, 19 | V | F | — |
| 20 | V | V | 20 |
| 21 | **F** → sai | | |

Saída: `12 16 20`.

<details class="recall-box">
<summary>🧠 Sua vez — o que imprime? int t = 0; for (int i = 1; i <= 4; i++) { t = t + i * i; } Console.WriteLine(t);</summary>

t vai acumulando os quadrados: 1 + 4 + 9 + 16 = **30**.

| i | i*i | t |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 4 | 5 |
| 3 | 9 | 14 |
| 4 | 16 | 30 |

</details>

### 6. Vetores (arrays): uma fileira de caixinhas

Uma variável guarda **um** valor. E se você quer guardar as notas de 5 provas? Criar `nota1`, `nota2`, … `nota5` não escala. Um **vetor** é **uma variável com várias posições numeradas**, todas do **mesmo tipo**:

```text
notas:   [ 7.5 ][ 8.0 ][ 6.0 ][ 9.5 ][ 5.0 ]
índice:     0      1      2      3      4
```

> [!CAUTION]
> **O índice começa em 0.** Um vetor de 5 posições vai de **0 a 4**. A posição 5 **não existe** — acessar `notas[5]` faz o programa quebrar com o erro `IndexOutOfRangeException` (índice fora do intervalo).

**Criando vetores em C#** — os colchetes ficam **colados no tipo**:

```csharp
int[] idades = new int[3];               // 3 posições, todas valendo 0
idades[0] = 16;
idades[1] = 17;
idades[2] = 15;

double[] notas = { 7.5, 8.0, 6.0, 9.5, 5.0 };   // já cria com os valores
string[] nomes = new string[] { "Ana", "Bia" };

Console.WriteLine(notas[0]);             // 7.5 (primeira posição)
Console.WriteLine(notas[4]);             // 5   (última posição)
Console.WriteLine(notas.Length);         // 5   (quantas posições tem)
```

> [!WARNING]
> **🔁 Já caiu — dez/2023 (questão 35):** "a forma correta para inicializar um array de inteiros de cinco posições, com os números de 1 até 5" → **`int[] Inteiros = {1,2,3,4,5};`**. As erradas colocavam o colchete depois do nome (`int Inteiros[]`, estilo da linguagem C) ou o tamanho na declaração (`int[5]`).

**Percorrendo o vetor com `for`** — o padrão que você vai usar no laboratório:

```csharp
double[] notas = { 7.5, 8.0, 6.0, 9.5, 5.0 };
double soma = 0;
double maior = notas[0];

for (int i = 0; i < notas.Length; i++)      // i vai de 0 até 4
{
    soma += notas[i];
    if (notas[i] > maior)
        maior = notas[i];
}

Console.WriteLine("Média: " + soma / notas.Length);   // 36 / 5 = 7.2
Console.WriteLine("Maior: " + maior);                 // 9.5
```

Repare no `i < notas.Length` (**menor**, não menor ou igual): como o último índice é `Length - 1`, usar `<=` passaria do fim do vetor.

<details class="recall-box">
<summary>🧠 Sua vez — int[] v = { 4, 9, 2, 7 }; o que vale v[1] + v[v.Length - 1]?</summary>

v[1] = **9** (segunda posição). v.Length = 4, então v[3] = **7** (última). 9 + 7 = **16**.

</details>

### 7. Matrizes: uma tabela de linhas e colunas

Uma **matriz** é como uma planilha: tem **linhas** e **colunas**, e cada valor é encontrado por **dois índices** — `[linha, coluna]`, os dois começando em 0.

```text
             coluna 0   coluna 1   coluna 2
linha 0  →      1          2          3
linha 1  →      4          5          6
```

Em C#, matriz usa **vírgula dentro do colchete**: `int[,]`.

```csharp
int[,] m = { { 1, 2, 3 },
             { 4, 5, 6 } };          // 2 linhas, 3 colunas

Console.WriteLine(m[0, 2]);          // linha 0, coluna 2 → 3
Console.WriteLine(m[1, 0]);          // linha 1, coluna 0 → 4
Console.WriteLine(m.GetLength(0));   // número de linhas  → 2
Console.WriteLine(m.GetLength(1));   // número de colunas → 3
```

**Percorrendo a matriz: um `for` dentro de outro.** O de fora anda pelas **linhas**; o de dentro, pelas **colunas**:

```csharp
int[,] m = { { 1, 2, 3 }, { 4, 5, 6 } };
for (int i = 0; i < 2; i++)              // linhas
{
    for (int j = 0; j < 3; j++)          // colunas
    {
        Console.Write(m[i, j] + " ");
    }
    Console.WriteLine();                 // pula linha ao terminar cada linha
}
```

Saída:

```text
1 2 3 
4 5 6 
```

O laço de dentro roda **inteiro** para cada volta do laço de fora: (i=0: j=0,1,2) e depois (i=1: j=0,1,2).

**A pegadinha dos índices trocados.** Se o código usar `m[j, i]` em vez de `m[i, j]`, ele lê **coluna por coluna** — e a saída muda completamente. Teste com a matriz quadrada abaixo:

```csharp
int[,] q = { { 1, 2 }, { 3, 4 } };
for (int i = 0; i < 2; i++)
{
    for (int j = 0; j < 2; j++)
        Console.Write(q[j, i] + " ");    // índices trocados!
    Console.WriteLine();
}
```

| i | j | q[j, i] | mostra |
|---|---|---|---|
| 0 | 0 | q[0,0] = 1 | 1 |
| 0 | 1 | q[1,0] = 3 | 3 |
| | | quebra linha | |
| 1 | 0 | q[0,1] = 2 | 2 |
| 1 | 1 | q[1,1] = 4 | 4 |

Saída: `1 3` e, na linha de baixo, `2 4` — a matriz "virada" (a **transposta**). Sempre olhe **qual variável está em qual posição** do colchete.

**Matriz irregular (*jagged*).** Em C#, também existe "vetor de vetores", em que cada linha pode ter um tamanho diferente:

```csharp
int[][] irregular = new int[2][];
irregular[0] = new int[] { 1, 2 };          // linha com 2 elementos
irregular[1] = new int[] { 3, 4, 5, 6 };    // linha com 4 elementos
Console.WriteLine(irregular[1][3]);         // 6
```

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questão 37):** pedia a afirmação **incorreta** sobre vetores e matrizes. A falsa era: "uma matriz bidimensional **sempre** deve ter o mesmo número de colunas em todas as linhas, **independentemente da linguagem**" — errado, porque existem matrizes irregulares como a de cima. As verdadeiras: vetor guarda vários valores do mesmo tipo com índice; matriz é "vetor de vetores"; o tamanho costuma ser fixo; cada elemento da matriz usa dois índices.

### 8. Quando o programa dá errado: três tipos de erro

| Tipo | Quando aparece | Exemplo | O que acontece |
|---|---|---|---|
| **Erro de sintaxe** (de compilação) | antes de rodar | faltou `;`, faltou `}`, escreveu `Consle` | o **compilador recusa**: o programa **nem roda**, e o Visual Studio sublinha a linha em vermelho |
| **Erro de execução** (exceção) | durante a execução | digitar "abc" num `int.Parse`; acessar `v[10]` num vetor de 5 | o programa **quebra** no meio, com uma mensagem de exceção |
| **Erro de lógica** | o programa roda até o fim | média sem parênteses; `>` no lugar de `>=` | roda "normal", mas o **resultado está errado** |

O **compilador** é o programa que **traduz** o seu código-fonte para uma forma que o computador executa. Se ele encontra erro de sintaxe, **não gera** o programa e **mostra onde está o problema** — ele **não corrige sozinho**.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2024 (questão 37):** "compilador é um programa que **analisa o código-fonte e gera um código binário**". As erradas diziam que ele "corrige automaticamente erros de lógica" ou "evita o fechamento do programa".

**Compilada, interpretada ou híbrida?**

- **Compilada** (C, C++): traduz **tudo antes** de rodar e gera um executável (`.exe`).
- **Interpretada** (Python, JavaScript, PHP): um interpretador lê e executa **linha a linha** na hora.
- **Híbrida** (**C#**, Java): o código é compilado para uma **linguagem intermediária** (no C#, a *IL*; no Java, o *bytecode*), que roda numa **máquina virtual** (no .NET, o *CLR*; no Java, a *JVM*).

> [!WARNING]
> **🔁 Já caiu — dez/2023 (questão 33):** a afirmação correta era a de que "linguagens como **Java e C#** têm seus códigos-fonte transformados em uma **linguagem intermediária**, que será interpretada pela **máquina virtual** da linguagem".

### 9. Tratamento de exceções: try / catch

O usuário vai digitar errado — sempre. Se o programa espera um número e a pessoa digita "dez", o `int.Parse` lança uma **exceção** (`FormatException`) e o programa **quebra**. Para isso não acontecer, usamos **`try` / `catch`**:

```csharp nocheck
try
{
    // código que PODE dar erro
}
catch (Exception)
{
    // o que fazer SE der erro (em vez de quebrar)
}
```

Exemplo completo — pedir de novo até a pessoa digitar um inteiro **positivo**:

```csharp in=abc|-4|9
int numero = 0;
bool ok = false;
while (!ok)
{
    Console.Write("Digite um inteiro positivo: ");
    try
    {
        numero = int.Parse(Console.ReadLine());    // "abc" gera exceção AQUI
        if (numero > 0)
            ok = true;                               // positivo: pode sair do laço
        else
            Console.WriteLine("Precisa ser maior que zero.");
    }
    catch (FormatException)
    {
        Console.WriteLine("Isso não é um número inteiro. Tente de novo.");
    }
}
Console.WriteLine("Você digitou " + numero);
```

Digitando `abc`, depois `-4`, depois `9`, a saída é:

```text
Digite um inteiro positivo: Isso não é um número inteiro. Tente de novo.
Digite um inteiro positivo: Precisa ser maior que zero.
Digite um inteiro positivo: Você digitou 9
```

Repare em duas coisas que a prova cobrou:

1. O `try/catch` **pega a entrada inválida** (letras) — sem ele, o programa fecharia.
2. O número **−4 não gera exceção** (é um inteiro válido!). Para recusar negativos, ainda é preciso o **`if`**.

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questão 35):** um programa deve pedir um inteiro positivo e, se o usuário digitar letras ou negativos, pedir de novo. Verdadeiras: (I) o tratamento de exceções captura entradas inválidas como letras; (II) mesmo com tratamento de exceções, ainda é preciso verificar se o número é maior que zero. Falsa: (III) "o programa deve necessariamente ser encerrado".

Existe também um bloco **`finally`**, que roda **sempre**, dando erro ou não (usado para fechar arquivos, por exemplo).

### 10. Depuração: breakpoints

**Depurar** (*debug*) é procurar e corrigir defeitos. No **Visual Studio**:

1. Clique na **margem cinza à esquerda** de uma linha (ou aperte **F9**): aparece uma **bolinha vermelha** — o **breakpoint** (ponto de parada).
2. Rode com **F5** (Iniciar depuração). Quando a execução chega na linha marcada, o programa **pausa**.
3. Passe o mouse sobre as variáveis (ou veja a janela **Locais/Autos**) para ver **o valor de cada uma naquele momento**.
4. Avance **uma linha por vez** com **F10** (passa por cima) ou **F11** (entra dentro de um método).

É o teste de mesa feito pelo computador. Muito útil quando o programa roda mas dá resultado errado (erro de lógica).

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questão 36):** "Qual é o papel de um breakpoint?" → **pausar a execução num ponto marcado, permitindo inspecionar valores, fluxo e comportamento**. A pegadinha dizia que ele pausa "**apenas quando ocorre uma exceção**" (errado: pausa sempre que passa ali).

### 11. Bônus que já caiu: objetos e aplicativos

**Criar um objeto com `new`** — caiu em **dez/2023 (questão 34)**. Na orientação a objetos, uma **classe** é o molde (a "planta") e o **objeto** é a coisa criada a partir dele. Você já usa isso: `new int[5]` cria um vetor.

```csharp nocheck
Carro meuCarro = new Carro();   // tipo  nome = new Classe();
```

(Para rodar, a classe `Carro` precisa existir — no 1º ano, decore o formato: **Tipo nome = new Tipo();**.)

**Tipos de aplicativo móvel** — caiu em **dez/2023 (questões 39 e 40)**:

| Tipo | Feito com | Roda em | Ponto forte |
|---|---|---|---|
| **Nativo** | linguagem do sistema (Kotlin no Android, Swift no iOS) | **um** sistema só | mais rápido e acesso total ao aparelho |
| **Híbrido** | tecnologias web + framework (React Native, Flutter, Ionic) | Android **e** iOS com um código só | economia de tempo |
| **Web app** | HTML, CSS e JavaScript no navegador | qualquer aparelho com navegador | não precisa instalar |

Um app nativo de Android **não roda** no iOS — por isso existem os híbridos.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Esquecer de atualizar a variável do `while`** → laço infinito.
> - **Achar que o `for` mostra primeiro o valor já somado**: o passo (`i++`) vem **depois** do bloco.
> - **Usar `<=` com `Length`**: `for (int i = 0; i <= v.Length; i++)` passa do fim do vetor (erro de execução).
> - **Começar vetor no índice 1** — começa no **0**.
> - **Não zerar o acumulador** antes do laço (ou zerar **dentro** do laço, apagando a soma a cada volta).
> - **Esquecer o `;` no fim do `do { } while (...);`**.
> - **Achar que `try/catch` resolve tudo**: ele pega exceções, mas regra de negócio (como "não pode ser negativo") precisa de `if`.

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — O que imprime? int i = 5; while (i > 0) { Console.Write(i + " "); i -= 2; }</summary>

| i | i > 0? | mostra |
|---|---|---|
| 5 | V | 5 |
| 3 | V | 3 |
| 1 | V | 1 |
| −1 | F → sai | |

Saída: **`5 3 1`**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Quantas vezes "Oi" aparece? int k = 10; do { Console.WriteLine("Oi"); k++; } while (k < 5);</summary>

**Uma vez.** O `do … while` executa antes de testar; depois testa 11 < 5 (falso) e para. Com `while` comum seria **zero**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — O que imprime? for (int i = 1; i <= 10; i++) { if (i % 3 == 0) Console.Write(i + " "); }</summary>

Os múltiplos de 3 entre 1 e 10: **`3 6 9`**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — int[] v = { 3, 8, 1, 6 }; int s = 0; for (int i = 1; i < v.Length; i += 2) s += v[i]; Console.WriteLine(s);</summary>

i começa em **1** e pula de 2 em 2: i = 1 (v[1] = 8) e i = 3 (v[3] = 6). i = 5 já não é menor que 4. s = 8 + 6 = **14**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Na matriz int[,] m = { {5, 1, 7}, {2, 9, 4} }, quanto vale m[1, 2] + m[0, 1]?</summary>

m[1, 2] → linha 1, coluna 2 → **4**. m[0, 1] → linha 0, coluna 1 → **1**. Total: **5**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Classifique o erro: (a) faltou "}" no fim do Main (b) int.Parse("doze") (c) a média deu 13 em vez de 6,5</summary>

(a) **sintaxe** — não compila. (b) **execução** — `FormatException` ao rodar. (c) **lógica** — provavelmente faltaram os parênteses: `n1 + n2 / 2`.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Qual laço usar: (a) mostrar a tabuada do 7 (b) ler senhas até acertar (c) mostrar um menu e repetir até a opção 0</summary>

(a) **for** (10 vezes, quantidade conhecida). (b) **while** (não se sabe quantas tentativas). (c) **do … while** (o menu precisa aparecer pelo menos uma vez).

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — Sobre o breakpoint, é correto: (A) apaga linhas com erro (B) pausa em um ponto marcado para inspecionar variáveis (C) só funciona quando há exceção (D) deixa o programa mais rápido (E) corrige a sintaxe</summary>

**B.** Breakpoint = ponto de parada para inspecionar o programa enquanto ele roda.

</details>

### 🖥️ Mão na massa (30–40 minutos)

No **dotnetfiddle.net** (C#, Console), digite e rode:

**Programa 1 — tabuada:** leia um número e mostre a tabuada dele de 1 a 10 no formato `7 x 3 = 21`.

**Programa 2 — notas da turma:** crie um vetor com 5 notas (`double[] notas = { … };`), calcule a **média**, a **maior** e a **menor** nota, e conte **quantas** ficaram abaixo de 6.

**Programa 3 — entrada à prova de erro:** use `try/catch` dentro de um `while` para ler a idade até a pessoa digitar um número inteiro entre 0 e 120.

**Programa 4 — depuração no Visual Studio (se tiver no PC):** abra o Programa 2, coloque um breakpoint (F9) dentro do `for`, rode com F5 e avance com F10 vendo `soma` e `i` mudarem.

<details class="recall-box">
<summary>✅ Uma resposta possível para os Programas 1 e 2</summary>

```csharp in=7
// Programa 1 — tabuada
Console.Write("Tabuada do: ");
int n = int.Parse(Console.ReadLine());
for (int i = 1; i <= 10; i++)
{
    Console.WriteLine(n + " x " + i + " = " + (n * i));
}

// Programa 2 — notas da turma
double[] notas = { 7.5, 4.0, 9.0, 5.5, 8.0 };
double soma = 0, maior = notas[0], menor = notas[0];
int abaixo = 0;
for (int i = 0; i < notas.Length; i++)
{
    soma += notas[i];
    if (notas[i] > maior) maior = notas[i];
    if (notas[i] < menor) menor = notas[i];
    if (notas[i] < 6) abaixo++;
}
Console.WriteLine("Média: " + soma / notas.Length);
Console.WriteLine("Maior: " + maior + " | Menor: " + menor);
Console.WriteLine("Abaixo de 6: " + abaixo);
```

Saída do Programa 2: `Média: 6.8`, `Maior: 9 | Menor: 4`, `Abaixo de 6: 2`.

Atenção ao `(n * i)` entre parênteses: sem eles, o `+` com texto viria antes e juntaria os números como texto.

</details>

### ✅ Resumo de 1 minuto

- **while**: testa **antes**; pode rodar **0** vezes. Use quando não sabe quantas voltas.
- **do … while**: testa **depois**; roda **ao menos 1** vez. Use em menus e validação. Termina com `;`.
- **for (início; condição; passo)**: quantidade conhecida. O primeiro valor mostrado é o **inicial**; o passo vem **depois** do bloco.
- **Acumulador** `soma += x` e **contador** `cont++` começam em **0** antes do laço.
- **Vetor** `int[] v = {…}`: índices de **0 a Length − 1**. Percorra com `for (int i = 0; i < v.Length; i++)`.
- **Matriz** `int[,] m`: `m[linha, coluna]`, dois `for` aninhados. Cuidado com `[j, i]` trocado.
- Erros: **sintaxe** (não compila), **execução/exceção** (quebra rodando), **lógica** (resultado errado).
- **try/catch** captura exceções (como letras no `int.Parse`); negativos ainda precisam de `if`.
- **Breakpoint** pausa a execução num ponto marcado para inspecionar variáveis (F9, F5, F10).
- **C# e Java** são compilados para linguagem intermediária e rodam em máquina virtual.
