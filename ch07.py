
def main():
    a = 2
    b = 3
    c = a/b
    print(f"c = {c:.4%}")
    print(f"{c=:.4%}")

    s = "{}/{} = {:.4%}".format(a,b,c)

    # s = "{2} = {0}/{1}".format(a,b,c)
    print(s)

    l = [2,3,2/3]
    s = "{}/{} = {:.4%}".format(*l)
    print(s)
    d = {
        "a":2,
        "b":3,
        "c":3/2
    }

    s = "{a}/{b} = {c:.4%}".format(a=2,b=3,c=2/3)
    print(s)
    s = "{a}/{b} = {c:.4%}".format(**d)
    print(s)


def hello(name,firstname):
    print("hello",name,firstname)

if __name__=='__main__':
    # main()
    l = ["GAURAT","Fred"]
    d = {
        "name":"GAURAT",
        "firstname":"Fred",
    }
    # hello(name="GAURAT",firstname="Fred")
    hello(**d)




