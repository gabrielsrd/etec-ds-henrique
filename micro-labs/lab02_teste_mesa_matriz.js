/**
 * Lab 02 (JavaScript / Node.js):
 * Teste de mesa, matriz 3x3 (diagonal principal), pilha LIFO, tabela verdade e recursividade.
 */

function linha(titulo) {
  console.log("\n" + "=".repeat(62));
  console.log(titulo);
  console.log("=".repeat(62));
}

function demoTesteMesaBinario(numero) {
  linha(`1. TESTE DE MESA (Executar Linha a Linha) — Entrada y = ${numero}`);
  console.log("Algoritmo: enquanto y > 0: resto = y MOD 2; x = resto + x; y = y DIV 2");
  console.log("Passo | y antes | y MOD 2 | y DIV 2 | x (binario)");
  console.log("-".repeat(62));

  let y = numero;
  let x = "";
  let passo = 1;

  while (y > 0) {
    const resto = y % 2;
    const proxY = Math.floor(y / 2);
    x = String(resto) + x;
    console.log(
      `${String(passo).padEnd(5)} | ${String(y).padEnd(7)} | ${String(resto).padEnd(7)} | ${String(proxY).padEnd(7)} | ${x}`
    );
    y = proxY;
    passo += 1;
  }
  console.log(`Resultado: ${numero}(10) = ${x}(2) = ${numero.toString(16).toUpperCase()}(16)`);
}

function demoMatriz3x3() {
  linha("2. MATRIZ BIDIMENSIONAL 3x3 (Questao 10 da Prova 2025)");
  const matriz = [
    [1, 3, 5],
    [2, 4, 8],
    [1, 1, 1],
  ];

  let diagPrincipal = 0;
  let diagSecundaria = 0;
  const n = matriz.length;

  for (let i = 0; i < n; i++) {
    const cols = [];
    for (let j = 0; j < n; j++) {
      const val = matriz[i][j];
      const marca = i === j ? "*" : " ";
      cols.push(`M[${i}][${j}]=${val}${marca}`);
      if (i === j) diagPrincipal += val;
      if (i + j === n - 1) diagSecundaria += val;
    }
    console.log("  " + cols.join("  |  "));
  }

  console.log("\n* Diagonal Principal (linha == coluna): M[0][0] + M[1][1] + M[2][2] =", diagPrincipal);
  console.log(`  (PEGADINHA: Diagonal Secundaria = ${diagSecundaria})`);
}

function demoPilhaLifo() {
  linha("3. PILHA LIFO (Last In, First Out) — PUSH e POP");
  const pilha = [];
  const ops = [
    ["PUSH", 10],
    ["PUSH", 5],
    ["POP", null],
    ["PUSH", 7],
    ["PUSH", 3],
    ["POP", null],
    ["POP", null],
  ];

  for (const [op, val] of ops) {
    let desc;
    if (op === "PUSH") {
      pilha.push(val);
      desc = `PUSH(${val})`;
    } else {
      desc = `POP() -> tirou ${pilha.pop()}`;
    }
    console.log(`  ${desc.padEnd(20)} | Pilha: [${pilha.join(", ")}]`);
  }
}

function demoTabelaVerdade() {
  linha("4. TABELA VERDADE (AND &&, OR ||, NOT !)");
  const fmt = (b) => (b ? "V" : "F");
  console.log("P | Q | P AND Q | P OR Q | NOT P");
  console.log("-".repeat(38));
  for (const p of [true, false]) {
    for (const q of [true, false]) {
      console.log(`${fmt(p)} | ${fmt(q)} | ${fmt(p && q).padEnd(7)} | ${fmt(p || q).padEnd(6)} | ${fmt(!p)}`);
    }
  }
}

function fatorial(n, nivel = 0) {
  const pad = "  ".repeat(nivel);
  console.log(`${pad}-> chamando fat(${n})`);
  if (n <= 1) {
    console.log(`${pad}<- caso base fat(${n}) = 1`);
    return 1;
  }
  const res = n * fatorial(n - 1, nivel + 1);
  console.log(`${pad}<- retorno fat(${n}) = ${res}`);
  return res;
}

demoTesteMesaBinario(10);
demoTesteMesaBinario(250);
demoMatriz3x3();
demoPilhaLifo();
demoTabelaVerdade();
linha("5. RECURSIVIDADE — Fatorial 4!");
console.log("Resultado final: 4! =", fatorial(4));
