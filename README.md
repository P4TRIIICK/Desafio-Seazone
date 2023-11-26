# Desafio-Seazone <h1>

*[Limpeza de Dados](https://github.com/P4TRIIICK/Desafio-Seazone/edit/master/README.md#limpeza-de-dados-)

*[Questão 1](https://github.com/P4TRIIICK/Desafio-Seazone#1-ordene-as-cidades-em-ordem-crescente-de-n%C3%BAmero-de-listings-)

*[Questão 2](https://github.com/P4TRIIICK/Desafio-Seazone#2-ordene-as-cidades-em-ordem-decrescente-de-metros-quadrados-)

*[Questão 3](https://github.com/P4TRIIICK/Desafio-Seazone#3-quais-cidades-t%C3%AAm-mais-avalia%C3%A7%C3%B5es-)

*[Questão 4](https://github.com/P4TRIIICK/Desafio-Seazone#4-quais-cidades-t%C3%AAm-a-maior-m%C3%A9dia-de-avalia%C3%A7%C3%B5es-e-a-menor-m%C3%A9dia-)

*[Questão 5](https://github.com/P4TRIIICK/Desafio-Seazone#5-existem-correla%C3%A7%C3%B5es-entre-as-caracter%C3%ADsticas-de-um-an%C3%BAncio-e-a-sua-localiza%C3%A7%C3%A3o-a-quais-explique-)

*[Questão 6](https://github.com/P4TRIIICK/Desafio-Seazone#6-existem-rela%C3%A7%C3%B5es-entre-a-nota-do-an%C3%BAncio-e-os-recursos-dispon%C3%ADveis-no-im%C3%B3vel-a-quais-explique-)

*[Questão 7](https://github.com/P4TRIIICK/Desafio-Seazone#7-existe-alguma-rela%C3%A7%C3%A3o-entre-a-nota-recebida-e-a-localiza%C3%A7%C3%A3o-a-quais-explique-)

*[Questão 8](https://github.com/P4TRIIICK/Desafio-Seazone#8-o-que-voc%C3%AA-pode-inferir-sobre-as-notas-dos-im%C3%B3veis-)

*[Questão 9](https://github.com/P4TRIIICK/Desafio-Seazone#9-quais-s%C3%A3o-os-an%C3%BAncios-que-te-parecem-cr%C3%ADticos-explique-)

*[Questão 10](https://github.com/P4TRIIICK/Desafio-Seazone#10-quais-outras-an%C3%A1lises-voc%C3%AA-faria-desses-dados-use-sua-criatividade-)

*[Questão 11](https://github.com/P4TRIIICK/Desafio-Seazone#11-como-voc%C3%AA-projetaria-um-dashboard-para-mostrar-essas-informa%C3%A7%C3%B5es-)

*[Questão 12](https://github.com/P4TRIIICK/Desafio-Seazone#12-quais-outras-informa%C3%A7%C3%B5esdados-voc%C3%AA-relacionaria-com-essas-bases-caso-tivesse-acesso-)

*[Questão 13](https://github.com/P4TRIIICK/Desafio-Seazone#13-extra-com-base-nesses-dados-e-nos-an%C3%BAncios-fornecidos-como-voc%C3%AA-melhoraria-as-notas-)

*[Feedback](https://github.com/P4TRIIICK/Desafio-Seazone#feedback-sobre-o-desafio-)

> Para formular essas questões, foi utilizado as bibliotecas pandas para a manipulação e análise de dados, além de matplotlib e seaborn para criar gráficos. Optei pelo estilo visual 'fivethirtyeight' para os gráficos, enquanto a biblioteca nltk foi empregada na representação visual das palavras mais frequentemente utilizadas
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
Posteriormente, ocorreu a fusão das duas tabelas utilizando o método **.merge()**, onde foi especificado o parâmetro 'inner' para juntar apenas as linhas comuns em relação à coluna 'hotel_id'. Em seguida, foram removidas as linhas duplicadas com base na coluna 'hotel_id'. Após esse processo, csvData4 recebeu um novo **pd.DataFrame()** contendo apenas as colunas necessárias para a análise
~~~python
#Unindo as duas tabelas em uma unica e atribuindo a uma váriavel
csvData3 = pd.merge(csvData2, csvData1, how='inner', on=['hotel_id'])

#Removendo linhas repetidas 
csvData3 = csvData3.drop_duplicates(subset='hotel_id')

#Armazenando as colunas que serão necesárias para a análise 
csvData4 = pd.DataFrame(csvData3, columns=['hotel_id','city_name' , 'number_of_ratings'])
~~~
Para calcular a quantidade de avaliações por cidade, foi utilizado o método **.groupby()** para somar o número de 'number_of_ratings' em relação à 'city_name'. Em seguida, foi aplicado um filtro para selecionar as cinco principais cidades com o maior número de avaliações, seguido por uma ordenação utilizando o método **.sort_values()**
~~~python
#Criando uma tabela com a contagem de avaliações por cidade
cidades_avaliadas1 = csvData4.groupby(['city_name'], as_index=False)['number_of_ratings'].sum()

#Estabeleci um filtro para pegar as 5 cidades com mais avaliações
filtro = cidades_avaliadas1['number_of_ratings'] > 50
cidades_avaliadas2 = cidades_avaliadas1[filtro]

#Ordenei a tabela em ordem do mais avaliado para o menos avaliado
cidades_avaliadas2.sort_values(["number_of_ratings"], axis=0, ascending=[False], inplace=True)
~~~
Para concluir, foram armazenadas as colunas desejadas em variáveis e, em seguida, elaborou-se a construção de um gráfico com base nesses dados
~~~python
#Armazenando dados para o gráfico
avaliacao = cidades_avaliadas2['number_of_ratings']
cidades = cidades_avaliadas2['city_name']

#Gráfico
plt.figure(figsize=(6,2))
plt.title('Cidades com mais avaliações'); plt.xlabel('Valor')
plt.barh(cidades, avaliacao, color='#0099ff', )
#Exibição do gráfico
plt.show()
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/a7781563-7f07-47a0-93f6-03fef5b622c8)
## 4. Quais cidades têm a maior média de avaliações? E a menor média? <h5>
Padrão
~~~python
import pandas as pd
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
~~~
Em seguida, realizou-se um filtro para remover as linhas da coluna 'Total' que estavam vazias, aprimorando a análise. Logo após, utilizando o método **.groupby()**, calculou-se a média da coluna 'Total' e atribuiu-se esse valor a cada cidade na tabela. As cidades foram então ordenadas para facilitar a observação dos dados
~~~python

#Filtro para excluir os locais sem avaliação
filtro = csvData5['Total'] > 0
csvData5 = csvData5[filtro]

#Criando uma tabela com a contagem de avaliações por cidade
cidades_avaliadas1 = csvData5.groupby(['city_name'], as_index=False)['Total'].mean()

#Ordenei a tabela em ordem do mais avaliado para o menos avaliado
cidades_avaliadas1.sort_values(["Total"], axis=0,ascending=[False], inplace=True)
~~~
E para finalizar, ocorreu o armazenamento das colunas necessárias para a construção do gráfico, seguido pela elaboração do próprio gráfico
~~~python
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
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/cdc220e3-b2ad-498c-8202-24279a268328)

#### a. Existe alguma explicação para isso? Conjecture. <h6>
> A prevalência de anúncios em Florianópolis influencia uma média inferior, em contraste
com Brasília,Angra dos Reis e Ilhéus, que, apesar de contar com poucos anúncios,
destacam-se por avaliações excepcionais. Nesse contexto, Brasília,Angra dos Reis e
Ilhéus alcançaram a primeira posição devido à qualidade superior de seus escassos
anúncios. Por outro lado, em Camboriú, apesar do número reduzido de anúncios, a média
de avaliações não se revela positiva.
## 5. Existem correlações entre as características de um anúncio e a sua localização? a. Quais? Explique. <h7>
> Sim, todas as características de um imóvel exercem influência em sua avaliação, e a
localização é uma peça chave nesse quebra-cabeça. Mesmo que o imóvel apresente
excelentes comodidades, limpeza e outros atrativos, obtendo avaliações positivas, a
proximidade em relação ao centro ou a pontos turísticos específicos pode impactar
negativamente em sua taxa de ocupação. É possível que, apesar das qualidades do
imóvel, a localização menos estratégica resulte em uma ocupação abaixo do desejado,
demonstrando a importância de considerar não apenas as características internas, mas
também a acessibilidade e conveniência proporcionadas pela localização do imóvel.
## 6. Existem relações entre a nota do anúncio e os recursos disponíveis no imóvel? a. Quais? Explique. <h8>
>Nesta questão, abordei a correlação entre "nota" e "recursos disponíveis" de duas maneiras distintas, registrando cada abordagem em **dois arquivos separados**, nomeados "questao6.py" e "questao6b.py". Essa abordagem foi adotada devido à suspeita de algum equívoco na aplicação da correlação entre essas variáveis. Dessa forma, busquei assegurar uma análise abrangente, explorando diferentes métodos para garantir a precisão dos resultados.

Ambos os arquivos compartilham uma estrutura inicial idêntica, divergindo apenas na seção correspondente ao "questaob.py", que incorpora a biblioteca **seaborn (sns)** para criar a matriz de correlação. As etapas comuns incluem a importação das bibliotecas necessárias, a seleção das colunas relevantes para análise, a eliminação de duplicatas com base na coluna "hotel_name" e a remoção de linhas sem informações, tendo como critério a avaliação de "conforto"
~~~python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

#Armazenando tabelas em variáveis 
csvData1 = pd.read_csv("Data\desafio_details_new.csv", encoding='latin-1', sep=';')
csvData2 = pd.read_csv("Data\desafio_ratings_new.csv", encoding='latin-1', sep=';')

#Alocar somente as colunas necessárias para a análise
csvData3 = pd.DataFrame(csvData1, columns=['hotel_name', 'room_facilities'])
csvData4 = pd.DataFrame(csvData2, columns=['Conforto','Comodidades','Limpeza','Custo-benefício','Localização','Total','WiFi gratuito','hotel_name'])

#Unindo as duas tabelas em uma unica e atribuindo a uma váriavel
csvData5 = pd.merge(csvData3, csvData4, how='inner', on=['hotel_name'])

#Removendo linhas repetidas
csvData5 = csvData5.drop_duplicates(subset='hotel_name')

#Removendo linhas sem avaliações
filtro = csvData5['Conforto'] > 0
csvAux = csvData5[filtro]
~~~
Agora, ao iniciar a análise com o arquivo "questao6.py", realizou-se a conversão de cada palavra de uma linha em uma nova coluna com o método **.explode()**, para facilitar a análise. Posteriormente, efetuou-se uma comparação entre os utensílios da hospedagem e as notas de conforto, visando obter a média de pontuação para cada utensílio. Em seguida, os resultados foram ordenados em ordem decrescente para uma melhor visualização e interpretação
~~~python
#Transformando cada utensílio de uma coluna em uma nova linha
csvData5['room_facilities'] = csvData5['room_facilities'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",'').split(','))
csvAux = csvData5.explode('room_facilities')

#Formatando a escrita das linhas para não haver error na hora de comparar
csvAux['room_facilities'] = csvAux['room_facilities'].str.strip()

#Armazenando a comparação entre cada utensílio por nota 
cidades_avaliadas1 = csvAux.groupby(['room_facilities'], as_index=False)['Conforto'].mean()

#Ordenei a tabela 
cidades_avaliadas1.sort_values(["Conforto"], axis=0,ascending=[False], inplace=True)
~~~
Logo em seguida, aplica-se dois filtros para a geração de dois gráficos distintos, selecionando os utensílios com as maiores médias em um filtro e, em outro, os utensílios com as menores médias. Esses resultados são então armazenados em novas variáveis para facilitar análises subsequentes
~~~python

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
~~~
E para concluir, realiza-se a criação de dois gráficos, um destacando os utensílios com as melhores médias e outro enfocando os utensílios com as piores médias. Isso permite uma observação visual das tendências e variações nas avaliações, fornecendo insights valiosos para a análise
~~~python
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
~~~
![Melhor](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/3abd3610-50e1-41f1-a6a4-65db1b94d799)
![Pior](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/f94a6132-8044-4d47-ae06-b6f785463e30)
Com isso se ver que utensílios como "telefone" e "cartão de acesso" agradam mais os hospedes do que "fontes de monóxido de carbono" 

>Agora, ao iniciar o arquivo 'questao6b.py', onde tenho incertezas sobre sua precisão. Como mencionado anteriormente, o início é semelhante entre os dois scripts
Inicialmente, cada palavra presente nas linhas é transformada em uma nova coluna através do método **.explode()** para simplificar a análise. Em seguida, é criado um novo DataFrame contendo os dados necessários
~~~python
#Transformando cada utensílio de uma coluna em uma nova linha
csvData5['room_facilities'] = csvData5['room_facilities'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",'').split(','))
csvAux = csvData5.explode('room_facilities')
csvAux['room_facilities'] = csvAux['room_facilities'].str.strip()
#Novo dataframe que contém apenas os hoteis e os utensílios das salas
csvAux2 = csvAux[['Conforto', 'room_facilities']]
~~~~
Para simplificar a criação da matriz de correlação, utilizei o método pd.get_dummies, que converte a coluna 'room_facilities' em valores binários (0 ou 1). Isso é feito para evitar discrepâncias nos números atribuídos a cada utensílio, o que poderia levar o método de correlação a interpretar erroneamente a importância relativa entre eles, especialmente quando valores mais altos poderiam ser interpretados como indicativos de maior importância
~~~python
# Colunas dummy para cada utensílio. O valor será 1 se o hotel possuir esse utensílio e 0 caso contrário
csvAux2 = pd.get_dummies(csvAux2, columns=['room_facilities'], prefix='', prefix_sep='')
~~~
Esse trecho de código realiza uma análise de correlação entre a classificação de conforto (contida na coluna 'Conforto') e a presença de cada utensílio nas salas de um hotel. O método utilizado para calcular essa correlação é a correlação de Spearman, uma medida que avalia relações monotônicas, ou seja, relações que não precisam ser necessariamente lineares, mas mantêm uma consistência de tendência.
A função corrwith é utilizada para calcular a correlação entre as colunas que representam a presença de utensílios e a coluna 'Conforto'. Após esse cálculo, a matriz de correlação resultante é ordenada em ordem decrescente. Isso significa que os utensílios com maior correlação positiva com a classificação de conforto estarão no topo da lista, fornecendo insights sobre quais itens podem ter uma influência mais significativa na percepção de conforto pelos usuários
~~~python
# Matriz de correlação entre a classificação de conforto e a presença de cada utensílio nas salas
corrMatrix = csvAux2[csvAux2.columns[1:]].corrwith(csvAux2['Conforto'], method='spearman')
corrMatrix = corrMatrix.sort_values(ascending=False)
~~~
Por fim, o código cria uma visualização da matriz de correlação por meio de um gráfico, utilizando a biblioteca seaborn (sns). Essa representação gráfica oferece uma perspectiva mais intuitiva das relações entre a presença dos utensílios das hospedagens e a classificação de conforto.
~~~python
# Exibir a matriz de correlação ordenada em ordem decrescente
plt.figure(figsize=(8, 12))

# Converte a série em um DataFrame
correlation_df = pd.DataFrame({'Correlation': corrMatrix.head(10)})

# Transpõe o DataFrame
correlation_df = correlation_df.T

sns.heatmap(correlation_df, annot=True, cmap='coolwarm', linewidths=.5, cbar_kws={'label': 'Correlation'})
plt.title('Correlação com a Nota total')
plt.show()
~~~
![Correlacao](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/c53021be-586f-46b6-b690-b4aa5ab550ea)

A correlação de Spearman é uma medida que varia de -1 a 1. Aqui está a interpretação dos valores:

**Correlação de Spearman = 1: Correlação Positiva Perfeita**
Neste caso, quando uma variável aumenta, a outra também aumenta de forma monotônica. Isso indica uma relação positiva perfeita entre as variáveis. Em termos práticos, se uma variável está relacionada à outra por uma função monotônica crescente, a correlação de Spearman será 1.

**Correlação de Spearman = 0: Ausência de Correlação**
Quando o valor é 0, não há uma relação sistemática monotônica entre as variáveis. Isso significa que as mudanças em uma variável não estão relacionadas de maneira consistente às mudanças na outra.

**Correlação de Spearman = -1: Correlação Negativa Perfeita**
Neste cenário, quando uma variável aumenta, a outra diminui de forma monotônica. Indica uma relação negativa perfeita entre as variáveis. Se uma variável está relacionada à outra por uma função monotônica decrescente, a correlação de Spearman será -1.

**Valores Intermediários: Correlações Moderadas e Fracas**
Valores entre -1 e 1 indicam correlações moderadas. Quanto mais próximo de -1 ou 1, mais forte é a relação monotônica. Se o valor estiver próximo de 0, a relação é mais fraca.

O valor mais elevado obtido, que corresponde a "ferro de passar roupa" com uma correlação de 0.035, sugere uma associação extremamente fraca ou praticamente inexistente entre a presença desse utensílio nas acomodações e a nota de conforto. A correlação de Spearman positiva próxima de zero indica que não há uma relação monotônica significativa entre essas variáveis. Em termos práticos, isso sugere que a presença ou ausência do "ferro de passar roupa" não está fortemente vinculada à percepção de conforto, conforme avaliada pelas notas atribuídas. 
## 7. Existe alguma relação entre a nota recebida e a localização? a. Quais? Explique. <h9>
>Para realizar esta análise, utilizei a biblioteca **nltk** para identificar as palavras mais frequentes nos anúncios com avaliações 10

Inicialmente, coleta-se as colunas necessárias para a análise, ativa-se a biblioteca nltk e remove dados duplicados das colunas, utilizando a coluna 'hotel_name' como referência
~~~python
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import nltk

# Certifique-se de ter o nltk baixado. Execute esta linha apenas uma vez.
nltk.download('punkt')

# Ler o CSV e selecionar as colunas relevantes
csvData1 = pd.read_csv("Data/desafio_ratings_new.csv", encoding='latin-1', sep=';')
csvData1 = pd.DataFrame(csvData1, columns=['Localização', 'hotel_name'])

# Remover linhas duplicadas
csvData2 = csvData1.drop_duplicates(subset='hotel_name')
~~~
Posteriormente, aplica-se um filtro para coletar as listagens com nota 10, utilizando como base a avaliação de localização, e, em seguida, transforma-se cada palavra das listagens em uma nova linha da coluna, padronizando todas as linhas em minúsculas
~~~python
#Filtro para pegar os hoteis com somente avaliação 10
filtro = csvData2['Localização'] > 9.9
csvData2 = csvData2[filtro]

#passar cada palavra de um anuncio para uma coluna e formatar a escrita
csvData2['hotel_name'] = csvData2['hotel_name'].apply(lambda x: str(x).replace('/','').split(' '))
csvData3 = csvData2.explode('hotel_name')
csvData3['hotel_name'] = csvData3['hotel_name'].str.strip()
csvData3['hotel_name'] = csvData3['hotel_name'].str.lower()

# Juntar todas as strings em uma única string
all_hotel_names = ' '.join(csvData3['hotel_name'])
~~~
Nesta linha, os nomes dos hotéis contidos na variável all_hotel_names são tokenizados, ou seja, divididos em palavras individuais. A função word_tokenize da biblioteca nltk é utilizada para realizar essa tarefa
~~~python
# Tokenizar as palavras
words = word_tokenize(all_hotel_names)
~~~
Aqui, é criado um objeto FreqDist (distribuição de frequência) a partir da lista de palavras tokenizadas. Esse objeto armazenará a contagem de quantas vezes cada palavra aparece na coleção
~~~python
# Calcular a frequência das palavras
freq_dist = FreqDist(words)
~~~
Finalizando, é gerado um gráfico de frequência para visualizar a distribuição das palavras nos anúncios. O gráfico é plotado usando a biblioteca matplotlib. O eixo x representa as palavras e o eixo y representa a frequência de cada palavra. freq_dist.plot(30, cumulative=False) plota as 30 palavras mais frequentes, e cumulative=False indica que o gráfico não deve ser cumulativo.
~~~python
# Plotar o gráfico de frequência
plt.figure(figsize=(12, 6))
plt.title('Frequência das Palavras nos anúncios')
freq_dist.plot(30, cumulative=False)
plt.show()
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/7cdd5894-1067-4efd-ae45-03cdd64cb9d9)
Observando as 30 palavras mais frequentes nas listagens com avaliação 10, notamos a presença proeminente de termos como "praia", "mar", "vista" e "centro". Vale ressaltar que locais nas proximidades dessas palavras frequentemente recebem avaliações mais positivas, possivelmente devido à sua proximidade a pontos turísticos ou à costa. Para alguns, a proximidade com a praia é sinônimo de qualidade e tranquilidade, refletindo-se positivamente nas avaliações

## 8. O que você pode inferir sobre as notas dos imóveis? <h10>
> As avaliações dos imóveis refletem a importância da localização, mas também revelam a
necessidade de uma abordagem equilibrada para atender às expectativas dos hóspedes.
Embora propriedades bem localizadas geralmente recebem notas mais altas,
características como comodidades, limpeza e custo-benefício desempenham papéis
cruciais. Uma localização excelente pode, em parte, compensar avaliações menos
favoráveis em outras categorias. Além disso, a presença de WiFi gratuito emerge como um
fator significativo nas avaliações, indicando a valorização da conectividade pelos
hóspedes. A análise detalhada também revela variações nas avaliações entre diferentes
tipos de acomodações e a influência do número de avaliações na confiabilidade dos
resultados. Essas nuances destacam a importância de uma gestão holística e
personalizada para garantir avaliações positivas e a satisfação duradoura dos clientes.

## 9. Quais são os anúncios que te parecem críticos? Explique. <h11>
> Anúncios com avaliações persistentemente baixas são considerados críticos, sinalizando a
presença de questões substanciais que têm um impacto significativo e negativo na
experiência e satisfação dos hóspedes. Essas avaliações indicam não apenas a existência
de problemas, mas também a necessidade urgente de intervenção e melhoria.

## 10. Quais outras análises você faria desses dados? Use sua criatividade <h12>
> Uma análise pertinente envolveria a comparação entre 'room_surface_in_m2' e
'comodidades', a fim de investigar se o tamanho de uma hospedagem tem impacto em
suas avaliações. Além disso, considerar a relação entre 'accommodation_type' e
'number_of_ratings', somando a quantidade de avaliações por tipo, proporciona insights
sobre tendências preferenciais entre apartamentos e casas, ajudando a entender as
preferências dos hóspedes em relação ao número de avaliações recebidas.

### Código da segunda ideia: <h13>

Padrão:
~~~python
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
~~~
Um filtro foi aplicado para excluir as listagens que não possuíam avaliações
~~~python
#Filtro para excluir os locais sem avaliação
filtro = csvData5['number_of_ratings'] > 0
csvData5 = csvData5[filtro]
~~~
Posteriormente, procedeu-se inicialmente à coleta de avaliações por tipo de acomodação, seguida pela contagem das listagens com seus respectivos tipos de acomodação e, finalmente, à ordenação das tabelas
~~~python

#Contando a quantidade de avaliações por tipo de acomodação
Quantidade_AV = csvData5.groupby(['accommodation_type'], as_index=False)['number_of_ratings'].sum()

#Contando a quantidade de acomodações 
Quantidade_AC = csvData5['accommodation_type'].value_counts().reset_index()

#Ordenando as linhas da coluna
Quantidade_AV.sort_values(["number_of_ratings"], axis=0,ascending=[True], inplace=True)
Quantidade_AC.sort_values(["count"], axis=0,ascending=[True], inplace=True)
~~~
O primeiro gráfico gerado é refente a quantidade de avaliações por tipo de acomodação
~~~python
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
~~~
![Gráfico](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/062801f5-bad2-4533-a1fd-97a6a2848e88)

Na segunda etapa, foi realizada a análise da quantidade de tipos de acomodação presentes na tabela
~~~python
#Gráfico da quantidade de acomodações listadas
plt.figure(figsize=(8, 6))
plt.bar(Quantidade_AC['accommodation_type'], Quantidade_AC['count'])
plt.xticks(rotation=80)
plt.xlabel('Tipo de acomodação')
plt.ylabel('Quantidade')
plt.title('Tipos de acomodações com mais avaliações')
plt.tight_layout()
plt.show()
~~~
![AV2](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/2481e4da-135d-4eec-8ead-629e8d87fd5d)

Com base nesses dois gráficos, é possível observar que, mesmo nos resorts com poucas listagens, esse tipo de acomodação se destaca como o que recebe a maior quantidade de avaliações, ao contrário dos apartamentos, que possuem um grande número de listagens, mas não necessariamente uma quantidade proporcional de avaliações.

É importante destacar que, embora o número de avaliações forneça insights valiosos, não é possível afirmar com certeza que os resorts são preferidos pelos hóspedes, uma vez que sempre existe uma porcentagem que opta por não avaliar a hospedagem. Para obter resultados mais precisos, seria recomendável considerar o número total de pessoas que passaram pela hospedagem, proporcionando uma métrica mais abrangente.

## 11. Como você projetaria um dashboard para mostrar essas informações? <h14>
>O dashboard foi realizado no Power BI e o arquivo se chama **"SeazoneChallenge.pbix"**

![Dashboard](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/48d51acb-971f-45c2-bf95-8f8d37d21514)
![Dashboard](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/b85fd255-629f-4239-9a25-1bc6f2790f5c)

## 12. Quais outras informações/dados você relacionaria com essas bases, caso tivesse acesso? <h15>
> ● Estação do Ano, para explorar se as estações do ano afetam as avaliações,
considerando fatores climáticos ou eventos sazonais que possam influenciar a
experiência dos hóspedes.

> ● Preços médios, analisando se os hóspedes estão procurando hospedagens por
localização ou preço ou até mesmo um meio termo entre os dois

> ● Comentários dos hóspedes, visando encontrar os pontos que prejudicam a
avaliação de um local e consecutivamente melhorar esse ponto.

> ● Tipo de Viagem, com o objetivo diferenciar as avaliações com base no tipo de
viagem (negócios, lazer, familiar) para entender as expectativas específicas de cada
categoria de hóspede.

## 13. (Extra) Com base nesses dados e nos anúncios fornecidos, como você melhoraria as notas? <h16>
> Investir em utensílios aprimora significativamente as notas de conforto, proporcionando aos
hóspedes uma experiência mais acolhedora. Oferecer uma conexão WiFi rápida e
confiável é uma estratégia eficaz para atender às expectativas dos hóspedes, garantindo
conectividade sem interrupções. Uma limpeza eficiente não apenas torna o local mais
agradável, mas também cria a possibilidade de fidelizar o cliente, incentivando seu retorno.
Destacar pontos turísticos próximos ao local é uma prática que enriquece a experiência do
hóspede, proporcionando informações valiosas sobre as atrações ao redor. Além disso, a
implementação de promoções especiais não apenas atrai mais pessoas para o local, mas
também cria oportunidades para experiências diferenciadas, incentivando o interesse e a
satisfação dos visitantes.
 
## Feedback sobre o desafio <h17>
> O desafio me cativou profundamente, pois não se tratava de uma tarefa fácil, acessível a
qualquer um, mas também não era excessivamente difícil. Consegui completá-lo antes do
prazo estimado, o que reforçou minha confiança, e destacou minhas habilidades na área
de análise de dados, utilizando Python e a biblioteca Pandas para uma análise abrangente.
É justo admitir que enfrentei alguns obstáculos durante a resolução de certas questões,
especialmente na questão 6, onde tive bastante dificulldade de proceder com a questão.
Diante desse desafio, optei por duas abordagem diferentes que se mostrou mais eficaz.
Expresso minha gratidão à Seazone por proporcionar essa experiência enriquecedora, que
ampliou significativamente meu conhecimento. Estou ansioso para enfrentar novos
desafios semelhantes, pois acredito que cada um deles contribui para meu crescimento
profissional e pessoal
