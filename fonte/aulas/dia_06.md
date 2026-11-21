## Dia 6 (26/11) — Banco de Dados I: tabelas, chaves, DER, normalização e SQL

Todo sistema que você usa guarda dados em algum lugar: sua conta do Discord, seu inventário no jogo, suas notas na escola. Esse lugar é um **banco de dados**. Na prova de Taboão, Banco de Dados aparece **todo ano** (de 2 a 4 questões, quase sempre conceitos diretos: tabela, registro, chave primária, chave estrangeira, DER, dicionário de dados, normalização). E no laboratório, modelar umas tabelinhas e escrever SQL é uma tarefa bem provável.

### 1. Dado, informação, banco e SGBD

- **Dado**: um valor solto, sem contexto. `16`, `"Henrique"`, `8.5`.
- **Informação**: dado **com significado**. "Henrique tem 16 anos e tirou 8,5 em Matemática."
- **Banco de dados**: um conjunto **organizado** de dados relacionados, guardado de forma que dê para **consultar, inserir, alterar e apagar** com facilidade.
- **SGBD** (*Sistema Gerenciador de Banco de Dados*): o **programa** que cuida do banco — guarda, protege, controla quem acessa. Exemplos: **MySQL**, **SQL Server**, **PostgreSQL**, **Oracle**, **SQLite**.

Por que não usar só uma planilha do Excel? Porque um banco **aguenta milhões de registros**, deixa **várias pessoas usarem ao mesmo tempo**, **impede dados inconsistentes** (como um pedido de um cliente que não existe) e é consultado por programas com a linguagem **SQL**.

### 2. Tabela, registro e campo

No modelo mais usado (o **relacional**), os dados ficam em **tabelas**, parecidas com planilhas:

**Tabela `aluno`**

| ra | nome | data_nasc | cidade |
|---|---|---|---|
| 101 | Ana Souza | 2009-03-14 | Taboão da Serra |
| 102 | Bruno Lima | 2010-07-02 | Embu das Artes |
| 103 | Carla Dias | 2009-11-25 | São Paulo |

| Termo | O que é | No exemplo | Outros nomes |
|---|---|---|---|
| **Tabela** | conjunto de dados sobre **um mesmo assunto** | a tabela `aluno` | entidade (no DER), relação |
| **Registro** | **uma linha** completa, com os dados de **um item** | `102, Bruno Lima, 2010-07-02, Embu das Artes` | linha, tupla |
| **Campo** | **uma coluna**: um tipo de informação | `nome` | coluna, atributo |

> [!WARNING]
> **🔁 Já caiu — dez/2025 (questões 38, 39 e 40):**
> - "Qual situação representa o conceito de **tabela**?" → "uma lista de alunos com suas matrículas, nomes e notas".
> - "Um **registro** pode ser comparado a:" → "uma linha completa com informações sobre um item específico".
> - "Procurar um contato na lista do celular é similar a:" → "**consultar** um banco de dados".

**Tipos de dados** — cada campo tem um tipo, como as variáveis em C#:

| Tipo SQL | Guarda | Exemplo |
|---|---|---|
| `INT` | número inteiro | `ra INT` |
| `DECIMAL(5,2)` | número com casas decimais (5 dígitos, 2 depois da vírgula) | `preco DECIMAL(5,2)` → até 999.99 |
| `VARCHAR(n)` | texto de **até** n caracteres | `nome VARCHAR(80)` |
| `CHAR(n)` | texto de **exatamente** n caracteres | `uf CHAR(2)` → `SP` |
| `DATE` | data (ano-mês-dia) | `data_nasc DATE` |

### 3. Chave primária (PK)

Se dois alunos se chamam "Ana Souza", como o sistema sabe de qual você está falando? Cada tabela precisa de um campo que **identifique cada registro de forma única**: a **chave primária** (*primary key*, **PK**).

Duas regras da chave primária:

1. **Não pode repetir** (dois alunos não podem ter o mesmo RA).
2. **Não pode ficar vazia** (`NOT NULL`).

