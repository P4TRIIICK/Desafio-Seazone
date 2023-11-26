import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data\desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data\desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData1, columns=['hotel_name', 'room_facilities'])
csvData4 = pd.DataFrame(csvData2, columns=['Conforto','hotel_name'])

#Unindo as duas tabelas em uma unica e atribuindo a uma váriavel
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Removendo linhas repetidas
csvData5 = csvData5.drop_duplicates(subset='hotel_name')

#Removendo linhas sem avaliações
filtro = csvData5['Conforto'] > 0
csvAux = csvData5[filtro]

#Transformando cada utensílio de uma coluna em uma nova linha
csvData5['room_facilities'] = csvData5['room_facilities'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",'').split(','))
csvAux = csvData5.explode('room_facilities')
csvAux['room_facilities'] = csvAux['room_facilities'].str.strip()
# Primeiro, crie um novo dataframe que contém apenas os hoteis e os utensílios das salas
csvAux2 = csvAux[['Conforto', 'room_facilities']]

# Em seguida, crie colunas dummy para cada utensílio. O valor será 1 se o hotel possuir esse utensílio e 0 caso contrário
csvAux2 = pd.get_dummies(csvAux2, columns=['room_facilities'], prefix='', prefix_sep='')
# Agora, calcule a matriz de correlação entre a classificação de conforto e a presença de cada utensílio nas salas
corrMatrix = csvAux2[csvAux2.columns[1:]].corrwith(csvAux2['Conforto'], method='spearman')
corrMatrix = corrMatrix.sort_values(ascending=False)
# Por fim, exiba a matriz de correlação
# Exibir a matriz de correlação ordenada em ordem decrescente
plt.figure(figsize=(8, 12))

# Converte a série em um DataFrame
correlation_df = pd.DataFrame({'Correlation': corrMatrix.head(10)})

# Transpõe o DataFrame
correlation_df = correlation_df.T

sns.heatmap(correlation_df, annot=True, cmap='coolwarm', linewidths=.5, cbar_kws={'label': 'Correlation'})
plt.title('Correlação com a Nota total')
plt.show()