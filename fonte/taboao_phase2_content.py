# -*- coding: utf-8 -*-
"""
Conteúdo completo da Aba 2ª Fase (08/12 — Avaliação Prática em Laboratório + Entrevista Individual)
100% baseado no Edital nº 02, Plano de Curso 612 e histórico real da Etec de Taboão da Serra.
"""

PHASE2_DATA = {
    "dateLabel": "Terça, 08/12/2026 • 13h00 às 15h30 (2h30 no laboratório)",
    "introAlert": (
        "<strong>Por que esta aba vale a sua vaga:</strong> Nos últimos 3 anos em Taboão da Serra, "
        "<strong>todos os 7 candidatos aprovados na escrita reprovaram aqui na prática</strong> por travarem na tela em branco. "
        "Você <strong>não precisa ser programador sênior</strong> — basta sair do zero e tirar menção <strong>R (Regular), B ou MB</strong> "
        "mostrando que sabe montar uma página HTML+CSS, rodar um programinha simples em C# e modelar uma tabela/DER!"
    ),
    "labs": [
        {
            "id": "p2_web",
            "badge": "Desafio Prático #1 • Programação Web I",
            "title": "Página Completa HTML5 + CSS3 + Flexbox (VS Code)",
            "time": "30–40 min",
            "tool": "VS Code + Chrome/Edge (F12)",
            "mission": (
                "Crie uma pasta chamada <code>site_etec</code> com dois arquivos: <code>index.html</code> e <code>style.css</code>. "
                "A página deve ter cabeçalho, um cartão centralizado na tela usando <strong>Flexbox</strong>, uma imagem com <code>alt</code>, "
                "um pequeno formulário de cadastro usando <code>method=\"POST\"</code> e adaptação para celular com <code>@media</code>."
            ),
            "steps": [
                "Abra o VS Code (ou Bloco de Notas se não tiver VS Code) → crie <code>index.html</code> e <code>style.css</code> na mesma pasta.",
                "Digite <code>!</code> + <code>Tab</code> no VS Code para gerar o esqueleto HTML5 e mude <code>lang=\"pt-BR\"</code>.",
                "Ligue o CSS dentro do <code>&lt;head&gt;</code> usando <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code>.",
                "Monte o conteúdo visível dentro de <code>&lt;body&gt;</code> usando tags semânticas (<code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;footer&gt;</code>).",
                "No <code>style.css</code>, centralize o cartão com <code>display: flex; justify-content: center; align-items: center;</code> e ajuste <code>padding</code> (interno) e <code>margin</code> (externo).",
                "Dê duplo clique em <code>index.html</code> para abrir no Chrome e aperte <code>F12</code> para conferir se não há erros!"
            ],
            "codeTitle": "index.html (HTML5 Semântico + Formulário POST + img alt)",
            "code": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal Aluno — Etec Taboão</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="topo">
    <h1>Desenvolvimento de Sistemas — Etec</h1>
    <p>Prática de Programação Web I</p>
  </header>

  <main class="palco">
    <section class="cartao">
      <img src="logo.png" alt="Logotipo da Etec Taboão da Serra" class="logo">
      <h2>Cadastro do Estudante</h2>
      <hr>
      <form action="#" method="POST">
        <label for="nome">Nome completo:</label>
        <input id="nome" type="text" placeholder="Digite seu nome" required>

        <label for="email">E-mail institucional:</label>
        <input id="email" type="email" placeholder="aluno@etec.sp.gov.br" required>

        <label for="senha">Senha:</label>
        <input id="senha" type="password" required>

        <button type="submit">Enviar Cadastro</button>
      </form>
    </section>
  </main>

  <footer><p>Etec de Taboão da Serra • 2026</p></footer>
</body>
</html>""",
            "code2Title": "style.css (Box Model + Flexbox + Responsivo @media)",
            "code2": """* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin: 0; background: #f1f5f9; color: #0f172a; }

.topo { background: #1e3a8a; color: #fff; text-align: center; padding: 20px; }

/* FLEXBOX: centraliza horizontal e verticalmente! */
.palco {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
  padding: 16px;
}

/* BOX MODEL: padding interno, borda e sombra */
.cartao {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 24px;
  width: 100%;
  max-width: 420px;
}

label { display: block; margin-top: 12px; font-weight: bold; }
input { width: 100%; padding: 10px; margin-top: 4px; border: 1px solid #94a3b8; border-radius: 8px; }
button {
  width: 100%; margin-top: 16px; padding: 12px; border: none;
  border-radius: 8px; background: #16a34a; color: #fff; font-weight: bold; cursor: pointer;
}

/* MEDIA QUERY: ajuste para celular estreito */
@media (max-width: 600px) {
  .cartao { padding: 16px; }
  .topo h1 { font-size: 20px; }
}""",
            "checklist": [
                "O arquivo HTML tem <code>&lt;!DOCTYPE html&gt;</code>, <code>&lt;head&gt;</code> e <code>&lt;body&gt;</code> fechados certinho?",
                "A tag <code>&lt;img&gt;</code> tem o atributo <code>alt=\"...\"</code> preenchido?",
                "O formulário de senha usa <code>method=\"POST\"</code> e <code>type=\"password\"</code>?",
                "O cartão está centralizado usando <code>display: flex; justify-content: center; align-items: center;</code>?"
            ]
        },
        {
            "id": "p2_csharp",
            "badge": "Desafio Prático #2 • Técnicas de Programação (TPA)",
            "title": "3 Programas Reais em C# Console (Visual Studio ou Online)",
            "time": "45 min",
            "tool": "Visual Studio (Console App C#) ou dotnetfiddle.net",
            "mission": (
                "No laboratório de Taboão da Serra a linguagem oficial é <strong>C#</strong>. "
                "Treine digitar e rodar estes 3 mini-programas clássicos: (1) Condicional <code>if/else</code> com <code>try/catch</code>, "
                "(2) Repetição com <code>for</code>/<code>while</code> e resto <code>%</code>, e (3) Vetor de notas com cálculo da média. "
                "<em>Dica: você pode testar agora mesmo no navegador em <strong>dotnetfiddle.net</strong> sem instalar nada!</em>"
            ),
            "steps": [
                "No Visual Studio da Etec: <em>Criar novo projeto → Aplicativo de Console (C#)</em>. (Em casa, abra <code>dotnetfiddle.net</code>).",
                "Lembre das 3 regras que mais dão erro de compilação em C#: toda instrução termina com <code>;</code>, letras maiúsculas importam (<code>Console.WriteLine</code>), e toda chave <code>{</code> precisa fechar com <code>}</code>!",
                "Para ler texto do teclado use <code>Console.ReadLine()</code>; para transformar em número use <code>int.Parse(...)</code> ou <code>double.Parse(...)</code>.",
                "Se o enunciado pedir para impedir erro se o usuário digitar letras, envolva a leitura em <code>try { ... } catch { ... }</code>.",
                "Aperte <strong>F5</strong> (ou <em>Run</em>) para executar; se aparecer sublinhado vermelho, leia a linha indicada pelo compilador!"
            ],
            "codeTitle": "Programa A (if/else + try/catch) — Imposto e Aprovação",
            "code": """using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.Write("Digite o valor do produto (R$): ");
            double valor = double.Parse(Console.ReadLine());
            double imposto;

            if (valor < 100.0)
            {
                imposto = valor * 0.05; // 5%
            }
            else
            {
                imposto = valor * 0.12; // 12%
            }

            Console.WriteLine("Imposto calculado: R$ " + imposto.ToString("F2"));
            Console.WriteLine("Total final: R$ " + (valor + imposto).ToString("F2"));
        }
        catch (FormatException)
        {
            Console.WriteLine("Erro: digite apenas numeros validos!");
        }
    }
}""",
            "code2Title": "Programa B (for + vetor + pares) — Média de 4 Notas e Contagem",
            "code2": """using System;

class Program
{
    static void Main(string[] args)
    {
        double[] notas = new double[4]; // Vetor com 4 posicoes (indices 0, 1, 2, 3)
        double soma = 0;

        for (int i = 0; i < notas.Length; i++)
        {
            Console.Write("Digite a nota " + (i + 1) + ": ");
            notas[i] = double.Parse(Console.ReadLine());
            soma += notas[i];
        }

        double media = soma / notas.Length;
        Console.WriteLine("Media final: " + media.ToString("F1"));

        if (media >= 6.0)
            Console.WriteLine("Situacao: APROVADO!");
        else
            Console.WriteLine("Situacao: RECUPERACAO");
    }
}""",
            "checklist": [
                "Todas as instruções terminam com ponto e vírgula <code>;</code>?",
                "Usou <code>==</code> para comparar igualdade (e nunca <code>=</code> sozinho dentro do <code>if</code>)?",
                "Usou <code>&amp;&amp;</code> para 'E' e <code>||</code> para 'OU'?",
                "Se der erro e faltar tempo, deixou comentários <code>//</code> explicando sua lógica para o avaliador?"
            ]
        },
        {
            "id": "p2_bd",
            "badge": "Desafio Prático #3 • Banco de Dados I",
            "title": "Modelagem DER + Chaves (PK/FK) + SQL Básico",
            "time": "30 min",
            "tool": "brModelo / Papel / MySQL Workbench / SQLite",
            "mission": (
                "Cenário clássico de laboratório: <em>\"A biblioteca da Etec precisa cadastrar Alunos, Livros e os Empréstimos realizados. "
                "Um aluno pode pegar vários livros ao longo do ano, e um livro pode ser emprestado para vários alunos.\"</em> "
                "Modele as entidades, chaves primárias (PK), chaves estrangeiras (FK) e escreva os comandos SQL básicos."
            ),
            "steps": [
                "Identifique os 'substantivos' principais → viram <strong>Entidades (Tabelas)</strong>: <code>ALUNO</code> e <code>LIVRO</code>.",
                "Defina a <strong>Chave Primária (PK)</strong> de cada uma (código único que nunca repete): <code>id_aluno</code> e <code>id_livro</code>.",
                "Analise a cardinalidade: 1 aluno pega N livros, e 1 livro pode ir para N alunos → <strong>N:N (Muitos para Muitos)</strong>!",
                "Resolva o <code>N:N</code> criando a <strong>3ª Tabela Associativa</strong>: <code>EMPRESTIMO</code> recebendo <code>id_aluno (FK)</code> e <code>id_livro (FK)</code> + <code>data_retirada</code>.",
                "Confira a <strong>1ª Forma Normal (1FN)</strong>: nenhum campo tem dois valores separados por vírgula (ex.: telefones separados em outra tabela ou 1 por campo)."
            ],
            "codeTitle": "Modelo Lógico + Script SQL Essencial (DDL + DML + DQL)",
            "code": """-- 1. Criando tabelas (DDL) com Chave Primaria (PK) e Estrangeira (FK)
CREATE TABLE aluno (
    id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    ra VARCHAR(20) NOT NULL
);

CREATE TABLE livro (
    id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(120) NOT NULL,
    autor VARCHAR(80)
);

-- Tabela associativa resolvendo N:N
CREATE TABLE emprestimo (
    id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    id_aluno INT NOT NULL,
    id_livro INT NOT NULL,
    data_retirada DATE NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro)
);

-- 2. Inserindo registros (DML)
INSERT INTO aluno (nome, ra) VALUES ('Henrique Silva', '2026001');
INSERT INTO livro (titulo, autor) VALUES ('Logica de Programacao', 'Forbellone');
INSERT INTO emprestimo (id_aluno, id_livro, data_retirada) VALUES (1, 1, '2026-12-08');

-- 3. Consultando dados (DQL)
SELECT nome, ra FROM aluno WHERE id_aluno = 1;""",
            "code2Title": "Esquema DER (Notação Peter Chen) para Desenhar no Papel ou brModelo",
            "code2": """  (id_aluno PK)  (nome)                      (id_livro PK)  (titulo)
        \\         /                                 \\         /
     ┌───────────────┐      ┌───────────────┐     ┌───────────────┐
     │     ALUNO     │──(N)─│  EMPRESTIMO   │─(N)─│     LIVRO     │
     └───────────────┘      │ (data_retira) │     └───────────────┘
                            └───────────────┘
   -> No Modelo Logico, o losango N:N vira a 3a tabela EMPRESTIMO com FK de ALUNO e FK de LIVRO!""",
            "checklist": [
                "Toda tabela tem uma <strong>Chave Primária (PK)</strong> única e não nula?",
                "Em relacionamentos <code>1:N</code>, colocou a <strong>FK</strong> sempre no lado <code>N</code>?",
                "Em relacionamentos <code>N:N</code>, criou a <strong>3ª tabela intermediária</strong>?",
                "Sabe explicar em 1 frase a diferença entre Tabela, Registro (linha) e Campo (coluna)?"
            ]
        }
    ],
    "interview": [
        {
            "q": "1. Por que você quer transferir para o 2º ano do M-Tec em Desenvolvimento de Sistemas aqui na Etec de Taboão?",
            "tip": "Mostre interesse genuíno em tecnologia + foco no curso da Etec (não diga só 'porque minha mãe mandou' ou 'porque é de graça').",
            "model": "\"Eu sempre gostei de computadores e tecnologia, mas no ano passado acabei indo pro Ensino Médio regular. Esse ano decidi que quero seguir carreira na área de programação/TI, estudei a grade do 1º ano de vocês pelo Plano de Curso e quero muito aproveitar a formação prática da Etec.\""
        },
        {
            "q": "2. Como você estudou os conteúdos técnicos do 1º ano sem ter feito a 1ª série aqui?",
            "tip": "Os professores adoram proatividade e honestidade. Cite que estudou pelo Plano de Curso oficial 612, provas anteriores e projetos práticos!",
            "model": "\"Eu baixei o Plano de Curso de DS da Etec de Taboão, estudei as 6 matérias técnicas do 1º ano — lógica em C#, HTML5/CSS3 com Flexbox, modelagem de banco de dados (DER/chaves), UML e fundamentos — e fiz vários exercícios práticos no computador em casa.\""
        },
        {
            "q": "3. O curso é Período Integral (M-Tec-PI) e você terá atividades de adaptação do 1º ano. Você consegue acompanhar a rotina?",
            "tip": "O Edital (Item III.3) cita explicitamente o programa de adaptação! Mostre organização e comprometimento.",
            "model": "\"Sim! Eu já me organizei com minha família para a rotina em período integral e estou totalmente disposto a fazer as atividades de adaptação para nivelar 100% com a turma.\""
        },
        {
            "q": "4. (Pergunta técnica olhando sua tela) Para que serve essa Chave Primária e essa Chave Estrangeira que você criou?",
            "tip": "Resposta curta, limpa e segura — sem enrolar!",
            "model": "\"A Chave Primária (PK) identifica cada linha de forma única, sem deixar repetir nem ficar vazia. A Chave Estrangeira (FK) pega a PK de outra tabela para ligar as duas com segurança.\""
        },
        {
            "q": "5. (Pergunta técnica) Qual a diferença entre o laço while e o do/while em C#?",
            "tip": "Clássico da prova de Taboão!",
            "model": "\"O while testa a condição antes de entrar — se já começar falsa, roda 0 vezes. O do/while executa o bloco pelo menos 1 vez garantida e só testa a condição no final.\""
        },
        {
            "q": "6. (Pergunta técnica) Para que serve o atributo alt na tag <img> e como você centralizou o bloco no CSS?",
            "tip": "Caiu literal nas provas de Taboão 2024 e 2025!",
            "model": "\"O alt mostra um texto alternativo se a imagem não carregar e ajuda na acessibilidade para leitores de tela. Para centralizar no CSS usei Flexbox com display: flex, justify-content: center e align-items: center.\""
        },
        {
            "q": "7. (Pergunta técnica) O que você faz quando aparece um erro vermelho no código em C#?",
            "tip": "Mostre método de depuração (breakpoint + leitura do erro)!",
            "model": "\"Primeiro eu olho a linha que o compilador marcou — geralmente é falta de ponto e vírgula, chave aberta ou erro de digitação. Se o programa roda mas dá o resultado errado, coloco um breakpoint para pausar e inspecionar o valor das variáveis passo a passo.\""
        },
        {
            "q": "8. Qual a diferença entre Requisito Funcional e Requisito Não Funcional?",
            "tip": "A frase clássica que Taboão repetiu em 2022 e 2024!",
            "model": "\"Requisito Funcional diz O QUE o sistema deve fazer, ou seja, suas funções e cadastros. Requisito Não Funcional diz COMO o sistema se comporta — velocidade, segurança, usabilidade e portabilidade.\""
        }
    ]
}
