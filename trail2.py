# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df_cancer = pd.read_csv("D:\Data_Science\data.csv")

df_cancer_cleaned = df_cancer.dropna(axis=1)

df_cancer_cleaned1 = df_cancer_cleaned.drop(columns=["id"])

st.write('''
         # InClass Assignment-5
         Designing web dashboard with user inputs
         ''')

optionx = st.selectbox(
    'what column do you want to use as x?',
    df_cancer_cleaned1.columns.to_list(),index=1)

st.write('Your selected column:', optionx)

optiony = st.selectbox(
    'what column do you want to use as y?',
    df_cancer_cleaned1.columns.to_list(),index=2)

st.write('Your selected column:', optiony)

#Scatter plot

st.write('''
         # Scatter plot
         ''')
sns.scatterplot(data=df_cancer_cleaned1,x=optionx,y=optiony,hue="diagnosis")
st.pyplot(plt.gcf())


#distribution plot1
#fig2 = plt.figure()
st.write('''
         # Distribution plot
         ''')
sns.displot(data=df_cancer_cleaned1.loc[:,[optionx,optiony]],kind="kde")
st.pyplot(plt.gcf())

#distribution plot - 2
#fig3 = plt.figure()
st.write('''
         # Histogram plot
         ''')

sns.histplot(data=df_cancer_cleaned1.loc[:,[optionx,optiony]])
st.pyplot(plt.gcf())


#regression plot 2
fig4 = plt.figure()
st.write('''
         # Regression plot
         ''')
sns.regplot(data=df_cancer_cleaned1,x=optionx,y=optiony,color="red",marker="*",line_kws={"color":"black"})

st.pyplot(fig4)



#Regression plot 1
st.write('''
         # LM plot
         ''')
sns.lmplot(data=df_cancer_cleaned1,x=optionx,y=optiony,hue="diagnosis",)

st.pyplot(plt.gcf())






#strip plot
fig6 = plt.figure()
st.write('''
         # Strip plot
         ''')
sns.stripplot(data=df_cancer_cleaned1,x=optionx,y="diagnosis")
st.pyplot(fig6)


#Swarm plot
fig7 = plt.figure()
st.write('''
         # Swarm plot
         ''')
sns.swarmplot(data=df_cancer_cleaned1,x=optionx,y="diagnosis")
st.pyplot(fig7)




#fig8=plt.figure(figsize=(10,10))
st.write('''
         # Joint plot
         ''')
sns.jointplot(data=df_cancer_cleaned1,x=optionx,y=optiony,hue="diagnosis")
st.pyplot(plt.gcf())



