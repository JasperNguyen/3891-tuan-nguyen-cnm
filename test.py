import numpy as np
import pandas as pd

arr = np.random.randint(0, 255, size=(20, 20), dtype=np.uint8)

data = pd.DataFrame(arr)
data.to_csv('a.csv')
print('thanh cong')