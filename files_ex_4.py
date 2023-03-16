import pandas as pd
df=pd.read_csv("D:\\MARKLIST.csv")
print(" ")
print("when open csv file")
print(df)
df["TOTAL MARKS"]=0
print(" ")
print("add the total marks column")
print(df)
df["TOTAL MARKS"]=df["ENG"]+df["TAMIL"]+df["MATHS"]+df["SCIENCE"]
print(" ")
print("add the values in total marks column")
print(df)
df=df.drop(columns='TOTAL MARKS')
print(" ")
print("after drop the total mark column")
print(df)