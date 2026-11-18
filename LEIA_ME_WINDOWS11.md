# Guia Rápido para Windows 11 — Kit ETEC DS (2º Módulo)

Bem-vindo! Este pacote foi preparado para funcionar **no Windows 11 sem precisar configurar ambientes complexos**.

---

## Passo 1 — Extrair o arquivo `.zip` (Muito Importante!)
1. Clique com o **botão direito** no arquivo `Kit_Estudo_ETEC_DS_Windows11.zip`.
2. Escolha **Extrair Tudo...** (*Extract All...*) e salve na sua pasta de Documentos ou Área de Trabalho.
3. **Não tente abrir os arquivos de dentro do `.zip` sem extrair**, senão os links entre as páginas e o PDF não carregam!

---

## Passo 2 — Como Começar em 10 Segundos (Zero Instalação)
Dentro da pasta `estudo-etec-ds`:
* **Opção A (Mais simples):** Dê um duplo clique em **`COMECE_AQUI.html`**. Ele abre no Microsoft Edge ou Google Chrome com botões prontos para:
  * Ler a **Apostila Completa em PDF** (`apostila\Apostila_Completa_ETEC_DS.pdf`)
  * Jogar o **App de Flashcards & Apostas** (`cards-app\index.html`)
  * Abrir as **Provas Reais** (`provas-reais\`)
  * Rodar os **4 Micro-Laboratórios** direto no navegador!
* **Opção B (Menu Automático Windows 11):** Dê um duplo clique em **`INICIAR_ESTUDO_WINDOWS.bat`**.
  * *(Se o Windows Defender SmartScreen mostrar aviso de arquivo baixado, clique em **Mais informações** $\rightarrow$ **Executar assim mesmo**, ou use direto o `COMECE_AQUI.html`.)*

---

## Passo 3 — Colocar os 100 Flashcards no Celular
1. No celular **Android**, baixe o app gratuito **AnkiDroid Flashcards** na Play Store.
2. Envie o arquivo **`flashcards\ETEC_DS_2Modulo_Fundacao_FAT.apkg`** pelo WhatsApp Web para o seu celular e toque para abrir no AnkiDroid.
3. No **iPhone**, instale o **Quizlet** (e cole o texto de `flashcards\quizlet_import_etec.tsv`) ou abra o arquivo **`cards-app\index.html`** pelo navegador!

---

## Passo 4 — (Opcional) Rodar Python no Windows 11
Você **não precisa** instalar nada para estudar (pois o `COMECE_AQUI.html` já simula o Lab 02 e o Lab 03 no navegador). Mas se quiser rodar os scripts `.py` no terminal do Windows 11:
1. Abra o **Terminal** ou **PowerShell** no Windows 11 e digite:
   ```powershell
   winget install -e --id Python.Python.3.12
   ```
2. Feche e reabra o Terminal (ou rode pelo `INICIAR_ESTUDO_WINDOWS.bat` opção `[5]`).
3. Para testar **Cookies reais via HTTP (`localhost:8080`)** no DevTools (`F12`) do Edge/Chrome, use a opção `[6]` do `INICIAR_ESTUDO_WINDOWS.bat` ou rode na pasta `estudo-etec-ds`:
   ```powershell
   python -m http.server 8080
   ```
   E acesse `http://localhost:8080/COMECE_AQUI.html`.
