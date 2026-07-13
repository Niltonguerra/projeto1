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


tipo de setor(financeiro,varejo,serviços e etc) que a empresa está


## abordagens para facilitar a leitura de uma empresa:


### **1. Scores compostos consagrados

#### **Altman Z-Score** (Edward Altman, 1968) 
- Descrição: 
	- combina 5 índices (liquidez, lucros retidos/ativos, EBIT/ativos, valor de mercado/dívida, vendas/ativos) numa única fórmula que gera um número prevendo probabilidade de falência. É citado até hoje em análise de crédito.
##### formula para gerar esse índice:
**1. Z-Score original (1968) — empresas de capital aberto, manufatura**

Z = 1.2×A + 1.4×B + 3.3×C + 0.6×D + 1.0×E

Onde:

- **A** = Capital de Giro / Ativos Totais → (Ativo Circulante − Passivo Circulante) / Ativos Totais
- **B** = Lucros Retidos / Ativos Totais
- **C** = EBIT / Ativos Totais
- **D** = Valor de Mercado do Patrimônio / Passivo Total (valor de mercado das ações / dívida total)
- **E** = Receita / Ativos Totais

**Interpretação:**

- Z > 2.99 → zona segura (baixo risco de falência)
- 1.81 < Z < 2.99 → zona de alerta (cinza)
- Z < 1.81 → zona de perigo (alto risco de falência)

---

**2. Z'-Score — empresas de capital fechado (privadas)**

Mesma estrutura, mas o componente D usa valor contábil do patrimônio líquido em vez de valor de mercado (já que não há preço de ação):

Z' = 0.717×A + 0.847×B + 3.107×C + 0.420×D + 0.998×E

Faixas mudam: Z' > 2.9 seguro, 1.23–2.9 zona cinza, Z' < 1.23 perigo.

---

**3. Z''-Score — empresas não-manufatureiras (serviços, varejo, etc.)**

Remove o componente E (giro de ativos), porque em setores de serviço a relação receita/ativos não é comparável à indústria:

Z'' = 6.56×A + 3.26×B + 6.72×C + 1.05×D

Faixas: Z'' > 2.6 seguro, 1.1–2.6 zona cinza, Z'' < 1.1 perigo.



#### **Piotroski F-Score** (Joseph Piotroski, 2000) 
- Descrição:  
	- pega 9 critérios binários (ROA positivo, fluxo de caixa operacional positivo, ROA crescente, alavancagem caindo, liquidez corrente subindo, etc.) e soma 1 ponto para cada critério atendido. Resultado: um score de 0 a 9. Empresas com F-Score alto (8-9) historicamente superam o mercado — isso tem paper acadêmico com dados de décadas sustentando.
##### formula para gerar esse índice:
**Categoria 1 — Rentabilidade (4 pontos possíveis)**

1. **ROA positivo** → Lucro Líquido / Ativos Totais > 0
2. **Fluxo de Caixa Operacional positivo** → FCO > 0
3. **ROA crescente** → ROA do ano atual > ROA do ano anterior
4. **Qualidade do lucro (accruals)** → Fluxo de Caixa Operacional > Lucro Líquido (indica que o lucro é sustentado por caixa real, não por ajustes contábeis)

**Categoria 2 — Alavancagem, Liquidez e Fonte de Capital (3 pontos possíveis)**

5. **Alavancagem caindo** → Dívida de Longo Prazo / Ativos Totais do ano atual < ano anterior
6. **Liquidez corrente subindo** → (Ativo Circulante / Passivo Circulante) do ano atual > ano anterior
7. **Sem diluição acionária** → Número de ações em circulação do ano atual ≤ ano anterior (empresa não emitiu novas ações, o que indicaria necessidade de captar capital)

**Categoria 3 — Eficiência Operacional (2 pontos possíveis)**

8. **Margem Bruta crescente** → Margem Bruta do ano atual > ano anterior
9. **Giro de Ativos crescente** → (Receita / Ativos Totais) do ano atual > ano anterior

---

**Interpretação:**

