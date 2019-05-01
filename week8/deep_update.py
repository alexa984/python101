#Implement deep_update(data, key, val) which updates every occurance of the given key in the data with val.
from collections.abc import Iterable
def deep_update(data, key, val):
    for k, v in data.items():
        if k==key:
            data[k] = val
        elif isinstance(v, Iterable) and not isinstance(v, str):
            if type(v) is dict:
                deep_update(v, key, val)
            else:
                for i in v:
                    deep_update(i, key, val)


# if __name__=='__main__':
#     #test
#     sample_data = {1: {'pet': 'dog', 'food': 'pizza'},
#                     3: 'summer',
#                     4: [{'mother': 'mom', 'father': 'dad'}, {'friend': 'mariika' }, {'pet': 'dog', 'food': 'burger'}]
#                     }   

#     deep_update(sample_data, 'food', 'orange')
#     print(sample_data)
