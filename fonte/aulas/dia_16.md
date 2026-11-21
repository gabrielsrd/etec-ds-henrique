## Dia 16 (07/12) — Laboratório 3: modelar um banco e escrever SQL — e ensaiar a entrevista

Último dia antes da 2ª fase. De manhã (ou na primeira metade do estudo): **banco de dados no papel e no computador**. Depois: **a entrevista**, em voz alta. Hoje também sai o **resultado da prova escrita** — veja no site da Etec (`etects.cps.sp.gov.br`) ou na secretaria.

## PARTE 1 — DO ENUNCIADO AO BANCO

### 1. O método em 6 passos

Diante de um enunciado como *"Uma biblioteca escolar quer controlar seus livros, os alunos e os empréstimos"*, siga sempre a mesma ordem:

1. **Sublinhe os substantivos importantes** → candidatos a **entidades** (tabelas): biblioteca, **livro**, **aluno**, **empréstimo**.
2. **Para cada entidade, liste os atributos** (as informações): aluno → ra, nome, turma; livro → código, título, autor.
3. **Escolha a chave primária** de cada uma (o atributo **único**): ra, código.
4. **Ache os verbos que ligam as entidades** → **relacionamentos**: "aluno **empresta** livro".
5. **Defina a cardinalidade** perguntando nos dois sentidos:
   - "Um aluno pode emprestar **quantos** livros?" → **vários**.
   - "Um livro pode ser emprestado por **quantos** alunos?" → **vários** (em datas diferentes).
   - Vários × vários = **N:N** → vira uma **tabela associativa** (`emprestimo`).
6. **Passe para tabelas com PK e FK** e escreva o **SQL**.

### 2. Caso resolvido: biblioteca escolar

**Modelo conceitual (DER):**

```text
   (ra) (nome) (turma)                         (codigo) (titulo) (autor)
        \  |  /                                      \    |    /
     ┌─────────┐ N        ◇ empresta ◇        N  ┌──────────┐
     │  ALUNO  │──────────────────────────────────│  LIVRO   │
     └─────────┘                │                 └──────────┘
                    (data_emprestimo) (data_devolucao)
```

Os atributos `data_emprestimo` e `data_devolucao` pertencem ao **relacionamento** (não são do aluno nem do livro).

**Modelo lógico:**

```text
aluno(ra PK, nome, turma)
livro(codigo PK, titulo, autor)
emprestimo(id_emprestimo PK, ra FK → aluno, codigo_livro FK → livro, data_emprestimo, data_devolucao)
```

**Modelo físico (SQL):**

```sql
CREATE TABLE aluno (
    ra INT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    turma VARCHAR(10)
);

CREATE TABLE livro (
    codigo INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(80)
);

CREATE TABLE emprestimo (
    id_emprestimo INT PRIMARY KEY,
    ra INT NOT NULL,
    codigo_livro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (ra) REFERENCES aluno(ra),
    FOREIGN KEY (codigo_livro) REFERENCES livro(codigo)
);

INSERT INTO aluno VALUES (1, 'Ana', '2A');
INSERT INTO aluno VALUES (2, 'Bruno', '2A');
INSERT INTO aluno VALUES (3, 'Carla', '2B');

INSERT INTO livro VALUES (10, 'Dom Casmurro', 'Machado de Assis');
INSERT INTO livro VALUES (11, 'O Cortiço', 'Aluísio Azevedo');
INSERT INTO livro VALUES (12, 'Capitães da Areia', 'Jorge Amado');

INSERT INTO emprestimo VALUES (100, 1, 10, '2026-11-03', '2026-11-10');
INSERT INTO emprestimo VALUES (101, 1, 12, '2026-11-20', NULL);
INSERT INTO emprestimo VALUES (102, 3, 11, '2026-11-21', NULL);
```

**Consultas que o professor pode pedir:**

