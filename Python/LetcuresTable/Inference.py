from py2neo import *
import argparse
import module.GetItemFromCSV as GIFC
import pandas as pd
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default="src/TableDB.csv",required=False)
args = parser.parse_args()


class GraphDatabase:

    matcher=None
    rmatcher=None
    graph=None
    start_nodes=[]
    end_nodes=[]
    relastionships=[]
    def __init__(self,graph):
        print("initialize")
        self.matcher = NodeMatcher(graph)

        self.rmatcher = RelationshipMatcher(graph)

        self.graph=graph
        self.Initialize(self.graph)


    def Initialize(self,graph):
        print("initialize over 1")
        '''
        a=Node('Lecture',name='操作系统',length=64,class_nums=3)
        b=Node('Lecture',name='计算机组成原理',length=48,class_nums=3)
        c=Node('Lecture',name='电视上',length=48)
        T1=Node('Owner',name='付琦',total=0)
        T2=Node('Owner',name='感受感受',total=0)
        r1=Relationship(T1,'Get',a)
        r2=Relationship(T1,'Get',b)
        r3=Relationship(T2,'Get',c)

        #s=a|b|r1
        #graph.merge(Teacher)
        #print(a,b,r1,r2)
        graph.create(r1)
        graph.create(r2)
        graph.create(r3)
        #print(self.GetAllLectures(T1))
        '''
        self.ModifyDB(graph)
        print("initialize over 2")

    def ModifyDB(self,graph):
        print("DB 2")
        graph=graph
        #testDict = {'Name': '', 'L_name': '', 'Class_num': '', 'Total': ''}
        pandas_table = GIFC.GetItemFromCSV(args.file)

        print("DB over ")
        self.GenerateNodeList(pandas_table,graph)

    def GenerateNodeList(self,pandas_table,graph):
        print("GenerateNodeList 2")
        name_list = pandas_table['Name']
        l_name_list = pandas_table['L_name']
        length_list = pandas_table['Length']
        class_name_list = pandas_table['Class_num']
        total_list = pandas_table['Total']
        print("GenerateNodeList over")
        for t in range( len(pandas_table)):
            print(t)
            n=Node('Owner',name=name_list[t],total=total_list[t])
            self.start_nodes.append(n)
            l=Node('Lecture',name=l_name_list[t],length=length_list[t],class_nums=class_name_list[t])
            self.start_nodes.append(l)
            self.GenerateRelationshipList(graph,n,l)
            print("for success")


    def GenerateRelationshipList(self,graph,start,end):
        r=Relationship(start,'Get',end)
        graph.create(r)
        self.relastionships.append(r)

    #print(r1.end_node['length'])


    def GetAllLectures(self,Node):
        sum=0
        res = list(self.rmatcher.match({Node}, r_type='Get', limit=None))
        #print(res[0].start_node['name'])
        for i in res:
            tempt=i.end_node['length']*i.end_node['class_nums']
            sum+=tempt
            print(i.end_node['name']+"  ")
            print(sum)
            #print(i.start_node['name'],i.end_node['name'])

        Node['total'] = sum
        graph.push(Node)
        return Node['total']


if __name__ == '__main__':
    #try:
        graph=Graph("http://localhost:7474",auth=("neo4j","szmt123456789"),name='neo4j')
        print("success")
        graph.run('match (n) detach delete n')
        print("success")
        GraphDB=GraphDatabase(graph)
        print("success")

    # except:
    #     print("error")