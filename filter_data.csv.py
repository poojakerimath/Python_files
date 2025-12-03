import pandas as pd
data = {
   'name ' : ['alice','bob','charlie','david',None],
   'age' : ['23','22',None,'21','20'],
   'city' : ['mumbai','delhi','gurgon','kolkata',None]
}

df = pd.DataFrame(data)
filter_data = df.dropna()
print(filter_data)