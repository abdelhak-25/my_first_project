def selection_sort(list):
    n=len(list)
    for i in range(n):
        index_min=i
        for j in range(i,n):
            if list[j]<list[index_min]:
                index_min=j
        list[i],list[index_min]=list[index_min],list[i]

arr=[13,12,2,32,44,5]
selection_sort(arr)

print(arr)


