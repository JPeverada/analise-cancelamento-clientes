import pandas as pd
import plotly.express as px

tabela = pd.read_csv('Docs/cancelamentos.csv')

print(tabela.info())

tabela = tabela.dropna()

print(tabela.info())

tabela = tabela.drop(columns='CustomerID')

#print(tabela["cancelou"].value_counts()) # Em números absolutos
#print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) # Em porcentagem

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True)
    grafico.show()
