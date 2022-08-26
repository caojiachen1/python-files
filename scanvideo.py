from tkinter import filedialog
import file
import shutil
import os

path=''
null=True
while null:
    path=filedialog.askdirectory()
    if path!='':
        null=False
path=path.replace('/',"\\")
path_=path+'_h265'
'''if not os.path.exists(path_):
    os.makedirs(path_)'''

count=0
exist=False
for item in os.scandir(path):
    if item.is_file():
        v=file.video(item.path)
        p=item.path
        if v=={}:
            continue
        print(item.path+'   '+v.codec)
        '''if v.codec=='hevc':
            exist=True
            #shutil.copy(item.path,path_)
            rename=str(count)+'.mp4'          
            dir,name=os.path.split(item.path) 
            #os.rename(item.path,os.path.split(item.path)[0]+str(count))
            count=count+1'''

'''if not exist:
    shutil.rmtree(path_)'''
