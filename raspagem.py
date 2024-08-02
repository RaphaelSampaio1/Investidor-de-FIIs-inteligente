from bs4 import BeautifulSoup
import requests

# REQUISIÇÃO
def raspar_pvp(url):
    headers = {'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        # PEGAR P/VP
        pvp_item = soup.find('h3', class_='title m-0', string='P/VP')
        if pvp_item:
            pvp = pvp_item.find_next('strong', class_='value').get_text(strip=True)
            return pvp
        else:
            return "N/A"
    else:
        return "Erro na requisição"