Bons exemplos de PK: RA do aluno, CPF, código do produto, número do pedido. Péssimos exemplos: nome (repete), idade (repete), cidade.

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 38):** "O que caracteriza uma chave primária?" → "**ela identifica unicamente cada registro**". As erradas: "permite valores repetidos", "aceita nulos", "relaciona duas tabelas" (isso é a **estrangeira**).

Termos que podem aparecer: **chave candidata** = todo campo que **poderia** ser a PK (RA e CPF, por exemplo); **chave composta** = PK formada por **dois ou mais** campos juntos.

### 4. Chave estrangeira (FK) e integridade referencial

Um aluno faz várias matrículas em disciplinas. Em vez de repetir o nome e a cidade do aluno em cada matrícula, a tabela `matricula` guarda **só o RA** — que aponta para a tabela `aluno`:

**Tabela `matricula`**

| id_matricula | ra_aluno | disciplina | ano |
|---|---|---|---|
| 1 | 101 | Programação | 2026 |
| 2 | 101 | Banco de Dados | 2026 |
| 3 | 103 | Programação | 2026 |

O campo `ra_aluno` é uma **chave estrangeira** (*foreign key*, **FK**): um campo de uma tabela que guarda o valor da **chave primária de outra tabela** (ou da mesma), criando a **ligação** entre elas.

```text
  aluno                              matricula
┌──────────┐                       ┌──────────────┐
│ ra (PK)  │◄──────────────────────│ ra_aluno (FK)│
│ nome     │   "1 aluno tem        │ id_matricula │
│ cidade   │    N matrículas"      │ disciplina   │
└──────────┘                       └──────────────┘
```

**Integridade referencial** = toda referência tem que apontar para algo que **existe**. O SGBD, por causa da FK, **não deixa**:

- criar uma matrícula com `ra_aluno = 999` se não existe aluno 999;
- apagar o aluno 101 enquanto ainda existirem matrículas dele.

> [!WARNING]
> **🔁 Já caiu:**
> - **2021 (questão 37):** "Uma chave estrangeira pode ser definida como: **um campo que aponta para a chave primária de outra tabela ou da mesma tabela**".
> - **dez/2023 (questão 32):** "No modelo relacional, a integridade referencial é garantida pela: **chave estrangeira**". (A chave **primária** garante a integridade **de entidade** — cada linha ser única.)

### 5. Os três modelos: conceitual, lógico e físico

Projetar um banco é como construir uma casa: primeiro o **desenho da ideia**, depois a **planta técnica**, depois a **obra**.

| Modelo | É | Feito com | Exemplo |
|---|---|---|---|
| **Conceitual** | o desenho **abstrato** da realidade, sem pensar em computador | **DER** (retângulos, losangos, elipses) | "Aluno **cursa** Disciplina" |
| **Lógico** | a realidade organizada em **tabelas**, colunas e chaves, sem escolher o SGBD | tabelas com PK e FK | `aluno(ra PK, nome)`, `matricula(id PK, ra FK)` |
| **Físico** | o banco **de verdade**, num SGBD específico | comandos **SQL** | `CREATE TABLE aluno (...)` no MySQL |

> [!WARNING]
> **🔁 Já caiu — dez/2023 (questão 31):** "A fase do projeto de banco de dados em que criamos um **modelo abstrato da realidade** é:" → **modelo conceitual**.

### 6. O DER: desenhando o modelo conceitual

O **DER** (*Diagrama Entidade-Relacionamento*), criado por Peter Chen, usa três formas:

| Forma | Representa | Exemplo |
|---|---|---|
| ▭ **retângulo** | **entidade** — uma "coisa" do mundo real sobre a qual guardamos dados | Aluno, Livro, Produto |
| ◯ **elipse** | **atributo** — uma característica da entidade (sublinhado = identificador/PK) | <u>ra</u>, nome |
| ◇ **losango** | **relacionamento** — a ligação entre entidades (um verbo) | "cursa", "faz", "pertence" |

