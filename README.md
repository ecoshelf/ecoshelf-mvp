# ecoshelf-users-microservice
MVP Projeto Ecoshelf (Startup ONE &amp; Engineering Software Development - FIAP)

Users Microservice

**Como executar?**

Primeiro, clone o repositório:

- git clone https://github.com/ecoshelf/ecoshelf-users-microservice/

Após, faça o build do DockerFile

- docker build .

Ao final do build, será mostrado o hash da imagem, por exemplo:

=> => writing image sha256:fd5a05a4fb4092a33a01668d9b2b26436c15af62ebf466ba07cdd55329f008c1       

Utilizar o hash para executar o container:

- docker run -p 8000:8000 sha256:fd5a05a4fb4092a33a01668d9b2b26436c15af62ebf466ba07cdd55329f008c1       

