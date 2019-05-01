#implement deep_find_all(data, key) which finds the given key in the data and returns array of the found values.
from collections.abc import Iterable
from collections.abc import ItemsView
def deep_find_all_dfs(data, key, vals = []):
    for k, v in data.items():
        if k==key:
            vals.append(v)
        elif isinstance(v, Iterable) and not isinstance(v, str):
            if type(v) is dict:
                deep_find_all_dfs(v, key, vals)
            else:
                for i in v:
                    deep_find_all_dfs(i, key, vals)
    return vals


def deep_find_all_bfs(d, key):
    iters = list(d.items())
    findings =[]
    while iters:
        it = list(iters.pop())
        if it[0]==key:
            findings.insert(0, it[1])
        elif isinstance(it[1], Iterable) and not isinstance(it[1], str):
            if type(it[1]) is dict:
                for item in list(it[1].items()):
                    iters.insert(0, item)
            else:
                for el in it[1]:
                    for item in list(el.items()):
                        iters.insert(0, item)

    return findings

# if __name__=='__main__':
#     #test
#     sample_data = {1: {'pet': 'dog', 'food': 'pizza'},
#                     3: 'summer',
#                     4: [{'mother': 'mom', 'father': 'dad'}, {'friend': 'mariika' }, {'pet': 'dog', 'food': 'burger'}]
#                     }   

#     print(deep_find_all_bfs(sample_data, 'food'))
#     print(deep_find_all_dfs(sample_data, 'food'))
