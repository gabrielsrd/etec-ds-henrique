## Dia 11 (01/12) — Matemática: os moldes que se repetem

Matemática vale **4 questões** por prova em Taboão — e a Etec **repete muito**. As mesmas 4 questões (conjuntos, inequação, logaritmo e poupança) caíram **idênticas em 2021, dez/2023 e dez/2024**. Em dez/2025 vieram áreas, porcentagem e leitura de gráficos (questões do ENEM). Esta aula cobre exatamente esses moldes, com contas **sem calculadora** (ela é proibida na prova).

> [!TIP]
> **Estratégia para Matemática na prova:** faça primeiro as questões que você reconhece (os moldes desta aula). Questões com conta longa ficam para a 2ª passada. E lembre: dá para **testar as alternativas** — às vezes é mais rápido conferir qual alternativa funciona do que resolver do zero.

### 1. As duas questões "com defeito" que sempre voltam

Comece pelos pontos mais fáceis de toda a prova: duas questões que têm **erro no enunciado**, mas que a Etec repetiu três vezes **sempre com a mesma resposta oficial**.

> [!WARNING]
> **🔁 Caíram em 2021, dez/2023 e dez/2024 — com a mesma resposta oficial:**
>
> 1. **Inequação:** "O conjunto solução, nos números reais, da inequação (1 − x)/(1 + x) … −1, é igual a:" → gabarito oficial **A) {x ∈ ℝ | x < −1}**.
> 2. **Logaritmo:** "Dados logₐ m = 11 e logₐ n = 6, qual é o valor de logₐ(m²n²)?" → gabarito oficial **C) 45**.
>
> Se aparecerem de novo com esse texto e essas alternativas, **marque A e C** e siga em frente.

Por que "com defeito"? Para você entender (e não ficar inseguro na hora):

- **Inequação:** com o sinal "> −1", a conta dá **x > −1**, que não está nas alternativas. A resposta A (x < −1) só sai com o sinal "**<**":
  (1 − x)/(1 + x) < −1 → (1 − x)/(1 + x) + 1 < 0 → (1 − x + 1 + x)/(1 + x) < 0 → **2/(1 + x) < 0** → como 2 é positivo, precisa 1 + x < 0 → **x < −1**.
- **Logaritmo:** as propriedades são **log(a · b) = log a + log b** e **log(aᵏ) = k · log a**. Com m²n²: 2 · 11 + 2 · 6 = **34** (não está nas alternativas). O 45 sai de **m³n²**: 3 · 11 + 2 · 6 = 33 + 12 = **45**.

### 2. Conjuntos e diagrama de Venn

**O molde que repetiu 3 vezes:** "92 responderam sim à primeira pergunta, 80 à segunda, 35 às duas e 33 não às duas. Quantos operários?"

**Método: comece SEMPRE pela interseção.**

```text
        1ª pergunta                2ª pergunta
     ┌───────────────┐       ┌───────────────┐
     │               │       │               │
     │   só 1ª       │  as   │   só 2ª       │
     │  92 − 35      │ duas  │  80 − 35      │
     │   = 57        │  35   │   = 45        │
     │               │       │               │
     └───────────────┘       └───────────────┘
                 nenhuma (fora): 33
```

Total = 57 + 35 + 45 + 33 = **170**.

**Fórmula direta:** total = A + B − (A∩B) + nenhum = 92 + 80 − 35 + 33 = **170**.

O erro clássico é somar 92 + 80 (os 35 que responderam às duas seriam contados duas vezes).

**Operações com conjuntos** (caiu em 2022):

| Símbolo | Nome | Pega | Exemplo com A = {1, 2, 3, 4} e B = {3, 4, 5} |
|---|---|---|---|
| A **∩** B | interseção | o que está nos **dois** | {3, 4} |
| A **∪** B | união | **tudo** dos dois, sem repetir | {1, 2, 3, 4, 5} |
| A **−** B | diferença | o que está em A e **não** em B | {1, 2} |

Com parênteses, resolva **o de dentro primeiro**: (A ∩ B) ∪ C → primeiro a interseção, depois junte com C.

**Conjuntos numéricos** (caiu em 2022):

| Conjunto | O que tem | Exemplos |
|---|---|---|
| **ℕ** naturais | 0, 1, 2, 3, … | contagem |
| **ℤ** inteiros | naturais + **negativos** | −3, 0, 5 |
| **ℚ** racionais | tudo que vira **fração** (inclui decimais finitos e **dízimas periódicas**) | ½, 0,75, 0,333… = ⅓ |
| **I** irracionais | **não** vira fração (dízima **não** periódica) | **π**, **√2**, √3 |
| **ℝ** reais | racionais + irracionais | todos acima |

