---
id: prev_tec_a
titulo: Simulado de Previsão — Técnico A
data: 11/2026
curso: DS
gabarito: elaborado para a plataforma
---

## 1 | fund | Decimal para hexadecimal (variação do 187)
Calcule e responda: qual número hexadecimal corresponde ao número decimal 172?

A) BC
B) AC
C) CA
D) 9C
E) AB

> Resposta: B

172 ÷ 16 = **10** (160), resto **12**. Em hexadecimal, 10 = **A** e 12 = **C** → **AC**. Conferindo: 10 × 16 + 12 = 172 ✔. A pegadinha C (CA) inverte a ordem: o primeiro dígito é o **quociente**, o segundo é o **resto**. Esta é uma variação da questão do 187 (= BB), que caiu duas vezes.

## 2 | fund | Interface CLI (questão que se repete)
O que caracteriza uma interface CLI?

A) Interface multiusuário por linha de comando
B) Interface monotarefa com interface gráfica
C) Interface multitarefa por linha de comando
D) Interface monotarefa por linha de comando
E) Interface compartilhada por linha de comando

> Resposta: D

Caiu igual em dez/2024 e dez/2025, só com as alternativas em outra ordem. **CLI = Command Line Interface** → **linha de comando**, e a banca de Taboão a chama de **monotarefa**. Procure as duas palavras juntas: **monotarefa + linha de comando**.

## 3 | fund | Decimal para binário
Qual é a representação binária do número decimal 150?

A) 10010110
B) 10100110
C) 10010101
D) 11010010
E) 10110010

> Resposta: A

Pelas casas (128, 64, 32, 16, 8, 4, 2, 1): 150 − 128 = 22 → 22 − 16 = 6 → 6 − 4 = 2 → 2 − 2 = 0. Ligadas: 128, 16, 4, 2 → **1 0 0 1 0 1 1 0**.

Atalho: 150 é **par**, então o binário termina em **0** — isso já elimina a C. Conferindo as outras: B = 166, D = 210, E = 178.

## 4 | web | Tags HTML em sequência
Assinale a alternativa que apresenta, respectivamente, as tags de lista não ordenada, item de lista, quebra de linha, imagem e link.

A) `<ol>`, `<li>`, `<hr>`, `<img>`, `<a>`
B) `<ul>`, `<li>`, `<br>`, `<img>`, `<link>`
C) `<ul>`, `<il>`, `<br>`, `<image>`, `<a>`
D) `<ol>`, `<li>`, `<br>`, `<img>`, `<a>`
E) `<ul>`, `<li>`, `<br>`, `<img>`, `<a>`

> Resposta: E

Mesmo formato da questão de dez/2025 ("parágrafo, linha horizontal, título, pular linha e corpo"). Confira **uma por uma**: lista **não ordenada** = `<ul>` (A e D usam `<ol>`, que é numerada); item = `<li>` (C inverte para `<il>`); quebra de linha = `<br>` (A usa `<hr>`, que é linha horizontal); imagem = `<img>`; link clicável = `<a>` (B usa `<link>`, que serve para ligar o CSS).

## 5 | web | DNS, HTTPS e SMTP
Analise as afirmações:

I. O DNS traduz nomes de domínio, como etects.com.br, em endereços IP.<br>
II. O HTTPS é a versão segura do HTTP, com os dados criptografados.<br>
III. O SMTP é o protocolo usado para receber e-mails no celular.

Está correto o que se afirma em:

A) I, apenas.
B) III, apenas.
C) I e II, apenas.
D) II e III, apenas.
E) I, II e III.

> Resposta: C

I ✔ (DNS = "lista telefônica" da internet). II ✔ (o S de HTTPS = *secure*). III ✗: o **SMTP envia** e-mails; para **receber** usam-se **POP3** ou **IMAP**. Macete: **S**MTP = **S**end.

## 6 | web | Box model: espaço interno
Em CSS, a propriedade que define o espaço **entre o conteúdo e a borda** de um elemento é:

A) margin
B) border
C) padding
D) outline
E) spacing

> Resposta: C

**Padding** = espaço **interno** (entre o conteúdo e a borda). **Margin** = espaço **externo** (entre a borda e os vizinhos). Ordem do box model, de dentro para fora: conteúdo → padding → border → margin. `spacing` não existe no CSS.

## 7 | web | Centralizar com Flexbox
Qual combinação de propriedades CSS, aplicada a um contêiner, centraliza seus elementos filhos na horizontal **e** na vertical?

A) `display: flex; justify-content: center; align-items: center;`
B) `display: flex; justify-content: space-between;`
C) `display: block; text-align: center;`
D) `display: inline; margin: auto;`
E) `display: flex; align-content: left;`

> Resposta: A

