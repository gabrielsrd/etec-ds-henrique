## Dia 8 (28/11) — Fundamentos da Informática: bases numéricas, hardware, SO e segurança

Fundamentos da Informática é a matéria com as questões **mais repetidas** de Taboão: "qual hexadecimal corresponde a 187?" e "o que caracteriza uma interface CLI?" caíram **com o mesmo enunciado** em dez/2024 e em dez/2025. Também caem conversão para binário, sistema operacional, hardware, software livre e segurança. São perguntas curtas — com esta aula, você deve conseguir **todas** desta matéria.

> [!IMPORTANT]
> Lembre que **não pode usar calculadora** na prova. As conversões de base precisam sair na mão. Faça os exemplos com lápis e papel.

### 1. Hardware, software e peopleware

Um sistema computacional tem três partes:

| Parte | O que é | Exemplos |
|---|---|---|
| **Hardware** | a parte **física**, que dá para tocar (o "maquinário") | processador, memória, placa-mãe, teclado, monitor |
| **Software** | a parte **lógica**: programas e instruções | Windows, Chrome, Minecraft, o app do banco |
| **Peopleware** | as **pessoas** que usam, operam e desenvolvem | você, o técnico, o programador |

Frase clássica: *"hardware é o que você chuta; software é o que você xinga"*.

**Tipos de software:**

- **Sistema operacional** (software básico): gerencia o computador — Windows, Linux, Android, iOS, macOS.
- **Aplicativos**: fazem tarefas para o usuário — Word (texto), **Excel** (planilhas e cálculos), Chrome (navegar), Photoshop (imagens).
- **Utilitários**: manutenção do sistema — antivírus, compactador (WinRAR), desfragmentador.
- **Firmware**: software gravado **dentro** do hardware, que controla o aparelho (o BIOS da placa-mãe, o sistema do roteador).

> [!WARNING]
> **🔁 Já caiu:** 2022 (questão 34) "Hardware é: **maquinário**"; Informática para Internet, dez/2025 (questão 15) "hardware = **elementos físicos e tangíveis** responsáveis pela execução das operações"; e (questão 16) software para planilhas e cálculos = **Excel**.

### 2. Por dentro do computador

| Componente | Função | Analogia |
|---|---|---|
| **CPU** (processador) | executa as instruções, faz as contas | o cérebro |
| **Memória RAM** | guarda o que está **sendo usado agora** (programas abertos) — **volátil**: apaga ao desligar | a mesa onde você estuda |
| **Memória ROM** | memória **só de leitura**, **não volátil**, com o programa de inicialização | o manual que vem de fábrica |
| **HD / SSD** (armazenamento) | guarda arquivos e o sistema **de forma permanente** | o armário |
| **Placa-mãe** | liga todos os componentes | o esqueleto com os "fios" |
| **Placa de vídeo (GPU)** | processa imagens (jogos!) | |
| **Fonte** | transforma a energia da tomada para o PC | |

**HD × SSD:** o **HD** tem um disco que gira e uma agulha que lê (mais lento, mais barato); o **SSD** usa chips, sem peças móveis (muito mais rápido). Um SSD faz o PC ligar em segundos.

**Periféricos:**

- **Entrada** (mandam dados para o PC): teclado, mouse, microfone, webcam, scanner.
- **Saída** (mostram o resultado): monitor, caixa de som, impressora.
- **Entrada e saída**: tela touch, pendrive, HD externo, headset com microfone.

**BIOS/UEFI e o POST:** quando você liga o PC, o primeiro programa a rodar é o **BIOS** (ou **UEFI**, a versão moderna), gravado num chip da placa-mãe. Ele faz o **POST** (*Power-On Self-Test*, um autoteste do hardware — aquele "bip" ao ligar) e depois **carrega o sistema operacional** do disco para a **RAM** (o *boot*).

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2024:** (questão 29) "a memória **RAM** é usada para armazenar dados **temporários** durante a execução de programas"; (questão 30) o BIOS **realiza o POST e carrega o sistema operacional na memória RAM**.

