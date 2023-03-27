Faturamento_mensal = { 'SP' : 67836.43 ,  'RJ' : 36678.66 ,  'MG' : 29229.88 ,
                        'ES' : 27165.48 ,  'Outros' : 19849.53 }

valor_total = sum(Faturamento_mensal.values())

lista = []

for estado in Faturamento_mensal.values():
    aux = estado / valor_total
    lista.append(round(aux * 100 , 2))

aux = 0 

for estado in Faturamento_mensal.keys():
    print(estado, lista[aux])
    aux = aux + 1