import os

path =os.chdir("D:\\test")
i=0
for file in os.listdir(path):
     new_file_name= "pic{}.jpeg".format(i)
     os.rename(file,new_file_name)
     i=i+1