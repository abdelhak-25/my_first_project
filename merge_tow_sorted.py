#def merge_two_sorted(a,b):
#    n=len(a)
#    m=len(b)
#    i=0
#    j=0
#    r=[]
#    while i<n and j<m:
#        if a[i]<b[j]:
#            r.append(a[i])
#            i+=1
#        else:
#            r.append(b[j])
#            j+=1
#    while i<n:
#        r.append(a[i])
#        i+=1
#    while j<m:
#        r.append(b[j])
#        j+=1
#    return r
#def merge_sort(array):
#    n=len(array)
#    mid=n//2
#    if n==1:
#        return array
#    a=merge_sort(array[0:mid])
#    b=merge_sort(array[mid:n])
#    r=merge_two_sorted(a,b)
#    return r
#arr=[1,4,3,2,23,43,24,2,2,34,5,64]
#r=merge_sort(arr)
#print(r)

def merge_two_sorted(a,b):
    n=len(a)
    m=len(b)
    i=0
    j=0
    r=[]
    while i<n and j<m:
        if a[i]<b[j]:
            r.append(a[i])
            i+=1
        else:
            r.append(b[j])
            j+=1
    while i<n:
        r.append(a[i])
        i+=1
    while j<m:
        r.append(b[j])
        j+=1
    return r
def merge_sort(arr):
    n=len(arr)
    if n==1:
        return arr
    mid=n//2
    a=merge_sort(arr[0:mid])
    b=merge_sort(arr[mid:n])
    r=merge_two_sorted(a,b)
    return r

b=[21,23243,533,533553,34]
r=merge_sort(b)
print(r)
        
        