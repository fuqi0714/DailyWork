import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--location', type=str, default=r'I:\DataFiles\ls\music',required=False)
parser.add_argument('--destiny_path', type=str, default=r'E:\MP3',required=False)
parser.add_argument('--filter_type', type=str, default='.flac',required=False)
args = parser.parse_args()


class FilesSelection:
    def ExecutionPath(self,location,target):
        self.dir_list=[]
        self.path=location
        files_list=os.listdir(self.path)
        #print(files_list)
        for f in files_list:
            full_path=os.path.join(location, f)
            if os.path.isdir(full_path):
                #print(full_path)
                self.dir_list.append(full_path)

        self.FilesMoving(self.dir_list,args.filter_type,target)





    def FilesMoving(self,files_list,file_type,target):

        for files in files_list:
            print(files)
            for file in os.listdir(files):
                #print(file)
                if file.endswith(file_type):
                    shutil.move(os.path.join(files, file),target)

        print("over")
            #print(os.path.join(files, "*" + file_type))
            # if files in glob.glob(os.path.join(files,"*"+file_type)):
            #     print("f")
            #     print(files)







if __name__ == '__main__':
    FS=FilesSelection()
    FS.ExecutionPath(args.location,args.destiny_path)