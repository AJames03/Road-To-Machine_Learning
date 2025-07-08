import pandas as pd
import numpy as np

data = {
    "A": [1, 2, 3, np.nan],
    "B": [4, np.nan, 6, 7],
    "C": [8, 9, np.nan, 11]
}

df = pd.DataFrame(data)
df_clean = df.dropna()
print(df_clean)