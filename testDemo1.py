
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 3] * 3,
    "B": ['a', 'b', np.nan, 'd', 'f', 20],
    "C": [np.nan, 10, np.nan, 14, 35, 'c']
})

print(df)

