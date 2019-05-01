# Implement deep_apply(func, data) which applies the given func to all keys from the given data.
from collections.abc import Iterable
def deep_apply(func, data):
    if not hasattr(func, '__call__'):
        raise TypeError

    for k, v in data.items():
        new_key = func(k)
        data[new_key] = data.pop(k)
        if isinstance(v, Iterable) and not isinstance(v, str):
            if type(v) is dict:
                deep_apply(func, v)
            else:
                for i in v:
                    deep_apply(func, i)


# if __name__ == '__main__':
#     def change(val):
#         return str(val) + '_changed'

#     sample_data = {'one': {'pet': 'dog', 'food': 'pizza'},
#                 'two': 'summer',
#                 'three': [{'mother': 'mom', 'father': 'dad'}, {'friend': 'mariika' }, {'pet': 'dog', 'food': 'burger'}]
#                 }   

#     deep_apply(change, sample_data)
#     print(sample_data)
