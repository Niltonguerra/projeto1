### Aggregate Root: `Empresa`

```java
public class Empresa {
    private CNPJ cnpj;                    // identidade legal única
    private String razaoSocial;
    private Set<Ticker> tickers;          // uma empresa pode ter várias ações (PETR3, PETR4)
    private Setor setor;                  // enum — crítico para elegibilidade de score
    private GovernancaCorporativa governanca;
    private List<DadosFinanceirosPeriodo> historicoFinanceiro; // ordenado por período
    private DadosMercado dadosMercadoAtual;
}
```



### Value Object: `Setor`

```java
public enum Setor {
    FINANCEIRO(false, false),      // elegível Altman?, elegível MagicFormula?
    VAREJO(true, true),
    SERVICOS(true, true),
    INDUSTRIA(true, true),
    UTILIDADE_PUBLICA(true, false); // Greenblatt também recomenda excluir utilities

    private final boolean elegivelAltman;
    private final boolean elegivelMagicFormula;
    // ...
}
```



### Value Object: `DadosFinanceirosPeriodo` (snapshot, imutável)

```java
public class DadosFinanceirosPeriodo {
    private Periodo periodo;              // ano + trimestre (ou "anual")
    private BigDecimal ativoTotal;
    private BigDecimal ativoCirculante;
    private BigDecimal ativoImobilizadoLiquido;
    private BigDecimal passivoCirculante;
    private BigDecimal passivoTotal;
    private BigDecimal patrimonioLiquido;
    private BigDecimal lucroLiquido;
    private BigDecimal lucroBruto;
    private BigDecimal receita;
    private BigDecimal ebit;
    private BigDecimal ebitda;
    private BigDecimal fluxoCaixaOperacional;
    private BigDecimal dividaLongoPrazo;
    private BigDecimal dividaTotal;
    private BigDecimal caixaEEquivalentes;
    private BigDecimal lucrosRetidos;
    private BigDecimal despesaFinanceira; // NOVO — para NOPLAT 
    private BigDecimal impostosPagos; // NOVO — para NOPLAT
    private long numeroAcoesCirculacao;
}
```



### Value Object: `DadosMercado` (atualizado com frequência, não historicizado do mesmo jeito)

```java
public class DadosMercado {
    private BigDecimal precoAtual;
    private BigDecimal valorDeMercado; // marketCap = preço × ações em circulação
    private Instant atualizadoEm;
}
```




## definir os scores como strategys ao invés de dados em um sgbd
```java
public interface ScoreCalculator {
    boolean isElegivel(Setor setor);
    Score calcular(Empresa empresa, Periodo periodoReferencia);
}

public class AltmanZScoreCalculator implements ScoreCalculator { ... }
public class PiotroskiFScoreCalculator implements ScoreCalculator { ... }

public class MagicFormulaRanking { 
	public List<EmpresaRankeada> calcular(List<Empresa> universo) { // ranking por Earnings Yield + ranking por ROIC → soma de posições 
	} 
}

```













