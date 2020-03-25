from data_utils_semeval16 import *

data_dir='../data/semeval2016/bert-pair/'

labels=['positive', 'neutral', 'negative', 'none']

file_names = get_files(data_dir, "csv")

# generate files for NLI_B and QA_B task

for file_name in file_names:
    if 'NLI_M' in file_name:
        with open(data_dir+file_name,"r",encoding="utf-8") as f, \
            open(data_dir+file_name[:-5]+"B.csv","w",encoding="utf-8") as g_nli, \
            open(data_dir+file_name[:-9]+"QA_B.csv","w",encoding="utf-8") as g_qa:
            s=f.readline().strip()
            while s:
                cols=s.split("\t")
                for label in labels:
                    target, aspect = cols[2].split("-")
                    t_nli = label + " - " + cols[2]
                    t_qa = "the polarity of the aspect " + aspect + " of " + target + " is " + label + " ."
                    if cols[1]==label:
                        g_nli.write(cols[0]+"\t1\t"+t_nli+"\t"+cols[3]+"\n")
                        g_qa.write(cols[0]+"\t1\t"+t_qa+"\t"+cols[3]+"\n")
                    else:
                        g_nli.write(cols[0]+"\t0\t"+t_nli+"\t"+cols[3]+"\n")
                        g_qa.write(cols[0]+"\t0\t"+t_qa+"\t"+cols[3]+"\n")
                s = f.readline().strip()