import csv
import pandas as pd
import seaborn as sns

#COLETA DOS DADOS
with open('gasolina.csv', mode='r', encoding='utf8') as fp:
  gasolina_df = pd.read_csv('gasolina.csv', sep=',')

#GRÁFICO
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço da Gsolina', xlabel='dia', ylabel='venda');

# SALVE COMO PNG
grafico_png = grafico.get_figure()
grafico_png.savefig('gasolina.png', format='png')
