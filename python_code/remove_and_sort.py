import tqdm
def remove_and_sort(edge_key_list):
#去除自环
    edge_list_unique=[]
    remove_list=[]
    for i in tqdm(range(len(edge_key_list))) :
        #自环
        if edge_key_list[i][0]==edge_key_list[i][1]:
            remove_list.append((i,edge_key_list[i]))
        #重复边
        if edge_key_list[i] not in edge_list_unique:
            edge_list_unique.append(edge_key_list[i])



        # print(i)
    # print(remove_list)
    # value__remove_list=[edge_value_list[i] for i,_ in remove_list]

    # for i,ele in remove_list:
    #
    #     edge_key_list.remove(ele)
    edge_list_sort=[[int(x[0]),int(x[1])]if int(x[0])<int(x[1]) else [int(x[1]),int(x[0])] for x in edge_list_unique]
# edge_list_sort
    sort_d = [value for index, value in sorted(enumerate(edge_list_sort), key=lambda d:d[1])]
    # sort_d
    return sort_d