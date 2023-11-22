import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando a tabela numa variável
csvData = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep = ';')

#Coletando as colunas que serão necessárias 
csvData1 = pd.DataFrame(csvData, columns=['city_name', 'room_surface_in_m2'])                                       

#Filtro para eliminar as linhas que não possuem a informação desejada
filtro = csvData1['room_surface_in_m2'] >= 0
csvData1 = csvData1[filtro]

#Coletando as médias de metro quadrado por cidade 
cidades_metroquadrado = csvData1.groupby(['city_name'], as_index=False)['room_surface_in_m2'].mean()

#Ordenando as linhas do com maior metro quadrado para o menor
cidades_metroquadrado.sort_values(["room_surface_in_m2"], axis=0,ascending=False, inplace=True)

#Construção do gráfico
plt.figure(figsize=(10, 6))
plt.bar(cidades_metroquadrado['city_name'], cidades_metroquadrado['room_surface_in_m2'])
plt.xticks(rotation=80)
plt.title('Média de Metros Quadrados por Cidade (Ordem Decrescente)')
plt.ylabel('Média de Metros Quadrados')
plt.xlabel('Cidade')
plt.tight_layout()
# Exibindo o gráfico
plt.show()