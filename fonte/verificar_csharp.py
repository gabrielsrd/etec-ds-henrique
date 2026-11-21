"""Compila e executa todos os blocos ```csharp das aulas (fonte/aulas/*.md) usando o SDK .NET no Docker.

- Blocos com "nocheck" no cabeçalho (```csharp nocheck) são trechos ilustrativos e são pulados.
- Blocos sem "class " são embrulhados em um Main.
- Entrada do teclado: ```csharp in=7|8  (cada | vira uma linha digitada).
Uso: python3 fonte/verificar_csharp.py [dia_02.md ...]
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FONTE = Path(__file__).resolve().parent
BLOCK = re.compile(r"^```csharp([^\n]*)\n(.*?)^```", re.M | re.S)


def blocos(md_text):
    for m in BLOCK.finditer(md_text):
        info, code = m.group(1), m.group(2)
        # ignora blocos dentro de citações (linhas começando com "> ")
        start = md_text.rfind("\n", 0, m.start()) + 1
        if md_text[start:m.start()].strip().startswith(">"):
            continue
        yield info.strip(), code


def main():
    arquivos = sys.argv[1:] or sorted(p.name for p in (FONTE / "aulas").glob("dia_*.md"))
    casos = []
    for nome in arquivos:
        txt = (FONTE / "aulas" / nome).read_text(encoding="utf-8")
        for i, (info, code) in enumerate(blocos(txt), start=1):
            if "nocheck" in info:
                continue
            entrada = ""
            m = re.search(r"in=(\S+)", info)
            if m:
                entrada = "\n".join(m.group(1).split("|")) + "\n"
            casos.append((f"{nome}#{i}", code, entrada))
    if not casos:
        print("nenhum bloco")
        return
    with tempfile.TemporaryDirectory(dir=os.environ.get("VERIF_TMP")) as tmp:
        tmp = Path(tmp)
        (tmp / "v.csproj").write_text(
            '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType>'
            '<TargetFramework>net8.0</TargetFramework><ImplicitUsings>disable</ImplicitUsings>'
            '<Nullable>disable</Nullable><StartupObject>Runner</StartupObject>'
            '<NoWarn>CS0168;CS0219;CS8321;CS0162</NoWarn></PropertyGroup></Project>')
        disp = []
        for k, (nome, code, _) in enumerate(casos):
            ns = f"S{k}"
            if "class " in code:
                usings = "\n".join(l for l in code.splitlines() if l.startswith("using "))
                body = "\n".join(l for l in code.splitlines() if not l.startswith("using "))
                src = f"{usings or 'using System;'}\nnamespace {ns} {{\n{body}\n}}\n"
            else:
                src = f"using System;\nnamespace {ns} {{ class Program {{ static void Main() {{\n{code}\n}} }} }}\n"
            (tmp / f"s{k}.cs").write_text(src)
            disp.append(f'case {k}: {{ var t = typeof({ns}.Program); var m = t.GetMethod("Main", '
                        f'System.Reflection.BindingFlags.Static|System.Reflection.BindingFlags.Public|System.Reflection.BindingFlags.NonPublic); '
                        f'm.Invoke(null, m.GetParameters().Length == 0 ? null : new object[]{{ new string[0] }}); break; }}')
        (tmp / "Runner.cs").write_text(
            "using System;\nclass Runner { static void Main(string[] a) { "
            "System.Globalization.CultureInfo.DefaultThreadCurrentCulture = new System.Globalization.CultureInfo(\"en-US\");"
            "System.Threading.Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo(\"en-US\");"
            "switch (int.Parse(a[0])) { " + "\n".join(disp) + " } } }\n")
        own = f"chown -R {os.getuid()}:{os.getgid()} /src"
        docker = ["docker", "run", "--rm", "-i", "-v", f"{tmp}:/src", "-w", "/src", "-e", "DOTNET_CLI_TELEMETRY_OPTOUT=1",
                  "-e", "DOTNET_NOLOGO=1", "mcr.microsoft.com/dotnet/sdk:8.0"]
        r = subprocess.run(docker + ["bash", "-c", f"dotnet build -o out -v q -nologo; rc=$?; {own}; exit $rc"], capture_output=True, text=True)
        if r.returncode != 0:
            erros = [l for l in r.stdout.splitlines() if "error" in l]
            if not erros:
                print(r.stdout[-3000:], r.stderr[-2000:])
            for l in erros[:40]:
                m = re.search(r"/src/s(\d+)\.cs\((\d+)", l)
                quem = casos[int(m.group(1))][0] if m else "?"
                print(f"ERRO [{quem}] {l.split(': error ')[-1][:160]}")
            sys.exit(1)
        script = " ; ".join(
            f"echo '===== {nome}' ; printf %s {sh(entrada)} | dotnet out/v.dll {k}" for k, (nome, _, entrada) in enumerate(casos))
        r = subprocess.run(docker + ["bash", "-c", script + f" ; {own}"], capture_output=True, text=True)
        print(r.stdout)
        if r.stderr.strip():
            print("STDERR:", r.stderr[-2000:])


def sh(s):
    return "'" + s.replace("'", "'\\''") + "'"


if __name__ == "__main__":
    main()
