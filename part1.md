Instalar os seguintes pacotes do python3

sudo apt install python3-pytest-flask
sudo apt install python3-flask-httpauth

exportar a variavel de ambiente 
export TOKEN_PASS=Token

Executar a aplicação:
python3 app.py 

Realizar o teste de conexão:
curl -H "Authorization: Token Token" http://localhost:8081/




