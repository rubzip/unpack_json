import pandas as pd
from dateutil.parser import parse

def is_date(code)->bool:
    try:
        parse(code, fuzzy=False)
        return True
    except:
        return False
    
def return_type(value):
    val_type = type(value).__name__
    if value is None:
        return '???'
    elif val_type!='str':
        return val_type
    elif is_date(value):
        return 'date'
    else:
        return val_type

def get_tree(father:dict, father_name="", depth=0):
    data = []
    for son_name in father.keys():
        son = father[son_name]
        son_type = return_type(son)
        data.append([father_name, son_name, son_type, depth])
        if son_type=="dict":
            data += get_tree(son, son_name, depth+1)
        elif son_type=="list":
            if len(son)>0:
                if type(son[0]) is dict:
                    data += get_tree(son[0], son_name, depth+1)
    return data

def write_tree(tree):
    file = ""
    for node in tree:
        name, dtype, depth = node[1:4]
        if depth>0:
            file += '│   '*depth
        file += f"├── {name} : {dtype}\n"
    return file