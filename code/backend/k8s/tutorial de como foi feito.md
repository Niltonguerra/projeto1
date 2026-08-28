## pre requisitos:
| Ferramenta                | Finalidade                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **kubectl**               | Interface de linha de comando (CLI) oficial para gerenciar clusters Kubernetes.                                                                        |
| **Kind** ou **Minikube**  | Criação de um cluster Kubernetes local para desenvolvimento e testes.                                                                                  |
| **Helm**                  | Gerenciador de pacotes do Kubernetes, utilizado para instalar e gerenciar aplicações por meio de *Helm Charts* (como RabbitMQ, Kafka e Elasticsearch). |
| **Docker**                | Construção das imagens dos serviços que serão executados no cluster Kubernetes.                                                                        |
| **Skaffold** *(opcional)* | Automatiza o ciclo de desenvolvimento no Kubernetes, realizando build, deploy e atualização (*hot reload*) das aplicações durante o desenvolvimento.   |


## Design de infraestrutura:
```
k8s/
├── namespaces/
│   ├── infra.yaml
│   └── services.yaml
├── infra/
│   └──  postgres.yaml
├── helm/
│   ├── elasticsearch-values.yaml   # values do helm
│   ├── rabbitmq-values.yaml
│   └── kafka-values.yaml
├── services/
│   ├── account-service.yaml
│   ├── payment-service.yaml
│   ├── transaction-service.yaml
│   └── ...
├── config/
│   ├── secrets/
│   └── configmaps/
├── ingress/
│   └── api-gateway.yaml
├── istio/
│   └── PeerAuthentication.yaml
└── Makefile  # atalhos para apply, delete, logs
```




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

- criar o cluster
```
kind create cluster --name banco-simplificado
```

- criar e configurar a comunicação mTls
  - Istio é a opção mais completa
    - Com Istio ativo, o mTLS entre pods do namespace services é automático via sidecar.
````bash
istioctl install --set profile=demo -y
kubectl label namespace services istio-injection=enabled
````


## criar os secrets do ambiente

### Secret do Postgres
Postgres (leitura — CQRS)
```bash
kubectl create secret generic postgres-secret \
--from-literal=username=banco_user \
--from-literal=password=sua_senha_aqui \
-n infra
```

### comando para criar Chart do elasticSearch
Elasticsearch (leitura — CQRS)
```bash
helm repo add elastic https://helm.elastic.co
helm install elasticsearch elastic/elasticsearch \
--namespace infra \
--set replicas=1 \
--set resources.requests.memory=512Mi \
--set resources.limits.memory=1Gi
```

### comandos para criar  Chart do rabbitMQ
broker principal
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install rabbitmq bitnami/rabbitmq \
--namespace infra \
--set auth.username=admin \
--set auth.password=sua_senha_aqui \
--set replicaCount=1
```


### comando para criar o chart do airflow
```bash
helm install airflow apache-airflow/airflow \
  --namespace infra \
  --values k8s/helm/airflow-values.yaml
```

### comandos para criar  Chart do Kafka
path específico
```bash
helm install kafka bitnami/kafka \
--namespace infra \
--set replicaCount=1 \
--set zookeeper.replicaCount=1
```


## comandos utéis

criar namespaces:
```bash 
kubectl apply -f namespaces/infra.yaml
```

verificar namespaces criados:
``` bash
kubectl get namespaces
```
lista todos os recursos no cluster:
```bash
kubectl get all -n infra
```



## Referências
- [Kubernetes Docs](https://kubernetes.io/docs/) 
- [Helm Hub](https://artifacthub.io/)
- [Istio Getting Started](https://istio.io/latest/docs/setup/getting-started/)
- [kind — Kubernetes in Docker](https://kind.sigs.k8s.io/)