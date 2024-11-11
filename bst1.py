import pandas as pd

df = pd.read_csv("bike.csv")

df["Середні продажі"] = df.loc[:, "Підприємець_1":"Підприємець_3"].mean(axis=1)

df[["Місяц", "Середні продажі"]].to_csv("average.csv", index=False)