A "receita" do Flexbox: `display: flex` liga o modo flex; `justify-content: center` centraliza no eixo principal (horizontal); `align-items: center` centraliza no eixo cruzado (vertical). B espalha os itens pelas pontas; C centraliza só texto.

## 8 | web | GET ou POST no login
Em um formulário de login, qual método de envio é o mais adequado e por quê?

A) GET, pois é o método padrão dos formulários.
B) GET, pois envia os dados mais rapidamente pela URL.
C) POST, pois mostra os dados na barra de endereço para conferência.
D) GET, pois não tem limite de tamanho.
E) POST, pois os dados vão no corpo da requisição e não aparecem na URL.

> Resposta: E

Senha **nunca** deve ir na URL (ficaria no histórico e na barra de endereço). No **POST**, os dados vão no **corpo** da requisição. A é verdadeira (GET é o padrão), mas não é motivo para usá-lo num login. C e D descrevem o GET ao contrário.

## 9 | tpa | Teste de mesa: while com %
Analise o código em C#:

```csharp
int n = 3;
int s = 0;
while (n <= 12)
{
    if (n % 3 == 0)
        s = s + n;
    n++;
}
Console.WriteLine(s);
```

O valor exibido é:

A) 12
B) 30
C) 21
D) 42
E) 33

> Resposta: B

O laço passa por n = 3, 4, …, 12 e soma só os **múltiplos de 3** (resto zero na divisão por 3): 3 + 6 + 9 + 12 = **30**. Quando n vira 13, a condição `n <= 12` fica falsa e o laço para. Quem esquece o 12 (achando que `<=` exclui o 12) chega a 18; quem soma o 15 chega a 45.

## 10 | tpa | Teste de mesa: for com passo negativo
O que o código abaixo exibe?

```csharp
for (int i = 10; i > 0; i -= 3)
{
    Console.Write(i + " ");
}
```

A) 10 7 4 1 -2
B) 7 4 1
C) 10 7 4
D) 10 7 4 1
E) 9 6 3 0

> Resposta: D

| i | i > 0? | mostra |
|---|---|---|
| 10 | sim | 10 |
| 7 | sim | 7 |
| 4 | sim | 4 |
| 1 | sim | 1 |
| −2 | **não** → sai | |

O primeiro valor exibido é o **inicial** (10) — o passo (`i -= 3`) só acontece depois do bloco. O −2 não aparece porque a condição é testada antes de mostrar.

## 11 | tpa | Matriz com índices trocados
Considere o código:

```csharp
int[,] m = { { 1, 2, 3 }, { 4, 5, 6 } };
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 2; j++)
    {
        Console.Write(m[j, i] + " ");
    }
    Console.WriteLine();
}
```

O que é exibido?

A) 1 2 3 em uma linha e 4 5 6 na outra
B) 1 4 2 5 3 6 em uma única linha
C) 4 1, depois 5 2, depois 6 3, cada par em uma linha
D) 1 4, depois 2 5, depois 3 6, cada par em uma linha
E) Erro: índice fora do intervalo da matriz

> Resposta: D

A matriz tem **2 linhas e 3 colunas**. O código usa **`m[j, i]`**: o laço de fora (`i`, de 0 a 2) percorre as **colunas**, e o de dentro (`j`, de 0 a 1) percorre as **linhas**. Para cada coluna, ele mostra os dois elementos dela e pula a linha:

- i = 0: m[0,0] = 1, m[1,0] = 4 → `1 4`
- i = 1: m[0,1] = 2, m[1,1] = 5 → `2 5`
- i = 2: m[0,2] = 3, m[1,2] = 6 → `3 6`

Não há erro de índice: `j` vai só até 1 (linhas) e `i` até 2 (colunas). Índices trocados são uma pegadinha clássica de Taboão: sempre confira qual variável está em cada posição do colchete.

## 12 | tpa | do/while executa ao menos uma vez
Qual valor é exibido?

```csharp
int x = 5;
do
{
    x = x + 2;
} while (x < 5);
Console.WriteLine(x);
```

A) 5
B) 9
C) Nada é exibido
D) Erro de compilação
E) 7

> Resposta: E

O `do … while` executa o bloco **antes** de testar: x passa de 5 para **7**. Depois testa `7 < 5` → falso → sai. Mostra **7**. Com um `while` comum, o bloco nunca rodaria e o resultado seria 5 (pegadinha A).

## 13 | tpa | Tratamento de exceções
Sobre o tratamento de exceções em C#, analise:

I. O bloco `catch` só é executado quando ocorre uma exceção dentro do bloco `try`.<br>
II. `int.Parse("12a")` gera uma exceção, pois o texto não representa um número inteiro.<br>
III. O `try/catch` corrige automaticamente o valor digitado errado pelo usuário.

Está correto o que se afirma em:

