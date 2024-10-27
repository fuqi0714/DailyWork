import pandas as pd
import numpy as np

class Average:
    def GetItemFromCSV(self,file1,file2):
        title=pd.read_csv(file1, names=["Lectures","Avg"])
        #table=title.to_dict('records')

        score_table = pd.read_csv(file2, names=["Lectures", "Score"])
        self.CaculationAvg(title, score_table)



    def CaculationAvg(self,table,score_table):
        #print(table)
        temptDict={'Lecture': '', 'Score': ''}
        n=len(score_table)
        for i in range(0,n):
            temptDict['Lecture']=score_table[i:i+1][['Lectures']].to_string(index=False, header=0)
            score=float(score_table[i:i+1][["Score"]].to_string(index=False, header=0))
            print((score))
            temptDict['Score']= score
            print(  temptDict['Lecture'])
            print( temptDict['Score'])
            row_index=table.loc[table['Lectures']==temptDict['Lecture']].index[0]
            column_index=table.columns.get_loc('Avg')
            print(row_index)
            print(column_index)
            temptValue=float(table.iloc[row_index,column_index])



            print('--------')
            table.iloc[row_index,column_index]=score+temptValue
            print(table.iloc[row_index,column_index])
            #table.replace({temptDict['Lecture']},temptDict['Score'])
        table.to_csv('src/output.csv')




if __name__ == '__main__':
    AVG=Average()
    AVG.GetItemFromCSV("src/lecturesTitle.csv","src/lecturesScore.csv")