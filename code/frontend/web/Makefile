.PHONY: help dev stop highlight_card teste123 consumer

PROVIDER_DIR := provider
CONSUMER_DIR := simple_bank

help:
	@echo "Comandos disponíveis:"
	@echo "  make dev          - Sobe todos os providers e o consumer"
	@echo "  make highlight_card - Sobe apenas o provider highlight_card (porta 3001)"
	@echo "  make teste123       - Sobe apenas o provider teste123 (porta 3002)"
	@echo "  make consumer       - Sobe apenas o consumer simple_bank (porta 3000)"

dev:
	@echo "Subindo providers e consumer..."
	@cd $(PROVIDER_DIR)/highlight_card && pnpm dev & \
	 cd $(PROVIDER_DIR)/teste123 && pnpm dev & \
	 cd $(CONSUMER_DIR) && pnpm dev

highlight_card:
	cd $(PROVIDER_DIR)/highlight_card && pnpm dev

teste123:
	cd $(PROVIDER_DIR)/teste123 && pnpm dev

consumer:
	cd $(CONSUMER_DIR) && pnpm dev