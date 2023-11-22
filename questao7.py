import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData1 = pd.DataFrame(csvData1, columns=['Localização', 'hotel_name'])

#Removendo linhas repetidas
csvData2 = csvData1.drop_duplicates(subset='hotel_name')

#Formatando cada palavra do anúncio e transformar em uma nova coluna 
csvData2['hotel_name'] = csvData2['hotel_name'].apply(lambda x: str(x).replace('/','').split(' '))
csvData3 = csvData2.explode('hotel_name')
#Removendo os espaços e transformando em minúscula
csvData3['hotel_name'] = csvData3['hotel_name'].str.strip()
csvData3['hotel_name'] = csvData3['hotel_name'].str.lower()

#Filtro para pegar os hoteis com somente avaliação 10
filtro = csvData3['Localização'] > 9.9
csvAux = csvData3[filtro]

#Contando a quantidade de vezes que apareceu a palavra
csvAux['Quantidade'] = csvAux.groupby('hotel_name')['hotel_name'].transform('count')
csvAux.sort_values(["Quantidade"], axis=0,ascending=[False], inplace=True)

#Pegando os que apareceram mais de 20 vezes
filtro = csvAux['Quantidade'] > 20
csvAux = csvAux[filtro]

#Criaçao do gráfico
plt.figure(figsize=(8,4))
plt.title('Palavras presentes em localizações nota 10'); plt.xlabel('Quantidade')
plt.barh(csvAux['hotel_name'],csvAux['Quantidade'], color='#0099ff', )
#Exibição do gráfico
plt.show()

#Pegando todas as avaliações
filtro = csvData3['Localização'] > 0
csvAux = csvData3[filtro]

#Pegando a média das notas associadas a palavra
local = csvAux.groupby(['hotel_name'], as_index=False)['Localização'].mean()

#Média das notas que apareceu praia e mar 
praia = local[local['hotel_name'] == 'praia' ]
mar =  local[local['hotel_name'] == 'mar']
print(praia , mar)