Pegadinha: **dízima periódica é racional** (0,333… = 1/3), não irracional.

<details class="recall-box">
<summary>🧠 Sua vez — Numa turma, 25 jogam futebol, 18 jogam vôlei, 7 jogam os dois e 4 não jogam nada. Quantos alunos?</summary>

Só futebol = 25 − 7 = 18; só vôlei = 18 − 7 = 11; os dois = 7; nenhum = 4. Total = 18 + 11 + 7 + 4 = **40**. (Ou 25 + 18 − 7 + 4 = 40.)

</details>

### 3. Progressão aritmética (PA) — caiu 4 vezes

**PA** = sequência que **soma sempre o mesmo valor** (a **razão**, r): 40, 50, 60, 70… (r = 10).

**Termo geral:** **aₙ = a₁ + (n − 1) · r**

- a₁ = primeiro termo; r = razão; n = posição; aₙ = o termo na posição n.

**O molde "quantos termos?"** (a poupança da Marta, 2021, dez/2023 e dez/2024): depósitos de 40, 50, 60… até 520. Quantos depósitos?

520 = 40 + (n − 1) · 10 → 480 = (n − 1) · 10 → n − 1 = 48 → **n = 49**.

**Mesmo molde, outro tema** (postes, IPI dez/2024): postes a 90 m, 110 m, 130 m… até 1 470 m; cada poste custa R$ 8 000.

1470 = 90 + (n − 1) · 20 → 1380 = (n − 1) · 20 → n − 1 = 69 → **n = 70 postes** → 70 × 8 000 = **R$ 560 000**.

**Soma dos termos de uma PA** (pode cair): **Sₙ = (a₁ + aₙ) · n / 2**. Ex.: 1 + 2 + … + 100 = (1 + 100) · 100 / 2 = **5 050**.

**PG (progressão geométrica)** = **multiplica** sempre pelo mesmo valor (a razão q): 2, 6, 18, 54… (q = 3). Na questão dos triângulos (IPI dez/2024), a área preta é multiplicada por **¾** a cada figura → PG de razão 3/4.

<details class="recall-box">
<summary>🧠 Sua vez — Uma PA começa em 7 e tem razão 4. Qual é o 20º termo?</summary>

a₂₀ = 7 + (20 − 1) · 4 = 7 + 76 = **83**.

</details>

### 4. Porcentagem e leitura de gráficos (dez/2025)

**Porcentagem é "por cem":** 11,4% = 11,4/100 = 0,114.

Truques **sem calculadora**:

- **10%** de qualquer número = tira um zero (ou anda a vírgula uma casa): 10% de 350 = 35.
- **1%** = anda a vírgula duas casas: 1% de 350 = 3,5.
- **5%** = metade de 10%; **20%** = dobro de 10%; **25%** = um quarto; **50%** = metade.
- 12% de 350 = 10% (35) + 1% (3,5) + 1% (3,5) = **42**.

**Aumento e desconto:**

- aumentar 20% → multiplicar por **1,20**;
- descontar 20% → multiplicar por **0,80**;
- "cresceu na mesma **taxa**" → descubra quantas **vezes** cresceu: de 1 400 para 3 500 → 3 500 ÷ 1 400 = **2,5 vezes**.

**Gráfico de setores (pizza)** — dez/2025: as duas maiores regiões (38,3% + 37,2% = 75,5%) produzem 119,8 milhões de toneladas. Quanto produz o Sudeste (11,4%)?

**Regra de três:**

```text
75,5%  ────  119,8 milhões
11,4%  ────  x
x = 119,8 × 11,4 ÷ 75,5
```

Sem calculadora, **arredonde**: 120 × 11,4 ÷ 75,5 ≈ 120 × 0,15 = **18** → a alternativa mais próxima é **18,1**.

**Gráfico de barras** — dez/2025: leia **cada mês** (receita − despesa), monte uma tabela no rascunho e só depois faça a conta pedida. Lucro = positivo; prejuízo = negativo.

> [!TIP]
> Nas questões de gráfico, **as alternativas costumam estar bem separadas** (11,4; 13,6; 15,7; 18,1; 35,6). Arredondar é seguro e economiza tempo.

### 5. Geometria: áreas, Pitágoras e semelhança

**Fórmulas de área:**

| Figura | Área |
|---|---|
| quadrado de lado L | **L²** |
| retângulo b × h | **b · h** |
| triângulo | **b · h / 2** (no retângulo: cateto × cateto ÷ 2) |
| trapézio | **(B + b) · h / 2** |
| círculo de raio r | **π · r²** |

**Perímetro** = soma de todos os lados (é o "contorno", a cerca).

**Teorema de Pitágoras** (triângulo retângulo): **hipotenusa² = cateto² + cateto²**.

