# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


# input()


l = ['Valeur 01','Valeur 02','Valeur 03']

for v in l:
    print(v)

for i in range(len(l)):
    print(str(i)+" "+l[i])
    print(i,l[i])


print(range(5))
print(list(range(5)))

l = [3,5,2,6]
s = 0
for v in l:
    # s = s +v 
    s+=v 

for i in range(len(l)):
    s+=l[i] 
print(s)# 16

l = [3,5,2,6,5,8,9,12]
f = 2444

print(l)
for v in l:
    print(v)
    if v == f:
        found=True
        break
else:
    found=False
    print("pas trouvé")
print(found)

print(50*'-')

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

def fib2(n=200):
    """Return a Fibonacci series up to n."""
    l=[]
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l


l = fib2(n=2000) 
print(l)# [1,1,2,3,5,8,...]
l = fib2() 
print(l)# [1,1,2,3,5,8,...]


print(50*"-")

def hello(name,firstname="toto"):
    print("name "+name+" firstname : "+firstname)

hello('GAURAT','Frédéric')
hello(firstname='Frédéric',name='GAURAT')

print(50*"-")


def add(*args)->int:
    """
    return sum of all values in l
    """
    print(l)
    s = 0
    for v in args:
        # s = s +v 
        s+=v 
    return s

mes_valeurs = [3,5,2,6]
# result = add(mes_valeurs)
result = add(3,5,2,6)
print(result) # 16
result = add(*mes_valeurs)
print(result) # 16

print("toto","tutu","tata",sep="-")

print(*mes_valeurs,sep=";")

def hello(**kwargs):# Keywords arguments : kwargs
    print(kwargs)
    print("name",kwargs['name'],
          "firstname",kwargs['firstname'])

hello(firstname='Frédéric',name='GAURAT')


print(50*"-")

def mult2(v):
    return v*2


l2 = list(map(mult2,l1))

# mult2 = lambda v:v*2
l2 = list(map(lambda v:v*2,l1))

print(l1)
print(l2)

# l2 = [2,4,6,8,10]



