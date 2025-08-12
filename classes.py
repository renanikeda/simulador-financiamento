
from dataclasses import dataclass
from typing import List

@dataclass
class Parcela:
    numero: int
    amortizacao: float
    juros: float
    prestacao: float
    saldo_devedor: float

class Financiamento:
    def __init__(self, valor_imovel: float, valor_entrada: float, taxa_juros_anual: float, prazo_anos: int):
        self.valor_imovel = valor_imovel
        self.valor_entrada = valor_entrada
        self.valor_financiado = valor_imovel - valor_entrada
        self.taxa_juros_anual = taxa_juros_anual / 100 if taxa_juros_anual > 1 else taxa_juros_anual
        self.taxa_juros_mensal = (1 + self.taxa_juros_anual) ** (1/12) - 1
        self.prazo_meses = prazo_anos * 12
        
    def calcular_sac(self) -> List[Parcela]:
        parcelas = []
        amortizacao = self.valor_financiado / self.prazo_meses
        saldo_devedor = self.valor_financiado
        
        for i in range(1, self.prazo_meses + 1):
            juros = saldo_devedor * self.taxa_juros_mensal
            prestacao = amortizacao + juros
            saldo_devedor -= amortizacao
            
            parcela = Parcela(
                numero=i,
                amortizacao=amortizacao,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor=saldo_devedor
            )
            parcelas.append(parcela)
            
        return parcelas
    
    def calcular_price(self) -> List[Parcela]:
        parcelas = []
        fator_price = (1 - (1 + self.taxa_juros_mensal) ** -self.prazo_meses) / self.taxa_juros_mensal
        prestacao = self.valor_financiado / fator_price
        saldo_devedor = self.valor_financiado
        
        for i in range(1, self.prazo_meses + 1):
            juros = saldo_devedor * self.taxa_juros_mensal
            amortizacao = prestacao - juros
            saldo_devedor -= amortizacao
            
            parcela = Parcela(
                numero=i,
                amortizacao=amortizacao,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor=saldo_devedor
            )
            parcelas.append(parcela)
            
        return parcelas
