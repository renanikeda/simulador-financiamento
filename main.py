from classes import Financiamento
from utils import gerar_html_tabela, show_table
import numpy as np

def main():
    valor_imovel = 600_000
    entrada = 300_000
    taxa_juros_anual = 12 # % ao ano
    prazo_anos = 30
    amortizacao_adicional = 0  # Valor adicional de amortização mensal
    parcela_total = 7000
    taxa_tr = 0 # % ao ano
    simulacao = Financiamento(valor_imovel, entrada, taxa_juros_anual, taxa_tr, prazo_anos, amortizacao_adicional, parcela_total)
    
    print("\nSimulação SAC:")
    parcelas_sac = simulacao.calcular_sac()
    for i in np.linspace(0, len(parcelas_sac) - 1, 4, dtype=int):
        p = parcelas_sac[i]
        print(f"Parcela {p.numero}: Prestação = R$ {p.prestacao:.2f}, "
              f"Amortização = R$ {p.amortizacao:.2f}, Juros = R$ {p.juros:.2f}, "
              f"Saldo Devedor = R$ {p.saldo_devedor_atualizado:.2f}")
    
    print("\nSimulação Price:")
    parcelas_price = simulacao.calcular_price()
    for i in np.linspace(0, len(parcelas_price) - 1, 4, dtype=int):
        p = parcelas_price[i]
        print(f"Parcela {p.numero}: Prestação = R$ {p.prestacao:.2f}, "
              f"Amortização = R$ {p.amortizacao:.2f}, Juros = R$ {p.juros:.2f}, "
              f"Saldo Devedor = R$ {p.saldo_devedor_atualizado:.2f}")

    html_txt = gerar_html_tabela(parcelas_sac, parcelas_price)
    show_table(html_txt)


if __name__ == "__main__":
    main()
