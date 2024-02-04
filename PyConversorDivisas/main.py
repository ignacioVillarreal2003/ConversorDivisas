import  requests
import os

API_KEY = os.environ.get('EXCHANGE_RATE_API_KEY')
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

def get_Tasas():
    response = requests.get(URL)
    data = response.json()
    if (response.status_code != 200):
        print('Error')
    else:
        return data['conversion_rates']

def get_Divisas():
    print("Valor en USD de cada divisa")
    tasa = get_Tasas()
    divisas = ""
    for e in tasa.keys():
        divisas += f"{e} - {tasa[e]}\n"
    print(divisas)

def convertir_moneda(cantidad, monedaInicial, monedaConvertida, monedas):
    if (monedaInicial != 'USD'):
        cantidad = cantidad / monedas[monedaInicial]
    return cantidad * monedas[monedaConvertida]

def main():
    tasa = get_Tasas()
    if (tasa):
        cantidad = float(input('Ingrese el monto a convertir: '))
        monedaInicial = input('Moneda que quiere convertir: ')
        monedaConvertida = input('Moneda a la cual quiere convertir: ')
        resultado = convertir_moneda(cantidad, monedaInicial, monedaConvertida, tasa)
        print(f'{cantidad} {monedaInicial} = {resultado:.2f} {monedaConvertida}')

get_Divisas()
if __name__ == '__main__':
    main()
