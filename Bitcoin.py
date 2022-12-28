import requests


def find_bitcoin():
    # Faz uma chamada HTTP à API da CoinMarketCap para obter a cotação atual do bitcoin
    response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', headers={'X-CMC_PRO_API_KEY': '57c5e4f0-33f9-4a48-976b-c3f610ea5ffe'})

    # Verifica se a chamada foi bem-sucedida
    if response.status_code == 200:
        # Carrega os dados da resposta em um dicionário
        data = response.json()

        # Obtém a cotação do bitcoin a partir do dicionário
        bitcoin_quote = data['data'][0]['quote']['USD']

        # Obtém o preço atual do bitcoin a partir da cotação
        bitcoin_price = bitcoin_quote['price']

        bitcoin_price = round(bitcoin_price,2)

        # Imprime o preço atual do bitcoin
        print(f'Preço atual do bitcoin: {bitcoin_price}')
    else:
        # A chamada à API falhou, imprime o código de status da resposta
        print(f'Erro ao obter cotação do bitcoin: {response.status_code}')