```text
   (ra)   (nome)                         (codigo)  (titulo)
      \    /                                 \       /
   ┌─────────┐   1     ◇ empresta ◇    N   ┌──────────┐
   │  ALUNO  │─────────────────────────────│  LIVRO   │
   └─────────┘                             └──────────┘
```

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 40):** "Em um modelo ER, o que é uma entidade?" → "**um objeto do mundo real que pode ser identificado**".

**Cardinalidade** — **quantos** de um lado se ligam a **quantos** do outro:

| Cardinalidade | Significa | Exemplo | Como vira tabela |
|---|---|---|---|
| **1:1** | um para um | 1 pessoa tem 1 CPF | a FK vai em qualquer um dos lados |
| **1:N** | um para muitos | 1 cliente faz N pedidos (cada pedido é de 1 cliente) | a **FK vai no lado N** (`pedido.id_cliente`) |
| **N:N** | muitos para muitos | N alunos cursam N disciplinas | cria uma **terceira tabela** (associativa) com as duas FKs |

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 39):** "Um relacionamento de cardinalidade **1:N** significa que: **uma entidade A pode se relacionar com muitas entidades B**".

**O caso N:N** — um aluno cursa várias disciplinas e uma disciplina tem vários alunos. Não dá para colocar a FK em nenhum dos dois lados sem repetir dados. A solução é uma **tabela no meio**:

```text
 aluno                cursa (tabela associativa)          disciplina
┌───────────┐       ┌─────────────────────────────┐      ┌───────────────┐
│ ra (PK)   │◄──────│ ra (FK)            ┐ PK      │─────►│ id_disc (PK)  │
│ nome      │       │ id_disc (FK)       ┘ composta│      │ nome          │
└───────────┘       │ nota                         │      └───────────────┘
                    └─────────────────────────────┘
```

### 7. Dicionário de dados

O **dicionário de dados** é um documento que **descreve cada campo** do banco: nome, tipo, tamanho, se é obrigatório, se é chave e o que significa. É o "manual" do banco para quem vai usá-lo.

**Dicionário da tabela `aluno`:**

| Campo | Tipo | Tamanho | Obrigatório | Chave | Descrição |
|---|---|---|---|---|---|
| ra | INT | — | sim | PK | Registro do aluno |
| nome | VARCHAR | 80 | sim | | Nome completo |
| data_nasc | DATE | — | não | | Data de nascimento |
| cidade | VARCHAR | 50 | não | | Cidade onde mora |

> [!WARNING]
> **🔁 Já caiu — 2022 (questão 32), com a mesma frase em outra prova recente:** "Um dicionário de dados é uma coleção de **nomes, atributos** e definições sobre elementos de **dados** que estão sendo usados em seu estudo." Decore a frase: **nomes, atributos … dados**.

### 8. Normalização: arrumando a bagunça

**Normalizar** é reorganizar as tabelas para **evitar redundância** (o mesmo dado repetido à toa) e **anomalias** (erros ao inserir, alterar ou apagar).

Veja esta tabela mal feita:

| ra | nome | telefones | curso | coordenador_curso |
|---|---|---|---|---|
| 101 | Ana | 1199991111, 1198882222 | DS | Prof. Marcos |
| 102 | Bruno | 1197773333 | DS | Prof. Marcos |
| 103 | Carla | 1196664444 | Informática | Profa. Lúcia |

Problemas:

- Dois telefones **na mesma célula** → difícil buscar "quem tem o telefone X".
- "Prof. Marcos" **repetido** em todo aluno de DS. Se o coordenador mudar, é preciso alterar dezenas de linhas — e se esquecer uma, o banco fica **inconsistente** (anomalia de alteração).
- Se o último aluno de Informática sair, a informação de quem coordena Informática **some junto** (anomalia de exclusão).

As **formas normais** (FN) são as regras para consertar:

