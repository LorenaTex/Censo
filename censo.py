# -*- coding: utf-8 -*-
"""Censo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FniWjtw8IKP1SrNEPdI149CFs3xZ6SF1
"""

import requests

def x():
  nome= input("Digite o nome: ")
  caixa= requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}/".format(nome))
  censo=caixa.json()
  print(censo)
  #print(f"Nome: {censo['nome']}")
x()

import requests
import pandas as pd
#panda tabela, extrai dados, ler e trata arquivos pdf, ler e apresentar dados 

def x():
  nome= input("Digite o nome: ")
  censo= pd.read_json("https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}/".format(nome))
  censo=pd.json_normalize(censo['res'][0][5:])
  tabela=pd.DataFrame(censo)
  #tabela = df
  #dataframe : tabela extração e construção
  print(tabela)
x()