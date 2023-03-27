a=[1,3,2,4,3]

for i in a:
    print (f'item:{i}')
#Dictionary:

b={"name":"raziel","last_name":"Afandaev","age":1200}

for k in b:
    print(f'they key:{k},points at {b[k]}')

#set the out put is : {1, 2, 3, 4}

s={1,3,2,4,4,1,2}
print(s)

d=[1,5,2,5,3]
g=[1,2]
ans=[]
for i in d:
    if i in g:
        continue
    else:
        ans.append(i)
print(set(ans))

ans1=[i for i in d if i not in g]
print(ans1)

gset=set(g)

for i in d:
    if i not in gset:
        ans.append(i)
print(ans)