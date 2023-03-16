import pandas as pd
f=pd.read_csv("D:\\EX Programs\\ARUN_MARK_LISTS.csv")
df=pd.DataFrame(f)
"""
print(df)
print(df[['NAME','ENGLISH']].head())
print(df[1:10])
print(df)

print(df[['REG','NAME','TAMIL']][1:10])
print(df[['REG','NAME','TAMIL']])
print(df[['REG','NAME','TAMIL']][:6])
print(df.loc[5])
print(df[['REG','NAME','TAMIL']][:6:2])
print(df.describe())
print(df.columns)
print(df.shape)
print(df.tail())
print(df.tail(7))
print(df.head())
print(df.head(7))
print(df.shape)
print(df.count())
print(df[:10])
print(df[5:])
print(df[1:10:2])
print(df[:11:])
print(df[1:10])
print(df.loc[5,6,4,7])
print(df['NAME']=="A")
print(df)
print(df.loc[['NAME']=='A'])
for index, rows in df.iterrows():
    print(index,rows['NAME'])
print("....................")
print(".....................")
for index, rows in df.iterrows():
    print(index, rows['NAME':'TAMIL'])
for index, rows in df.iterrows():
    print( rows)
print(df.iterrows())
for index, rows in df.iterrows():
    print(index, rows)
k=df.drop("NAME")
Print(df)
print(df.drop(columns='NAME'))"""

"""print(df)"""

#f=pd.DataFrame()
"""fu=df['TAMIL'].dropna()
print(fu)"""
#print(df)
#print(df.fillna("miss"))

# Get Index as Series
print(df.index)
# Outputs
# RangeIndex(start=0, stop=3, step=1)

# Get Index as List
print(df.index.values)
# Outputs
# [0 1 2]