**Unidades de medida:**

| Unidade | Vale |
|---|---|
| **bit** | 0 ou 1 (a menor unidade) |
| **byte** | **8 bits** (um caractere, como a letra "A") |
| KB (kilobyte) | 1024 bytes |
| MB (megabyte) | 1024 KB |
| GB (gigabyte) | 1024 MB |
| TB (terabyte) | 1024 GB |

### 3. Bases numéricas: por que o computador fala em binário

O computador só entende **dois estados**: tem corrente (**1**) ou não tem (**0**). Por isso ele usa a base **2** (**binário**). Nós usamos a base **10** (decimal). Os programadores também usam a base **16** (**hexadecimal**), porque ela escreve números binários grandes de forma curta.

| Base | Nome | Dígitos usados |
|---|---|---|
| 2 | **binário** | 0, 1 |
| 8 | **octal** | 0 a 7 |
| 10 | **decimal** | 0 a 9 |
| 16 | **hexadecimal** | 0 a 9 e **A=10, B=11, C=12, D=13, E=14, F=15** |

**A ideia de "casa" (posição).** No decimal, cada casa vale 10 vezes a da direita: em **347**, temos 3 × 100 + 4 × 10 + 7 × 1. Em **qualquer base**, é igual — só muda o número que multiplica:

| Base | Valor das casas (da direita para a esquerda) |
|---|---|
| 2 | 1, 2, 4, 8, 16, 32, 64, 128, 256 … |
| 4 | 1, 4, 16, 64, 256 … |
| 8 | 1, 8, 64, 512 … |
| 16 | 1, 16, 256, 4096 … |

#### 3.1 Decimal → binário (divisões por 2)

Divida por 2 sem parar e anote os **restos**. A resposta são os restos **de baixo para cima**.

Exemplo: **173** (caiu em 2021, questão 32):

| Divisão | Quociente | Resto |
|---|---|---|
| 173 ÷ 2 | 86 | **1** |
| 86 ÷ 2 | 43 | **0** |
| 43 ÷ 2 | 21 | **1** |
| 21 ÷ 2 | 10 | **1** |
| 10 ÷ 2 | 5 | **0** |
| 5 ÷ 2 | 2 | **1** |
| 2 ÷ 2 | 1 | **0** |
| 1 ÷ 2 | 0 | **1** |

De baixo para cima: **173 = 10101101₂**.

**Jeito mais rápido — pelas casas:** escreva as casas (128, 64, 32, 16, 8, 4, 2, 1) e vá "ligando" da maior para a menor, subtraindo:

```text
173 - 128 = 45   → casa 128 = 1
 45 <  64        → casa  64 = 0
 45 -  32 = 13   → casa  32 = 1
 13 <  16        → casa  16 = 0
 13 -   8 =  5   → casa   8 = 1
  5 -   4 =  1   → casa   4 = 1
  1 <   2        → casa   2 = 0
  1 -   1 =  0   → casa   1 = 1
                    resultado: 1 0 1 0 1 1 0 1
```

**Atalho de prova:** número **ímpar** termina em **1** em binário; **par** termina em **0**. Isso elimina alternativas na hora.

#### 3.2 Binário → decimal

Some o valor das casas que têm **1**:

```text
 1   1   0   0   1   0   1
64  32  16   8   4   2   1
──────────────────────────
64 + 32       + 4     + 1 = 101
```

**1100101₂ = 101**.

#### 3.3 Decimal → hexadecimal (o 187!)

Divida por **16**. Os restos de 10 a 15 viram letras.

**187** (caiu em dez/2024 e em dez/2025, igual):

```text
187 ÷ 16 = 11, resto 187 − 176 = 11
 11 ÷ 16 =  0, resto 11
```

Restos de baixo para cima: **11** e **11** → **B** e **B** → **187 = BB₁₆**.

Conferindo: B × 16 + B = 11 × 16 + 11 = 176 + 11 = **187** ✔.

