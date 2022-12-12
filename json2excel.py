# the purpose of this program is to conver a json with an array of dicts
# to an excel file
#

file_name = "./out/all.json"

import json
import pandas as pd

with open(file_name, "r") as f:
    data = json.load(f)

    df = pd.DataFrame(data)

    df.to_excel("./out/all.xlsx")

    
