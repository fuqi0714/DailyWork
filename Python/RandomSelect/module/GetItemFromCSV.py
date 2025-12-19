

import pandas as pd
import matplotlib.pyplot as plt


def GetItemFromCSV(file,type_list):

    table = pd.read_csv(file, names=type_list)
    return pd.DataFrame(table)