```sql
-- 1. Todos os livros em ordem alfabética de título
SELECT * FROM livro ORDER BY titulo;

-- 2. Alunos da turma 2A
SELECT nome FROM aluno WHERE turma = '2A';

-- 3. Empréstimos ainda não devolvidos
SELECT * FROM emprestimo WHERE data_devolucao IS NULL;

-- 4. Quantos empréstimos cada aluno fez
SELECT ra, COUNT(*) AS total FROM emprestimo GROUP BY ra;

-- 5. Nome do aluno e título do livro de cada empréstimo (JOIN)
SELECT aluno.nome, livro.titulo, emprestimo.data_emprestimo
FROM emprestimo
JOIN aluno ON aluno.ra = emprestimo.ra
JOIN livro ON livro.codigo = emprestimo.codigo_livro;

-- 6. Registrar a devolução do empréstimo 101
UPDATE emprestimo SET data_devolucao = '2026-12-01' WHERE id_emprestimo = 101;
```

Resultados esperados (antes do UPDATE): a consulta 3 traz os empréstimos **101 e 102**; a 4 traz o aluno 1 com **2** empréstimos e o aluno 3 com **1**; a 5 traz Ana–Dom Casmurro, Ana–Capitães da Areia e Carla–O Cortiço.

> [!NOTE]
> Para testar se um campo está **vazio**, use **`IS NULL`** (não `= NULL`). `GROUP BY` agrupa as linhas para contar ou somar por grupo; `AS` dá um apelido à coluna.

### 3. Onde fazer no laboratório

- **MySQL Workbench** (se o laboratório tiver MySQL): conecte, crie o banco com `CREATE DATABASE biblioteca;` e `USE biblioteca;`, cole os comandos e execute com o **raio** (⚡) ou **Ctrl + Shift + Enter**.
- **brModelo** (para desenhar o DER): ferramenta brasileira e gratuita, muito usada em Etecs para o modelo conceitual e lógico.
- **sqliteonline.com** (para treinar em casa): funciona no navegador, sem instalar.
- **No papel:** desenhe o DER com régua (retângulos, losangos, elipses) e escreva as tabelas com PK sublinhada.

### 4. Desafios cronometrados

<details class="recall-box">
<summary>⏱️ Desafio 1 (15 min) — Pet shop: "O pet shop cadastra os donos (CPF, nome, telefone) e os animais (nome, espécie, raça). Cada animal tem um único dono; um dono pode ter vários animais." Faça o DER, o modelo lógico e o CREATE TABLE.</summary>

**Cardinalidade:** dono 1 — N animal (cada animal tem um dono; um dono, vários animais). A **FK vai no lado N** (animal).

```text
dono(cpf PK, nome, telefone)
animal(id_animal PK, nome, especie, raca, cpf_dono FK → dono)
```

```sql
CREATE TABLE dono (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    telefone VARCHAR(15)
);
CREATE TABLE animal (
    id_animal INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    especie VARCHAR(30),
    raca VARCHAR(30),
    cpf_dono CHAR(11) NOT NULL,
    FOREIGN KEY (cpf_dono) REFERENCES dono(cpf)
);
```

O animal ganhou um `id_animal` porque o nome não é único (pode haver vários "Thor").

</details>

<details class="recall-box">
<summary>⏱️ Desafio 2 (20 min) — Escola de cursos livres: "Alunos (RA, nome) se matriculam em cursos (código, nome, carga horária). Um aluno pode fazer vários cursos e um curso tem vários alunos. Na matrícula guardamos a data e a nota final." Modelo lógico + SQL + uma consulta com o nome do aluno, o nome do curso e a nota.</summary>

N:N → tabela associativa `matricula`, com os atributos do relacionamento (data e nota).

```sql
CREATE TABLE aluno (ra INT PRIMARY KEY, nome VARCHAR(80) NOT NULL);
CREATE TABLE curso (codigo INT PRIMARY KEY, nome VARCHAR(60) NOT NULL, carga_horaria INT);
CREATE TABLE matricula (
    ra INT,
    codigo_curso INT,
    data_matricula DATE,
    nota_final DECIMAL(4,2),
    PRIMARY KEY (ra, codigo_curso),
    FOREIGN KEY (ra) REFERENCES aluno(ra),
    FOREIGN KEY (codigo_curso) REFERENCES curso(codigo)
);

SELECT aluno.nome, curso.nome, matricula.nota_final
FROM matricula
JOIN aluno ON aluno.ra = matricula.ra
JOIN curso ON curso.codigo = matricula.codigo_curso;
```

