import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

faturamento = 0
dia_trabalho = 0
dia_positivo = 0
faturamento_medio = 0
dia_max = 0
dia_min = 0

for dado in dados:
    if dado['valor'] > 0:
        dia_trabalho = dia_trabalho + 1
        faturamento = faturamento + dado['valor']
        if dado['valor'] > dia_max:
            dia_max = dado['valor']

faturamento_medio = faturamento / dia_trabalho
dia_min = dia_max

for dado in dados:
    if dado['valor'] > 0:
        if dado['valor'] < dia_min:
            dia_min = dado['valor']

for dado in dados:
    if dado['valor'] > faturamento_medio:
        dia_positivo = dia_positivo + 1

print(dia_max)
print(dia_min)
print(dia_positivo)