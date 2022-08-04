from inner import inner

def nested_str():
    return "this is nest"

def inner_nested():
    x = 3
    return [inner(), x]

def nested_nums():
    return {0:[1,2,3], 1:[2,3,4]}