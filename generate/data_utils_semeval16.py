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