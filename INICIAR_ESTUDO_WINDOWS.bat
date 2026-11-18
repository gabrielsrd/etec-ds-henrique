@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
cd /d "%~dp0"

:MENU
cls
echo ========================================================================
echo   KIT INTENSIVO ETEC DS (2o MODULO - FUNDACAO FAT) - WINDOWS 11
echo ========================================================================
echo.
echo   [1] Abrir Central de Estudos (COMECE_AQUI.html) - RECOMENDADO
echo   [2] Abrir App Gamificado de Cards ^& Apostas (cards-app\index.html)
echo   [3] Abrir Apostila Completa em PDF (apostila\Apostila_Completa_ETEC_DS.pdf)
echo   [4] Abrir Micro-Labs Visuais (Lab 01 Web/Cookies e Lab 04 Design)
echo   [5] Executar Micro-Labs de Terminal (Lab 02 Teste de Mesa e Lab 03 SQL)
echo   [6] Iniciar Servidor Web Local (localhost:8080) p/ testar Cookies no F12
echo   [7] Abrir pasta Flashcards para enviar .apkg ao Celular
echo   [0] Sair
echo.
set /p OP="Escolha uma opcao (0-7): "

if "%OP%"=="1" goto OPT1
if "%OP%"=="2" goto OPT2
if "%OP%"=="3" goto OPT3
if "%OP%"=="4" goto OPT4
if "%OP%"=="5" goto OPT5
if "%OP%"=="6" goto OPT6
if "%OP%"=="7" goto OPT7
if "%OP%"=="0" goto END
goto MENU

:OPT1
call :FIND_PYTHON
if defined PY_CMD (
    echo.
    echo Iniciando servidor local em http://localhost:8765/COMECE_AQUI.html ...
    echo ^(Permite player de video embutido sem Erro 153 e testes reais de Cookies^)
    start "Servidor ETEC DS (localhost:8765)" /MIN cmd /c "%PY_CMD% -m http.server 8765 --bind 127.0.0.1"
    ping -n 2 127.0.0.1 >nul
    start "" "http://localhost:8765/COMECE_AQUI.html"
    goto MENU
)
start "" "%~dp0COMECE_AQUI.html"
goto MENU

:OPT2
start "" "%~dp0cards-app\index.html"
goto MENU

:OPT3
start "" "%~dp0apostila\Apostila_Completa_ETEC_DS.pdf"
goto MENU

:OPT4
start "" "%~dp0micro-labs\lab01_web_cookies.html"
start "" "%~dp0micro-labs\lab04_design_vetor_vs_bitmap.html"
goto MENU

:OPT5
call :FIND_PYTHON
if defined PY_CMD (
    cls
    echo Executando Lab 02 ^(Teste de Mesa, Matriz 3x3 e Pilha^)...
    %PY_CMD% "%~dp0micro-labs\lab02_teste_mesa_matriz.py"
    echo.
    pause
    cls
    echo Executando Lab 03 ^(SQL DDL/DML/DQL e 1FN^)...
    %PY_CMD% "%~dp0micro-labs\lab03_sql_pratico.py"
    echo.
    pause
    goto MENU
)
where node >nul 2>nul
if %errorlevel%==0 (
    cls
    echo Python nao encontrado, executando Lab 02 com Node.js...
    node "%~dp0micro-labs\lab02_teste_mesa_matriz.js"
    echo.
    echo Para o Lab 03 SQL sem instalar nada, use o simulador em COMECE_AQUI.html!
    pause
    goto MENU
)
echo.
echo [!] Python 3 nao encontrado neste Windows 11.
echo [1] Instalar Python 3.12 oficial agora via winget (Windows 11)
echo [2] Abrir COMECE_AQUI.html (simula Lab 02 e Lab 03 direto no navegador!)
echo [0] Voltar
set /p INST="Escolha: "
if "%INST%"=="1" (
    winget install -e --id Python.Python.3.12
    echo Se a instalacao terminou, feche e abra este script novamente.
    pause
) else if "%INST%"=="2" (
    start "" "%~dp0COMECE_AQUI.html"
)
goto MENU

:OPT6
call :FIND_PYTHON
if not defined PY_CMD (
    echo.
    echo [!] Python necessario para o servidor local. Instale na opcao [5] ou abra os arquivos diretamente.
    pause
    goto MENU
)
echo.
echo Servidor iniciado em http://localhost:8080/COMECE_AQUI.html
echo (Para testar Cookies no F12: http://localhost:8080/micro-labs/lab01_web_cookies.html)
echo Feche a janela ou pressione CTRL+C para encerrar o servidor.
start "" "http://localhost:8080/COMECE_AQUI.html"
%PY_CMD% -m http.server 8080
goto MENU

:OPT7
explorer "%~dp0flashcards"
goto MENU

:FIND_PYTHON
set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 -c "import sys" >nul 2>nul
    if !errorlevel!==0 set "PY_CMD=py -3"
)
if not defined PY_CMD (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python -c "import sys; assert sys.version_info[0]==3" >nul 2>nul
        if !errorlevel!==0 set "PY_CMD=python"
    )
)
goto :eof

:END
exit /b 0
