import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData1, columns=['hotel_name', 'city_name'])
csvData4 = pd.DataFrame(csvData2, columns=['Total', 'hotel_name'])

#Unir as duas listas para pegar somente as listangens com url no booking.com
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Removendo linhas repetidas 
csvData5 = csvData5.drop_duplicates(subset='hotel_name')

#Filtro para excluir os locais sem avaliação
filtro = csvData5['Total'] > 0
csvData5 = csvData5[filtro]

#Criando uma tabela com a contagem de avaliações por cidade
cidades_avaliadas1 = csvData5.groupby(['city_name'], as_index=False)['Total'].mean()

#Ordenei a tabela em ordem do mais avaliado para o menos avaliado
cidades_avaliadas1.sort_values(["Total"], axis=0,ascending=[False], inplace=True)

#Selecionando colunas específicas
avaliacao = cidades_avaliadas1['Total']
cidades = cidades_avaliadas1['city_name']

#Gráfico
plt.figure(figsize=(8, 6))
plt.bar(cidades, avaliacao)
plt.xticks(rotation=80)
plt.xlabel('Cidade')
plt.ylabel('Média')
plt.title('Cidades com Maior e Menor Média de Avaliações')
plt.tight_layout()
plt.show()
