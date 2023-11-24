import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData1, columns=['hotel_name', 'accommodation_type'])
csvData4 = pd.DataFrame(csvData2, columns=['number_of_ratings', 'hotel_name'])

#Unir as duas listas 
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Removendo linhas repetidas 
csvData5 = csvData5.drop_duplicates(subset='hotel_name')

#Filtro para excluir os locais sem avaliação
filtro = csvData5['number_of_ratings'] > 0
csvData5 = csvData5[filtro]

#Contando a quantidade de avaliações por tipo de acomodação
Quantidade_AV = csvData5.groupby(['accommodation_type'], as_index=False)['number_of_ratings'].sum()

#Contando a quantidade de acomodações 
Quantidade_AC = csvData5['accommodation_type'].value_counts().reset_index()#Ordenei a tabela em ordem do mais avaliado para o menos avaliado

#Ordenando as linhas da coluna
Quantidade_AV.sort_values(["number_of_ratings"], axis=0,ascending=[True], inplace=True)
Quantidade_AC.sort_values(["count"], axis=0,ascending=[True], inplace=True)

#Selecionando colunas específicas
avaliacao = Quantidade_AV['number_of_ratings']
cidades = Quantidade_AV['accommodation_type']


#Gráfico da quantidade de avaliações por acomodação
plt.figure(figsize=(8, 6))
plt.bar(cidades, avaliacao)
plt.xticks(rotation=80)
plt.xlabel('Tipo de acomodação')
plt.ylabel('Quantidade')
plt.title('Tipos de acomodações com mais avaliações')
plt.tight_layout()
plt.show()

#Gráfico da quantidade de acomodações listadas
plt.figure(figsize=(8, 6))
plt.bar(Quantidade_AC['accommodation_type'], Quantidade_AC['count'])
plt.xticks(rotation=80)
plt.xlabel('Tipo de acomodação')
plt.ylabel('Quantidade')
plt.title('Tipos de acomodações com mais avaliações')
plt.tight_layout()
plt.show()
