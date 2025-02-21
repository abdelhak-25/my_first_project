def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i,n):
            if arr[min_index]>arr[j]:
                min_index=j
            arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr
def bubble_sort(arr):
    n=len(arr)
    permition=True
    while permition:
        permition=False
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
                permition=True
    return arr
print('welcome')
print('1:sorting by selection\n2:bubble sorting')

array=[]

try:
    n=int(input('Enter your choise:'))
    while True:
        try:
            numbers=int(input('enter number to add to the list/or 99 to end :'))
            array.append(numbers)
            if numbers==99:
                break
        except:
            print('enter just numbers')
        
    print('your list befor :')
    if 99 in array:
        array.remove(99)
    print(array)
    if n==1:
        array=selection_sort(array)
    elif n==2:
        array=bubble_sort(array)
    print('your list after')
    print(array)
except:
    print('Enter valaid numbers')



