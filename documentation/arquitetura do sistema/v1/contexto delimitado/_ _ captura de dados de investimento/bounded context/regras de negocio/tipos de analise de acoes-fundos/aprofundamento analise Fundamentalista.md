## Parâmetros usados para a Análise Fundamentalista
- **Rentabilidade**
	- ROE (Return on Equity) — lucro líquido / patrimônio líquido
	- ROA (Return on Assets) — lucro líquido / ativos totais
	- ROIC (Return on Invested Capital) — retorno sobre capital investido, exclui efeito de alavancagem
	- Margem Bruta — (receita - custo) / receita
	- Margem EBITDA — EBITDA / receita
	- Margem Líquida — lucro líquido / receita

- **Endividamento/Alavancagem**
	- Dívida Líquida/EBITDA — capacidade de pagamento da dívida
	- Dívida Líquida/Patrimônio Líquido
	- Índice de Cobertura de Juros (EBIT/Despesa financeira)
	- Grau de Alavancagem Financeira

- **Liquidez**
	- Liquidez Corrente — ativo circulante/passivo circulante
	- Liquidez Seca — (ativo circulante - estoque)/passivo circulante
	- Liquidez Imediata

- **Eficiência Operacional**
	- Giro de Ativos — receita/ativos totais
	- Prazo Médio de Recebimento
	- Prazo Médio de Pagamento
	- Prazo Médio de Estoque
	- Ciclo de Conversão de Caixa

- **Múltiplos de Valuation (relativo)**
	- P/L (Preço/Lucro)
	- P/VP (Preço/Valor Patrimonial)
	- EV/EBITDA
	- EV/EBIT
	- P/S (Preço/Vendas)
	- PEG Ratio (P/L ajustado pelo crescimento)

- **Dividendos**
	- Dividend Yield
	- Payout Ratio (% do lucro distribuído)

- **Fluxo de Caixa**
	- Fluxo de Caixa Operacional
	- Fluxo de Caixa Livre (FCF)
	- FCF Yield (FCF/valor de mercado)

- **Crescimento**
	- CAGR de Receita (histórico, geralmente 3-5 anos)
	- CAGR de Lucro
	- Crescimento de EBITDA

- **Estrutura de Capital/Governança (qualitativo, mas frequentemente quantificado)**
	- Free Float
	- Tag Along
	- Nível de governança na B3 (Novo Mercado, Nível 1, Nível 2)


## abordagens para facilitar a leitura de uma empresa:


### **1. Scores compostos consagrados

#### **Altman Z-Score** (Edward Altman, 1968) 
- Descrição: 
	- combina 5 índices (liquidez, lucros retidos/ativos, EBIT/ativos, valor de mercado/dívida, vendas/ativos) numa única fórmula que gera um número prevendo probabilidade de falência. É citado até hoje em análise de crédito.
##### formula para gerar esse índice:




#### **Piotroski F-Score** (Joseph Piotroski, 2000) 
- Descrição:  
	- pega 9 critérios binários (ROA positivo, fluxo de caixa operacional positivo, ROA crescente, alavancagem caindo, liquidez corrente subindo, etc.) e soma 1 ponto para cada critério atendido. Resultado: um score de 0 a 9. Empresas com F-Score alto (8-9) historicamente superam o mercado — isso tem paper acadêmico com dados de décadas sustentando.
##### formula para gerar esse índice:





#### **Magic Formula** (Joel Greenblatt, "The Little Book That Beats the Market") 
- Descrição: 
	- reduz tudo a apenas 2 índices: Earnings Yield (EBIT/Enterprise Value, mede "barateza") e ROIC (mede "qualidade"). Rankeia empresas nos dois critérios, soma os rankings, e pronto — 2 índices substituindo dezenas.
##### formula para gerar esse índice:






### **2. Redução estatística de dimensionalidade**
#### **Análise Fatorial / PCA (Principal Component Analysis)** 
- Descrição: 
	- técnica estatística que pega múltiplos índices correlacionados (ex: ROE, ROA, ROIC são todos "rentabilidade") e comprime em componentes principais que capturam a maior parte da variância com muito menos variáveis. É o método que fundos quant usam de verdade para reduzir 50 indicadores em 4-5 fatores ortogonais.
##### formula para gerar esse índice:

