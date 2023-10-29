from py2neo import *
import argparse
import module.GetItemFromCSV as GIFC
import pandas as pd
import time
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

        self.ModifyDB(graph)

    def ModifyDB(self,graph):
        graph=graph
        pandas_table = GIFC.GetItemFromCSV(args.file)

        self.GenerateNodeList(pandas_table,graph)

    def GenerateNodeList(self,pandas_table,graph):
        name_list = pandas_table['Name']
        l_name_list = pandas_table['L_name']
        length_list = pd.to_numeric(pandas_table['Length'])
        class_name_list = pd.to_numeric(pandas_table['Class_num'])
        total_list = pd.to_numeric(pandas_table['Total'])
        #print(total_list)
        for t in range( len(pandas_table)):
            print(t)
            n=Node('Owner',name=name_list[t],total=int(total_list[t]))
            time.sleep(0.2)
            #self.start_nodes.append(n)
            l=Node('Lecture',name=l_name_list[t],length=int(length_list[t]),class_nums=int(class_name_list[t]))
            time.sleep(0.3)
            #self.start_nodes.append(l)
            self.GenerateRelationshipList(graph,n,l)





    def GenerateRelationshipList(self,graph,start,end):
        r=Relationship(start,'Get',end)
        print(r)
        graph.merge(start, "Owner", "name")
        graph.merge(end, "Lecture", "name")
        graph.create(r)
        self.relastionships.append(r)
        self.GetAllLectures(start)


    def SubGraph(self):
        subgraph=Subgraph(self.start_nodes,self.relastionships)
        tx=graph.begin()
        tx.create(subgraph)
        graph.commit(tx)

    def GetAllLectures(self,Node):
        #self.SubGraph()
        sum=0
        res = list(self.rmatcher.match({Node}, r_type='Get', limit=None))
        #print(res[0].start_node['name'])
        for i in res:
            tempt=i.end_node['length']*i.end_node['class_nums']
            sum+=tempt

            #print(i.start_node['name'],i.end_node['name'])

        Node['total'] = sum
        graph.push(Node)


if __name__ == '__main__':
    # try:
        graph=Graph("http://localhost:7474",auth=("neo4j","szmt123456789"),name='neo4j')
        print("success")
        graph.run('match (n) detach delete n')
        print("success")
        GraphDB=GraphDatabase(graph)
        print("success")

    # except:
    #     print("error")