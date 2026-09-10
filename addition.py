import pandas as pd
data= {
    'name' :['madhav', 'harsh', 'shiv'],
    'age' :[20, 21, 22],
    'salary':[10000, 20000, 30000]
}
df = pd.DataFrame(data)
print(type(df))