
from collections import deque
# https://jsonplaceholder.typicode.com/todos
# https://mockaroo.com


l1 = [1,2,4,3,4,5,5,7,6,9,12]
print(l1)

v = l1.pop()
print(v)
print(l1)
print("nb 5 ?",l1.count(5))

if 7 in l1:
    print('ok')
else:
    print('ko')

print(l1)

l1.insert(0,0)
print(l1)
first_value = l1.pop(0)
print(l1)
print("first_value",first_value)

l1_deque = deque(l1)
l1_deque.appendleft(0)
first_value = l1_deque.popleft()
print(l1_deque)
print("first_value",first_value)



l = [1,2,3,4,5]
l1 = []
for i in l:
    if i %2 ==0:
        l1.append(i*2)
print(l1)

l1 = list(map(lambda v:v*2,l))
print(l1)

l1 = [i*2 for i in l if i %2 ==0]
print(l1)
print(50*'-')

l = [" ligne1  ","  ligne2","  ligne3   "]
l1 = [v.strip() for v in l]
print(l)
print(l1)

l = ['toto','titi','tata']
l1 = [12,56,78]
z = zip(l,l1)
print(list(z))
print(50*'-')

t = 10,20,30,40,50
s = 12,
print(t)
print(s)
a,b=0,1

def f():
    return "toto","titi",'tata',"toto","titi",'tata'

r1,r2,*r = f()
print(r1)
print(r2)
print(r)

a,b,*c=0,1,2,3

print(50*'-')
s = {12,20,34,20,12,54,76}
print(s)
l = [12,20,34,20,12,54,76]
l = list(set(l))

print(50*'-')


d = {
    "name":"GAURAT",
    "firstname":"Fred",
}

print(d)
print(d['name'])

for k in d:
    print(k,d[k])

values = d.values()
keys = d.keys()

print(values)
print(keys)


for k,v in d.items():
    print(k,v)

l = ["Valeur 01","Valeur 02","Valeur 03","Valeur 04"]

for i,v in enumerate(l):
    print(i,v)

if 'Fred' in d.values():
    print("ok")
else:
    print("ko")


    