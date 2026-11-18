#!/usr/bin/env python3
"""Lab 02: Teste de mesa, matriz 3x3 (diagonal principal), pilha LIFO e fatorial."""


def linha(titulo: str) -> None:
    print(f"\n{'=' * 62}\n{titulo}\n{'=' * 62}")


def demo_teste_mesa_binario(numero: int) -> None:
    """Executa teste de mesa do algoritmo Portugol (DIV e MOD) da prova FAT."""
    linha(f"1. TESTE DE MESA (Executar Linha a Linha) — Entrada y = {numero}")
    print("Algoritmo: enquanto y > 0: resto = y MOD 2; x = resto + x; y = y DIV 2")
    print(f"{'Passo':<6} | {'y antes':<8} | {'y MOD 2':<8} | {'y DIV 2':<8} | {'x (binario)'}")
    print("-" * 62)

    y = numero
    x = ""
    passo = 1
    while y > 0:
        resto = y % 2  # MOD
        prox_y = y // 2  # DIV
        x = str(resto) + x
        print(f"{passo:<6} | {y:<8} | {resto:<8} | {prox_y:<8} | {x}")
        y = prox_y
        passo += 1
    print(f"Resultado final: {numero}(10) = {x}(2) = {hex(numero)[2:].upper()}(16)")


def demo_matriz_3x3() -> None:
    """Mostra indices [linha][coluna] base 0 e soma da diagonal principal."""
    linha("2. MATRIZ BIDIMENSIONAL 3x3 (Questao 10 da Prova 2025)")
    matriz = [
        [1, 3, 5],
        [2, 4, 8],
        [1, 1, 1],
    ]
    diag_principal = 0
    diag_secundaria = 0
    n = len(matriz)

    for i in range(n):
        linha_fmt = []
        for j in range(n):
            val = matriz[i][j]
            marca = "*" if i == j else " "
            linha_fmt.append(f"M[{i}][{j}]={val}{marca}")
            if i == j:
                diag_principal += val
            if i + j == n - 1:
                diag_secundaria += val
        print("  " + "  |  ".join(linha_fmt))

    print("\n* Elementos com linha == coluna formam a Diagonal Principal:")
    print(f"  M[0][0]({matriz[0][0]}) + M[1][1]({matriz[1][1]}) + M[2][2]({matriz[2][2]}) = {diag_principal}")
    print(f"  (CUIDADO: Diagonal Secundaria = {matriz[0][2]}+{matriz[1][1]}+{matriz[2][0]} = {diag_secundaria} eh pegadinha!)")


def demo_pilha_lifo() -> None:
    """Simula operacoes PUSH e POP em uma pilha (LIFO)."""
    linha("3. PILHA LIFO (Last In, First Out) — PUSH e POP")
    pilha: list[int] = []
    operacoes = [
        ("PUSH", 10),
        ("PUSH", 5),
        ("POP", None),
        ("PUSH", 7),
        ("PUSH", 3),
        ("POP", None),
        ("POP", None),
    ]
    for op, val in operacoes:
        if op == "PUSH" and val is not None:
            pilha.append(val)
            desc = f"PUSH({val})"
        else:
            removido = pilha.pop()
            desc = f"POP() -> tirou {removido}"
        print(f"  {desc:<20} | Pilha atual: {pilha}")
    print(f"Valor residual na pilha: {pilha}")


def fatorial(n: int, nivel: int = 0) -> int:
    """Calcula n! recursivamente imprimindo a pilha de chamadas."""
    recuo = "  " * nivel
    print(f"{recuo}-> chamando fat({n})")
    if n <= 1:
        print(f"{recuo}<- caso base fat({n}) = 1")
        return 1
    res = n * fatorial(n - 1, nivel + 1)
    print(f"{recuo}<- retorno fat({n}) = {res}")
    return res


def demo_tabela_verdade() -> None:
    """Imprime tabela verdade basica de AND (E), OR (OU) e NOT (NAO)."""
    linha("4. TABELA VERDADE (AND ^, OR v, NOT ~)")
    print(f"{'P':<3} | {'Q':<3} | {'P AND Q':<8} | {'P OR Q':<8} | {'NOT P'}")
    print("-" * 42)
    for p in (True, False):
        for q in (True, False):
            fmt = lambda b: "V" if b else "F"
            print(f"{fmt(p):<3} | {fmt(q):<3} | {fmt(p and q):<8} | {fmt(p or q):<8} | {fmt(not p)}")


if __name__ == "__main__":
    demo_teste_mesa_binario(10)
    demo_teste_mesa_binario(250)
    demo_matriz_3x3()
    demo_pilha_lifo()
    demo_tabela_verdade()
    linha("5. RECURSIVIDADE — Fatorial 4! (4 x 3 x 2 x 1)")
    print(f"Resultado final: 4! = {fatorial(4)}")
