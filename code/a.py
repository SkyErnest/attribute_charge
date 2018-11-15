import numpy as np

indices=[]
wrong=[]
label=[]
pair=[]
with open('wrong_predictions.txt','r') as f:
    for line in f:
        indices.append(int(line.strip('()\n').split(', ')[0]))
        wrong.append(int(line.strip('()\n').split(', ')[1]))
        label.append(int(line.strip('()\n').split(', ')[2]))
        pair.append([wrong[-1],label[-1]])
# with open('data/test','r',encoding='utf-8') as f:
#     res=np.array(f.read().split('\n'))[indices]
#     with open('wrong_pred_data.txt','w',encoding='utf-8') as f2:
#         for each in res:
#             f2.write(each)
#             f2.write('\n')
count_pred,count_l={},{}
count_pair={}
for each in wrong:
    if each not in count_pred:
        count_pred[each]=1
    else:
        count_pred[each]+=1
for each in label:
    if each not in count_l:
        count_l[each]=1
    else:
        count_l[each]+=1
for each in pair:
    each=tuple(each)
    if each not in count_pair:
        count_pair[each]=1
    else:
        count_pair[each]+=1
print(sorted(count_pred.items(),key=lambda x:x[1]))
print(sorted(count_l.items(),key=lambda x:x[1]))
print(sorted(count_pair.items(),key=lambda x:x[1]))