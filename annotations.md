### Gunicorn

Por default, ao inicializar o webserver (Gunicorn), é utilizada o endereço 120.0.0.1:8000 para disponibilizar a aplicação.
Ao se utilizar um container docker e expôr a porta 8000 para acesso externo ao container, o docker faz isso olhando para o localhost
dentro do container que não é endereçado pelo 127.0.0.1, mas sim pelo 0.0.0.0