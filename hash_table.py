l=[1,33,566,44,55,43,434,2,2]
d=dict()
for e in l :
    if e in d.keys():
        d[e]+=1
    else:
        d[e]=1
print(d)