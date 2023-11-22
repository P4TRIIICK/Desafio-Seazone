import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lendo um csv e atribuindo para uma variável 
csvData = pd.read_csv("Data/desafio_details.csv", encoding='latin-1', sep = ';')
csvData2 = pd.read_csv("Data/desafio_ratings.csv", encoding='latin-1', sep = ';')

#Remoção de dados duplicados
csvData3 = csvData.drop_duplicates(subset='hotel_id')
csvData4 = csvData2.drop_duplicates(subset='hotel_id')

#Transformar "hotel_id" em index para facilitar a exclusão de dados indesejados
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

#Convertendo para csv novamente 
csvData3.to_csv('Data/desafio_details_new.csv', index=True, sep=';', encoding='latin-1')
csvData4.to_csv('Data/desafio_ratings_new.csv', index=True, sep=';', encoding='latin-1')