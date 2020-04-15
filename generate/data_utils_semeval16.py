import re
import os
    
def get_files(data_dir, data_type="xml"):
    files = []
    for file in os.listdir(data_dir):
        m = re.match("^EN_Laptop.*\."+data_type,file)
        if m:
            files.append(m.group())
    return files

LAPTOP_TARGETS = [
    "LAPTOP", "DISPLAY", "CPU", "MOTHERBOARD", "HARD_DISC", "MEMORY",
    "BATTERY", "POWER_SUPPLY", "KEYBOARD", "MOUSE", "FANS_COOLING",
    "OPTICAL_DRIVES", "PORTS", "GRAPHICS", "MULTIMEDIA_DEVICES", 
    "HARDWARE", "OS", "SOFTWARE", "WARRANTY", "SHIPPING", "SUPPORT", 
    "COMPANY"
]

ASPECTS = [
    "GENERAL", "PRICE", "QUALITY", "OPERATION_PERFORMANCE",
    "USABILITY", "DESIGN_FEATURES", "PORTABILITY", 
    "CONNECTIVITY", "MISCELLANEOUS"
]

# SAMPLING = {"Over_":(12,1),
#             "Under_":(1,0.08),
#             "Combo_":(5,0.4)
#            }
SAMPLING = {"Over_2_":{"positive":2,"neutral":2,"negative":2,"conflict":2,"none":1},
            "Over_Mix_1_":{"positive":1.5,"neutral":3,"negative":2.2,"conflict":5,"none":1},
            "Combo_5_04_":{"positive":5,"neutral":5,"negative":5,"conflict":5,"none":0.4},
            "Combo_3_045_":{"positive":3,"neutral":3,"negative":3,"conflict":3,"none":0.45},
            "Combo_2_05_":{"positive":2,"neutral":2,"negative":2,"conflict":2,"none":0.5}
           }