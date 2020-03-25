import re
import os

def quantify_polarity(pol):
    if 'positive' in pol:
        return 1
    elif 'negative' in pol:
        return -1
    else:
        return 0

def cal_polarity(polarities):
    pol_sum = sum(polarities)
    if pol_sum > 0:
        return 'positive'
    elif pol_sum < 0:
        return 'negative'
    else:
        return 'neutral'
    
def get_files(data_dir):
    files = []
    for file in os.listdir(data_dir):
        m = re.match("^(EN_Laptop|CH_Cell).*\.xml",file)
        if m:
            files.append(m.group())
    return files

LAPTOP_TARGETS = [
    "LAPTOP", "DISPLAY", "CPU", "HARD_DISC", "MEMORY",
    "BATTERY", "POWER_SUPPLY", "KEYBOARD", "PORTS", "GRAPHICS",
    "MULTIMEDIA_DEVICES", "HARDWARE", "OS", "SOFTWARE", "WARRANTY", 
    "SHIPPING", "SUPPORT", "COMPANY"
]

CELL_TARGETS = [
    "PHONE", "DISPLAY", "CPU", "HARD_DISC", "MEMORY",
    "BATTERY", "POWER_SUPPLY", "KEYBOARD", "PORTS",
    "GRAPHICS", "MULTIMEDIA_DEVICES", "HARDWARE", "OS",
    "SOFTWARE", "WARRANTY", "SHIPPING", "SUPPORT", "COMPANY"
]

ASPECTS = [
    "GENERAL", "PRICE", "QUALITY", "OPERATION_PERFORMANCE",
    "USABILITY", "DESIGN_FEATURES", "CONNECTIVITY", "MISCELLANEOUS"
]