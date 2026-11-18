# Micro-Laboratórios Práticos Zero-Setup (15 min cada)

Estes 4 laboratórios existem para você **ver na prática** as pegadinhas que a Fundação FAT cobra na teoria. Nenhum deles exige instalar bibliotecas externas.

---

## Lab 01 — HTML, Links (`_blank` vs `_self`), Árvore DOM e Cookies (`lab01_web_cookies.html`)
- **Como rodar:** Dê um duplo clique em `lab01_web_cookies.html` para abrir no Google Chrome, Edge ou Firefox.
- **O que fazer (15 min):**
  1. Teste a diferença entre `<a target="_self">` e `<a target="_blank">` (Questão 20 da prova 2025).
  2. Crie um **Cookie de Sessão** e um **Cookie Permanente** nos botões da página.
  3. Aperte **`F12`** $\rightarrow$ aba **Application (Aplicativo)** $\rightarrow$ **Cookies** para provar que cookies ficam gravados **no navegador (~4 KB)** e **NUNCA na nuvem** (Questão 21 da prova 2025).
  4. Teste os comandos DOM (`getElementById`, `createTextNode`, `documentElement`, `parentNode`).

## Lab 02 — Teste de Mesa, Matriz 3x3, Tabela Verdade e Pilha (`lab02_teste_mesa_matriz.py` / `.js`)
- **Como rodar:** No terminal, execute:
  - Python: `python3 lab02_teste_mesa_matriz.py`
  - Node.js: `node lab02_teste_mesa_matriz.js`
- **O que observar (15 min):**
  1. Passo a passo do algoritmo de **Teste de Mesa (Executar Linha a Linha)** convertendo decimal para binário com `DIV` e `MOD`.
  2. Visualização da matriz `3x3` com índices `[i][j]` base 0, cálculo da **Diagonal Principal** (`1+4+1 = 6`) e alerta da pegadinha da diagonal secundária (`10`).
  3. Simulação da **Pilha LIFO (`PUSH` e `POP`)** e **Fatorial Recursivo (`4! = 24`)**.

## Lab 03 — SQL na Prática (DDL, DML, DQL) e Normalização 1FN (`lab03_sql_pratico.py`)
- **Como rodar:** No terminal, execute:
  - `python3 lab03_sql_pratico.py`
- **O que observar (15 min):**
  1. Criação de tabela em memória com **DDL** (`CREATE TABLE`, `ALTER TABLE`).
  2. Inserção/alteração/exclusão de registros com **DML** (`INSERT`, `UPDATE`, `DELETE`).
  3. Consulta e contagem com **DQL** (`SELECT COUNT(*) FROM clientes WHERE cidade = 'São Paulo';`) e alerta contra a inversão DDL ↔ DQL.
  4. Exemplo visual de tabela violando a **1ª Forma Normal (1FN)** (dois telefones na mesma célula) sendo normalizada para valores atômicos.

## Lab 04 — Vetor vs. Bitmap, Rasterização, Cores e Gestalt (`lab04_design_vetor_vs_bitmap.html`)
- **Como rodar:** Dê um duplo clique em `lab04_design_vetor_vs_bitmap.html` no navegador.
- **O que fazer (15 min):**
  1. Arraste o **Slider de Zoom (100% a 800%)** e compare o `<svg>` vetorial (sempre nítido) com o `<canvas>` bitmap (pixelado).
  2. Brinque com o seletor **RGB / Hexadecimal / CMYK** para fixar padrões de cores.
  3. Teste as transformações **CSS3** (`scale`, `skew`, `translate`, `rotate`) e os **5 Princípios da Gestalt**.
