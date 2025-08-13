from classes import Financiamento
from utils import gerar_html_tabela, show_table
import numpy as np

def main():
    valor_imovel = 600_000
    entrada = 300_000
    taxa_juros_anual = 12  # % ao ano
    prazo_anos = 30
    amortizacao_adicional = 2000  # Valor adicional de amortização mensal
    simulacao = Financiamento(valor_imovel, entrada, amortizacao_adicional, taxa_juros_anual, prazo_anos)
    
    print("\nSimulação SAC:")
    parcelas_sac = simulacao.calcular_sac()
    for i in np.linspace(0, len(parcelas_sac) - 1, 4, dtype=int):
        p = parcelas_sac[i]
        print(f"Parcela {p.numero}: Prestação = R$ {p.prestacao:.2f}, "
              f"Amortização = R$ {p.amortizacao:.2f}, Juros = R$ {p.juros:.2f}, "
              f"Saldo Devedor = R$ {p.saldo_devedor:.2f}")
    
    print("\nSimulação Price:")
    parcelas_price = simulacao.calcular_price()
    for i in np.linspace(0, len(parcelas_price) - 1, 4, dtype=int):
        p = parcelas_price[i]
        print(f"Parcela {p.numero}: Prestação = R$ {p.prestacao:.2f}, "
              f"Amortização = R$ {p.amortizacao:.2f}, Juros = R$ {p.juros:.2f}, "
              f"Saldo Devedor = R$ {p.saldo_devedor:.2f}")

    html_txt = gerar_html_tabela(parcelas_sac, parcelas_price)
    show_table(html_txt)


if __name__ == "__main__":
    main()