import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv



df = pd.read_csv('doc_reports.csv')
df2 = pd.read_csv('facial_similarity_reports.csv')

df3=pd.DataFrame(df)
df3= df.groupby(['user_id'],sort=False)


df3.first()
df4=pd.DataFrame(df2)
df4 =df.groupby(['user_id'],sort=False)

df4.first()

len(df4)


df5 =pd.merge(df3, df4, on="user_id")
