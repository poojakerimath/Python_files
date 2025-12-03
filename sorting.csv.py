import pandas as pd
data ={
    'products' :['a','b','c','d','e','f','g'],
    'rating' : ['5','3','2','1','9','4','8'],
}

df = pd.DataFrame(data)
sorted_df = df.sort_values(by= 'rating', ascending = False)
print(sorted_df)
