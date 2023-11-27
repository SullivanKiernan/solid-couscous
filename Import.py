import pandas as pd
x = pd.read_csv(r'C:\Users\sulli\OneDrive\Python activities\Data.csv')
# Just put r before your normal string. It converts a normal string to a raw string:
print(x.to_string())
z = x["Calories"].mean()
y = x.fillna(z)
print(y.to_string())

print(x.compare(y))

