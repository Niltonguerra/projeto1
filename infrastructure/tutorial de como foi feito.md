## pre requisitos:
| Ferramenta                | Finalidade                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **kubectl**               | Interface de linha de comando (CLI) oficial para gerenciar clusters Kubernetes.                                                                        |
| **Kind** ou **Minikube**  | Criação de um cluster Kubernetes local para desenvolvimento e testes.                                                                                  |
| **Helm**                  | Gerenciador de pacotes do Kubernetes, utilizado para instalar e gerenciar aplicações por meio de *Helm Charts* (como RabbitMQ, Kafka e Elasticsearch). |
| **Docker**                | Construção das imagens dos serviços que serão executados no cluster Kubernetes.                                                                        |
| **Skaffold** *(opcional)* | Automatiza o ciclo de desenvolvimento no Kubernetes, realizando build, deploy e atualização (*hot reload*) das aplicações durante o desenvolvimento.   |

### como instalar:
```
//instalador:
curl -Lo kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/

//confirmar instalação
kind version
```

```
//instalador:
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

//confirmar instalação:
echo "$(cat kubectl.sha256)  /usr/local/bin/kubectl" | sha256sum --check
```


```
//instalador:
curl -Lo kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/

//confirmar instalação
kind version
```
```
//instalador:
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

//confirmar instalação:
helm version

```


- para instalar o docker basta acessar o site e baixar, link do site: https://www.docker.com/products/docker-desktop/


## comandos para criar o sistema:
```
kind create cluster --name banco-simplificado
```