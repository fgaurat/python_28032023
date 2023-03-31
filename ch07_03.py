import json

def main():
    data = []
    with open('todos.json') as f:
        data = json.load(f)

    with open('todos_join.csv','w') as f:
        header = ";".join(data[0].keys())+"\n"
        f.write(header)
        
        for todo in data:
            values = todo.values()
            str_values = [str(v) for v in values]
            # for v in values:
            #     str_values.append(str(v))

            values = ";".join(str_values)+"\n"
            f.write(values)

def main_print():
    data = []
    with open('todos.json') as f:
        data = json.load(f)

    with open('todos.csv','w') as f:
        header = data[0].keys()
        print(*header,sep=";",file=f)
        for todo in data:
            print(*todo.values(),sep=";",file=f)

if __name__=='__main__':
    main()
