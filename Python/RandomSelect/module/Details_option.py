import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import module.GetItemFromCSV as GIFC


class Details_option:
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Show Chinese label
    plt.rcParams['axes.unicode_minus'] = False  # These two lines need to be set manually

    ScoresList = []#读取成绩明细表的列表对象
    DatesList = []

    '''
    IdList=[]
    ScoreList=[]
    '''
    def GetDate(self, file):
        type_list = ["Date", "Score", "Time"]#根据加载的成绩明细表，修改加载表的表头
        pandas_table = GIFC.GetItemFromCSV(file, type_list)
        print(pandas_table)
        self.ScoresList = pandas_table["Score"].tolist()
        print(self.ScoresList)
        self.DatesList = pandas_table["Date"].tolist()
        '''
        self.NumsList = pandas_table["Id"].tolist()
        self.NamesList = pandas_table["Score"].tolist()
        
        '''
        self.VisualizationResult()

    def GetMaxValue(self,list):
        return max(list)+1

    def VisualizationResult(self):
        plt.figure(dpi=80, figsize=(22, 9))

        # 使用DataFrame
        df = pd.DataFrame({
            'Date': self.DatesList,
            'Score': self.ScoresList
        })

        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # 只显示实际获得的分数作为纵坐标
        unique_scores = sorted(set(self.ScoresList))

        # 绘制折线图
        plt.plot(df['Score'], marker='o', markevery=1, linewidth=2, markersize=8)

        # 设置标签
        plt.xlabel('日期', fontsize=18)
        plt.ylabel('分数', fontsize=18)

        # 设置标题
        plt.title('成绩趋势图', fontsize=20, fontweight='bold')

        # 设置x轴刻度（日期）
        if len(self.DatesList) <= 20:
            plt.xticks(range(len(self.DatesList)), self.DatesList, rotation=45, fontsize=12)
        else:
            # 如果日期太多，只显示部分
            step = max(1, len(self.DatesList) // 10)
            indices = range(0, len(self.DatesList), step)
            plt.xticks(list(indices), [self.DatesList[i] for i in indices], rotation=45, fontsize=12)

        # 设置y轴刻度 - 关键修改：只显示实际获得的分数
        plt.yticks(unique_scores, fontsize=12)

        # 设置y轴范围，稍微扩展一点让图表更好看
        y_min = min(self.ScoresList)
        y_max = max(self.ScoresList)
        plt.ylim(y_min - 0.5, y_max + 0.5)

        # 添加网格线
        plt.grid(True, alpha=0.3, linestyle='--')

        # 显示具体分数值在数据点上
        for i, score in enumerate(self.ScoresList):
            plt.text(i, score + 0.1, str(score), ha='center', fontsize=10)

        # 调整布局
        plt.tight_layout()
        plt.show()
