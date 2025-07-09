import pandas as pd
import numpy as np

scores = [50, 60, 70, 80, 90, 100]
mean = np.mean(scores)
std = np.std(scores)

z_score_normalized = [ (x - mean) / std for x in scores ]

df = pd.DataFrame({'scores': scores, 'z_score_normalized': z_score_normalized})
print(df)
