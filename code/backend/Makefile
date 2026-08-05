CLUSTER_NAME := banco-simplificado

.PHONY: help bootstrap destroy namespaces secrets infra helm services ingress istio status cluster load deploy proxy ingress-controller

help:
	@echo "Comandos disponíveis:"
	@echo "  make bootstrap          - Cria todo o ambiente"
	@echo "  make destroy            - Remove o cluster"
	@echo "  make namespaces         - Cria os namespaces"
	@echo "  make secrets            - Cria os secrets"
	@echo "  make helm               - Instala RabbitMQ, Kafka e Elasticsearch"
	@echo "  make infra              - Aplica infraestrutura própria"
	@echo "  make services           - Publica os microsserviços"
	@echo "  make ingress            - Aplica o Ingress"
	@echo "  make ingress-controller - Instala o NGINX Ingress Controller"
	@echo "  make istio              - Instala e configura o Istio"
	@echo "  make status             - Lista os recursos"
	@echo "  make cluster            - Cria o cluster kind"
	@echo "  make load               - Carrega imagens locais no kind"
	@echo "  make deploy             - Publica serviços e ingress"
	@echo "  make proxy              - Expõe o Ingress no Windows via WSL (porta 8080)"

bootstrap: cluster namespaces secrets helm infra ingress-controller

deploy: load services ingress
	kubectl rollout restart deployment -n services

load:
	@for image in banco/crawler-service banco/account-service; do \
		kind load docker-image $$image:latest --name $(CLUSTER_NAME); \
	done

cluster:
	kind create cluster --name $(CLUSTER_NAME)

namespaces:
	kubectl apply -f k8s/namespaces/

secrets:
	kubectl create secret generic postgres-secret \
		--from-literal=username=banco_user \
		--from-literal=password=sua_senha_aqui \
		-n infra || true

helm:
	helm repo add elastic https://helm.elastic.co || true
	helm repo add bitnami https://charts.bitnami.com/bitnami || true
	helm repo update

	helm upgrade --install elasticsearch elastic/elasticsearch \
		-n infra \
		-f k8s/helm/elasticsearch-values.yaml

	helm upgrade --install rabbitmq bitnami/rabbitmq \
		-n infra \
		-f k8s/helm/rabbitmq-values.yaml

	helm upgrade --install kafka bitnami/kafka \
		-n infra \
		-f k8s/helm/kafka-values.yaml

infra:
	kubectl apply -f k8s/infra/

ingress-controller:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/cloud/deploy.yaml
	kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=90s

services:
	@if find k8s/services -maxdepth 1 \( -name "*.yaml" -o -name "*.yml" \) | grep -q .; then \
		kubectl apply -f k8s/services/; \
	else \
		echo "Nenhum manifesto encontrado em k8s/services. Pulando etapa."; \
	fi

ingress:
	kubectl apply -f k8s/ingress/

proxy:
	@echo "Expondo Ingress na porta 8080 — acesse http://banco.local:8080 no Windows"
	@echo "Mantenha esse terminal aberto enquanto usar o cluster"
	kubectl port-forward service/ingress-nginx-controller 8080:80 -n ingress-nginx --address 0.0.0.0

istio:
	istioctl install --set profile=demo -y
	kubectl label namespace services istio-injection=enabled --overwrite
	kubectl apply -f k8s/istio/

status:
	kubectl get all -A

destroy:
	kind delete cluster --name $(CLUSTER_NAME)