Este projeto implementa um simulador de financiamento imobiliário em Python que calcula as prestações pelos sistemas SAC (Sistema de Amortização Constante) e Price (Sistema Francês de Amortização).

## Funcionalidades

- Cálculo de financiamento pelo sistema SAC
- Cálculo de financiamento pelo sistema Price 
- Visualização das parcelas em formato de tabela HTML
- Comparativo entre os dois sistemas
- Configuração flexível de:
  - Valor do imóvel
  - Valor da entrada
  - Taxa de juros anual
  - Prazo em anos

## Como usar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd simulacao_financiamento
```

2. Execute o script principal:
```bash
python main.py
```

3. O programa irá:
   - Calcular as parcelas nos sistemas SAC e Price
   - Gerar uma visualização em HTML com os resultados
   - Mostrar uma tabela comparativa entre os dois sistemas

## Exemplo de uso

```python
valor_imovel = 600_000
entrada = 200_000
taxa_juros_anual = 12  # % ao ano
prazo_anos = 30
amortizacao_adicional = 2000  # Valor adicional de amortização mensal
parcela_total = 7000 # Valor total de prestação + amortização adicional, é priorizado frente amortizacao_adicional

simulacao = Financiamento(valor_imovel, entrada, taxa_juros_anual, prazo_anos, amortizacao_adicional, parcela_total)
parcelas_sac = simulacao.calcular_sac()
parcelas_price = simulacao.calcular_price()
```

## Estrutura do projeto

```
simulacao_financiamento/
│
├── main.py          # Script principal
├── classes.py       # Definição das classes
└── utils.py         # Funções auxiliares
```

## Requisitos

- Python 3.6 ou superior

## Detalhes técnicos

- Sistema SAC: mantém a amortização constante ao longo do financiamento
- Sistema Price: mantém a prestação constante ao longo do financiamento
- Os cálculos consideram:
  - Taxa de juros convertida de anual para mensal
  - Amortização do capital
  - Juros sobre o saldo devedor
  - Prestação total (amortização + juros)

## Licença

MIT