---
id: prev_tec_b
titulo: Simulado de Previsão — Técnico B
data: 11/2026
curso: DS
gabarito: elaborado para a plataforma
---

## 1 | tpa | Breakpoint
Durante a depuração de um programa no Visual Studio, ao atingir um breakpoint, o programador pode:

A) apagar automaticamente as linhas que contêm erros.
B) pausar o programa apenas quando ocorrer uma exceção.
C) pausar a execução naquele ponto, inspecionar os valores das variáveis e avançar linha a linha.
D) acelerar a execução do programa.
E) corrigir automaticamente os erros de sintaxe.

> Resposta: C

**Breakpoint** = ponto de parada marcado numa linha (F9). Ao chegar ali, a execução **pausa** e dá para ver as variáveis e avançar com F10. Ele para **sempre** que a execução passa por aquela linha, não só em exceções (B). Caiu em dez/2025.

## 2 | tpa | Erro de sintaxe
Ao compilar um programa em C# em que falta o ponto e vírgula no final de uma instrução:

A) o compilador aponta o erro, indicando a linha, e o programa não é gerado nem executado.
B) o programa é executado normalmente, ignorando o erro.
C) o programa compila, mas não é executado.
D) o compilador corrige o erro automaticamente.
E) o programa executa até a linha do erro e depois para.

> Resposta: A

Erro de **sintaxe** impede a **compilação**: o compilador não gera o programa e mostra o erro (no Visual Studio, sublinhado em vermelho com a linha). Ele **não corrige sozinho**. Um programa que "roda até o erro e para" (E) é o que acontece numa **exceção** em tempo de execução.

## 3 | tpa | Índices de um vetor
Após a declaração `int[] v = new int[4];`, os índices válidos do vetor `v` são:

A) de 1 a 4.
B) de 0 a 4.
C) de 1 a 3.
D) de 0 a 5.
E) de 0 a 3.

> Resposta: E

O vetor tem **4 posições**, e o índice **começa em 0**: v[0], v[1], v[2], v[3]. Tentar acessar v[4] gera `IndexOutOfRangeException`.

## 4 | tpa | Algoritmo
Uma sequência finita e ordenada de passos, sem ambiguidade, para resolver um problema é chamada de:

A) logaritmo.
B) algoritmo.
C) compilador.
D) variável.
E) fluxo de dados.

> Resposta: B

Definição de **algoritmo** — caiu duas vezes em 2021 e em dez/2025. **Logaritmo** é uma operação matemática, e foi exatamente a pegadinha de 2021.

## 5 | tpa | Símbolo do fluxograma
Em um fluxograma, o símbolo em forma de **losango** representa:

A) o início e o fim do algoritmo.
B) a entrada de dados pelo teclado.
C) um cálculo ou atribuição.
D) uma decisão (condição com saídas Sim e Não).
E) um conector entre páginas.

> Resposta: D

Oval = início/fim; paralelogramo = entrada/saída; retângulo = processamento; **losango = decisão** (vira o `if` no código).

## 6 | tpa | Tabela verdade
Sabendo que A é verdadeiro e B é falso, qual das expressões resulta em **verdadeiro**?

A) A OU B
B) A E B
C) NÃO A
D) B E A
E) (NÃO A) OU B

> Resposta: A

**OU** basta **um** verdadeiro → V OU F = **V**. **E** exige os dois → V E F = F (B e D). NÃO A = F (C). (NÃO A) OU B = F OU F = F (E).

## 7 | tpa | Teste de mesa: else if no limite
O que o código exibe?

```csharp
double valor = 100;
if (valor > 100)
    Console.WriteLine("Frete grátis");
else if (valor >= 50)
    Console.WriteLine("Frete R$ 10");
else
    Console.WriteLine("Frete R$ 20");
```

A) Frete grátis
B) Frete R$ 20
C) Frete grátis e Frete R$ 10
D) Frete R$ 10
E) Nada é exibido

> Resposta: D

`100 > 100` é **falso** (maior, não maior ou igual) → testa o `else if`: `100 >= 50` é verdadeiro → **Frete R$ 10**. O `if / else if / else` escolhe **um** caminho só (C está errada). A pegadinha é o valor **exatamente no limite**.

## 8 | web | Tipo primitivo em JavaScript
Em JavaScript, a instrução `let ativo = true;` declara uma variável do tipo:

A) string
B) number
C) boolean
D) object
E) undefined

> Resposta: C

`true` e `false` são do tipo **boolean**. Se fosse `"true"` (com aspas), seria **string**. Tipos primitivos do JS: number, string, boolean, undefined, null.

## 9 | web | Seletor de id
Dado o elemento `<p id="destaque" class="aviso">Atenção</p>`, qual seletor CSS o seleciona **pelo id**?

A) `.destaque`
B) `destaque`
C) `p.destaque`
D) `*destaque`
E) `#destaque`

> Resposta: E

Id = **#**; classe = **ponto**. O seletor pela classe seria `.aviso`. `.destaque` (A) procuraria uma **classe** chamada destaque, que não existe aqui.

## 10 | web | Media query
A regra CSS `@media (max-width: 768px) { … }` significa que:

A) as regras valem apenas em telas maiores que 768 px.
B) as regras valem apenas em telas de até 768 px de largura.
C) a página fica limitada a 768 px de largura em qualquer tela.
D) uma imagem de 768 px será criada.
E) as regras valem apenas na impressão.

> Resposta: B

`max-width: 768px` = "**no máximo** 768 px" → celulares e tablets. É a base do layout **responsivo**, junto com a meta **viewport**.

## 11 | web | Elementos de bloco e em linha
Assinale a alternativa correta sobre HTML.

