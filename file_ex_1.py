
import pandas as pd
df=pd.read_csv("D:\\MARKLIST.csv")
#f=pd.DataFrame(df)
#print(df)
f=df.sort_values("STUDENT NAME",ascending=False)
print(f)
print("-------------------------------------")
print(df)