| Forma | Regra (bem simplificada) | No exemplo |
|---|---|---|
| **1FN** | cada célula guarda **um valor só** (valor **atômico**), sem listas nem grupos repetidos | tirar os dois telefones da mesma célula → tabela `telefone(ra, numero)` |
| **2FN** | estar na 1FN e todo campo depender da **chave inteira** (importa quando a chave é composta) | em `cursa(ra, id_disc, nota, nome_aluno)`, o `nome_aluno` depende só do `ra` → sai dali |
| **3FN** | estar na 2FN e nenhum campo depender de **outro campo que não é chave** | `coordenador_curso` depende de `curso`, não do aluno → criar a tabela `curso(curso, coordenador)` |

Resultado normalizado:

```text
aluno(ra PK, nome, curso FK)
telefone(ra FK, numero)            ← 1FN
curso(curso PK, coordenador)       ← 3FN
```

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 37):** "A normalização tem como objetivo principal: **evitar redundância e anomalias nos dados**". Aumentar o número de tabelas é **consequência**, não objetivo.

### 9. SQL: conversando com o banco

**SQL** (*Structured Query Language*) é a linguagem para criar e usar bancos. Os comandos se dividem em grupos:

| Grupo | Significa | Comandos | Faz |
|---|---|---|---|
| **DDL** | *Data **Definition** Language* | `CREATE`, `ALTER`, `DROP` | cria, altera e apaga a **estrutura** (tabelas) |
| **DML** | *Data **Manipulation** Language* | `INSERT`, `UPDATE`, `DELETE` | mexe nos **dados** (linhas) |
| **DQL** | *Data **Query** Language* | `SELECT` | **consulta** os dados |
| **DCL** | *Data **Control** Language* | `GRANT`, `REVOKE` | dá e tira **permissões** |

Também se fala em **CRUD**: **C**reate (`INSERT`), **R**ead (`SELECT`), **U**pdate (`UPDATE`), **D**elete (`DELETE`) — as quatro operações básicas de qualquer sistema.

**Criando as tabelas (DDL):**

```sql
CREATE TABLE aluno (
    ra INT PRIMARY KEY,               -- chave primária
    nome VARCHAR(80) NOT NULL,        -- obrigatório
    cidade VARCHAR(50)
);

CREATE TABLE matricula (
    id_matricula INT PRIMARY KEY,
    ra_aluno INT NOT NULL,
    disciplina VARCHAR(50) NOT NULL,
    nota DECIMAL(4,2),
    FOREIGN KEY (ra_aluno) REFERENCES aluno(ra)   -- chave estrangeira
);
```

Comentários em SQL começam com `--`. Cada comando termina com `;`.

**Inserindo dados (DML):**

```sql
INSERT INTO aluno (ra, nome, cidade) VALUES (101, 'Ana Souza', 'Taboão da Serra');
INSERT INTO aluno (ra, nome, cidade) VALUES (102, 'Bruno Lima', 'Embu das Artes');
INSERT INTO aluno (ra, nome, cidade) VALUES (103, 'Carla Dias', 'Taboão da Serra');

INSERT INTO matricula VALUES (1, 101, 'Programação', 8.5);
INSERT INTO matricula VALUES (2, 101, 'Banco de Dados', 6.0);
INSERT INTO matricula VALUES (3, 103, 'Programação', 9.5);
```

Texto vai entre **aspas simples** em SQL (`'Ana'`).

**Consultando (DQL) — o `SELECT`:**

```sql
SELECT nome, cidade FROM aluno;                          -- colunas escolhidas, todas as linhas
SELECT * FROM aluno WHERE cidade = 'Taboão da Serra';    -- * = todas as colunas; WHERE = filtro
SELECT * FROM matricula WHERE nota >= 7 ORDER BY nota DESC;   -- ordena da maior para a menor
SELECT COUNT(*) FROM aluno;                              -- quantos alunos existem
```

Lendo o `SELECT` em português: "**SELECIONE** estas colunas **DE** tal tabela **ONDE** esta condição for verdadeira, **ORDENADO POR** tal campo".

A segunda consulta devolve:

