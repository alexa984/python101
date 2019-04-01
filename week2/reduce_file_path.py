#reduce_file_path

def reduce_file_path(path):

    res_path=path
    
    #remove //
    res_path=''.join([res_path[i] for i in range(len(res_path)-1)
        if res_path[i+1] != res_path[i] or res_path[i]!='/']+[res_path[-1]])

    #removing ../ as parent dir
    while '../' in res_path:
        pos = res_path.rfind('../')
        if pos == 1:
            res_path = res_path[3:]
        else:
            res_path = res_path[:pos-1] + res_path[(pos+4):]
            while True:
                res_path = res_path[:pos-1]
                if res_path.endswith('/'):
                    break
                pos-=1

    #remove ./
    res_path = res_path.replace('./', '')

    #remove last /
    if res_path[-1] == '/' and len(res_path) > 1:
        res_path = res_path[:len(res_path)-1]

    return res_path

#print(reduce_file_path("/etc/../etc/../etc/../"))