A) `<span>` é um elemento de bloco.
B) `<div>` é um elemento em linha (inline).
C) `<ol>` cria uma lista com marcadores (bolinhas).
D) `<body>` é o cabeçalho visível da página.
E) `<div>` é um elemento de bloco e `<span>`, um elemento em linha.

> Resposta: E

`div` = **bloco** (caiu em 2022); `span` = **em linha**. `<ol>` cria lista **numerada** (com marcadores é `<ul>`). `<body>` é o **corpo** da página; o cabeçalho visível é o `<header>`.

## 12 | bd | Primeira forma normal
A primeira forma normal (1FN) exige que:

A) toda tabela tenha uma chave estrangeira.
B) cada campo armazene um único valor (valor atômico).
C) não existam chaves primárias.
D) as tabelas tenham no máximo 10 colunas.
E) todos os campos sejam numéricos.

> Resposta: B

**1FN** = nada de listas ou vários valores numa mesma célula (como "telefones: 1199…, 1198…"). A normalização como um todo serve para **evitar redundância e anomalias**.

## 13 | bd | Formas do DER
No Diagrama Entidade-Relacionamento (notação de Peter Chen), entidades, relacionamentos e atributos são representados, respectivamente, por:

A) retângulos, losangos e elipses.
B) losangos, retângulos e elipses.
C) elipses, retângulos e losangos.
D) círculos, setas e quadrados.
E) tabelas, linhas e colunas.

> Resposta: A

**Entidade = retângulo** (Aluno), **relacionamento = losango** ("cursa"), **atributo = elipse** (nome). Tabelas, linhas e colunas (E) são do modelo **lógico/físico**, não do DER.

## 14 | bd | Dicionário de dados (questão que se repete)
Escolha a alternativa que complete adequadamente a afirmação: "Um dicionário de dados é uma coleção de ________, ________ e definições sobre elementos de ________ que estão sendo usados em seu estudo."

A) Objetos, atributos, entidades.
B) Características, dados, relacionamentos.
C) Relacionamentos, atributos, entidades.
D) Nomes, atributos, dados.
E) Tabelas, registros, sistemas.

> Resposta: D

Caiu com essa frase em 2022 e de novo numa prova recente. Decore: "coleção de **nomes, atributos** e definições sobre elementos de **dados**".

## 15 | bd | Comandos DML
São comandos SQL do grupo DML (manipulação de dados):

A) CREATE, ALTER e DROP.
B) GRANT e REVOKE.
C) INSERT, UPDATE e DELETE.
D) SELECT, apenas.
E) CREATE, INSERT e SELECT.

> Resposta: C

**DDL** (estrutura): CREATE, ALTER, DROP. **DML** (dados): **INSERT, UPDATE, DELETE**. **DQL** (consulta): SELECT. **DCL** (permissões): GRANT, REVOKE. E mistura grupos.

## 16 | aps | Modelo cascata (questão que se repete)
Escolha a alternativa que complete adequadamente a afirmação sobre o modelo cascata: "Sua principal característica é a divisão das tarefas em ________ predeterminadas, que são executadas de forma ________."

A) fases e evolutiva
B) blocos e contínua
C) sprints e iterativa
D) etapas e sequencial
E) sistemas e evolutiva

> Resposta: D

Cascata = **etapas** definidas antes, executadas de forma **sequencial** (uma após a outra). "Sprints" e "iterativa" (C) descrevem o **Scrum**; "evolutiva" descreve outro modelo. A versão linear/sequencial caiu também em dez/2025.

## 17 | aps | Multiplicidade no diagrama de classes
Em um diagrama de classes, a associação entre Cliente e Pedido tem multiplicidade **1** do lado do Cliente e **0..\*** do lado do Pedido. Isso indica que:

A) cada pedido pode ter vários clientes.
B) Cliente é um atributo de Pedido.
C) a classe Pedido herda da classe Cliente.
D) um cliente tem exatamente um pedido.
E) um cliente pode ter zero ou muitos pedidos, e cada pedido pertence a um cliente.

> Resposta: E

Leia cada número do lado da classe **que ele quantifica**: "um cliente tem **0..\*** (zero ou muitos) pedidos"; "um pedido tem **1** cliente". Herança (C) é outro tipo de ligação (seta com triângulo).

## 18 | design | RGB e CMYK
Uma arte que será impressa em gráfica deve ser preparada no modo de cor ________; uma arte para um site, no modo ________.

A) CMYK; RGB
B) RGB; CMYK
C) RGB; RGB
D) CMYK; CMYK
E) HEX; CMYK

> Resposta: A

**Papel/tinta → CMYK** (subtrativo). **Tela/luz → RGB** (aditivo). Hexadecimal (`#FF0000`) é só uma forma de **escrever** cores RGB.

## 19 | fund | Sistema multiusuário
Um servidor em que vários usuários se conectam ao mesmo tempo, cada um com suas aplicações e permissões, é um sistema:

A) monotarefa.
B) monousuário.
C) multiusuário.
D) de linha de comando única.
E) embarcado.

> Resposta: C

**Multiusuário** = várias **pessoas** no mesmo sistema ao mesmo tempo. **Multitarefa** = vários **programas** rodando ao mesmo tempo. Já caiu em prova de Taboão.

## 20 | fund | Software livre
Sobre software livre, é correto afirmar que:

A) é sempre gratuito.
B) permite estudar, modificar e distribuir o código-fonte, podendo ser gratuito ou pago.
C) é proibido modificar o seu código.
D) é o mesmo que freeware.
E) só funciona no sistema Linux.

> Resposta: B

**Livre** = liberdade (código aberto: estudar, modificar, distribuir), **não necessariamente grátis**. Freeware é grátis, mas geralmente com código **fechado** (WhatsApp, Discord). Caiu em 2022.
