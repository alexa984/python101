def deep_find(data, key):
    for k, v in data.items():
        if k==key:
            return v
        elif type(v) is list:
            for i in v:
                temp=deep_find(i, key) 
                if temp is not None:
                    return temp
        elif type(v) is dict:
            temp = deep_find(v, key)
            if temp is not None:
                return temp

