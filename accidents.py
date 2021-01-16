import numpy as np
import pandas as pd

def fix_zip(s):
    if "-" in str(s):
        temp = str(s)
        temp = temp[0:temp.index("-")]
        return float(temp)
    return float(s)


popdf = pd.read_csv("pop-by-zip-code.csv")
popdf = popdf.loc[:,["zip_code","y-2016"]]
popdf.columns = ["Zipcode", "Population"]
#print(popdf)
df = pd.read_csv("gooddata.csv")
df["Zipcode"] = df["Zipcode"].apply(fix_zip)
df = df.join(popdf.set_index("Zipcode"), on="Zipcode")
#print(df.loc[:,["Zipcode", "Street", "Population"]])
df = df.set_index("Zipcode").sort_index().loc[:,["Street","Population"]]
print(df)
#print(df.groupby(["Zipcode"]).agg({"Street": "value_counts"}))
#print(df.sort_index().loc[:,"Street"])
#print(df.loc[:,["Zipcode", "Street"]].groupby(["Zipcode"]))