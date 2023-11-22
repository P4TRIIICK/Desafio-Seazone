import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Unindo as duas tabelas em uma unica e atribuindo a uma váriavel
csvData3 = pd.merge(csvData2, csvData1, how='inner', on=['hotel_id'])

#Removendo linhas repetidas 
csvData3 = csvData3.drop_duplicates(subset='hotel_id')

#Armazenando as colunas que serão necesárias para a análise 
csvData4 = pd.DataFrame(csvData3, columns=['hotel_id','city_name' , 'number_of_ratings'])

#Criando uma tabela com a contagem de avaliações por cidade
cidades_avaliadas1 = csvData4.groupby(['city_name'], as_index=False)['number_of_ratings'].sum()

#Estabeleci um filtro para pegar as 5 cidades com mais avaliações
filtro = cidades_avaliadas1['number_of_ratings'] > 50
cidades_avaliadas2 = cidades_avaliadas1[filtro]

#Ordenei a tabela em ordem do mais avaliado para o menos avaliado
cidades_avaliadas2.sort_values(["number_of_ratings"], axis=0, ascending=[False], inplace=True)

#Armazenando dados para o gráfico
avaliacao = cidades_avaliadas2['number_of_ratings']
cidades = cidades_avaliadas2['city_name']

#Gráfico
plt.figure(figsize=(6,2))
plt.title('Cidades com mais avaliações'); plt.xlabel('Valor')
plt.barh(cidades, avaliacao, color='#0099ff', )
#Exibição do gráfico
plt.show()


