from dataclasses import dataclass
from typing import List
import webbrowser
import os


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

def formatar_valor(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def gerar_html_tabela(parcelas_sac: List[Parcela], parcelas_price: List[Parcela]) -> str:
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 40px;
                font-family: Arial, sans-serif;
            }
            .table-container {
                max-height: 400px;
                overflow-y: auto;
                margin-left: 5%;
                margin-right: 5%;
                margin-bottom: 40px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th {
                position: sticky;
                top: 0;
                background-color: #f2f2f2;
                text-align: center;
                padding: 12px 8px;
                border-bottom: 2px solid #ddd;
            }
            td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: right;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f5f5f5;
            }
            h2 {
                color: #333;
                margin-top: 30px;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>
    """
    
    # Tabela SAC
    html += "<h2>Simulação SAC</h2>"
    html += "<div class='table-container'>"
    html += """
    <table>
        <tr>
            <th>Parcela</th>
            <th>Saldo Devedor Corrigido</th>
            <th>Amortização</th>
            <th>Juros</th>
            <th>Prestação</th>
            <th>Amortização Adicional</th>
            <th>Prestação Total </th>
            <th>Saldo Devedor Atualizado</th>
        </tr>
    """
    
    for p in parcelas_sac:
        html += f"""
        <tr>
            <td>{p.numero}</td>
            <td>{formatar_valor(p.saldo_devedor_corrigido)}</td>
            <td>{formatar_valor(p.amortizacao)}</td>
            <td>{formatar_valor(p.juros)}</td>
            <td>{formatar_valor(p.prestacao)}</td>
            <td>{formatar_valor(p.amortizacao_adicional)}</td>
            <td>{formatar_valor(p.prestacao_total)}</td>
            <td>{formatar_valor(p.saldo_devedor_atualizado)}</td>
        </tr>
        """
    
    html += "</table></div>"
    
    # Tabela Price
    html += "<h2>Simulação Price</h2>"
    html += "<div class='table-container'>"
    html += """
    <table>
        <tr>
            <th>Parcela</th>
            <th>Saldo Devedor Corrigido</th>
            <th>Amortização</th>
            <th>Juros</th>
            <th>Prestação</th>
            <th>Amortização Adicional</th>
            <th>Prestação Total </th>
            <th>Saldo Devedor Atualizado</th>
        </tr>
    """
    
    for p in parcelas_price:
        html += f"""
        <tr>
            <td>{p.numero}</td>
            <td>{formatar_valor(p.saldo_devedor_corrigido)}</td>
            <td>{formatar_valor(p.amortizacao)}</td>
            <td>{formatar_valor(p.juros)}</td>
            <td>{formatar_valor(p.prestacao)}</td>
            <td>{formatar_valor(p.amortizacao_adicional)}</td>
            <td>{formatar_valor(p.prestacao_total)}</td>
            <td>{formatar_valor(p.saldo_devedor_atualizado)}</td>
        </tr>
        """
    
    html += "</table></div></body></html>"
    return html

def show_table(html_txt: str):
    with open("temp_page.html", "w") as file:
        file.write(html_txt)

    file_path = os.path.abspath("temp_page.html")
    webbrowser.open(f'file://{file_path}')
