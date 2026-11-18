#!/usr/bin/env python3
"""Lab 03: Sublinguagens SQL (DDL, DML, DQL) e Normalizacao na 1FN usando sqlite3 nativo."""

import sqlite3


def titulo(msg: str) -> None:
    print(f"\n{'=' * 64}\n{msg}\n{'=' * 64}")


def mostrar_tabela(cursor: sqlite3.Cursor, sql: str) -> None:
    cursor.execute(sql)
    colunas = [d[0] for d in cursor.description]
    linhas = cursor.fetchall()
    print(" | ".join(colunas))
    print("-" * 52)
    for row in linhas:
        print(" | ".join(str(v) for v in row))


def main() -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    # 1. DDL — Data Definition Language (CREATE / ALTER / DROP)
    titulo("1. DDL (Data Definition Language): CREATE e ALTER TABLE")
    print("Lembrete FAT: DDL mexe na ESTRUTURA, nunca eh SELECT!")
    cur.execute(
        """
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        );
        """
    )
    cur.execute("ALTER TABLE clientes ADD COLUMN ativo INTEGER DEFAULT 1;")
    print("Tabela 'clientes' criada e alterada com sucesso via DDL.")

    # 2. DML — Data Manipulation Language (INSERT / UPDATE / DELETE)
    titulo("2. DML (Data Manipulation Language): INSERT, UPDATE e DELETE")
    cur.executemany(
        "INSERT INTO clientes (nome, cidade) VALUES (?, ?);",
        [
            ("Ana Paula", "São Paulo"),
            ("Bruno Silva", "Campinas"),
            ("Carla Dias", "São Paulo"),
            ("Diego Rocha", "Santos"),
            ("Eduarda Lima", "São Paulo"),
        ],
    )
    cur.execute("UPDATE clientes SET cidade = 'Santos' WHERE nome = 'Bruno Silva';")
    cur.execute("DELETE FROM clientes WHERE nome = 'Diego Rocha';")
    conn.commit()
    mostrar_tabela(cur, "SELECT id, nome, cidade, ativo FROM clientes;")

    # 3. DQL — Data Query Language (SELECT + COUNT + WHERE)
    titulo("3. DQL (Data Query Language): SELECT COUNT(*) ... WHERE")
    query = "SELECT COUNT(*) AS total_sp FROM clientes WHERE cidade = 'São Paulo';"
    print("Executando:", query)
    total = cur.execute(query).fetchone()[0]
    print(f"Resultado: {total} clientes residem em São Paulo.")
    print("ALERTA FAT: Nunca use COUNT() dentro do WHERE!")

    # 4. Normalizacao — Violando e Corrigindo a 1FN (Valores Atomicos)
    titulo("4. 1a FORMA NORMAL (1FN): Valores Atomicos (Indivisiveis)")
    cur.execute("CREATE TABLE alunos_nao_1fn (id INTEGER, nome TEXT, telefones TEXT);")
    cur.execute("INSERT INTO alunos_nao_1fn VALUES (1, 'Carlos', '119999-0000, 118888-1111');")
    print("[ERRADO — Fora da 1FN: multiplos telefones na mesma celula]")
    mostrar_tabela(cur, "SELECT * FROM alunos_nao_1fn;")

    cur.execute("CREATE TABLE alunos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL);")
    cur.execute(
        """
        CREATE TABLE telefones_aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            numero TEXT NOT NULL,
            FOREIGN KEY (aluno_id) REFERENCES alunos(id)
        );
        """
    )
    cur.execute("INSERT INTO alunos VALUES (1, 'Carlos');")
    cur.executemany(
        "INSERT INTO telefones_aluno (aluno_id, numero) VALUES (?, ?);",
        [(1, "119999-0000"), (1, "118888-1111")],
    )
    print("\n[CERTO — Normalizado na 1FN: cada celula tem 1 valor atomico + FK]")
    mostrar_tabela(
        cur,
        """
        SELECT a.id, a.nome, t.numero AS telefone_atomico
        FROM alunos a
        JOIN telefones_aluno t ON t.aluno_id = a.id;
        """,
    )
    conn.close()


if __name__ == "__main__":
    main()
