# Plataforma Henrique — Etec Taboão da Serra (2ª série M-Tec-PI DS)

Assumido pelo Claude Code em 20/11/2026 (o agy foi parado). Um agente só, sem subagentes.
Prova escrita: sex 04/12/2026 13h–17h (40Q, corte 20/40). Prática + entrevista: ter 08/12/2026.
Informação do Henrique (20/11): um amigo que estuda na Etec disse que há vagas sobrando (desistências).

## Fatos verificados (não reabrir)
- Edital nº 02/2026 (M-Tec): 40Q base comum + técnico, corte 50%. Desempate: (a) aluno da Etec, (b) aluno de outra Etec, (c) idade/entrevista. NÃO tem menções MB/B/R/I (isso é do edital do Técnico Modular).
- Resultados: dez/2022 2 classificados (23, 23) → 0 aprovados na prática; dez/2023 1 (22) → 0; dez/2024 1 (21) de 8 → 0; dez/2025 5 (24, 23, 21, 20, 20) de 11 → 0. Total: 0 de 9 na prática em 4 anos. Mediana da escrita ≈ 17/40.
- Provas de Taboão: 30/11/2021 (Informática), 14/12/2022 DS, dez/2023 DS (o PDF diz 13/12/2018 no cabeçalho, mas é de 2023: Q28 cita 2023), 06/12/2024 DS, 05/12/2025 DS + irmãs IPI dez/2024, INF e IPI dez/2025.
- Gabaritos oficiais com erro: 2021 (Q22, 23, 31, 34, 38), 2022 (Q13, 27), dez/2023 (Q3), IPI dez/2024 (Q11, 23, 26, 28, 40). Questões com defeito que repetem com a mesma resposta oficial: inequação (A) e logaritmo (C).
- Dica estratégica: após 04/12, conferir o gabarito e mandar recurso em 48h (e293acad@cps.sp.gov.br).
- Gabarito oficial publicado de dez/2025 NÃO confere com o caderno (outra versão). Usamos gabarito revisado.
- Biologia cai (dez/2024 Q11–12, dez/2025 Q21–22) apesar de não estar na grade do 1º ano.
- O Plano 612 aceita Java, C#, C++ ou Python; C# aparece nas provas de dez/2023 e dez/2024 (não aparece em dez/2025).

## Etapas
- [x] 1. Hotfix publicado em 20/11 (commit e386140)
- [x] 2. Banco: 8 arquivos em fonte/provas/*.md (296 questões, gabarito verificado, explicações didáticas)
- [ ] 3. Mapa de assuntos e repetições (fonte/mapa_provas.md)
- [ ] 4. Aulas profundas dia a dia (fonte/aulas/dia_NN.md)
- [ ] 5. Simulados novos + banco de repetidas + cards
- [ ] 6. 2ª fase (labs + entrevista)
- [ ] 7. Limpeza (FAT, Portugol, cards-app, micro-labs FAT), testes no navegador, publicação

## Decisões de design (20/11)
- Ids de prova: taboao2026 (dez/2025, diagnóstico), taboao2025 (dez/2024, simulado do Dia 9), taboao2023, mtec2022 (mantido por compatibilidade), taboao2021; irmãs = grupo "banco" (só para quizzes).
- Quizzes dos dias 2–8 NÃO usam dez/2024 (fica limpa para o simulado do Dia 9).
- Áreas: 16 (fonte/provas.py AREAS). Remover provas FAT, apostas, sim1, sim2, sim_taboao2027 (gabarito viciado em B).
- Cronograma: 1 diag · 2 Prog I · 3 Prog II · 4 Web I · 5 Web II · 6 BD · 7 APS+Design · 8 Fundamentos (+simulado técnico) · 9 Simulado real dez/2024 · 10 Linguagens (Port, Ing, Arte) · 11 Mat · 12 Natureza (Fís, Quím, Bio) · 13 Humanas + Pesquisa + EdF + véspera · 14–16 laboratório.