> [!WARNING]
> **🔁 Já caiu duas vezes — dez/2024 e dez/2025 (questão 33):** "Qual número hexadecimal corresponde ao número decimal 187?" → **BB**. As alternativas eram 4C, 58, 3A, BB, F2. Se cair de novo, é a **BB**.

Para não errar a tabuada do 16: 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256.

#### 3.4 Hexadecimal → decimal

Cada casa vale uma potência de 16: **2F₁₆** = 2 × 16 + F (15) = 32 + 15 = **47**. **A0₁₆** = 10 × 16 + 0 = **160**. **FF₁₆** = 15 × 16 + 15 = **255** (o maior valor de um byte — por isso as cores do CSS vão de `00` a `FF`).

#### 3.5 Binário ↔ hexadecimal (o truque dos grupos de 4)

Como 16 = 2⁴, **cada dígito hexadecimal vale exatamente 4 bits**. Separe o binário em grupos de 4, **da direita para a esquerda**:

```text
10111011₂  →  1011 | 1011  →  11 | 11  →  B | B  →  BB₁₆
```

Repare: 187 = 10111011₂ = BB₁₆ — tudo bate. Para **octal** é a mesma ideia com grupos de **3** bits (8 = 2³).

#### 3.6 Outras bases

Use a mesma lógica. **86 em base 4** (caiu em Informática, dez/2025, questão 10): casas 64, 16, 4, 1 → 86 = **1**×64 + **1**×16 + **1**×4 + **2**×1 → **1112₄**. Na mesma questão: 86 em hexa = **56** (5×16 + 6), em binário = **1010110**, em octal = **126** (1×64 + 2×8 + 6).

<details class="recall-box">
<summary>🧠 Sua vez — Converta 200 para hexadecimal e 11110000₂ para decimal.</summary>

- 200 ÷ 16 = 12 (192), resto 8 → **C8₁₆** (C = 12). Confere: 12×16 + 8 = 200.
- 11110000₂ = 128 + 64 + 32 + 16 = **240**. (Ou pelos grupos: 1111 | 0000 = F0₁₆ = 15×16 = 240.)

</details>

Em C#, dá para conferir conversões assim (útil no laboratório):

```csharp
Console.WriteLine(Convert.ToString(187, 2));    // 10111011
Console.WriteLine(Convert.ToString(187, 16));   // bb
Console.WriteLine(Convert.ToInt32("BB", 16));   // 187
Console.WriteLine(Convert.ToInt32("10101101", 2)); // 173
```

### 4. Sistema operacional

O **sistema operacional (SO)** é o "gerente" do computador. Ele fica **entre o usuário (e os programas) e o hardware**:

```text
   Você (peopleware)
        │
   Aplicativos (Chrome, jogo, Word)
        │
   SISTEMA OPERACIONAL  ← gerencia memória, processador, arquivos, dispositivos, usuários
        │
   Hardware (CPU, RAM, disco, teclado…)
```

Funções do SO: **gerenciar o hardware** (memória, processador, discos), **organizar os processos** (programas rodando), **gerenciar arquivos e pastas**, **controlar usuários e permissões** e **permitir que os programas funcionem**. Exemplos: **Windows**, **Linux** (Ubuntu), **macOS**, **Android**, **iOS**.

> [!WARNING]
> **🔁 Já caiu:** 2022 (questão 35) "sistema operacional é **uma interface entre peopleware e hardware**"; Informática para Internet, dez/2025 (questão 17) função principal: "**gerenciar hardware, organizar processos e permitir a execução de softwares**" (as erradas usavam "somente", "apenas", "exclusivamente").

**Monotarefa, multitarefa e multiusuário:**

| Termo | Significa | Exemplo |
|---|---|---|
| **Monotarefa** | executa **uma tarefa por vez** | o antigo MS-DOS |
| **Multitarefa** | executa **vários programas ao mesmo tempo** | ouvir música enquanto joga |
| **Monousuário** | **um** usuário por vez | um celular comum |
| **Multiusuário** | **vários usuários** usando o mesmo sistema ao mesmo tempo, cada um com suas aplicações e permissões | um servidor Linux com várias pessoas conectadas |

