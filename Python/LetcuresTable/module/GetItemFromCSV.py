

import pandas as pd
import matplotlib.pyplot as plt


def GetItemFromCSV(file):
    table = pd.read_csv(file, names=["Name", "L_name", "Length","Class_num", "Total"])
    #print(table)
    return pd.DataFrame(table)