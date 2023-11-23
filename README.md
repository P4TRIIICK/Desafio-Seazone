# Desafio-Seazone <h1>
>Para a elaboração dessas questões, foram utilizadas as bibliotecas pandas para manipulação e análise de dados, juntamente com matplotlib para a construção de gráficos. O estilo visual adotado nos gráficos foi o 'fivethirtyeight'
## Limpeza de dados <h2>
> Nessa etapa foi realizada algumas alterações nos arquivos "Data/desafio_details.csv" e "Data/desafio_ratings.csv"

De início foi feita o armazenamento dos dados em variáveis
~~~python
import pandas as pd

csvData = pd.read_csv("Data/desafio_details.csv", encoding='latin-1', sep = ';')
csvData2 = pd.read_csv("Data/desafio_ratings.csv", encoding='latin-1', sep = ';')
~~~
Em seguida é feita a exclusão de dados repetidos através do método **drop_duplicate** tendo como base a coluna "hotel_id"
~~~python
csvData3 = csvData.drop_duplicates(subset='hotel_id')
csvData4 = csvData2.drop_duplicates(subset='hotel_id')
~~~
Durante uma análise dos dados, identificou-se que alguns anúncios continham a palavra "excluir". Diante desse contexto, interpretou-se a necessidade de eliminar esses anúncios. Para simplificar o processo de exclusão, a coluna "hotel_id" foi convertida em índice (.set_index()), possibilitando a remoção eficiente dos anúncios através do método **.drop()** 
~~~python
csvData3 = csvData3.set_index('hotel_id')
csvData4 = csvData4.set_index('hotel_id')

#Remoção dos dados nos quais estava escrito "Excluir" em hotel_name
csvData3 = csvData3.drop(index=[8726020, 8670985, 8262079, 7894257, 
                           7869137, 10891689, 10846059, 10845958, 
                           10037557, 9724595, 10878457, 10859037,
                           10602273,10534942], axis=0)
csvData4 = csvData4.drop(index=[8726020, 8670985, 8262079, 7894257, 
                           7869137, 10891689, 10846059, 10845958, 
                           10037557, 9724595], axis=0)
~~~
Para concluir o processo, as variáveis foram reconvertidas para o formato CSV utilizando o método **.to_csv**
~~~python
csvData3.to_csv('Data/desafio_details_new.csv', index=True, sep=';', encoding='latin-1')
csvData4.to_csv('Data/desafio_ratings_new.csv', index=True, sep=';', encoding='latin-1')
~~~
## 1. Ordene as cidades em ordem crescente de número de listings <h3>
Para iniciar essa questão foi utilizado ambos arquivos criados em "Limpeza de dados" e foram armazenados em variaveis.
~~~python
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando a tabela numa variável
csvData = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep = ';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep = ';')
~~~
"Os dois arquivos continham colunas que não seriam utilizadas nesta análise. Portanto, foi feita a seleção das colunas a serem utilizadas por meio do **pd.DataFrame**
~~~python
csvData3 = pd.DataFrame(csvData, columns=['hotel_name', 'city_name'])
csvData4 = pd.DataFrame(csvData2, columns=['url', 'hotel_name'])
~~~
Em seguida, procedeu-se com a fusão de ambos os dataframes, incorporando apenas as linhas em que os valores da coluna 'hotel_name' eram semelhantes
~~~python
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])
~~~
Para calcular o número de listagens por cidade, foi empregado o método **.value_counts()** na coluna 'city_name'. Em seguida, a ordenação foi realizada em ordem crescente usando o **.sort_values()**, com o parâmetro ascending ajustado para True. A utilização de **inplace=True** garante que a ordenação seja aplicada diretamente no DataFrame original, e o parâmetro **axis** foi especificado como 0 para indicar que as linhas referentes à coluna 'city_name' seriam ordenadas
~~~python
cidades_listada = csvData5['city_name'].value_counts().reset_index()
cidades_listada.sort_values(["count"], axis=0,ascending=True, inplace=True)
~~~
Concluindo a análise, foi gerado um gráfico para visualizar as informações obtidas, que consistem na quantidade de listagens por cidade
~~~python
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
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/2c88a3b7-cf01-4c5c-92d9-1eae35c3b1a4)

## 2. Ordene as cidades em ordem decrescente de metros quadrados <h4>
O início deste desafio segue um layout comum, no qual os dados são armazenados em variáveis e, posteriormente, são selecionadas as colunas necessárias para a análise
~~~python
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando a tabela numa variável
csvData = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep = ';')

#Coletando as colunas que serão necessárias 
csvData1 = pd.DataFrame(csvData, columns=['city_name', 'room_surface_in_m2'])                                       
~~~
Para melhorar a analise final foi feita a remoção de todos os anuncios que não tinha dados do metro quadrado armazenado na coluna "room_surface_in_m2"
~~~python
#Filtro para eliminar as linhas que não possuem a informação desejada
filtro = csvData1['room_surface_in_m2'] >= 0
csvData1 = csvData1[filtro]
~~~
Ao contrário da questão anterior, desta vez, o método **.groupby()** foi empregado para calcular a média da coluna 'room_surface_in_m2' e atribuí-la a cada cidade presente. Posteriormente, foi realizada uma ordenação utilizando o **.sort_values()**, sendo que, neste caso, o parâmetro ascending foi ajustado para False, indicando uma ordenação decrescente
~~~python
#Coletando as médias de metro quadrado por cidade 
cidades_metroquadrado = csvData1.groupby(['city_name'], as_index=False)['room_surface_in_m2'].mean()

#Ordenando as linhas do com maior metro quadrado para o menor
cidades_metroquadrado.sort_values(["room_surface_in_m2"], axis=0,ascending=False, inplace=True)
~~~
Para concluir esta análise, foi gerado um gráfico que visualiza os resultados finais obtidos após o cálculo da média da coluna 'room_surface_in_m2' para cada cidade e a subsequente ordenação decrescente
~~~python
#Gráfico
plt.figure(figsize=(6,2))
plt.title('Cidades com mais avaliações'); plt.xlabel('Valor')
plt.barh(cidades, avaliacao, color='#0099ff', )
#Exibição do gráfico
plt.show()
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/4a8e9f78-a0ee-413f-b1d1-e0f19fcbb33a)

## 3. Quais cidades têm mais avaliações? <h4>
Padrão
~~~python
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')
~~~