| ra | nome | cidade |
|---|---|---|
| 101 | Ana Souza | Taboão da Serra |
| 103 | Carla Dias | Taboão da Serra |

**Alterando e apagando (DML):**

```sql
UPDATE matricula SET nota = 7.0 WHERE id_matricula = 2;   -- muda a nota da matrícula 2
DELETE FROM matricula WHERE id_matricula = 3;             -- apaga a matrícula 3
```

> [!CAUTION]
> **Nunca esqueça o `WHERE` no `UPDATE` e no `DELETE`.** `DELETE FROM matricula;` sem WHERE apaga **todas** as linhas da tabela. `UPDATE matricula SET nota = 0;` zera a nota de **todo mundo**.

**Juntando duas tabelas (bônus que ajuda no laboratório):**

```sql
SELECT aluno.nome, matricula.disciplina, matricula.nota
FROM aluno
JOIN matricula ON matricula.ra_aluno = aluno.ra;
```

O `JOIN … ON` liga as linhas em que a FK (`ra_aluno`) bate com a PK (`ra`).

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Escolher o nome como chave primária** — nomes se repetem.
> - **Colocar a FK do lado errado** num 1:N — ela vai no lado **N** (o pedido guarda o cliente, não o contrário).
> - **Tentar resolver N:N sem tabela associativa.**
> - **Confundir registro (linha) com campo (coluna).**
> - **Confundir DDL com DML**: `CREATE/ALTER/DROP` mexem na **estrutura**; `INSERT/UPDATE/DELETE`, nos **dados**.
> - **`DELETE`/`UPDATE` sem `WHERE`.**
> - **Texto sem aspas simples** no SQL: `WHERE nome = Ana` dá erro; o certo é `WHERE nome = 'Ana'`.
> - **Guardar listas numa célula** (vários telefones juntos) — quebra a 1FN.

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Na tabela produto(codigo, nome, preco), "345, Mouse gamer, 89.90" é um(a): (A) campo (B) tabela (C) registro (D) chave estrangeira (E) atributo</summary>

**C — registro** (uma linha completa sobre um item).

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Qual campo é a melhor chave primária para a tabela cliente(cpf, nome, telefone, cidade)?</summary>

**cpf** — único para cada pessoa e sempre preenchido. Nome e cidade repetem; telefone pode mudar ou faltar.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — Uma loja: 1 cliente faz vários pedidos; cada pedido é de 1 cliente. Qual a cardinalidade e onde fica a FK?</summary>

**1:N**. A FK fica na tabela do lado **N**: `pedido(id_pedido PK, data, id_cliente FK)`.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Um jogador participa de vários campeonatos e cada campeonato tem vários jogadores. Como fica o modelo lógico?</summary>

É **N:N** → três tabelas:

```text
jogador(id_jogador PK, nick)
campeonato(id_camp PK, nome)
inscricao(id_jogador FK, id_camp FK, data_inscricao)   ← PK composta (id_jogador, id_camp)
```

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Classifique em DDL, DML ou DQL: (a) CREATE TABLE (b) INSERT INTO (c) SELECT (d) DROP TABLE (e) UPDATE</summary>

(a) DDL · (b) DML · (c) DQL · (d) DDL · (e) DML.

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — A tabela venda(id, cliente, itens) guarda em "itens" o texto "teclado, mouse, monitor". Qual forma normal ela fere?</summary>

A **1FN**: a célula tem **vários valores** (não atômica). Solução: uma tabela `item_venda(id_venda FK, produto)` com um produto por linha.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Escreva o SQL que mostra o nome dos alunos de Embu das Artes em ordem alfabética.</summary>

```sql
SELECT nome FROM aluno WHERE cidade = 'Embu das Artes' ORDER BY nome;
```

(`ORDER BY` sem nada é crescente — de A a Z. `DESC` inverte.)

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — Qual modelo é desenhado com retângulos, losangos e elipses, sem pensar em qual SGBD será usado? (A) físico (B) lógico (C) conceitual (D) relacional (E) descritivo</summary>

