REM -- Sequencia para instalar o Microblog desenvolvido em Flask e Python
CMD
REM --- informar caminho da base de dados na variavel  DATABASE_URL
SET DATABASE_URL=sqlite:///C:\Users\manuel.robalinho\Google Drive\Trab_Academicos\FLASK\microblog\app.db
REM
REM  Posicionar-se na pasta do microblog
cd C:\Users\manuel.robalinho\Google Drive\Trab_Academicos\FLASK\microblog
REM  -----------------------------------------
REM  ativar o ambiente virtual (venv) que tem as bibliotecas Python necessarias
venv\Scripts\activate
REM  -----------------------------------------
REM  Informar o Flask qual o nome do arquivo a executar
SET FLASK_APP=microblog.py
REM ------------------------------------------
REM Chamar o server Localhost que executa o Flask na aplicação definida no parametro FLASK_APP
flask run
