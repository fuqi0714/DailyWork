

import pandas as pd
import matplotlib.pyplot as plt


def GetItemFromCSV(file):
    table = pd.read_csv(file, names=["ID", "Name", "Sex", "Times", "PreviousDate"])
    return pd.DataFrame(table)