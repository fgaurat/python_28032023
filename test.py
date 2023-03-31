



a = "toto"

def hello():
    global a
    a = "tutu"
    print(a)

print(a)
hello()
print(a)