O triângulo **3-4-5** e seus múltiplos aparecem muito: **6-8-10, 9-12-15, 12-16-20, 30-40-50, 330-440-550**. Reconhecendo, você nem precisa fazer conta.

**O terreno de 2022:** um triângulo retângulo de catetos 40 e 30 em cima (hipotenusa 50 — é o 3-4-5 × 10) e um trapézio embaixo, de bases 50 e 36 e altura 40.

- Triângulo: 40 · 30 / 2 = **600 m²**
- Trapézio: (50 + 36) · 40 / 2 = 86 · 20 = **1 720 m²**
- Total: **2 320 m²**

**Área máxima com perímetro fixo** (2021): com o mesmo perímetro, o retângulo de **maior área é o quadrado**. Perímetro 360 → lado 90 → área 8 100.

**As peças de dez/2025:** quadrado 9 × 9 = **81**; triângulo retângulo de catetos 12 e 16 → 12 · 16 / 2 = **96** (a hipotenusa 20 **não** entra na área); retângulo 15 × 7 = **105**. Menor: quadrado; maior: retângulo.

**Semelhança de triângulos:** triângulos com os **mesmos ângulos** têm lados **proporcionais**. Monte a proporção lado-com-lado: x / 330 = 330 / 550 → x = 198 (dez/2025).

**Volume e semelhança** (Informática, dez/2025): se as medidas de duas figuras semelhantes estão na razão k, as **áreas** estão na razão **k²** e os **volumes** na razão **k³**. Cone pela metade do volume → altura × 1/∛2.

<details class="recall-box">
<summary>🧠 Sua vez — Um terreno retangular tem 24 m por 18 m. Quanto mede a diagonal e qual é a área?</summary>

24 e 18 = 6 × (4 e 3) → é um **3-4-5 × 6** → diagonal = **30 m**. Área = 24 × 18 = **432 m²**.

</details>

### 6. Contagem (princípio multiplicativo) — 2022

"De quantas maneiras" → **multiplique as opções de cada etapa**. Comece pela etapa com **restrição**.

Números de 3 algarismos **distintos** com 0, 1, 2, 3, 4, 5:

- centena: **não pode ser 0** → 5 opções;
- dezena: qualquer um menos o já usado (o 0 volta a valer) → 5 opções;
- unidade: menos os dois já usados → 4 opções.

Total = 5 × 5 × 4 = **100**. (Quem esquece a restrição do zero faz 6 × 5 × 4 = 120.)

### 7. Funções

**Função afim** (do 1º grau): **f(x) = ax + b** — o gráfico é uma **reta**.

- **a** = taxa de variação (inclinação): a = (y₂ − y₁) / (x₂ − x₁).
- **b** = onde a reta corta o eixo y → **f(0) = b**.

Exemplo (Informática e IPI, dez/2025): f(−1) = 5 e f(3) = −3. a = (−3 − 5) / (3 − (−1)) = −8/4 = **−2**. Então 5 = −2 · (−1) + b → b = **3** → **f(0) = 3**.

**Movimento uniforme** é uma função afim: **s = s₀ + v · t**. Num gráfico s × t que começa em −10 m e passa por 0 m em t = 2 s, a velocidade é 10/2 = **5 m/s**.

**Função do 2º grau:** **f(x) = ax² + bx + c** — o gráfico é uma **parábola**.

- **a > 0** → concavidade para **cima** (vértice = ponto de **mínimo**); **a < 0** → para **baixo** (vértice = **máximo**).
- **Δ = b² − 4ac**: Δ > 0 → **duas raízes reais diferentes**; Δ = 0 → duas iguais; Δ < 0 → nenhuma raiz real.
- Raízes (Bhaskara): **x = (−b ± √Δ) / 2a**.

Exemplo (2022): f(x) = x² − 2x − 3 → Δ = 4 + 12 = 16 → x = (2 ± 4)/2 → **3 e −1**. Duas raízes reais; a = 1 > 0, então concavidade para cima.

**Truque de soma e produto:** para x² + bx + c, as raízes somam **−b** e multiplicam **c**. Em y² − 50y + 600 = 0: dois números que somam 50 e multiplicam 600 → **20 e 30**.

### 8. Estatística: média, mediana, moda

| Medida | Como calcular | Exemplo com 3, 5, 5, 7, 10 |
|---|---|---|
| **Média** | soma ÷ quantidade | 30 ÷ 5 = **6** |
| **Mediana** | o valor **do meio** depois de **ordenar** (se a quantidade for par, a média dos dois do meio) | **5** |
| **Moda** | o valor que **mais aparece** | **5** |
| **Amplitude** | maior − menor | 10 − 3 = **7** |

**Passo que mais esquecem: ordenar antes da mediana.**

