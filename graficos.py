#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""

Escrever funções para mostrar os gráficos capazes de responder as seguintes questões:

Sobre os trabalhos selecionados:
    Quais são as palavras-chaves utilizadas?
    Qual o percentual de acerto? (quantas palavras da string de busca o artigo curtiu(????))
    Qual o número de páginas?

Sobre os trabalhos cortados:
    Quais são as palavras-chaves utilizadas?
    Quantas vezes as palavras utilizadas na string de busca apareceram nos artigos?

Para todos (feita):
    Qual o ano de publicação?

Perguntas que desistimos:
    Qual(is) a(s) linha(s) de pesquisa do(s) autor(es)?
        - Porque talvez tome tempo e não dê para agrupar de uma forma coerente



CALCULANDO MEDIAS:

mediaGrazi = dfPoint['notaGrazi'].mean()
mediaJessica = dfPoint['notaJessica'].mean()
mediaHugo = dfPoint['notaHugo'].mean()
mediaSoma = dfPoint['somatorio'].mean()

"""

#ponteiros globais para os dados do csv, que devem ser passados na chamada das funções
df1 = pd.DataFrame(pd.read_csv("todos.csv"))

df2 = pd.DataFrame(pd.read_csv("menosdedois.csv"))

df3 = pd.DataFrame(pd.read_csv("maisdedois.csv"))

def mostrar_grafico_artigos_por_ano(df):

    """
    Neste caso nao eh um histograma!!
    """

    dfPoint = pd.DataFrame(np.array(df.iloc[1:,8]))

    dfPoint.columns = ['ano']
    lista_de_anos = dfPoint['ano'].tolist()

    anos_dict = []
    for ano in lista_de_anos:
        e = (ano, lista_de_anos.count(ano))
        if e not in anos_dict:
            anos_dict.append(e)

    anos_dict.sort()
       
    plt.title("Artigos por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Numero de Artigos")

    plt.bar(range(len(anos_dict)), [e[1] for e in anos_dict], align='center')
    plt.xticks(range(len(anos_dict)), [e[0] for e in anos_dict])

    plt.show()

def mostrar_grafico_pontuacao_total_por_artigo(df):

    somatorio = pd.DataFrame(np.array(df.iloc[1:,7]))
    somatorio.columns = ['somatorio']
    somatorio = somatorio.apply(pd.to_numeric)

    s = somatorio['somatorio']

    N = len(s)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.5       # the width of the bars: can also be len(x) sequence

    p1t = plt.bar(ind, s, width, color='red', align='center')

    plt.autoscale(enable=True, axis='both', tight=None)
    plt.ylabel('Pontuacao')
    plt.xlabel('Artigos')
    plt.title('Pontuacao por Artigo')
    plt.xticks(ind,('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12', 'A13'))
    plt.yticks(np.arange(0, 3.5, 0.5))
    plt.show()


def mostrar_histograma_artigos_pontuacao(df, normalizado):

    dfPoint = pd.DataFrame(np.array(df.iloc[1:,7]))

    dfPoint.columns = ['somatorio']
    dfPoint = dfPoint.apply(pd.to_numeric)

    hist=np.histogram(dfPoint['somatorio'], density=True)

    plt.hist(dfPoint['somatorio'], bins='auto', normed=normalizado)  # arguments are passed to np.histogram
    plt.title("Histograma - Pontuacao dos Artigos")
    plt.xlabel("Pontuacao")
    plt.ylabel("Numero de Artigos")
    plt.show()
    

def mostrar_grafico_pontuacao_parcial_por_artigo(df):

    notaGrazi = pd.DataFrame(np.array(df.iloc[1:,4]))
    notaHugo = pd.DataFrame(np.array(df.iloc[1:,5]))
    notaJessica = pd.DataFrame(np.array(df.iloc[1:,6]))

    dfPoint = pd.concat([notaGrazi,notaHugo,notaJessica],axis=1)
    dfPoint.columns = ['notaGrazi','notaHugo','notaJessica']
    dfPoint = dfPoint.apply(pd.to_numeric)

    g = dfPoint['notaGrazi']
    j = dfPoint['notaJessica']
    h = dfPoint['notaHugo']

    N = len(s)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.5       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, g, width, color='red')
    p2 = plt.bar(ind, h, width, bottom=g, color='blue')
    p3 = plt.bar(ind, j, width, bottom=h+g, color='green')

    plt.ylabel('Pontuacao')
    plt.xlabel('Artigos')
    plt.title('Pontuacao por Artigo agrupado por Avaliador')
    plt.xticks(ind,('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12', 'A13'))
    plt.yticks(np.arange(0, 3.5, 0.5))
    plt.legend((p1[0], p2[0],p3[0]), ('Grazi','Hugo','Jessica'))
    plt.show()

