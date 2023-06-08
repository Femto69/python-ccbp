t=input()
l=int(len(t))
if t[l-1]=="M":
    ht=int(t[0:l-1])/60
    ht=round(ht,2)
    print(str(ht)+"H")
else:
    ht=int(t[0:l-1])/3600
    ht=round(ht,2)
    print(str(ht)+"H")