import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data\desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data\desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData1, columns=['hotel_name', 'city_name', 'room_facilities'])
csvData4 = pd.DataFrame(csvData2, columns=['Conforto', 'hotel_name'])

#Unindo as duas tabelas em uma unica e atribuindo a uma váriavel
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Removendo linhas repetidas
csvData5 = csvData5.drop_duplicates(subset='hotel_name')

#Removendo linhas sem avaliações
filtro = csvData5['Conforto'] > 0
csvData5 = csvData5[filtro]

#Transformando cada utensílio de uma coluna em uma nova linha
csvData5['room_facilities'] = csvData5['room_facilities'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",'').split(','))
csvAux = csvData5.explode('room_facilities')

#Formatando a escrita das linhas para não haver error na hora de comparar
csvAux['room_facilities'] = csvAux['room_facilities'].str.strip()

#Armazenando a comparação entre cada utensílio por nota 
cidades_avaliadas1 = csvAux.groupby(['room_facilities'], as_index=False)['Conforto'].mean()

#Ordenei a tabela 
cidades_avaliadas1.sort_values(["Conforto"], axis=0,ascending=[False], inplace=True)

#Filtro para obter os utensílios com melhores médias
filtro = cidades_avaliadas1['Conforto'] > 9.5
Aux1 = cidades_avaliadas1[filtro]

#Filtro para obter os utensílios com piores médias 
filtro2 = cidades_avaliadas1['Conforto']  < 8
Aux2 = cidades_avaliadas1[filtro2]

#Selecionando colunas específicas
avaliacao = Aux1['Conforto']
cidades = Aux1['room_facilities']
avaliacao2 = Aux2['Conforto']
cidades2 = Aux2['room_facilities']

#Gráfico dos utensílios com maiores médias
plt.figure(figsize=(8,4))
plt.title('A média das notas de "Conforto" em relação aos utensílios'); plt.xlabel('Média')
plt.barh(cidades, avaliacao, color='#0099ff', )
plt.show()

#Gráfico dos utensílios com piores médias
plt.figure(figsize=(8,4))
plt.title('A média das notas de "Conforto" em relação aos utensílios'); plt.xlabel('Média')
plt.barh(cidades2, avaliacao2, color='#0099ff', )
plt.show()