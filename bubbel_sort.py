def bubbel_sort(list):
    permitation=True
    while permitation:
        permitation=False
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                permitation=True
arr=[1,0,4,6,6]
bubbel_sort(arr)
print(arr)