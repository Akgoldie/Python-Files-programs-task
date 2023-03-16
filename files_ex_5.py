import pandas as pd
df=pd.read_csv("D:\\MARKLIST.csv")
df["TOTAL MARKS"]=0
df["TOTAL MARKS"]=df["ENG"]+df["TAMIL"]+df["MATHS"]+df["SCIENCE"]
df.to_csv("D:\\MARKLIST_total.csv",index=False,sep="$")
df.to_csv("D:\\MARKLIST_total.txt",index=False,sep="\t")
#df.to_excel("D:\\MARKLIST_total.xlsx")