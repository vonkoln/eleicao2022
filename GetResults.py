# O código é do @BrennoSullivan

import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
)
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for infos in json_data['cand']:

    if int(infos['seq']) in range(1,12):
        candidato.append(infos['nm'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])

df_eleicao = pd.DataFrame(
        list(zip(candidato, votos, porcentagem)),
        columns = ['Candidato', 'Nº de votos', 'Porcentagem']
)

print(df_eleicao)
print(" ")
print("Porcentagem das Urnas Apuradas: " + json_data['pst'] + "%")

