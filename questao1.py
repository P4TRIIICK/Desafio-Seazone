import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando a tabela numa variável
csvData = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep = ';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep = ';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData, columns=['hotel_name', 'city_name'])
csvData4 = pd.DataFrame(csvData2, columns=['url', 'hotel_name'])

#Unir as duas listas para pegar somente as listangens com url no booking.com
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Coletando as a quantidade de listings por cidade e ordenando em ordem crescente
cidades_listada = csvData5['city_name'].value_counts().reset_index()
cidades_listada.sort_values(["count"], axis=0,ascending=True, inplace=True)
#Construção do gráfico
plt.figure(figsize=(10, 6))
plt.bar(cidades_listada['city_name'],cidades_listada['count'])
plt.xticks(rotation=80)
plt.title('Listings por Cidade (Ordem Crescente)')
plt.ylabel('Quantidade')
plt.xlabel('Cidade')
plt.tight_layout()

# Exibição o gráfico
plt.show()
