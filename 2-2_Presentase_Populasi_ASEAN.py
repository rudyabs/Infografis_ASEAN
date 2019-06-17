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

plt.figure('Presentase Penduduk ASEAN', figsize = (12,8))
plt.pie(asean['Population'], labels = asean['Name'], autopct='%1.1f%%', textprops={'color': 'black'})
plt.title('Persentase Penduduk ASEAN')
plt.legend(asean['Name'], bbox_to_anchor=(1, 1), loc = 0)

plt.tight_layout()
plt.show()