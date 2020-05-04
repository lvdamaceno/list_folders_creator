'''
Formato do arquivo csv

MARCA 1 ; PRODUTO 1
MARCA 1 ; PRODUTO 2
MARCA 2 ; PRODUTO 3
MARCA 2 ; PRODUTO 4

Melhorias:
    Não funciona se o nome do produto tiver uma /, tem que trocar pra \.
    Não funciona se vier coluna NULL do banco.
'''

import csv
import os


def cria_marcas(lista_produtos):
    with open(lista_produtos, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        marcas = []
        for row in spam_reader:
            if row[0] not in marcas:
                marcas.append(row[0])
        # cria a pasta com o nome da marca
        [os.mkdir(marca) for marca in marcas[1:]]


def cria_produtos(lista_produtos):
    with open(lista_produtos, newline='', encoding='utf-8-sig') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in spam_reader:
            # entra na pasta da marca
            os.chdir(row[0])
            # cria a pasta com a descrição do produto
            os.mkdir(row[1])
            # sai da pasta
            os.chdir('..')


lista_produtos = 'PRODUTOS_SITE_TESTE.csv'
cria_marcas(lista_produtos)
cria_produtos(lista_produtos)
