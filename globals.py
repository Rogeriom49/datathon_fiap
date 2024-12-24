import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Rogeriom49/datathon_fiap/refs/heads/main/datasets/alunos.csv')

lAno = {'Todos': 'Todos','2020': 2020, '2021': 2021, '2022':2022}
lAno_2 = {'Todos': 'Todos','2020': 2020, '2021': 2021, '2022':2022}

# lIndicadores_1 = {'INDE':'INDE', 'IAA':'IAA', 'IEG':'','IPS','IDA', 'IPP', 'IPV','IAN'}

lIndicadores_1 = ['INDE', 'IAA', 'IEG','IPS','IDA', 'IPP', 'IPV','IAN']
lPedras = ['Topázio', 'Ametista', 'Ágata', 'Quartzo']