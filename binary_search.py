def binary(list,value):
    l=0
    h=len(list)-1
    while l<=h:
        m=(h+l)//2
        if list[m]==value:
            return True
        elif list[m]<value:
            l=m+1
        else:
            h=m-1
    return False
list=list(range(1,11))
print(binary(list,9))

