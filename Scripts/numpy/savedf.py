

import numpy as np
import pandas as pd

numpy_data = np.array([['Arroz', 'Leche'], ['Lentejas', 'Queso']])

df = pd.DataFrame(data=numpy_data, index=[1, 2], columns=["GRANOS", "LACTEOS"])
print(df)