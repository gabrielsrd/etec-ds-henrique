"""Aba 2ª Fase (08/12): três provas práticas simuladas e o ensaio da entrevista.
As soluções aparecem escondidas na página (o aluno tenta primeiro)."""

PHASE2 = {
    "dateLabel": "Terça, 08/12/2026 • 13h00 às 15h30 • prática no laboratório + entrevista individual",
    "introAlert": (
        "<strong>Por que esta aba vale a sua vaga:</strong> nos últimos 4 anos, as 9 pessoas que passaram da prova escrita "
        "não foram aprovadas na avaliação prática. A Etec não publica o enunciado, mas a prática avalia as matérias técnicas do "
        "1º ano. Treine as três provas abaixo <strong>no computador, cronometrando e sem copiar</strong>. Só abra a solução "
        "depois de terminar. As aulas dos Dias 14, 15 e 16 explicam cada passo."
    ),
    "labs": [
        {
            "id": "p2_web",
            "badge": "Prova prática simulada 1 • Programação Web",
            "title": "Página de inscrição de um evento (HTML + CSS)",
            "time": "40 min",
            "tool": "VS Code (ou Bloco de Notas) + navegador",
            "mission": (
                "<strong>Enunciado:</strong> crie, na pasta <code>prova-web</code>, os arquivos <code>index.html</code> e "
                "<code>style.css</code> de uma página para o <em>Festival de Robótica da Etec</em> com: (1) cabeçalho com o nome "
                "do evento e um menu com dois links internos; (2) uma seção com um parágrafo, uma imagem com texto alternativo e "
                "uma lista ordenada com 3 categorias; (3) uma tabela com 3 linhas de programação (horário e atividade); "
                "(4) um formulário de inscrição com nome, e-mail, data de nascimento, uma lista suspensa de categoria e um botão, "
                "enviado por POST; (5) um rodapé. No CSS: conteúdo centralizado com largura máxima, cabeçalho com Flexbox "
                "(título e menu nas pontas), formulário dentro de um cartão com borda arredondada e uma media query para celular."
            ),
            "steps": [
                "Crie a pasta, abra no VS Code e crie <code>index.html</code> (<code>!</code> + Tab) e <code>style.css</code>. Troque <code>lang</code> para <code>pt-BR</code>.",
                "Ligue o CSS com <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code> no <code>&lt;head&gt;</code>. Salve e abra no navegador.",
                "Monte as caixas: <code>header</code> (com <code>h1</code> e <code>nav</code>), <code>main</code> (duas <code>section</code> com <code>id</code>) e <code>footer</code>. Teste.",
                "Preencha o conteúdo: parágrafo, <code>img</code> com <code>alt</code>, <code>ol</code> com 3 <code>li</code>, tabela com <code>tr</code>/<code>th</code>/<code>td</code>. Teste.",
                "Faça o formulário: <code>form method=\"post\"</code>, cada campo com <code>label for</code> + <code>id</code>, <code>input type=\"email\"</code>, <code>type=\"date\"</code>, <code>select</code> com <code>option</code>, <code>button type=\"submit\"</code>.",
                "Escreva o CSS na ordem: <code>body</code> → <code>header</code> (flex, space-between, align-items) → <code>main</code> (max-width + margin 0 auto) → tabela → <code>.card</code> → formulário → <code>@media</code>.",
                "Abra o DevTools (F12), teste o modo celular e arrume a indentação (Shift + Alt + F). Salve tudo.",
            ],
            "codeTitle": "index.html (uma solução possível)",
            "code": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Festival de Robótica da Etec</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Festival de Robótica</h1>
    <nav>
      <a href="#sobre">Sobre</a>
      <a href="#inscricao">Inscrição</a>
    </nav>
  </header>

  <main>
    <section id="sobre">
      <h2>Sobre o festival</h2>
      <p>Equipes das escolas da região apresentam robôs e disputam três categorias.</p>
      <img src="https://placehold.co/400x200" alt="Robô montado com peças de LEGO sobre uma mesa">
      <ol>
        <li>Seguidor de linha</li>
        <li>Sumô de robôs</li>
        <li>Projeto livre</li>
      </ol>
      <table>
        <tr><th>Horário</th><th>Atividade</th></tr>
        <tr><td>9h</td><td>Credenciamento</td></tr>
        <tr><td>10h</td><td>Competições</td></tr>
        <tr><td>16h</td><td>Premiação</td></tr>
      </table>
    </section>

    <section id="inscricao" class="card">
      <h2>Inscrição</h2>
      <form action="#" method="post">
        <label for="nome">Nome</label>
        <input type="text" id="nome" name="nome" required>

        <label for="email">E-mail</label>
        <input type="email" id="email" name="email" required>

        <label for="nasc">Data de nascimento</label>
        <input type="date" id="nasc" name="nasc">

        <label for="cat">Categoria</label>
        <select id="cat" name="categoria">
          <option value="linha">Seguidor de linha</option>
          <option value="sumo">Sumô de robôs</option>
          <option value="livre">Projeto livre</option>
        </select>

        <button type="submit">Inscrever</button>
      </form>
    </section>
  </main>

  <footer>
    <p>Etec de Taboão da Serra</p>
  </footer>
</body>
</html>""",
            "code2Title": "style.css (uma solução possível)",
            "code2": """* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f1f5f9;
  color: #1e293b;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: #1e3a8a;
  color: white;
}

nav a { color: #bfdbfe; margin-left: 16px; text-decoration: none; }
nav a:hover { color: white; }

main { max-width: 800px; margin: 0 auto; padding: 16px; }

img { max-width: 100%; border-radius: 8px; }

table { border-collapse: collapse; width: 100%; margin-top: 12px; }
th, td { border: 1px solid #94a3b8; padding: 8px; text-align: left; }
th { background: #dbeafe; }

.card {
  background: white;
  margin-top: 24px;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

form { display: flex; flex-direction: column; }
input, select { padding: 8px; margin: 4px 0 12px 0; }

button {
  padding: 10px;
  border: none;
  border-radius: 8px;
  background: #16a34a;
  color: white;
  cursor: pointer;
}

footer { text-align: center; padding: 16px; color: #64748b; }

@media (max-width: 600px) {
  header { flex-direction: column; gap: 8px; }
}""",
            "checklist": [
                "Esqueleto completo: <code>&lt;!DOCTYPE html&gt;</code>, <code>lang=\"pt-BR\"</code>, <code>meta charset</code>, <code>meta viewport</code> e <code>title</code>.",
                "CSS externo ligado com <code>&lt;link rel=\"stylesheet\"&gt;</code> e funcionando.",
                "Tags semânticas: <code>header</code>, <code>nav</code>, <code>main</code>, <code>section</code>, <code>footer</code>.",
                "Imagem com <code>alt</code>, lista ordenada, tabela com <code>th</code>.",
                "Formulário com <code>method=\"post\"</code>, <code>label for</code> ligado ao <code>id</code>, <code>select</code> e botão <code>submit</code>.",
                "Cabeçalho com Flexbox (título e menu nas pontas) e conteúdo centralizado com <code>max-width</code> e <code>margin: 0 auto</code>.",
                "Cartão com <code>padding</code>, <code>border-radius</code> e sombra; media query funcionando no modo celular do F12.",
                "Consigo explicar cada parte em voz alta (semântica, link do CSS, Flexbox, POST, alt, padding × margin).",
                "Fiz tudo em até 40 minutos, sem consultar.",
            ],
        },
        {
            "id": "p2_csharp",
            "badge": "Prova prática simulada 2 • Programação (C#)",
            "title": "Controle de notas da turma (C# console)",
            "time": "40 min",
            "tool": "Visual Studio (Aplicativo de Console C#) ou dotnetfiddle.net",
            "mission": (
                "<strong>Enunciado:</strong> faça um programa de console que (1) pergunte quantos alunos tem a turma "
                "(entre 1 e 10, repetindo se o valor for inválido ou não for número); (2) leia o nome e a nota (0 a 10) de cada aluno, "
                "guardando em vetores; (3) mostre, para cada aluno, o nome, a nota e a situação: <em>Aprovado</em> (≥ 6), "
                "<em>Recuperação</em> (≥ 4) ou <em>Reprovado</em>; (4) mostre a média da turma, a maior nota e o nome de quem a tirou, "
                "e quantos foram aprovados."
            ),
            "steps": [
                "Crie o projeto (Aplicativo de Console C#). Escreva dentro do <code>Main</code>. Rode com <b>Ctrl + F5</b> a cada parte pronta.",
                "Parte 1: leia a quantidade com <code>int.Parse</code> dentro de um <code>while</code>, com <code>try/catch</code> para letras e um <code>if</code> para o intervalo 1–10.",
                "Parte 2: crie <code>string[] nomes = new string[qtd];</code> e <code>double[] notas = new double[qtd];</code> e preencha com um <code>for</code>.",
                "Parte 3: num segundo <code>for</code>, use <code>if / else if / else</code> para a situação e um contador de aprovados.",
                "Parte 4: acumule a soma para a média e guarde o índice da maior nota (para mostrar o nome).",
                "Teste com dados conhecidos (ex.: 3 alunos, notas 8, 5 e 3,5) e confira as contas à mão. Lembre: no Windows em português, digite decimal com vírgula.",
            ],
            "codeTitle": "Program.cs (uma solução possível)",
            "code": """using System;

class Program
{
    static void Main()
    {
        // 1. Quantidade de alunos, com validação
        int qtd = 0;
        while (qtd < 1 || qtd > 10)
        {
            Console.Write("Quantos alunos (1 a 10)? ");
            try
            {
                qtd = int.Parse(Console.ReadLine());
                if (qtd < 1 || qtd > 10)
                    Console.WriteLine("Digite um valor entre 1 e 10.");
            }
            catch (FormatException)
            {
                Console.WriteLine("Digite apenas números.");
                qtd = 0;
            }
        }

        // 2. Leitura dos nomes e notas
        string[] nomes = new string[qtd];
        double[] notas = new double[qtd];
        for (int i = 0; i < qtd; i++)
        {
            Console.Write($"Nome do aluno {i + 1}: ");
            nomes[i] = Console.ReadLine();
            Console.Write($"Nota de {nomes[i]}: ");
            notas[i] = double.Parse(Console.ReadLine());
        }

        // 3 e 4. Situação de cada um, média, maior nota e aprovados
        double soma = 0;
        int indiceMaior = 0;
        int aprovados = 0;
        Console.WriteLine();
        for (int i = 0; i < qtd; i++)
        {
            string situacao;
            if (notas[i] >= 6)
            {
                situacao = "Aprovado";
                aprovados++;
            }
            else if (notas[i] >= 4)
                situacao = "Recuperação";
            else
                situacao = "Reprovado";

            Console.WriteLine($"{nomes[i]} - nota {notas[i]} - {situacao}");
            soma += notas[i];
            if (notas[i] > notas[indiceMaior])
                indiceMaior = i;
        }

        Console.WriteLine($"Média da turma: {(soma / qtd):F1}");
        Console.WriteLine($"Maior nota: {notas[indiceMaior]} ({nomes[indiceMaior]})");
        Console.WriteLine($"Aprovados: {aprovados}");
    }
}""",
            "code2Title": "Exemplo de execução (o que você digita está depois dos dois-pontos)",
            "code2": """Quantos alunos (1 a 10)? abc
Digite apenas números.
Quantos alunos (1 a 10)? 3
Nome do aluno 1: Ana
Nota de Ana: 8
Nome do aluno 2: Bruno
Nota de Bruno: 5
Nome do aluno 3: Carla
Nota de Carla: 3,5

Ana - nota 8 - Aprovado
Bruno - nota 5 - Recuperação
Carla - nota 3,5 - Reprovado
Média da turma: 5,5
Maior nota: 8 (Ana)
Aprovados: 1""",
            "checklist": [
                "O programa compila sem erros (sem nada sublinhado de vermelho).",
                "Digitar letras na quantidade não fecha o programa (<code>try/catch</code>), e valores fora de 1–10 são recusados (<code>if</code>).",
                "Usei vetores (<code>string[]</code> e <code>double[]</code>) e <code>for</code> de 0 até <code>qtd - 1</code>.",
                "A situação usa <code>if / else if / else</code> com os limites certos (≥ 6 e ≥ 4).",
                "A média usa um acumulador que começa em 0; a maior nota mostra também o nome.",
                "Conferi as contas à mão com dados de teste.",
                "Consigo explicar: tipo, conversão (<code>Parse</code>), decisão, laço, acumulador, vetor e exceção.",
                "Fiz tudo em até 40 minutos, sem consultar.",
            ],
        },
        {
            "id": "p2_bd",
            "badge": "Prova prática simulada 3 • Banco de Dados",
            "title": "Modelagem e SQL de uma oficina de bicicletas",
            "time": "35 min",
            "tool": "Papel (DER) + MySQL Workbench, brModelo ou sqliteonline.com",
            "mission": (
                "<strong>Enunciado:</strong> uma oficina quer controlar seus <em>clientes</em> (CPF, nome, telefone), as "
                "<em>bicicletas</em> de cada cliente (código, marca, cor — cada bicicleta pertence a um único cliente) e os "
                "<em>serviços</em> oferecidos (código, descrição, preço). Cada <em>ordem de serviço</em> registra uma bicicleta, "
                "um serviço, a data e se já foi entregue. (1) Desenhe o DER com as cardinalidades. (2) Escreva o modelo lógico com "
                "PK e FK. (3) Crie as tabelas em SQL e insira pelo menos 2 registros em cada. (4) Escreva consultas para: os "
                "serviços em ordem de preço; as ordens ainda não entregues; o nome do cliente, a marca da bicicleta e a descrição "
                "do serviço de cada ordem."
            ),
            "steps": [
                "Sublinhe os substantivos: cliente, bicicleta, serviço, ordem de serviço → entidades.",
                "Cardinalidades: cliente 1:N bicicleta (FK na bicicleta). Bicicleta N:N serviço → a ordem de serviço é a tabela associativa (com data e entregue).",
                "Desenhe o DER no papel: retângulos, losangos, elipses, PK sublinhada, 1 e N nas linhas.",
                "Escreva o modelo lógico (nome da tabela e colunas, marcando PK e FK).",
                "Crie as tabelas em SQL na ordem certa: primeiro as que não têm FK (cliente, servico), depois bicicleta, por último ordem_servico.",
                "Insira os dados (respeitando as FKs) e escreva as 3 consultas. Rode e confira os resultados.",
            ],
            "codeTitle": "Modelo lógico + SQL (uma solução possível)",
            "code": """-- Modelo lógico
-- cliente(cpf PK, nome, telefone)
-- bicicleta(codigo PK, marca, cor, cpf_cliente FK -> cliente)
-- servico(codigo PK, descricao, preco)
-- ordem_servico(numero PK, codigo_bicicleta FK -> bicicleta, codigo_servico FK -> servico, data_os, entregue)

CREATE TABLE cliente (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    telefone VARCHAR(15)
);

CREATE TABLE servico (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(60) NOT NULL,
    preco DECIMAL(6,2) NOT NULL
);

CREATE TABLE bicicleta (
    codigo INT PRIMARY KEY,
    marca VARCHAR(40),
    cor VARCHAR(20),
    cpf_cliente CHAR(11) NOT NULL,
    FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf)
);

CREATE TABLE ordem_servico (
    numero INT PRIMARY KEY,
    codigo_bicicleta INT NOT NULL,
    codigo_servico INT NOT NULL,
    data_os DATE NOT NULL,
    entregue CHAR(1) DEFAULT 'N',            -- 'S' ou 'N'
    FOREIGN KEY (codigo_bicicleta) REFERENCES bicicleta(codigo),
    FOREIGN KEY (codigo_servico) REFERENCES servico(codigo)
);

INSERT INTO cliente VALUES ('11111111111', 'Ana Souza', '11999990001');
INSERT INTO cliente VALUES ('22222222222', 'Bruno Lima', '11999990002');

INSERT INTO servico VALUES (1, 'Troca de pneu', 40.00);
INSERT INTO servico VALUES (2, 'Revisão completa', 120.00);
INSERT INTO servico VALUES (3, 'Regulagem de freio', 25.00);

INSERT INTO bicicleta VALUES (10, 'Caloi', 'azul', '11111111111');
INSERT INTO bicicleta VALUES (11, 'Sense', 'preta', '22222222222');

INSERT INTO ordem_servico VALUES (100, 10, 2, '2026-12-01', 'S');
INSERT INTO ordem_servico VALUES (101, 11, 1, '2026-12-05', 'N');
INSERT INTO ordem_servico VALUES (102, 10, 3, '2026-12-06', 'N');

-- Consultas
SELECT * FROM servico ORDER BY preco;

SELECT * FROM ordem_servico WHERE entregue = 'N';

SELECT cliente.nome, bicicleta.marca, servico.descricao
FROM ordem_servico
JOIN bicicleta ON bicicleta.codigo = ordem_servico.codigo_bicicleta
JOIN cliente ON cliente.cpf = bicicleta.cpf_cliente
JOIN servico ON servico.codigo = ordem_servico.codigo_servico;""",
            "code2Title": "DER (para desenhar no papel ou no brModelo)",
            "code2": """ (cpf) (nome) (telefone)       (codigo) (marca) (cor)                 (codigo) (descricao) (preco)
      \\   |   /                     \\    |    /                            \\     |      /
   ┌───────────┐ 1   ◇ possui ◇  N ┌─────────────┐ N  ◇ ordem de ◇  N ┌───────────┐
   │  CLIENTE  │───────────────────│  BICICLETA  │─────  serviço  ─────│  SERVICO  │
   └───────────┘                   └─────────────┘          │          └───────────┘
                                                  (numero) (data_os) (entregue)""",
            "checklist": [
                "Identifiquei as 4 entidades e os atributos de cada uma.",
                "Cliente 1:N bicicleta, com a FK na bicicleta.",
                "Bicicleta N:N serviço resolvido pela tabela associativa ordem_servico (com data e entregue).",
                "Toda tabela tem PK; as FKs usam <code>FOREIGN KEY … REFERENCES</code>.",
                "Criei as tabelas na ordem certa (as referenciadas primeiro) e os INSERTs respeitam as FKs.",
                "As 3 consultas funcionam (ORDER BY, WHERE, JOIN).",
                "Consigo explicar PK, FK, cardinalidade e por que existe a tabela associativa.",
                "Fiz tudo em até 35 minutos, sem consultar.",
            ],
        },
    ],
    "interview": [
        {"q": "1. Por que você quer fazer Desenvolvimento de Sistemas aqui na Etec?",
         "tip": "Conte um interesse real por tecnologia (com um exemplo seu) e o que você fez para se preparar. Evite respostas como 'porque é de graça' ou 'porque mandaram'.",
         "model": "Estrutura: o que me atrai em tecnologia [exemplo real: jogos, configurar o PC, curiosidade de como os apps funcionam] → o que já fiz [estudei C#, HTML, CSS e banco de dados para esta seleção] → por que a Etec [técnico junto com o médio, preparo para trabalhar na área]."},
        {"q": "2. O curso é em período integral. Como vai ser a sua rotina?",
         "tip": "Mostre que você sabe que é integral e que tem como cumprir (transporte, horário, estudo em casa).",
         "model": "Estrutura: sei que é integral → moro em Taboão e consigo chegar no horário [como você vai] → já estou acostumado a estudar todo dia, porque segui um cronograma para esta seleção."},
        {"q": "3. Você não fez as matérias técnicas do 1º ano. Como pretende acompanhar a turma?",
         "tip": "O edital prevê atividades de adaptação. Mostre que você já começou e que vai levar as adaptações a sério.",
         "model": "Estrutura: já estudei o básico de lógica e C#, HTML e CSS, banco de dados, UML e requisitos → vou fazer as atividades de adaptação com prioridade → vou tirar dúvidas com os professores e com os colegas."},
        {"q": "4. O que você estudou para esta seleção? O que achou mais difícil?",
         "tip": "Use os nomes certos das matérias e escolha UMA dificuldade real, dizendo como você a superou.",
         "model": "Estrutura: estudei programação em C# do zero (variáveis, if, laços, vetores), HTML e CSS com Flexbox, banco de dados com chaves e SQL → o mais difícil foi [exemplo real: teste de mesa de laços, matrizes] → melhorei fazendo exercícios no papel, linha por linha."},
        {"q": "5. (Técnica) Explique o que este trecho do seu código faz.",
         "tip": "Leia linha por linha usando o vocabulário: declaro, converto, verifico, repito, acumulo. Se houver erro, diga o que tentou.",
         "model": "Exemplo: 'Aqui declaro uma variável double e converto o texto digitado com double.Parse. Este if verifica se a nota é maior ou igual a 6. Este for percorre o vetor de 0 até o tamanho menos 1, e a variável soma é um acumulador que começa em zero.'"},
        {"q": "6. (Técnica) Qual a diferença entre chave primária e estrangeira? E entre padding e margin? E entre while e do-while?",
         "tip": "Respostas curtas e precisas. Se não souber alguma, diga como descobriria.",
         "model": "A chave primária identifica cada registro (não repete e não é nula); a estrangeira aponta para a chave primária de outra tabela e cria o relacionamento. Padding é o espaço interno; margin, o externo. O while testa antes e pode não executar; o do-while testa depois e executa ao menos uma vez."},
        {"q": "7. Que área da tecnologia te interessa? Onde você se vê depois do curso?",
         "tip": "Uma área concreta e um passo realista (estágio, faculdade, primeiro emprego).",
         "model": "Estrutura: me interesso por [desenvolvimento web / jogos / apps / banco de dados] → quero fazer estágio durante o curso e [faculdade / trabalhar na área] → o curso me dá a base para isso."},
        {"q": "8. Você tem alguma pergunta para nós?",
         "tip": "Ter uma pergunta mostra interesse.",
         "model": "Exemplos: 'Como funcionam as atividades de adaptação do 1º ano?', 'Quais linguagens e ferramentas vocês usam no 2º ano?', 'O curso tem projetos em grupo ou TCC?'"},
    ],
}
