import dados

def dividir_investimento(total_investimento):
    total_investimento = float(total_investimento)
    dados_fiss = dados.obter_dados()

    def calcular_cotas(total_investimento, porcentagem, ticker):
        if total_investimento == 0:
            return (ticker, 0, 0)
        for fundo in dados_fiss:
            if fundo['ticker'] == ticker:
                valor_para_investir = (porcentagem / 100) * total_investimento
                quantidade_cotas = valor_para_investir // fundo['current_price']
                if quantidade_cotas < 1:
                    return (ticker, 0, 0)
                valor = quantidade_cotas * fundo['current_price']
                return (ticker, quantidade_cotas, valor)
        return (ticker, 0, 0)

    galpao_logistico = calcular_cotas(total_investimento, 40, 'HGLG11')
    fundos_fundos = calcular_cotas(total_investimento, 18, 'HFOF11')
    papel = calcular_cotas(total_investimento, 17, 'MXRF11')
    tijolo = calcular_cotas(total_investimento, 17, 'VILG11')
    hibrido = calcular_cotas(total_investimento, 8, 'RZTR11')

    calculo_porcentagem = [
        galpao_logistico,
        fundos_fundos,
        papel,
        tijolo,
        hibrido
    ]

    return calculo_porcentagem
