def insertion_sort(list):
    n=len(list)
    for i in range(n-1):
        j=i
        while j>0 and list[j-1]>list[j]:
            list[j-1],list[j]=list[j],list[j-1]
            j=j-1
arr=[1,4,2,4,2,5]
insertion_sort(arr)
print(arr)