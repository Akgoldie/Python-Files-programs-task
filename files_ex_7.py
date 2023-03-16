# Create DataFrame from Dictionary
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
"""df3 = df.filter(like='ur', axis=None)
print(df3)
df2 = df.filter(regex='e$', axis=1)
print(df2)
df2=df.filter(items=[0,1,2], axis=0)
print(df2)
df2=df.filter(items=['Courses','Fee'],axis=1)
print(df2)
df2 = df.filter(like='1', axis=0)
print(df2)
# Replace current esisting DataFrame
df.query("Courses == 'Spark'",inplace=True)
print(df)
# Using columns with special characters
print(df.query("'Courses Fee' == 23000"))"""

# By using lambda function
print(df.apply(lambda row: row[df['Courses'].isin(['Spark','PySpark'])]))





"""print(df)
df2=df.filter(items=['Courses','Duration'])
print(df2)
df2=df.filter(items=['Courses','Fee'])
print(df2)
# Using DataFrame.query()
print("****************************************************************")
df.query("Courses == 'Spark'",inplace=True)
print("****************************************************************")
df.query("Courses != 'Spark'")
print("****************************************************************")
df.query("Courses in ('Spark','PySpark')")
print("****************************************************************")
print(df.query( 'Fee'>= 23000 and 'Fee'<= 24000))
print("****************************************************************")
# Using DataFrame.loc[]
print(df.loc[df['Courses'] == 'PySpark'])
print("****************************************************************")
print(df.loc[df['Courses'] != 'Spark'])
print("****************************************************************")
print(df.loc[df['Courses'].isin('PySpark')])
print(df.loc[~df['Courses'].isin('PySpark')])
print("****************************************************************")
print(df.loc[(df['Discount'] >= 1000) & (df['Discount'] <= 2000)])
print("****************************************************************")
print(df.loc[(df['Discount'] >= 1200) & (df['Fee'] >= 23000 )])
print("****************************************************************")
#Using apply()
print(df.apply(lambda row: row[df['Courses'].isin(['Spark','PySpark'])]))
print("****************************************************************")
print(df.apply(lambda row: row[df['Courses'].isin(['Spark','arun'])]))
print("****************************************************************")
print(df.apply(lambda row: row[df['Courses'].isin(['arun'])]))
print("****************************************************************")

# Other ways to filter
df[df["Courses"] == 'Spark']
df[df['Courses'].str.contains("Spark")]
df[df['Courses'].str.lower().str.contains("spark")]
df[df['Courses'].str.startswith("P")]"""




