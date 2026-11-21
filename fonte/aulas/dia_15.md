## Dia 15 (06/12) — Laboratório 2: programas em C# no console

Programação é a matéria com mais aulas do 1º ano, e as provas de Taboão usam **C#**. No laboratório, a tarefa mais provável é **escrever um programa pequeno do zero**: ler dados, decidir com `if`, repetir com `for`/`while`, mostrar o resultado — e **consertar os erros** que aparecerem. Hoje você vai fazer isso **dez vezes**.

> [!IMPORTANT]
> Faça cada desafio **digitando**, com o cronômetro ligado, e **só depois** abra a solução. Se travar, olhe a aula do Dia 2 ou 3 — mas não a solução.

### 1. Criando o projeto no Visual Studio

O laboratório deve ter o **Visual Studio** (o Plano de Curso cita o .NET com Visual Studio ou VS Code). Passo a passo:

1. Abra o **Visual Studio** → **Criar um projeto**.
2. Na busca, digite **console** e escolha **Aplicativo de Console** com a etiqueta **C#** (cuidado para não pegar o de Visual Basic ou de C++).
3. Dê um **nome** ao projeto (sem espaço nem acento: `ProvaHenrique`) e escolha a **pasta** pedida pelo professor.
4. Na tela seguinte, escolha a versão do **.NET** que aparecer. Se houver a opção **"Não usar instruções de nível superior"**, **marque-a**: assim o arquivo vem com o esqueleto completo (`class Program`, `static void Main`), igual ao das aulas e das provas.
5. O arquivo **Program.cs** abre. Escreva seu código dentro do `static void Main(string[] args) { … }`.
6. **Rodar:** **Ctrl + F5** (Iniciar sem depurar) — a janela preta fica aberta no fim, esperando uma tecla. Com **F5** (depurar), ela pode fechar sozinha quando o programa termina.

> [!NOTE]
> **Se aparecer só uma linha** `Console.WriteLine("Hello, World!");` sem `class` nem `Main`, é o formato "de nível superior" do C# moderno. Ele também funciona: escreva os comandos direto ali, de cima para baixo. Mas o formato completo é o que as provas usam.

**Sem Visual Studio:** use **dotnetfiddle.net** (Language: C#, Project Type: Console), como nos Dias 2 e 3.

> [!CAUTION]
> **Números com vírgula no Windows em português:** ao **digitar** um número decimal no programa rodando, use **vírgula** (`7,5`); no **código**, use **ponto** (`7.5`). Se o `double.Parse` der erro com `7.5`, é isso.

### 2. Lendo os erros do compilador

Quando há erro de sintaxe, o Visual Studio sublinha de vermelho e mostra a **Lista de Erros** embaixo, com o **código** do erro e a **linha**. Os que mais aparecem:

| Erro | Significa | Conserto |
|---|---|---|
| **CS1002: ; esperado** | faltou ponto e vírgula | coloque `;` no fim da linha indicada (ou da anterior) |
| **CS1513: } esperado** | faltou fechar uma chave | conte as `{` e `}` |
| **CS0103: o nome 'x' não existe no contexto atual** | variável não declarada ou escrita diferente | declare (`int x = 0;`) ou corrija maiúsculas/minúsculas |
| **CS0029: não é possível converter 'string' em 'int'** | guardou texto em variável numérica | use `int.Parse(Console.ReadLine())` |
| **CS0165: uso de variável não atribuída** | usou a variável antes de dar valor a ela | inicialize: `int soma = 0;` |
| **FormatException** (ao rodar) | digitou algo que não é número | digite um número, ou trate com `try/catch` |
| **IndexOutOfRangeException** (ao rodar) | acessou posição que não existe no vetor | o índice vai de 0 a `Length - 1` |

Dica: **conserte o primeiro erro da lista e compile de novo** — muitas vezes um `;` faltando gera vários erros em cascata.

### 3. Uma ferramenta nova: switch

Quando uma variável pode ter **vários valores** e cada um leva a uma ação, o `switch` fica mais limpo que muitos `else if`:

```csharp in=2
Console.Write("Opção (1 a 3): ");
int op = int.Parse(Console.ReadLine());
switch (op)
{
    case 1:
        Console.WriteLine("Novo jogo");
        break;              // sai do switch (obrigatório no fim de cada case)
    case 2:
        Console.WriteLine("Carregar jogo");
        break;
    case 3:
        Console.WriteLine("Sair");
        break;
    default:                // qualquer outro valor
        Console.WriteLine("Opção inválida");
        break;
}
```

### 4. Os 10 desafios

Cada desafio traz **um exemplo de execução** (o que você digita aparece depois dos dois-pontos). Faça o seu programa produzir a mesma coisa.

<details class="recall-box">
<summary>💻 Desafio 1 (5 min) — Maioridade: leia nome e idade; mostre "Olá, NOME! Você é maior de idade." ou "…menor de idade."</summary>