Aqui a PK de `matricula` é **composta** (`ra` + `codigo_curso`): o mesmo aluno não pode se matricular duas vezes no mesmo curso.

</details>

<details class="recall-box">
<summary>⏱️ Desafio 3 (10 min) — Dicionário de dados da tabela animal do Desafio 1.</summary>

| Campo | Tipo | Tamanho | Obrigatório | Chave | Descrição |
|---|---|---|---|---|---|
| id_animal | INT | — | sim | PK | Código do animal |
| nome | VARCHAR | 50 | sim | | Nome do animal |
| especie | VARCHAR | 30 | não | | Cachorro, gato… |
| raca | VARCHAR | 30 | não | | Raça do animal |
| cpf_dono | CHAR | 11 | sim | FK → dono.cpf | Dono do animal |

</details>

## PARTE 2 — A ENTREVISTA

### 5. O que a entrevista quer saber

O edital diz que a entrevista individual serve para **"verificar a aderência do candidato à proposta curricular do Ensino Médio Integrado"**. E diz também que quem entrar vai fazer **atividades de adaptação** das matérias técnicas do 1º ano. Traduzindo, os professores querem saber:

1. **Você quer mesmo esse curso?** (interesse real por tecnologia, não "porque é de graça")
2. **Você aguenta o ritmo?** O M-Tec-**PI** é em **período integral**: Ensino Médio + Técnico.
3. **Você vai correr atrás do que perdeu do 1º ano técnico?** (as adaptações)
4. **Você entende o que fez na prática?** (perguntas técnicas sobre o seu código)

### 6. Como responder bem

- **Responda com a sua história verdadeira**, em 30 a 60 segundos por pergunta. Os modelos abaixo são **roteiros**: troque os colchetes `[…]` pelo que é **real** para você. Não decore frases prontas — professores percebem.
- **Dê exemplos concretos:** "eu instalo e configuro jogos e mods", "estudei por uma plataforma, fiz programas em C# e páginas em HTML".
- **Mostre o preparo:** você estudou **sozinho** HTML, CSS, C#, banco de dados — isso é exatamente a atitude que o curso precisa.
- **Admita o que não sabe e diga como aprenderia**: "ainda não vi isso a fundo, mas eu estudaria pelo material da disciplina e perguntaria ao professor".
- **Postura:** olhe para quem pergunta, fale com calma, sem pressa. Tudo bem pensar alguns segundos antes de responder.

### 7. As perguntas para ensaiar em voz alta

<details class="recall-box">
<summary>🎤 1. Por que você quer fazer Desenvolvimento de Sistemas na Etec?</summary>

**Roteiro:** o que te atrai em tecnologia (um exemplo real) → por que DS e não outro curso → por que a Etec (curso técnico junto com o médio, qualidade, oportunidade de estágio).

*Exemplo de estrutura:* "Eu sempre gostei de [jogos / computador / montar e configurar coisas — exemplo real]. Quando comecei a estudar para esta seleção, fiz meus primeiros programas em C# e páginas em HTML, e percebi que gosto de **criar** essas coisas, não só de usar. Quero fazer DS na Etec porque é técnico junto com o médio e já me prepara para trabalhar na área."

</details>

<details class="recall-box">
<summary>🎤 2. O curso é em período integral. Como vai ser a sua rotina?</summary>

**Roteiro:** confirme que você sabe que é integral → diga como vai se organizar (transporte, horários, estudo) → mostre disposição.

*Pontos para falar:* que você mora em Taboão (perto da escola), que tem como chegar no horário, e que está acostumado a estudar em casa porque se preparou para esta seleção com um cronograma diário.

</details>

<details class="recall-box">
<summary>🎤 3. Você vai entrar no 2º ano sem ter feito as matérias técnicas do 1º. Como pretende acompanhar?</summary>

**Roteiro:** mostre que você **já começou** → que vai fazer as atividades de adaptação com dedicação → como vai tirar dúvidas.

