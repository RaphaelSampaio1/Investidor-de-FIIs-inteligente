import yfinance as yf
import raspagem as rp

def obter_dados():
    tickers = ['HFOF11.SA','HGLG11.SA','MXRF11.SA','VILG11.SA','RZTR11.SA']
    dados_fiss = []

    for ticker in tickers:
        empresas = yf.Ticker(ticker)

        # Obtendo os valores necessários
        current_price = empresas.info.get('currentPrice')
        market_cap = empresas.info.get('marketCap'[0], 0)
        shares_outstanding = empresas.info.get('sharesOutstanding', 1)

        # Calculando o Valor Patrimonial por Ação
        valor_patrimonial = market_cap / shares_outstanding
        valor_patrimonial = float(f'{valor_patrimonial:.2f}')

        # Obtendo P/VP, se necessário via raspagem
        if market_cap:
            p_vp = current_price / valor_patrimonial
            p_vp = float(f"{p_vp:.2f}")
        else:
            p_vp = rp.raspar_pvp(f'https://statusinvest.com.br/fundos-imobiliarios/{ticker.split(".")[0]}')

        dados_fiss.append({
            'ticker': ticker.replace('.SA', ''),
            'current_price': current_price,
            'valor_patrimonial': valor_patrimonial,
            'p_vp': p_vp
        })
        
    return dados_fiss
