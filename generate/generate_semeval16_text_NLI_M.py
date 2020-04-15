import pandas as pd
import numpy as np
import os
import random
from collections import defaultdict

from data_utils_semeval16 import *

data_dir = "../data/semeval2016/"
dir_path = data_dir + "bert-pair/text-level/"
os.makedirs(dir_path, exist_ok=True)
file_names = {"EN_Laptop_Text_Train.xml": "EN_Laptop_Text_Train_Complete_NLI_M.csv",
              "EN_Laptop_Text_Test_Gold.xml": "EN_Laptop_Text_Test_Gold_NLI_M.csv"}

for key in file_names:
    with open(dir_path+file_names[key],"w",encoding="utf-8") as g:
        with open(data_dir+key,"r",encoding="utf-8") as f:
            s=f.readline().strip()   
            review_count = 0
            while s:
                category=[]
                polarity = defaultdict(lambda: [])
                if "<Review rid" in s:
                    review_count += 1
                    left=s.find("id")
                    right=s.find(">")
                    rid=s[left+4:right-1]
                    texts=[]
                    while not "</Review>" in s:
                        if "<text>" in s:
                            left=s.find("<text>")
                            right=s.find("</text>")
                            texts.append(s[left+6:right].replace("&apos;","'"))
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
                    for target in LAPTOP_TARGETS:
                        for aspect in ASPECTS:
                            if (target,aspect) in polarity:
                                g.write(rid+"\t"+polarity[(target,aspect)]+"\t"+target+"-"+aspect+"\t"+" ".join(texts)+"\n")
                            else:
                                g.write(rid+"\t"+"none"+"\t"+target+"-"+aspect+"\t"+" ".join(texts)+"\n")
                else:
                    s = f.readline().strip()

            print(f"processed {review_count} reivews")


train_file = dir_path+file_names["EN_Laptop_Text_Train.xml"]
train_file_df = pd.read_csv(train_file, 
                       delimiter = "\t",
                       names = ["review_id", "label", "entity:aspect", "text"]
                       )
# train_file_df["label"] = train_file_df.label.map({'positive':0, 'neutral':1, 'negative':2, 'conflict':3, 'none':4})
review_ids = train_file_df.review_id.drop_duplicates()
rand_state = np.random.RandomState(seed=12)
dev_reviews = review_ids.sample(80, random_state=rand_state)
dev_df = train_file_df.merge(dev_reviews.to_frame(), how = "inner", on = "review_id").iloc[:,:4]
train_df = train_file_df.merge(dev_reviews, how = "outer", on = "review_id", indicator = True)
train_df = train_df[train_df._merge == "left_only"].iloc[:,:4]
dev_df.to_csv(os.path.join(dir_path,"EN_Laptop_Text_Dev_NLI_M.csv"), sep = "\t", index = False, header = False)
train_df.to_csv(os.path.join(dir_path,"EN_Laptop_Text_Train_NLI_M.csv"), sep = "\t", index = False, header = False)

print(train_file_df.review_id.drop_duplicates().count())
print(dev_df.review_id.drop_duplicates().count())
print(train_df.review_id.drop_duplicates().count())


rg_none = random.Random(10)
rg_others = random.Random(5)

files = ["EN_Laptop_Text_Train_NLI_M.csv"]

for key in SAMPLING:
    sample_type = key
    multipliers = SAMPLING[key]
    for file in files:
        input_file = os.path.join(dir_path, file)
        output_file = os.path.join(dir_path, file[:-9] + sample_type + file[-9:])
        with open(output_file, "w", encoding="utf-8") as g:
            with open(input_file, "r", encoding="utf-8") as f:
                l=f.readline().strip() 
                while l:
                    rid, polarity, category, text = l.split("\t")
                    if polarity == "none":
                        if rg_none.random() < multipliers["none"]:
                            g.write(rid+"\t"+polarity+"\t"+category+"\t"+text+"\n")
                    else:
                        for i in range(int(multipliers[polarity])):
                            g.write(rid+"\t"+polarity+"\t"+category+"\t"+text+"\n")
                        if rg_others.random() < (multipliers[polarity] % 1):
                            g.write(rid+"\t"+polarity+"\t"+category+"\t"+text+"\n")
                    l = f.readline().strip()