A) I, apenas.
B) I e II, apenas.
C) II e III, apenas.
D) III, apenas.
E) I, II e III.

> Resposta: B

I ✔ (sem erro no `try`, o `catch` é pulado). II ✔ (`FormatException`). III ✗: o `try/catch` **captura** o erro para o programa não fechar — quem decide o que fazer (avisar, pedir de novo) é o programador. Mesmo formato (I, II, III) da questão de exceções de dez/2025.

## 14 | tpa | Operadores lógicos: intervalo
Em C#, qual expressão é verdadeira **somente** quando a idade está entre 14 e 17 anos, incluindo 14 e 17?

A) `idade > 14 && idade < 17`
B) `idade >= 14 || idade <= 17`
C) `idade >= 14 && idade <= 17`
D) `idade => 14 && idade =< 17`
E) `14 <= idade <= 17`

> Resposta: C

"Entre" com os extremos incluídos = **as duas** condições (`&&`) com **≥** e **≤**. A exclui 14 e 17; B usa **OU** e fica verdadeira para qualquer idade; D escreve os operadores ao contrário (o certo é `>=` e `<=`); E funciona em matemática, mas não em C#.

## 15 | bd | Campo, registro e tabela
Em uma tabela de produtos de uma loja, a coluna "preço" corresponde a um(a):

A) campo (atributo).
B) registro.
C) tupla.
D) chave estrangeira.
E) tabela.

> Resposta: A

**Coluna = campo = atributo**. **Linha = registro = tupla** (os dados de **um** produto). Um preço não aponta para outra tabela, então não é chave estrangeira.

## 16 | bd | Integridade referencial
Ao tentar cadastrar um pedido para um cliente que não existe na tabela de clientes, o banco de dados recusa a operação. Isso acontece por causa da:

A) chave estrangeira, que garante a integridade referencial.
B) chave primária da tabela de pedidos, que garante a integridade referencial.
C) normalização, que impede pedidos repetidos.
D) dicionário de dados, que valida os nomes.
E) consulta SELECT, que verifica os clientes.

> Resposta: A

A **chave estrangeira** (`pedido.id_cliente → cliente.id`) obriga cada pedido a apontar para um cliente **existente**: isso é a **integridade referencial**. A chave **primária** garante outra coisa: que cada registro seja único (B). Caiu parecido em dez/2023.

## 17 | bd | Cardinalidade 1:N: onde fica a FK
Em um sistema, **um cliente pode fazer vários pedidos** e **cada pedido pertence a um único cliente**. No modelo lógico, a chave estrangeira deve ficar:

A) na tabela cliente.
B) nas duas tabelas.
C) na tabela pedido.
D) obrigatoriamente em uma terceira tabela.
E) em nenhuma tabela, pois relacionamentos 1:N não usam chave estrangeira.

> Resposta: C

No relacionamento **1:N**, a FK vai no **lado N** (o pedido guarda o cliente: `pedido.id_cliente`). Uma terceira tabela (D) só é necessária no **N:N**.

## 18 | aps | Requisito não funcional
Assinale a alternativa que apresenta um requisito **não funcional**:

A) O sistema deve emitir o boleto da mensalidade.
B) O sistema deve permitir o cadastro de alunos.
C) O sistema deve gerar o relatório de notas.
D) O sistema deve responder às consultas em até 2 segundos.
E) O sistema deve permitir que o aluno altere sua senha.

> Resposta: D

**Funcional** = uma **função** ("emitir", "cadastrar", "gerar", "alterar"). **Não funcional** = uma **qualidade** ou restrição: desempenho, segurança, usabilidade. "Responder em até 2 segundos" é **desempenho**.

## 19 | aps | Somente métodos ágeis
Assinale a alternativa que apresenta **somente** métodos ágeis.

A) Cascata, Scrum e XP
B) Espiral, Kanban e UML
C) Scrum, Cascata e Kanban
D) UML, XP e Scrum
E) Scrum, XP e Kanban

> Resposta: E

Ágeis: **Scrum, XP e Kanban**. Cascata e espiral são modelos tradicionais; **UML** é linguagem de modelagem, não é método. Basta **um** intruso para a alternativa estar errada.

## 20 | aps | Diagrama de casos de uso
No diagrama de casos de uso de um aplicativo de entregas, "Cliente" e "Entregador" são ________, e "Fazer pedido" é um ________.

A) classes; atributo
B) atores; caso de uso
C) entidades; relacionamento
D) casos de uso; ator
E) objetos; método

> Resposta: B

No caso de uso, quem **usa** o sistema é **ator** (bonequinho) e o que o sistema **faz** é **caso de uso** (elipse, com verbo). Classes, atributos e métodos são do **diagrama de classes**; entidades e relacionamentos são do **DER**.
