# api->list->remove dup file->new module
items =[1,2,3,4,4,5,5,6,7,8,8,8,9,10]
dup = []
for i in items:
    count=0
    for j in items:
        if i == j:
            count=count+1
    if count>1 and i not in dup:
        dup.append(i) 
print(dup)