import pandas as pd
df=pd.read_csv("D:\\MARKLIST.csv")
df["TOTAL MARKS"]=0
df["TOTAL MARKS"]=df["ENG"]+df["TAMIL"]+df["MATHS"]+df["SCIENCE"]
print(df)