*Exemplo:* "Eu já estudei por conta própria o básico das matérias do 1º ano: lógica e C#, HTML e CSS, banco de dados, UML e requisitos. Sei que vou ter atividades de adaptação, e vou fazê-las com prioridade, tirando dúvida com os professores e com os colegas."

</details>

<details class="recall-box">
<summary>🎤 4. O que você estudou para esta seleção? O que achou mais difícil?</summary>

**Roteiro:** cite o que estudou (com os nomes certos) → escolha **uma** dificuldade real → diga como superou.

*Exemplo:* "Estudei programação em C# do zero — variáveis, if, laços, vetores —, HTML e CSS com Flexbox, banco de dados com chaves primária e estrangeira e SQL. O mais difícil foi [teste de mesa com laços / matrizes], e eu melhorei fazendo os exercícios no papel, linha por linha."

</details>

<details class="recall-box">
<summary>🎤 5. (Técnica) Explique o que este trecho do seu código faz.</summary>

**Roteiro:** leia **linha por linha** em voz alta usando os nomes certos: "aqui eu declaro…", "aqui eu converto o texto em número com int.Parse", "este **if** verifica se…", "este **for** repete de 1 até 10", "esta variável é um **acumulador**".

Treine explicando em voz alta os seus programas do Dia 15 e a sua página do Dia 14.

</details>

<details class="recall-box">
<summary>🎤 6. (Técnica) Qual a diferença entre chave primária e chave estrangeira? / Entre padding e margin? / Entre while e do-while?</summary>

Respostas curtas e certas:

- **PK** identifica cada registro (não repete, não é nula); **FK** é um campo que aponta para a PK de outra tabela e cria o relacionamento.
- **padding** = espaço **interno** (entre o conteúdo e a borda); **margin** = espaço **externo**.
- **while** testa antes e pode rodar zero vezes; **do-while** testa depois e roda pelo menos uma vez.

</details>

<details class="recall-box">
<summary>🎤 7. Onde você se vê depois do curso? Que área da tecnologia te interessa?</summary>

**Roteiro:** uma área concreta (desenvolvimento web, jogos, apps, banco de dados) → um passo realista (estágio, faculdade, primeiro emprego) → ligação com o curso.

</details>

<details class="recall-box">
<summary>🎤 8. Você tem alguma pergunta para nós?</summary>

Ter uma pergunta mostra interesse. Exemplos: "Como funcionam as atividades de adaptação do 1º ano?", "Quais linguagens e ferramentas vocês usam no 2º ano?", "O curso tem projetos ou TCC em grupo?".

</details>

### 8. Checklist de terça, 08/12

- [ ] **Documento original com foto** (RG ou CIN).
- [ ] Caneta, lápis e borracha (para desenhar DER, se pedirem).
- [ ] Almoçar antes; **chegar com antecedência** (a etapa começa às **13h**).
- [ ] Na prática: **ler o enunciado inteiro** antes de começar; fazer **primeiro o que é pedido** (o básico completo), depois enfeitar.
- [ ] **Salvar** com frequência, na **pasta indicada**, com o nome pedido.
- [ ] Se travar num erro por mais de 5 minutos, **deixe comentado** o que você tentou e siga para a próxima parte. Código explicado vale mais que código em branco.
- [ ] Na entrevista: calma, exemplos reais, vocabulário técnico.

### ✅ Resumo de 1 minuto

- Do enunciado ao banco: **substantivos → entidades**, **características → atributos**, **verbos → relacionamentos**, perguntar a **cardinalidade** nos dois sentidos.
- **1:N** → FK no lado N. **N:N** → tabela associativa com as duas FKs (e os atributos do relacionamento).
- SQL: `CREATE TABLE` com `PRIMARY KEY` e `FOREIGN KEY … REFERENCES`; `INSERT`; `SELECT … WHERE … ORDER BY`; `IS NULL`; `COUNT` com `GROUP BY`; `JOIN … ON`; `UPDATE … WHERE`.
- Entrevista: **interesse real**, **rotina do integral**, **plano para as adaptações**, **explicar o próprio código**. Respostas verdadeiras, com exemplos.