```csharp in=Henrique|16
Console.Write("Nome: ");
string nome = Console.ReadLine();
Console.Write("Idade: ");
int idade = int.Parse(Console.ReadLine());

if (idade >= 18)
    Console.WriteLine($"Olá, {nome}! Você é maior de idade.");
else
    Console.WriteLine($"Olá, {nome}! Você é menor de idade.");
```

Execução: `Nome: Henrique` / `Idade: 16` → `Olá, Henrique! Você é menor de idade.`

</details>

<details class="recall-box">
<summary>💻 Desafio 2 (10 min) — Média e situação: leia 3 notas; mostre a média com 1 casa decimal e "Aprovado" (≥ 6), "Recuperação" (≥ 4 e &lt; 6) ou "Reprovado" (&lt; 4).</summary>

```csharp in=7|5|6
Console.Write("Nota 1: ");
double n1 = double.Parse(Console.ReadLine());
Console.Write("Nota 2: ");
double n2 = double.Parse(Console.ReadLine());
Console.Write("Nota 3: ");
double n3 = double.Parse(Console.ReadLine());

double media = (n1 + n2 + n3) / 3;             // parênteses!
Console.WriteLine("Média: " + media.ToString("F1"));   // F1 = 1 casa decimal

if (media >= 6)
    Console.WriteLine("Aprovado");
else if (media >= 4)
    Console.WriteLine("Recuperação");
else
    Console.WriteLine("Reprovado");
```

Com 7, 5 e 6: `Média: 6.0` e `Aprovado` (num Windows em português, aparece `6,0`).

</details>

<details class="recall-box">
<summary>💻 Desafio 3 (10 min) — Calculadora: leia dois números e uma operação (+, -, *, /) e mostre o resultado. Na divisão por zero, mostre "Não é possível dividir por zero".</summary>

```csharp in=10|/|4
Console.Write("Primeiro número: ");
double a = double.Parse(Console.ReadLine());
Console.Write("Operação (+ - * /): ");
string op = Console.ReadLine();
Console.Write("Segundo número: ");
double b = double.Parse(Console.ReadLine());

switch (op)
{
    case "+": Console.WriteLine("Resultado: " + (a + b)); break;
    case "-": Console.WriteLine("Resultado: " + (a - b)); break;
    case "*": Console.WriteLine("Resultado: " + (a * b)); break;
    case "/":
        if (b == 0)
            Console.WriteLine("Não é possível dividir por zero");
        else
            Console.WriteLine("Resultado: " + (a / b));
        break;
    default: Console.WriteLine("Operação inválida"); break;
}
```

Com 10, / e 4: `Resultado: 2.5`.

</details>

<details class="recall-box">
<summary>💻 Desafio 4 (5 min) — Tabuada: leia um número e mostre a tabuada de 1 a 10 no formato "7 x 3 = 21".</summary>

```csharp in=7
Console.Write("Tabuada do: ");
int n = int.Parse(Console.ReadLine());
for (int i = 1; i <= 10; i++)
{
    Console.WriteLine(n + " x " + i + " = " + (n * i));
}
```

Sem os parênteses em `(n * i)`, o `+` com texto juntaria os números como texto.

</details>

<details class="recall-box">
<summary>💻 Desafio 5 (10 min) — Soma até zero: leia números até o usuário digitar 0; mostre a soma, a quantidade de números digitados e a média.</summary>

```csharp in=4|8|6|0
int soma = 0, qtd = 0;
Console.Write("Número (0 para sair): ");
int n = int.Parse(Console.ReadLine());
while (n != 0)
{
    soma += n;
    qtd++;
    Console.Write("Número (0 para sair): ");
    n = int.Parse(Console.ReadLine());
}
Console.WriteLine("Soma: " + soma);
Console.WriteLine("Quantidade: " + qtd);
if (qtd > 0)
    Console.WriteLine("Média: " + (double)soma / qtd);   // (double) evita a divisão inteira
```

Com 4, 8, 6 e 0: `Soma: 18`, `Quantidade: 3`, `Média: 6`.

O `(double)` antes de `soma` converte para decimal; sem ele, 19 / 3 daria 6 em vez de 6,33.

</details>

<details class="recall-box">
<summary>💻 Desafio 6 (10 min) — Pares e ímpares: leia N e, de 1 até N, conte quantos são pares e some os ímpares.</summary>

```csharp in=10
Console.Write("N: ");
int n = int.Parse(Console.ReadLine());
int pares = 0, somaImpares = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 2 == 0)
        pares++;
    else
        somaImpares += i;
}
Console.WriteLine("Pares: " + pares);
Console.WriteLine("Soma dos ímpares: " + somaImpares);
```

Com N = 10: `Pares: 5` e `Soma dos ímpares: 25` (1 + 3 + 5 + 7 + 9).

</details>

<details class="recall-box">
<summary>💻 Desafio 7 (15 min) — Notas da turma (vetor): leia 5 notas num vetor; mostre a média, a maior, a menor e quantas ficaram acima da média.</summary>

