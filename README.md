# Desafio-Seazone <h1>
> Para a elaboração dessas questões, foram utilizadas as bibliotecas pandas para manipulação e análise de dados, juntamente com matplotlib para a construção de gráficos. O estilo visual adotado nos gráficos foi o 'fivethirtyeight'
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

## 11. Como você projetaria um dashboard para mostrar essas informações? <h13>
>O dashboard foi realizado no Power BI e o arquivo se chama **"SeazoneChallenge.pbix"**

![Dashboard](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/48d51acb-971f-45c2-bf95-8f8d37d21514)
![Dashboard](https://github.com/P4TRIIICK/Desafio-Seazone/assets/107818715/b85fd255-629f-4239-9a25-1bc6f2790f5c)

## 12. Quais outras informações/dados você relacionaria com essas bases, caso tivesse acesso? <h14>
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

## 13. (Extra) Com base nesses dados e nos anúncios fornecidos, como você melhoraria as notas? <h15>
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
 
## Feedback sobre o desafio <h16>
> O desafio me cativou profundamente, pois não se tratava de uma tarefa fácil, acessível a
qualquer um, mas também não era excessivamente difícil. Consegui completá-lo antes do
prazo estimado, o que reforçou minha confiança, e destacou minhas habilidades na área
de análise de dados, utilizando Python e a biblioteca Pandas para uma análise abrangente.
É justo admitir que enfrentei alguns obstáculos durante a resolução de certas questões,
especialmente na questão 6, onde inicialmente tentei utilizar as funções
"pd.get_dummies()" e ".corr()", mas acabei gerando uma série de colunas nos dados.
Diante desse desafio, optei por uma abordagem diferente que se mostrou mais eficaz.
Expresso minha gratidão à Seazone por proporcionar essa experiência enriquecedora, que
ampliou significativamente meu conhecimento. Estou ansioso para enfrentar novos
desafios semelhantes, pois acredito que cada um deles contribui para meu crescimento
profissional e pessoal
