from inner import inner

def nested_str():
    return "this is nest"

def inner_nested():
    x = 3
    return [inner(), x]