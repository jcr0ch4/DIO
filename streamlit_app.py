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
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_excel(upload_file)
    st.write(information(df))




#Qual a Receita total?


# In[10]:


#Qual o custo Total?


# In[11]:


#Agora que temos a receita e custo e o total, podemos achar o Lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo


# In[12]:


#Total Lucro


# In[13]:


#Criando uma coluna com total de dias para enviar o produto


# In[14]:


#Extraindo apenas os dias


# In[15]:


#Verificando o tipo da coluna Tempo_envio


# In[16]:


#Média do tempo de envio por Marca


# In[18]:


#Verificando se temos dados faltantes


# **E, se a gente quiser saber o Lucro por Ano e Por Marca?**

# In[19]:


#Vamos Agrupar por ano e marca


# In[20]:


#Resetando o index


# In[21]:


#Qual o total de produtos vendidos?


# In[22]:


#Gráfico Total de produtos vendidos


# In[23]:


#Selecionando apenas as vendas de 2009


# In[24]:


#Tempo mínimo de envio


# In[25]:


#Tempo máximo de envio


# In[26]:


#Identificando o Outlier


# In[27]:


# Qual Loja que mais vendeu


# In[31]:


# Qual a quantidade de Lojas?
len(df['ID Loja'].unique())


# In[32]:


# Quais são as lojas ?
df['ID Loja'].unique()


# In[ ]:





