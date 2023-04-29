import pandas as pd
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




    def VisualizationResult(self):
        plt.figure(dpi=80, figsize=(22, 6))
        df = pd.DataFrame(self.NumsList,
                          index=self.NamesList)
        plt.xlabel('Name')
        plt.ylabel('Times')
        plt.xticks(label='Name', fontsize=12, color='green', rotation=35)
        plt.yticks(label='Times', fontsize=14)

        plt.plot(df, marker='o', markevery=1)
        plt.show()
