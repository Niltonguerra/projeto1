# criando um serviço do zero:
- crie o serviço na linguagem que desejar
- crie o DockerFile do service e o docker-compose para rodar localmente
- crie um endpoint para validar a saúde da app com o endpoint ``/health``
- copie o Makefile contido em k8s/scripts dentro da raiz do projeto
  - atualize o makefile para o seu projeto conforme informado no makefile
- execute o comando: 
<br>
cria o arquivo que integra o service ao kind(kubernetes)
```bash
make scaffold
```
Faz o deploy do service no kubernetes:
```bash
make deploy
```

Agora para criar uma rota para acesso do serviço no cluster você 
precisa ir em k8s/ingress e criar uma rota para o service usando NGINX, exemplo:
```yaml
- path: /<rota do ingress que vai ser exposta>(/|$)(.*)
  pathType: ImplementationSpecific
  backend:
    service:
      name: <nome do service dentro do kubernetes(é o mesmo nome que você definiu no makefile na variável SERVICE_NAME)>
      port:
        number: <porta do service que definiu no makefile>
```
depois você precisa na raiz do backend, ou seja, code/backend executar o deploy 
do ingress através do comando:
```bash 
make ingress
```

depois basta aguardar o kubernetes fazer o deploy se seu service, para 
monitorar o deploydo service você pode usar o comando:
```bash
make list
```

pronto, seu serviço está no ar

# após criar um serviço do zero, atualizando o mesmo:
- dentro do service que você criou execute:
```bash
make deploy
```
- depois acompanhe o deploy com o comando:
```bash
make list
```