- 8-9 pontos → empresa financeiramente forte
- 5-7 pontos → posição neutra/intermediária
- 0-2 pontos → posição financeira fraca (candidata a underperformance, segundo o estudo original de Piotroski)

---

**Dados que você precisa por empresa:**

- Ano atual e ano anterior de: Lucro Líquido, Ativos Totais, Fluxo de Caixa Operacional, Dívida de Longo Prazo, Ativo Circulante, Passivo Circulante, Número de Ações em Circulação, Receita, Lucro Bruto.




#### **Magic Formula** (Joel Greenblatt, "The Little Book That Beats the Market") 
- Descrição: 
	- reduz tudo a apenas 2 índices: Earnings Yield (EBIT/Enterprise Value, mede "barateza") e ROIC (mede "qualidade"). Rankeia empresas nos dois critérios, soma os rankings, e pronto — 2 índices substituindo dezenas.
##### formula para gerar esse índice:
**Componente 1 — Earnings Yield (o quão "barata" a empresa está)**

Fórmula original de Greenblatt:  
**Earnings Yield = EBIT / Enterprise Value (EV)**

Onde:

- **EBIT** = Lucro antes de juros e impostos
- **EV (Enterprise Value)** = Valor de Mercado das Ações + Dívida Total − Caixa e Equivalentes de Caixa

Quanto **maior** o Earnings Yield, mais barata a empresa está em relação ao lucro operacional que gera.

> [!Nota prática]
> como você viu nas fontes brasileiras, é comum usar o inverso — **EV/EBIT** — porque é o dado que plataformas como Fundamentus já disponibilizam pronto. Nesse caso, a lógica se inverte: quanto **menor** o EV/EBIT, mais barata a empresa.

---

**Componente 2 — Return on Capital / ROIC (o quão "boa" a empresa é)**

Fórmula original de Greenblatt:  
**ROC = EBIT / (Capital de Giro Líquido + Ativo Imobilizado Líquido)**

Onde:

- **Capital de Giro Líquido** = Ativo Circulante − Passivo Circulante (excluindo caixa e dívida de curto prazo, na versão mais rigorosa)
- **Ativo Imobilizado Líquido** = Ativo Fixo (imóveis, plantas, equipamentos) líquido de depreciação

Na adaptação brasileira mais comum (a que você já viu no Trader Brasil e QuantBrasil), usa-se o **ROIC** convencional como proxy:

**ROIC = NOPLAT / Capital Investido**

Onde NOPLAT = Lucro Líquido + Resultado Financeiro − Impostos, e Capital Investido = Patrimônio Líquido + Dívida Total − Caixa.

Quanto **maior** o ROIC, mais eficiente a empresa é na geração de retorno sobre o capital que usa.

---

**Combinação final (ranking, não soma direta de valores)**

1. Ranqueie todas as empresas do seu universo pelo Earnings Yield (ou EV/EBIT), da mais barata para a mais cara → atribua posição 1, 2, 3...
2. Ranqueie as mesmas empresas pelo ROIC, da mais eficiente para a menos eficiente → atribua posição 1, 2, 3...
3. Some as duas posições de ranking por empresa
4. Ordene pela soma (menor soma = melhor colocação combinada de "barata + boa")


> [!ponto de atenção]
> **Diferença importante em relação ao Altman e Piotroski:** a Magic Formula não gera um número absoluto interpretável isoladamente (tipo "Z > 2.99 é seguro") — ela só faz sentido **comparativamente**, dentro de um universo de empresas. Isso muda a implementação no seu sistema: Altman e Piotroski você calcula por empresa isolada; Magic Formula exige rodar sobre um conjunto de ações e reordenar toda vez que alguma entra ou sai do universo comparado.




### **2. Redução estatística de dimensionalidade**
#### **Análise Fatorial / PCA (Principal Component Analysis)** 
- Descrição: 
	- técnica estatística que pega múltiplos índices correlacionados (ex: ROE, ROA, ROIC são todos "rentabilidade") e comprime em componentes principais que capturam a maior parte da variância com muito menos variáveis. É o método que fundos quant usam de verdade para reduzir 50 indicadores em 4-5 fatores ortogonais.
##### formula para gerar esse índice:





