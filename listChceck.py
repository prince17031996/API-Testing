l1=[1,2,3,4,4,5]
l2=[5,5,4,3,2,1,1]

def listCheck(l1,l2):
    d1=dict()
    d2=dict()
    for x in l1:
        if x in d1:
            d1[x]+=1
        else:
            d1[x]=1
    for x in l2:
        if x in d2:
            d2[x]+=1
        else:
            d2[x]=1
    for k,v in d1.items():
        if d1[k]!=d2[k]:
            return False
    return True

print(listCheck(l1,l2))
