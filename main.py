# Pandas: Sum the values in a Column that match a Condition

import pandas as pd


df = pd.DataFrame({
    'A': [3, 5, 7, 10, 5, 19, 5],
    'B': [1, 2, 4, 9, 15, 30, 4]
})


print(df)

result = df.loc[df['A'] == 5, 'B'].sum()

print('-' * 50)

print(result)  # 👉️ 21