```csharp in=8|5|9|6|7
double[] notas = new double[5];
double soma = 0;
for (int i = 0; i < notas.Length; i++)
{
    Console.Write($"Nota {i + 1}: ");
    notas[i] = double.Parse(Console.ReadLine());
    soma += notas[i];
}

double media = soma / notas.Length;
double maior = notas[0], menor = notas[0];
int acima = 0;
for (int i = 0; i < notas.Length; i++)
{
    if (notas[i] > maior) maior = notas[i];
    if (notas[i] < menor) menor = notas[i];
    if (notas[i] > media) acima++;
}

Console.WriteLine("Média: " + media);
Console.WriteLine("Maior: " + maior + " | Menor: " + menor);
Console.WriteLine("Acima da média: " + acima);
```

Com 8, 5, 9, 6, 7: média 7, maior 9, menor 5, acima da média: 2 (o 8 e o 9).

Dois laços: o primeiro **lê e soma**; o segundo precisa da média **pronta** para contar quem ficou acima.

</details>

<details class="recall-box">
<summary>💻 Desafio 8 (10 min) — Menu com do/while: mostre "1 - Somar 2 - Dobrar 0 - Sair"; repita até a opção 0.</summary>

```csharp in=2|5|1|3|4|0
int op;
do
{
    Console.WriteLine("1 - Somar  2 - Dobrar  0 - Sair");
    op = int.Parse(Console.ReadLine());
    if (op == 1)
    {
        Console.Write("a: "); int a = int.Parse(Console.ReadLine());
        Console.Write("b: "); int b = int.Parse(Console.ReadLine());
        Console.WriteLine("Soma: " + (a + b));
    }
    else if (op == 2)
    {
        Console.Write("Número: "); int x = int.Parse(Console.ReadLine());
        Console.WriteLine("Dobro: " + (x * 2));
    }
} while (op != 0);
Console.WriteLine("Fim");
```

Por que **do/while**: o menu precisa aparecer **pelo menos uma vez**.

</details>

<details class="recall-box">
<summary>💻 Desafio 9 (15 min) — Entrada à prova de erro: leia a idade com try/catch, repetindo até ser um inteiro entre 0 e 120.</summary>

```csharp in=abc|200|16
int idade = -1;
while (idade < 0 || idade > 120)
{
    Console.Write("Idade: ");
    try
    {
        idade = int.Parse(Console.ReadLine());
        if (idade < 0 || idade > 120)
            Console.WriteLine("Idade fora do intervalo.");
    }
    catch (FormatException)
    {
        Console.WriteLine("Digite apenas números.");
        idade = -1;
    }
}
Console.WriteLine("Idade registrada: " + idade);
```

Digitando `abc`, `200` e `16`: "Digite apenas números.", "Idade fora do intervalo." e "Idade registrada: 16".

</details>

<details class="recall-box">
<summary>💻 Desafio 10 (15 min) — Matriz 3x3: preencha uma matriz com os valores de 1 a 9 (linha por linha), mostre-a em formato de tabela e calcule a soma da diagonal principal.</summary>

```csharp
int[,] m = new int[3, 3];
int valor = 1;
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        m[i, j] = valor++;          // usa o valor e depois soma 1

int diagonal = 0;
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
        Console.Write(m[i, j] + "\t");   // \t = tabulação
    Console.WriteLine();
    diagonal += m[i, i];                 // diagonal principal: linha == coluna
}
Console.WriteLine("Soma da diagonal: " + diagonal);
```

Saída: as linhas `1 2 3`, `4 5 6`, `7 8 9` e `Soma da diagonal: 15` (1 + 5 + 9).

</details>

### 5. Explicando o seu programa

Se o professor pedir para você explicar, use o vocabulário certo:

- "Declarei uma **variável** do tipo **int** chamada idade e **converti** o texto digitado com **int.Parse**."
- "Usei uma **estrutura de decisão** `if/else` para…"
- "Usei um **laço for** porque eu sabia quantas vezes ia repetir; usei **while** quando não sabia."
- "A variável `soma` é um **acumulador**, que começa em zero."
- "O **vetor** guarda as 5 notas; o índice vai de **0 a 4**."
- "Usei **try/catch** para o programa não fechar se a pessoa digitar letras."
- "Se der erro, eu leio a **lista de erros**, vejo a **linha** e corrijo. Também posso colocar um **breakpoint** para ver os valores."

### ✅ Resumo de 1 minuto

- Visual Studio: **Criar projeto → Aplicativo de Console (C#)** → escreva no `Main` → **Ctrl + F5**.
- Erros: **CS1002** (falta `;`), **CS0103** (nome não existe), **CS0029** (texto em variável int), **FormatException** (digitou letra).
- Decimal: **ponto no código**, **vírgula ao digitar** num Windows em português.
- Moldes: ler e decidir (`if`/`switch`), repetir (`for` com quantidade conhecida, `while` até um valor, `do/while` para menu), acumular (`soma += x`), vetor (`for` de 0 a `Length - 1`), validar (`try/catch` + `if`).
- Explique com o vocabulário da matéria: variável, tipo, conversão, decisão, laço, acumulador, vetor, exceção.
