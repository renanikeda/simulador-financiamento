
from classes import Parcela
from typing import List
import webbrowser
import os

def gerar_html_tabela(parcelas_sac: List[Parcela], parcelas_price: List[Parcela]) -> str:
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 30px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: right;
            }
            th {
                background-color: #f2f2f2;
                text-align: center;
            }
            h2 {
                color: #333;
            }
        </style>
    </head>
    <body>
    """
    
    # Tabela SAC
    html += "<h2>Simulação SAC</h2>"
    html += """
    <table>
        <tr>
            <th>Parcela</th>
            <th>Prestação</th>
            <th>Amortização</th>
            <th>Juros</th>
            <th>Saldo Devedor</th>
        </tr>
    """
    
    for p in parcelas_sac:
        html += f"""
        <tr>
            <td>{p.numero}</td>
            <td>R$ {p.prestacao:.2f}</td>
            <td>R$ {p.amortizacao:.2f}</td>
            <td>R$ {p.juros:.2f}</td>
            <td>R$ {p.saldo_devedor:.2f}</td>
        </tr>
        """
    
    html += "</table>"
    
    # Tabela Price
    html += "<h2>Simulação Price</h2>"
    html += """
    <table>
        <tr>
            <th>Parcela</th>
            <th>Prestação</th>
            <th>Amortização</th>
            <th>Juros</th>
            <th>Saldo Devedor</th>
        </tr>
    """
    
    for p in parcelas_price:
        html += f"""
        <tr>
            <td>{p.numero}</td>
            <td>R$ {p.prestacao:.2f}</td>
            <td>R$ {p.amortizacao:.2f}</td>
            <td>R$ {p.juros:.2f}</td>
            <td>R$ {p.saldo_devedor:.2f}</td>
        </tr>
        """
    
    html += "</table></body></html>"
    return html

def show_table(html_txt: str):
    with open("temp_page.html", "w") as file:
        file.write(html_txt)

    file_path = os.path.abspath("temp_page.html")
    webbrowser.open(f'file://{file_path}')
