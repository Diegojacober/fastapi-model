import requests
import time

def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f"Dutação foi de {tempo_final-tempo_inicial} segundos")
    return wrapper

@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])
    
    
@calcular_tempo

def contar_ate_100():
    for i in range(100):
        ...

pegar_cotacao_dolar()
contar_ate_100()