def group(my_list):
    result=[]
    curr_list=[]
    pre=my_list[0]

    for i in range(0, len(my_list)):
        if my_list[i]==pre:
            curr_list.append(my_list[i])
        else:
            result.append(curr_list)
            curr_list=[my_list[i]]
            pre = my_list[i]

    result.append(curr_list)
    return result