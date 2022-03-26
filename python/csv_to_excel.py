import pandas as pd

df_new = pd.read_csv('jsonoutput.csv')
 
# saving xlsx file
GFG = pd.ExcelWriter('outputexcel.xlsx')
df_new.to_excel(GFG, index=False)
 
GFG.save()