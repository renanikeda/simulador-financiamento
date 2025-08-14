from dataclasses import dataclass
from typing import List
import math

@dataclass
class Parcela:
    numero: int
    saldo_devedor_corrigido: float
    amortizacao: float
    amortizacao_adicional: float
    juros: float
    prestacao: float
    saldo_devedor_atualizado: float
    prestacao_total: float 

class Financiamento:
    def __init__(self, valor_imovel: float, valor_entrada: float, taxa_juros_anual: float, taxa_tr: float = 0,prazo_anos: int = 30, amortizacao_adicional: float = 0, parcela_total: float = 0):
        self.valor_imovel = valor_imovel
        self.valor_entrada = valor_entrada
        self.valor_financiado = valor_imovel - valor_entrada
        self.taxa_juros_anual = taxa_juros_anual / 100
        self.taxa_juros_mensal = round((1 + self.taxa_juros_anual) ** (1/12) - 1, 4)
        self.taxa_tr = taxa_tr / 100
        self.taxa_tr_mensal = round((1 + self.taxa_tr) ** (1/12) - 1, 4)
        self.prazo_meses = prazo_anos * 12
        self.amortizacao_adicional = amortizacao_adicional
        self.parcela_total = parcela_total

    def calculo_novo_prazo(self, saldo_devedor: float, prestacao_ideal: float) -> int:
        return math.floor(saldo_devedor/(prestacao_ideal - saldo_devedor * self.taxa_juros_mensal))
     
    def calculo_nova_amortizacao(self, saldo_devedor: float, prestacao_ideal: float) -> float:
        novo_prazo = self.calculo_novo_prazo(saldo_devedor, prestacao_ideal)
        return round(saldo_devedor / novo_prazo, 2) if novo_prazo > 0 else saldo_devedor


    def calcular_sac_sem_amortizacao(self) -> List[Parcela]:
        parcelas = []
        amortizacao = round(self.valor_financiado / self.prazo_meses, 2)
        saldo_devedor = self.valor_financiado
        
        for i in range(1, self.prazo_meses + 1):
            saldo_devedor_corrigido = round(saldo_devedor * (1 + self.taxa_tr_mensal), 2)
            amortizacao = round(amortizacao * (1 + self.taxa_tr_mensal), 2)
            juros = round(saldo_devedor_corrigido * self.taxa_juros_mensal, 2)
            prestacao = amortizacao + juros
            prestacao_total = prestacao 
            saldo_devedor = saldo_devedor_corrigido - amortizacao
            
            if saldo_devedor < 0:
                saldo_devedor = 0

            parcela = Parcela(
                numero=i,
                saldo_devedor_corrigido=saldo_devedor_corrigido,
                amortizacao=amortizacao,
                amortizacao_adicional=self.amortizacao_adicional,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor_atualizado=saldo_devedor,
                prestacao_total=prestacao_total
            )
            parcelas.append(parcela)
            
            if saldo_devedor == 0: 
                break

        return parcelas
    
    def calcular_sac(self) -> List[Parcela]:
        parcelas_original = self.calcular_sac_sem_amortizacao()
        if self.parcela_total > 0 and self.parcela_total < parcelas_original[0].prestacao:
            raise Exception("Parcela total não pode ser menor que a primeira prestação do SAC.")
        if self.amortizacao_adicional == 0:
            print("Amortização adicional não foi definida, utilizando amortização padrão.")
            return parcelas_original
        
        parcelas = []
        amortizacao = round(self.valor_financiado / self.prazo_meses, 2)
        saldo_devedor = self.valor_financiado
        
        for i in range(1, self.prazo_meses + 1):
            saldo_devedor_corrigido = round(saldo_devedor * (1 + self.taxa_tr_mensal), 2)
            if self.amortizacao_adicional > 0 and i > 1:
                amortizacao = self.calculo_nova_amortizacao(saldo_devedor_corrigido, parcelas_original[i].prestacao)


            juros = round(saldo_devedor_corrigido * self.taxa_juros_mensal, 2)
            prestacao = amortizacao + juros
            prestacao_total = self.parcela_total if self.parcela_total > 0 else prestacao + self.amortizacao_adicional

            amortizacao_adicional = self.amortizacao_adicional if self.parcela_total == 0 else self.parcela_total - prestacao
            saldo_devedor = saldo_devedor_corrigido - amortizacao - amortizacao_adicional

            if saldo_devedor < 0:
                amortizacao_adicional += saldo_devedor
                saldo_devedor = 0
            
            parcela = Parcela(
                numero=i,
                saldo_devedor_corrigido=saldo_devedor_corrigido,
                amortizacao=amortizacao,
                amortizacao_adicional=amortizacao_adicional,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor_atualizado=saldo_devedor,
                prestacao_total=prestacao_total
            )
            parcelas.append(parcela)

            if saldo_devedor == 0: 
                break
        return parcelas
    
    def calcular_price(self) -> List[Parcela]:
        parcelas = []
        fator_price = (1 - (1 + self.taxa_juros_mensal) ** -self.prazo_meses) / self.taxa_juros_mensal
        prestacao = round(self.valor_financiado / fator_price, 2)
        saldo_devedor = self.valor_financiado

        for i in range(1, self.prazo_meses + 1):
            juros = round(saldo_devedor * self.taxa_juros_mensal, 2)
            amortizacao = prestacao - juros
            prestacao_total = prestacao + self.amortizacao_adicional
            saldo_devedor = saldo_devedor - amortizacao - self.amortizacao_adicional
            
            if saldo_devedor < 0:
                self.amortizacao_adicional += saldo_devedor
                saldo_devedor = 0
            
            parcela = Parcela(
                numero=i,
                saldo_devedor_corrigido=saldo_devedor,
                amortizacao=amortizacao,
                amortizacao_adicional=self.amortizacao_adicional,
                juros=juros,
                prestacao=prestacao,
                saldo_devedor_atualizado=saldo_devedor,
                prestacao_total=prestacao_total
            )
            parcelas.append(parcela)
            
        return parcelas
