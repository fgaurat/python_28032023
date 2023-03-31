import copy

# theWorldIsFlat => camelCase
# TheWorldIsFlat => UpperCamelCase, PascalCase
# the_world_is_flat => snake_case
# the-world-is-flat => kebab-case


print('Hello World')

the_world_is_flat = True

if the_world_is_flat: 
    print("Be careful not to fall off!")
    print("autre ligne")


s = "L'orage gronde"
s = 'L\'orage gronde'
print(s)
p = "c:\\new\\truc"
print(p)

p = r"c:\new\truc"
print(p)


"""
Init d'une 
chaîne de caractère
multi-lignes
"""

lines = """Ligne 1
Ligne 2
Ligne 3
"""
print(lines)


a =3
s = "valeur de a : "+str(a)

print(s)
print(50*'-')
b = "toto"*a
print(b)
print(50*'-')
word = 'Python'
print(word[2])
print(len(word))
print(word[len(word)-1])
print(word[-1])

# word[0] = 'J'
print(word)
print(50*'-')

a=2
b=2

print(id(a))
print(id(b))

print(word[:2])
print(word[2:])
word2 = 'J'+word[1:]
print(word2)
print(50*'-')

squares = [1, 4, 9, 16, 25]

b = squares[:]

print(squares)
print(b)
b[0]=1000
print(squares)
print(b)

l = [
    [10,20],
    [30,40],
    [50,60],
]
l2 = l[:]
l2 = copy.deepcopy(l)
print(l)
print(l2)
l2[1][1] = 1000
print(l)
print(l2)

print(50*'-')

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b