### 5. CLI × GUI e os comandos

- **GUI** (*Graphical User Interface*): interface **gráfica** — janelas, ícones, mouse. O Windows que você usa.
- **CLI** (*Command Line Interface*): interface de **linha de comando** — você **digita comandos** em texto. O **CMD** e o **PowerShell** no Windows; o **Terminal** no Linux.

A banca de Taboão define a CLI como **"interface monotarefa por linha de comando"**: você digita **um comando**, ele roda, e só depois você digita o próximo.

> [!WARNING]
> **🔁 Já caiu duas vezes — dez/2024 e dez/2025 (questão 32):** "O que caracteriza uma interface CLI?" → **interface monotarefa por linha de comando**. As erradas trocam uma palavra: "**multi**tarefa por linha de comando", "monotarefa com interface **gráfica**", "**multiusuário** por linha de comando", "**compartilhada** por linha de comando". Leia com calma e procure a combinação **monotarefa + linha de comando**.

**Comandos do CMD (Windows) e do terminal Linux:**

| Faz | CMD (Windows) | Linux |
|---|---|---|
| listar arquivos da pasta | `dir` | `ls` |
| entrar numa pasta | `cd pasta` | `cd pasta` |
| voltar uma pasta | `cd ..` | `cd ..` |
| criar pasta | `md pasta` (ou `mkdir`) | `mkdir pasta` |
| apagar pasta | `rd pasta` | `rmdir pasta` / `rm -r pasta` |
| apagar arquivo | `del arq.txt` | `rm arq.txt` |
| copiar | `copy a.txt b.txt` | `cp a.txt b.txt` |
| renomear/mover | `ren` / `move` | `mv` |
| mostrar conteúdo | `type arq.txt` | `cat arq.txt` |
| limpar a tela | `cls` | `clear` |
| mostrar pasta atual | `cd` | `pwd` |
| **criar arquivo digitando** | **`copy con arq.txt`** (termina com Ctrl+Z e Enter) | `cat > arq.txt` (termina com Ctrl+D) |

> [!WARNING]
> **🔁 Já caiu — 2021 (questão 34):** comando do CMD para criar um arquivo pelo teclado **sem editor de texto** → **`copy con`**. (O gabarito oficial marcou "edit", que **é** um editor — erro explicado na questão.)

### 6. Software livre, gratuito e proprietário

| Tipo | Código-fonte | Pode modificar? | Custa? | Exemplos |
|---|---|---|---|---|
| **Software livre** | **aberto** | **sim** (e redistribuir) | pode ser grátis **ou pago** | Linux, LibreOffice, Firefox, GIMP, VS Code (base) |
| **Gratuito (freeware)** | normalmente **fechado** | não | grátis | WhatsApp, Discord, Chrome |
| **Proprietário** | fechado | não | normalmente pago | Windows, Photoshop, Office |

**Livre ≠ grátis.** "Livre" é sobre **liberdade**: usar, **estudar o código**, **modificar** e **distribuir**. Pode-se até cobrar por um software livre.

> [!WARNING]
> **🔁 Já caiu — 2022 (questão 36):** "Software livre é: (A) gratuito, (B) com permissão de alteração no código-fonte" → a certa: "**A e B são verdadeiras, mas nem sempre A implica em B**" (pode ser livre e pago, ou grátis e fechado).

**Desfragmentação** (caiu em 2021, questão 33): num **HD**, os pedaços de um arquivo podem ficar espalhados pelo disco. O desfragmentador **junta os pedaços**, **eliminando as lacunas** e **melhorando o acesso**. Em SSD não se desfragmenta.

### 7. Segurança da informação

**Os três pilares (tríade CID):**