**C — conceitual** (o DER).

</details>

### 🖥️ Mão na massa (40 minutos)

Abra **sqliteonline.com** (funciona no celular e no PC, sem instalar; é SQLite, mas os comandos básicos são iguais aos do MySQL).

1. Copie (agora pode!) os dois `CREATE TABLE` e os `INSERT` da seção 9 e clique em **Run**.
2. Rode cada `SELECT` da seção 9 e confira os resultados.
3. **Sozinho:** escreva consultas para:
   - todas as matrículas de Programação;
   - as matrículas com nota **menor que 7**;
   - quantas matrículas o aluno 101 tem (`COUNT(*)` com `WHERE`).
4. Teste a integridade: tente `INSERT INTO matricula VALUES (9, 999, 'Física', 5);` (aluno 999 não existe). No SQLite, a checagem de FK só vale depois de rodar `PRAGMA foreign_keys = ON;` — no MySQL ela já vem ligada.
5. **Modelagem no papel — "Locadora de games":** um cliente aluga vários jogos; um jogo pode ser alugado por vários clientes em datas diferentes. Desenhe o DER (entidades, atributos, relacionamento e cardinalidade) e depois escreva as tabelas com PK e FK.

<details class="recall-box">
<summary>✅ Respostas do item 3 e um modelo para a locadora</summary>

```sql
SELECT * FROM matricula WHERE disciplina = 'Programação';
SELECT * FROM matricula WHERE nota < 7;
SELECT COUNT(*) FROM matricula WHERE ra_aluno = 101;
```

Resultados: 2 matrículas de Programação; 1 com nota menor que 7 (a de Banco de Dados, nota 6); o aluno 101 tem 2 matrículas.

**Locadora** (N:N entre cliente e jogo, com atributos no aluguel):

```text
CLIENTE (cpf, nome, telefone) ──N── ◇ aluga ◇ ──N── JOGO (codigo, titulo, plataforma)
                                       │
                               (data_aluguel, data_devolucao, valor)
```

```sql
CREATE TABLE cliente (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    telefone VARCHAR(15)
);
CREATE TABLE jogo (
    codigo INT PRIMARY KEY,
    titulo VARCHAR(80) NOT NULL,
    plataforma VARCHAR(20)
);
CREATE TABLE aluguel (
    id_aluguel INT PRIMARY KEY,
    cpf_cliente CHAR(11) NOT NULL,
    codigo_jogo INT NOT NULL,
    data_aluguel DATE NOT NULL,
    data_devolucao DATE,
    valor DECIMAL(6,2),
    FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf),
    FOREIGN KEY (codigo_jogo) REFERENCES jogo(codigo)
);
```

(Aqui usamos um `id_aluguel` como PK porque o mesmo cliente pode alugar o mesmo jogo mais de uma vez em datas diferentes.)

</details>

### ✅ Resumo de 1 minuto

- **Dado** (valor solto) × **informação** (com significado). **SGBD** = programa que gerencia o banco (MySQL, SQL Server…).
- **Tabela** = assunto; **registro** = **linha**; **campo** = **coluna**.
- **PK**: identifica cada registro; **não repete, não é nula**. **FK**: aponta para a PK de outra tabela; garante a **integridade referencial**.
- Modelos: **conceitual** (DER, abstrato) → **lógico** (tabelas e chaves) → **físico** (SQL no SGBD).
- DER: **entidade** = retângulo; **atributo** = elipse; **relacionamento** = losango.
- **1:N** → FK no lado N. **N:N** → tabela associativa com as duas FKs.
- **Dicionário de dados**: "coleção de **nomes, atributos** e definições sobre elementos de **dados**".
- **Normalização** evita **redundância e anomalias**. 1FN = valores atômicos; 3FN = nada depende de campo que não é chave.
- SQL: **DDL** (CREATE, ALTER, DROP), **DML** (INSERT, UPDATE, DELETE), **DQL** (SELECT). `WHERE` sempre no UPDATE/DELETE.
