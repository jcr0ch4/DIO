#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import locale


st.sidebar.image(
         'https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png'
        )
st.sidebar.markdown('## Analise Exploratória de Dados ( EDA ) :sunglasses:')

#st.sidebar.title("Select Visual Charts")
#st.sidebar.markdown("Select the Charts/Plots accordingly:")

def information(dataset):
        '''
           Return a new dataset with columns :
               - columns ( columns in original dataset )
               - types (data types in your dataset)
               - size ( size of your dataset)
               - unique ( data unique in your dataset)
               - missing data percent ( Percent of data missing in your dataset )
        '''
        df_aux = pd.DataFrame(
                                {
                                    'columns':dataset.columns,
                                    'types': dataset.dtypes,
                                    'missing':dataset.isna().sum(),
                                    'count':dataset.count(),
                                    'size':dataset.shape[0],
                                    'std':dataset.std(),
                                    'min': dataset.min(),
                                    'max':dataset.max(),
                                    'unique':dataset.nunique()
                                }
        )
        df_aux['missing data percent'] = round(df_aux['missing']/df_aux['size'],2)
        df_aux['columns'] = df_aux.index
        
        return st.write(df_aux.astype(str))

uploaded_file = st.sidebar.file_uploader("Selecione o arquivo: ")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file,sep=';')

    #Qual a Receita total?
    #Qual o custo Total?
    #Agora que temos a receita e custo e o total, podemos achar o Lucro total
    #Vamos criar uma coluna de Lucro que será Receita - Custo
    #Total Lucro
    #Criando uma coluna com total de dias para enviar o produto
    #Extraindo apenas os dias
    #Verificando o tipo da coluna Tempo_envio
    #Média do tempo de envio por Marca
    #Verificando se temos dados faltantes
    # **E, se a gente quiser saber o Lucro por Ano e Por Marca?**
    #Vamos Agrupar por ano e marca
    #Resetando o index
    #Qual o total de produtos vendidos?
    #Gráfico Total de produtos vendidos
    #Selecionando apenas as vendas de 2009
     #Tempo mínimo de envio
    #Tempo máximo de envio
    #Identificando o Outlier
    # Qual Loja que mais vendeu
    # Qual a quantidade de Lojas?
    st.sidebar.write("Número de Lojas analisadas: {}".format(len(df['ID Loja'].unique()))) 
    #
    st.subheader("Informações do Dataset")
    information(df)

    st.subheader("Amostra dos dados do Dataset")
    st.dataframe(df)
#   st.bar_chart(df['Produto'],df['Valor Venda'])
    barras = alt.Chart(df).mark_bar().encode(
        y='Valor Venda:Q',
        x='Produto:O',
    )
 
    st.altair_chart(barras, use_container_width=True)
    #st.write(str( locale.getlocale() ))
    #locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    # Transformacao em Float
    # transformando data
    df['Data Envio'] = pd.to_datetime(df['Data Envio'])
    df['Data Venda'] = pd.to_datetime(df['Data Venda'])
    # Ano Venda
    df['Ano Venda']= pd.DatetimeIndex(df['Data Venda']).year

    # Mes Venda
    df['Mes Venda']= pd.DatetimeIndex(df['Data Venda']).month

    # Dia da Semana
    df['Dia Semana Venda']= pd.DatetimeIndex(df['Data Venda']).dayofweek

    # lead time
    df['LeadTime'] = (df['Data Envio']-df['Data Venda']).dt.days

    # Custo
    df['Custo Total'] = df['Custo Unitário'].mul(df['Quantidade'])

    # Lucro
    df['Lucro Total'] = df['Valor Venda'] - df['Custo Total']
    # Transformando Valor Monetário em float
    # ( Funciona no Jupyter, mas não funciona no Streamlit )
    df['Valor Venda'] = df['Valor Venda'].astype('float')
    #df['Valor Venda'] = df['Valor Desconto'].astype('float')
    #df['Valor Venda'] = pd.to_numeric(df['Valor Venda'],errors='coerce')

    # Funciona no Jupyter e no Streamlit
    #df['Valor Venda'] = pd.to_numeric(df['Valor Venda'],errors='coerce')
    df['Valor Desconto'] = pd.to_numeric(df['Valor Desconto'],errors='coerce')


    df['Custo Unitário'] = df['Custo Unitário'].astype('float')
    df['Preço Unitário'] = df['Preço Unitário'].astype('float')
   # ticket_medio = float(valor_venda_all / total_venda)
    


    #f['Valor Venda'] = pd.to_numeric(df['Valor Venda'],errors='coerce')
    st.write("Valor de Venda : {}".format(df['Valor Venda'].sum()))
    st.write("Quantidade de Vendas : {} ".format(df['No. Venda'].count()))
    valor_venda_all = df['Valor Venda'].sum()
    total_venda = df['No. Venda'].count()
    st.write("Tipo de Valor Venda : {}, Valor : {} | Tipo No. Venda : {}, Valor : {}".format(total_venda,total_venda,valor_venda_all,valor_venda_all))
    st.write("Ticket Médio : {}".format(locale.currency(df['Valor Venda'].sum()/df['No. Venda'].count(),grouping=True)))
    # Transformação de Objeto em Data
    #df['Data Venda'] = pd.to_datetime(df['Data Venda'])

    
