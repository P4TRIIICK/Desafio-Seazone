# Desafio-Seazone <h1>
## Limpeza de dados <h2>
> Nessa etapa foi realizada algumas alterações nos arquivos "Data/desafio_details.csv" e "Data/desafio_ratings.csv"

De início foi feita o armazenamento dos dados em variáveis
~~~python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Armazenando a tabela numa variável
csvData = pd.read_csv("Data/desafio_details_new.csv", encoding='latin-1', sep = ';')
csvData2 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep = ';')
~~~



