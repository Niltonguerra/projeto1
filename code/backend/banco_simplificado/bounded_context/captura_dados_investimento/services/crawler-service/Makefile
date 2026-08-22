SERVICE_NAME := crawler-service
PORT_SERVICE := 3500
VERSION := 1.0.1
IMAGE_NAME := banco/$(SERVICE_NAME)
CLUSTER_NAME := banco-simplificado
ROOT_DIR := $(shell cd $(dir $(abspath $(lastword $(MAKEFILE_LIST)))) && cd ../../../../../ && pwd)
K8S_DIR := $(ROOT_DIR)/k8s/services


.PHONY: help build dev load deploy scaffold logs list

help:
	@echo "Comandos disponíveis:"
	@echo "  make build      - Builda a imagem de produção"
	@echo "  make run-dev    - Sobe o serviço em modo desenvolvimento"
	@echo "  make load       - Carrega a imagem no cluster Kind"
	@echo "  make scaffold   - Gera os arquivos K8s do serviço"
	@echo "  make deploy     - Build + load + apply no Kind"
	@echo "  make logs       - Exibe os logs do deployment"
	@echo "  make list       - Lista os pods do namespace services"

build:
	docker build --target production -t $(IMAGE_NAME):$(VERSION) .

run-dev:
	docker compose up --build

load:
	kind load docker-image $(IMAGE_NAME):$(VERSION) --name $(CLUSTER_NAME)

scaffold:
	@bash $(ROOT_DIR)/scripts/scaffold.sh $(SERVICE_NAME) $(K8S_DIR) $(PORT_SERVICE) $(VERSION)

deploy: build load
	kubectl apply -f $(K8S_DIR)/
	kubectl rollout restart deployment/$(SERVICE_NAME) -n services

logs:
	kubectl logs -f deployment/$(SERVICE_NAME) -n services

list:
	kubectl get pods -n services