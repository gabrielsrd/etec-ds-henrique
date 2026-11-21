# Plataforma de estudos — Etec de Taboão da Serra (2ª série M-Tec-PI DS)

Site: https://gabrielsrd.github.io/etec-ds-henrique/

Preparação para as vagas remanescentes da 2ª série de Desenvolvimento de Sistemas (prova escrita em 04/12/2026, prática e entrevista em 08/12/2026).

## O que tem

- Trilha de 16 dias (13 até a prova escrita, 3 de laboratório), com aulas, prática e quiz de questões reais.
- Todas as provas de 2ª série publicadas pela Etec de Taboão (2021–2025), com gabarito conferido e explicação em cada questão (os PDFs originais estão em `provas-reais/`).
- Treino das questões que a Etec já repetiu, simulados de previsão e a página "Como a Etec monta a prova".
- Aba 2ª fase: três provas práticas simuladas (HTML/CSS, C#, banco de dados) e o ensaio da entrevista.

## Como atualizar

O conteúdo fica em `fonte/` (Markdown e Python). Para gerar o `dados_plataforma.js`:

```bash
python3 fonte/build.py
cp COMECE_AQUI.html index.html   # o GitHub Pages serve o index.html
```

Detalhes, decisões e ferramentas de verificação (compilador C# e SQLite): `fonte/PROGRESSO.md`.