| Pilar | Significa | Exemplo de proteção |
|---|---|---|
| **Confidencialidade** | só quem tem permissão **vê** | senha, criptografia |
| **Integridade** | o dado **não é alterado** sem autorização | assinatura digital, permissões |
| **Disponibilidade** | o dado está **acessível** quando precisa | backup, servidores reserva |

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 17):** "O que a Segurança de Dados visa proteger?" → "**a confidencialidade, integridade e disponibilidade dos dados**".

**Malware** (*malicious software*) = qualquer programa malicioso:

| Tipo | O que faz |
|---|---|
| **Vírus** | se anexa a arquivos e se espalha quando eles são abertos |
| **Worm** (verme) | se espalha **sozinho** pela rede |
| **Cavalo de Troia (trojan)** | finge ser um programa legítimo (um "crack" de jogo) e abre a porta para o atacante |
| **Spyware** | **espiona**: captura senhas, o que você digita |
| **Adware** | enche o computador de **propagandas e pop-ups** |
| **Ransomware** | **sequestra** os arquivos (criptografa) e pede resgate |

**Phishing** = golpe que **imita** um site ou mensagem confiável para roubar senha ou dados ("seu Pix foi bloqueado, clique aqui").

> [!WARNING]
> **🔁 Já caiu — Informática, dez/2025 (questão 13):** PC **lento** e com **pop-ups indesejados mesmo sem navegar** → causa mais provável: **infecção por malware**.

**Boas práticas:** senhas fortes e diferentes; **verificação em duas etapas (2FA)**; atualizar o sistema; antivírus; **backup**; desconfiar de links e de downloads "crackeados".

### 8. Leis da internet: Marco Civil e LGPD

- **Marco Civil da Internet (Lei 12.965/2014)**: a "Constituição da internet" brasileira. Pilares: **neutralidade da rede** (a operadora não pode deixar um site mais lento ou mais rápido por interesse comercial), **privacidade** e **liberdade de expressão**.
- **LGPD — Lei Geral de Proteção de Dados (Lei 13.709/2018)**: regras para empresas coletarem e usarem **dados pessoais** — precisa de finalidade, consentimento e segurança; o titular pode pedir para ver, corrigir e apagar seus dados.

> [!WARNING]
> **🔁 Já caiu — Informática para Internet, dez/2024 (questão 31):** princípio do Marco Civil → **neutralidade da rede**, que proíbe discriminar ou priorizar tráfego.

### ❌ Erros clássicos de iniciante

> [!CAUTION]
> - **Ler os restos de cima para baixo** na conversão — é **de baixo para cima**.
> - **Achar que 11 em hexa é "A"**: A = 10, **B = 11**, C = 12, D = 13, E = 14, F = 15.
> - **Esquecer que RAM é volátil** (apaga ao desligar) e ROM não.
> - **Trocar CLI com GUI**: CLI é **texto/linha de comando**; GUI é **gráfica**.
> - **Trocar multitarefa com multiusuário**: tarefas = programas; usuários = pessoas.
> - **Achar que software livre = grátis.**
> - **Confundir agente com vetor de ataque**: vírus/worm/trojan são malware; phishing é golpe de engenharia social.

### Exercícios resolvidos

<details class="recall-box">
<summary>🧠 Exercício 1 — Converta 45 para binário.</summary>

Casas: 32, 16, 8, 4, 2, 1. 45 − 32 = 13 → 1; 13 < 16 → 0; 13 − 8 = 5 → 1; 5 − 4 = 1 → 1; 1 < 2 → 0; 1 − 1 = 0 → 1. **45 = 101101₂**. (Ímpar → termina em 1 ✔.)

</details>

<details class="recall-box">
<summary>🧠 Exercício 2 — Qual o decimal de 3C₁₆?</summary>

3 × 16 + C (12) = 48 + 12 = **60**.

</details>

<details class="recall-box">
<summary>🧠 Exercício 3 — Qual o hexadecimal de 255? E de 100?</summary>

