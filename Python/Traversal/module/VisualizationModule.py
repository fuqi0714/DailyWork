import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import module.GetItemFromCSV as GIFC


class VisualizationDate:
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Show Chinese label
    plt.rcParams['axes.unicode_minus'] = False  # These two lines need to be set manually

    NumsList=[]
    NamesList=[]
    def GetDate(self, file):
        pandas_table = GIFC.GetItemFromCSV(file)
        self.NumsList = pandas_table["Times"].tolist()
        self.NamesList = pandas_table["Name"].tolist()
        self.VisualizationResult()

    def GetMaxValue(self,list):
        return max(list)+1


    def VisualizationResult(self):
        plt.figure(dpi=80, figsize=(22, 9))
        df = pd.DataFrame(self.NumsList,
                          index=self.NamesList)
        plt.xlabel('Name', fontsize=24)
        plt.ylabel('Times', fontsize=24)
        plt.ylim(0, self.GetMaxValue(self.NumsList))
        plt.xticks(label='Name', fontsize=14, color='green', rotation=35)
        plt.yticks(np.arange(0, self.GetMaxValue(self.NumsList), step=1),label='Times', fontsize=24)

        plt.plot(df, marker='o', markevery=1)
        plt.show()
