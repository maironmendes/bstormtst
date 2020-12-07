Instalar os seguintes pacotes do python3

sudo apt install python3-pytest-flask
sudo apt install python3-flask-httpauth

exportar a variavel de ambiente 
export TOKEN_PASS=Token

Executar a aplicação:
python3 app.py 

Sera apresentado o seguinte retorno:
python3 app.py 
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8081/ (Press CTRL+C to quit)



Realizar o teste de conexão:
curl -H "Authorization: Token Token" http://localhost:8081/

Ao conectar vai apresentar o seguinte retorno
devops test server flying!!

* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8081/ (Press CTRL+C to quit)
127.0.0.1 - - [07/Dec/2020 10:39:28] "GET / HTTP/1.1" 200 -



