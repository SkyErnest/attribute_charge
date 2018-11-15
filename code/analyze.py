import numpy as np

with open('data/test','r',encoding='utf-8') as f:
    accu_count={}
    for line in f:
        _,label,_=line.split('\t')
        if label not in accu_count:
            accu_count[label] = 1
        else:
            accu_count[label] += 1

with open('data/wrong_predictions.txt','r') as f:
    p_count={}
    l_count={}
    pl_count={}
    for line in f:
        index,p,l=line.strip()[1:-1].split(', ')
        if p not in p_count:
            p_count[p]=1
        else:
            p_count[p] += 1
        if l not in l_count:
            l_count[l]=1
        else:
            l_count[l] += 1
        if (p,l) not in pl_count:
            pl_count[(p,l)]=1
        else:
            pl_count[(p,l)] += 1

    print(sorted(accu_count.items(),key=lambda x:accu_count[x[0]]))
    print(sorted(p_count.items(),key=lambda x:p_count[x[0]]))
    print(sorted(l_count.items(),key=lambda x:l_count[x[0]]))
    print(sorted(pl_count.items(),key=lambda x:pl_count[x[0]]))