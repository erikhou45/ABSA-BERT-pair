import os
from collections import defaultdict

from data_utils_semeval16 import *

data_dir='../data/semeval2016/'
dir_path = data_dir+'single-entity/NLI_M/'

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

file_names = get_files(data_dir)

for file_name in file_names:
    with open(dir_path+"Laptop_"+file_name[10:-4]+"_NLI_M.csv","w",encoding="utf-8") as g_laptop:
        with open(data_dir+file_name,"r",encoding="utf-8") as f:
            s=f.readline().strip()   
            while s:
                category=[]
                polarity = defaultdict(lambda: [])
                if "<sentence id" in s:
                    left=s.find("id")
                    right=s.find(">")
                    id=s[left+4:right-1]
                    while not "</sentence>" in s:
                        if "<text>" in s:
                            left=s.find("<text>")
                            right=s.find("</text>")
                            text=s[left+6:right].replace("&apos;", "'")
                        if "<Opinion category" in s:
                            s = s.replace(" ", "")
                            left=s.find("category=")
                            pound=s.find("#")
                            right=s.find("polarity=")
                            target=s[left+10:pound]
                            aspect=s[pound+1:right-1]
                            left=s.find("polarity=")
                            right=s.find("/>")
                            polarity[(target,aspect)] = s[left+10:right-1]
                        s=f.readline().strip()
                    for target in ["LAPTOP"]:
                        for aspect in ASPECTS:
                            if (target,aspect) in polarity:
                                g_laptop.write(id+"\t"+polarity[(target,aspect)]+"\t"+aspect+"\t"+text+"\n")
                            else:
                                g_laptop.write(id+"\t"+"none"+"\t"+aspect+"\t"+text+"\n")
                else:
                    s = f.readline().strip()