> [!WARNING]
> **🔁 Já caiu:** **dez/2023 (questão 28):** dez notas, pedia a afirmação **incorreta** — era "**não é possível calcular a variância**" (sempre é possível). **Informática, dez/2025 (questão 9):** com 9 números, a mediana é o **5º** depois de ordenar; para a maior mediana possível, completa-se a lista com números grandes.

### 9. Álgebra rápida

**Fatorar para simplificar** (IPI, dez/2025): (3x² − 2x − 1)/(2x² − 3x + 1). O "x ≠ 1" do enunciado avisa que **(x − 1)** é fator dos dois: 3x² − 2x − 1 = (3x + 1)(x − 1) e 2x² − 3x + 1 = (2x − 1)(x − 1). Cortando: **(3x + 1)/(2x − 1)**.

**Atalho de prova: teste um número.** Coloque x = 0 na expressão original: −1/1 = −1. Só a alternativa que também dá −1 em x = 0 pode estar certa.

**Inequação do 1º grau:** resolve como equação, **mas, ao multiplicar ou dividir por número negativo, o sinal inverte**: −2x > 6 → x **<** −3.

### ❌ Erros clássicos

> [!CAUTION]
> - **Venn:** somar A + B sem tirar a interseção.
> - **PA:** usar n no lugar de (n − 1) na fórmula.
> - **Contagem:** esquecer que o número não pode começar com 0.
> - **Área do triângulo:** esquecer de dividir por 2 ou usar a hipotenusa como altura.
> - **Mediana:** não ordenar os números antes.
> - **Inequação:** esquecer de inverter o sinal ao dividir por negativo.
> - **Porcentagem:** confundir 5% (0,05) com 0,5.

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Quanto é 15% de 240, sem calculadora?</summary>

10% = 24; 5% = 12; 15% = 24 + 12 = **36**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Uma PA tem a₁ = 5 e a₁₀ = 50. Qual a razão?</summary>

50 = 5 + (10 − 1) · r → 45 = 9r → **r = 5**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — Dados A = {2, 4, 6, 8}, B = {4, 8, 12} e C = {1, 2}, calcule (A ∩ B) ∪ C.</summary>

A ∩ B = {4, 8}. União com C: **{1, 2, 4, 8}**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Uma rampa sobe 6 m de altura em 8 m de distância horizontal. Qual o comprimento da rampa?</summary>

6 e 8 → **3-4-5 × 2** → **10 m**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Quantas senhas de 3 dígitos (de 0 a 9) podem ser formadas, se os dígitos podem repetir? E se não podem?</summary>

Podendo repetir: 10 × 10 × 10 = **1 000**. Sem repetir: 10 × 9 × 8 = **720**. (Senha pode começar com 0 — não é um "número".)

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — Notas: 8, 3, 6, 9, 6, 4. Calcule média, mediana e moda.</summary>

Ordenando: 3, 4, 6, 6, 8, 9. Média = 36 ÷ 6 = **6**. Mediana = (6 + 6) ÷ 2 = **6** (são 6 números, média dos dois do meio). Moda = **6**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — f(x) = 2x + b passa pelo ponto (3, 11). Quanto vale f(0)?</summary>

11 = 2 · 3 + b → b = 5 → **f(0) = 5**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — Um produto de R$ 80 aumentou 25%. Qual o novo preço?</summary>

25% de 80 = 80 ÷ 4 = 20 → **R$ 100** (ou 80 × 1,25).

</details>

### 🖥️ Prática de hoje (30 minutos)

1. Abra o **🔁 Treino das Repetidas** e faça as 4 de Matemática (inequação, logaritmo, PA, Venn) até acertar sem pensar.
2. Na aba **Prática** deste dia, use o laboratório de logaritmo e Venn.
3. Refaça **sem olhar** as questões 11 a 14 da prova de dez/2025 (áreas, semelhança e gráficos) no modo treino.

### ✅ Resumo de 1 minuto

- **Inequação e logaritmo com defeito**: se caírem iguais, **A** e **C** (resposta oficial nas três vezes).
- **Venn**: comece pela interseção; total = A + B − ambos + nenhum.
- **PA**: aₙ = a₁ + (n − 1) · r. Use para "quantos termos" (poupança, postes).
- **Porcentagem sem calculadora**: 10%, 5%, 1% e some. Regra de três com arredondamento.
- **Áreas**: triângulo ÷ 2; trapézio (B + b) · h ÷ 2. **3-4-5** e múltiplos. Perímetro fixo → quadrado tem a maior área.
- **Contagem**: multiplique as opções; zero não começa número.
- **Função afim**: f(0) = b; a = Δy/Δx. **2º grau**: Δ > 0 → duas raízes; a > 0 → mínimo.
- **Mediana**: ordene primeiro.