255 ÷ 16 = 15 (240), resto 15 → **FF**. 100 ÷ 16 = 6 (96), resto 4 → **64₁₆** (cuidado: é "seis-quatro" em hexa, que vale 100 em decimal).

</details>

<details class="recall-box">
<summary>🧠 Exercício 4 — Classifique como entrada, saída ou entrada e saída: teclado, impressora, pendrive, microfone, monitor touch.</summary>

Teclado → entrada; impressora → saída; pendrive → entrada e saída; microfone → entrada; monitor touch → entrada e saída.

</details>

<details class="recall-box">
<summary>🧠 Exercício 5 — Qual memória perde os dados quando o computador desliga? (A) ROM (B) HD (C) SSD (D) RAM (E) BIOS</summary>

**D — RAM** (volátil).

</details>

<details class="recall-box">
<summary>🧠 Exercício 6 — No CMD, qual sequência entra na pasta "etec", cria a pasta "ds" dentro dela e lista o conteúdo?</summary>

```text
cd etec
md ds
dir
```

</details>

<details class="recall-box">
<summary>🧠 Exercício 7 — Um programa bloqueia seus arquivos e exige pagamento em criptomoeda. É: (A) adware (B) worm (C) ransomware (D) spyware (E) firewall</summary>

**C — ransomware** (sequestro de dados). Firewall nem é malware: é uma proteção que filtra o tráfego da rede.

</details>

<details class="recall-box">
<summary>🧠 Exercício 8 — "Ninguém além do aluno e da secretaria pode ver as notas dele." Que pilar da segurança é esse?</summary>

**Confidencialidade.**

</details>

### 🖥️ Mão na massa (30 minutos)

1. **Conversões sem calculadora** (depois confira na aba **Prática** deste dia, que tem um conversor interativo): converta para binário e para hexadecimal os números **19, 64, 127, 187, 250**.
2. **CMD de verdade** (no Windows): aperte **Win + R**, digite `cmd` e Enter. Faça:
   - `cd Desktop` (ou `cd Área de Trabalho`), `md teste-etec`, `cd teste-etec`;
   - `copy con notas.txt`, digite duas linhas, aperte **Ctrl + Z** e Enter;
   - `type notas.txt`, `dir`, `cls`.
3. Abra o **Gerenciador de Tarefas** (Ctrl + Shift + Esc) → aba **Desempenho**: veja quanta RAM seu PC tem, quanto está em uso, e se o disco é HD ou SSD.

<details class="recall-box">
<summary>✅ Respostas do item 1</summary>

| Decimal | Binário | Hexadecimal |
|---|---|---|
| 19 | 10011 | 13 |
| 64 | 1000000 | 40 |
| 127 | 1111111 | 7F |
| 187 | 10111011 | BB |
| 250 | 11111010 | FA |

</details>

### ✅ Resumo de 1 minuto

- **Hardware** (físico) × **software** (programas) × **peopleware** (pessoas).
- **RAM** = temporária, **volátil**; **ROM** = fixa; **HD/SSD** = armazenamento permanente. **BIOS** faz o **POST** e carrega o SO na RAM.
- **Decimal → binário**: divisões por 2, restos **de baixo para cima** (ou pelas casas 128, 64, 32…). Ímpar termina em 1.
- **Decimal → hexa**: divisões por 16; **A=10 … F=15**. **187 = BB** (caiu duas vezes!).
- Binário ↔ hexa: grupos de **4 bits** da direita para a esquerda.
- **SO** gerencia hardware, processos, arquivos e usuários; é a interface entre o usuário e o hardware.
- **CLI = interface monotarefa por linha de comando** (caiu duas vezes!). GUI = gráfica.
- **Multitarefa** = vários programas; **multiusuário** = várias pessoas. **copy con** cria arquivo no CMD.
- **Software livre** = código aberto e liberdade de modificar; **não é o mesmo que grátis**.
- Segurança: **confidencialidade, integridade, disponibilidade**. Pop-ups e lentidão → **malware**. Marco Civil → **neutralidade da rede**.
