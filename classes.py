from dataclasses import dataclass
from typing import List
import math

@dataclass
class Parcela:
    numero: int
    amortizacao: float
    amortizacao_adicional: float
    juros: float
    prestacao: float
    saldo_devedor: float
    prestacao_total: float 

class Financiamento:
    def __init__(self, valor_imovel: float, valor_entrada: float, amortizacao_adicional: float, taxa_juros_anual: float, prazo_anos: int):
        self.valor_imovel = valor_imovel
        self.valor_entrada = valor_entrada
        self.valor_financiado = valor_imovel - valor_entrada
        self.taxa_juros_anual = taxa_juros_anual / 100 if taxa_juros_anual > 1 else taxa_juros_anual
        self.taxa_juros_mensal = (1 + self.taxa_juros_anual) ** (1/12) - 1
        self.prazo_meses = prazo_anos * 12
        self.amortizacao_adicional = amortizacao_adicional
        
    def calculo_nova_amortizacao(self, saldo_devedor_atual : float) -> float:
        amortizacao_atual = self.valor_financiado / self.prazo_meses
        proxima_prestacao_estimada = (saldo_devedor_atual - amortizacao_atual) * self.taxa_juros_mensal  + amortizacao_atual
        return round(proxima_prestacao_estimada - (self.taxa_juros_mensal*saldo_devedor_atual), 2)

    def calcular_sac(self) -> List[Parcela]:
        parcelas = []
        amortizacao = self.valor_financiado / self.prazo_meses
        saldo_devedor = self.valor_financiado
        
        for i in range(1, self.prazo_meses + 1):
            saldo_devedor_anterior = saldo_devedor
            juros = saldo_devedor * self.taxa_juros_mensal
            prestacao = amortizacao + juros
            prestacao_total = prestacao + self.amortizacao_adicional
            saldo_devedor = saldo_devedor - amortizacao - self.amortizacao_adicional
            
            if saldo_devedor < 0:
                self.amortizacao_adicional += saldo_devedor
                saldo_devedor = 0
                break
            # if self.amortizacao_adicional > 0:
            #     amortizacao = self.calculo_nova_amortizacao(saldo_devedor_anterior)
            parcela = Parcela(
                numero=i,
                amortizacao=amortizacao,
                amortizacao_adicional=self.amortizacao_adicional,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor=saldo_devedor,
                prestacao_total=prestacao_total
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
            prestacao_total = prestacao + self.amortizacao_adicional
            saldo_devedor = saldo_devedor - amortizacao - self.amortizacao_adicional
            
            if saldo_devedor < 0:
                self.amortizacao_adicional += saldo_devedor
                saldo_devedor = 0
            
            parcela = Parcela(
                numero=i,
                amortizacao=amortizacao,
                amortizacao_adicional=self.amortizacao_adicional,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor=saldo_devedor,
                prestacao_total=prestacao_total
            )
            parcelas.append(parcela)
            
        return parcelas
