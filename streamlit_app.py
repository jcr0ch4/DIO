#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd

st.title('Minha primeira aplicação :sunglasses:')

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
        return df_aux

uploaded_file = st.file_uploader("Selecione o arquivo")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue())
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file,sep=';')
    st.table(information(df.astype(str)))

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
    len(df['ID Loja'].unique())

    # Quais são as lojas ?
    df['ID Loja'].unique()

