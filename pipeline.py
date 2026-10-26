import pyarrow
import sys
import pandas as pd
print("arguments", sys.argv)

month = sys.argv[1]
df = pd.DataFrame({"day": [1, 2, 3], "num_passengers": [10, 20, 30]})
df["month"] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet", engine="pyarrow", index=False)
print(f"Hello pipeline, month={month}")

