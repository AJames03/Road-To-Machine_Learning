import pandas as pd

ages = [21, 22, 25, 29, 34, 38, 41, 42, 47, 55]

df = pd.DataFrame({'age':ages})

bins = [20, 30, 40, 50, 60]
labels = ['Young', 'Middle-Age', 'Older', 'Senior']

df["Age groups"] = pd.cut(df["age"] , bins, labels=labels)

print(df)