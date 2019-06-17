import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy

mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://rudyabs:Kecapi48@localhost:3306/world'
)

df = pd.read_sql('SELECT * FROM country', mydb)
asean = df[df['Region']=='Southeast Asia'].reset_index()
warna = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'gray', 'yellow', 'pink', 'black', 'darkblue']

plt.figure('GNP ASEAN', figsize = (12,8))
plt.bar(asean['Name'], asean['GNP'], color = warna)
plt.title('Pendapatan Bruto Nasional Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')

for j in range(len(asean)):
    plt.text(asean['Name'][j], asean['GNP'][j] + 1000, asean['GNP'][j])

plt.tight_layout()
plt.show()
