import os
import pandas as pd
from csv import writer, reader

path = './fld2'
counter = 0
for file in os.listdir(path):
    filename = os.path.join(path, file)
    df = pd.read_csv(filename, header=0)
    df["Target"] = ""
    for i in range(len(df)):
        if(df["Turbine current"][i] <= 1.70):
            df["Target"][i] = 0
        else:
            df["Target"][i] = 1
    df.to_csv("novi.csv", index=False)
            


