from pprint import pprint

def main():
    data = []
    with open('todos.csv') as f:
        lines = f.readlines()
        header = lines[0].strip().split(';')
        values = lines[1:]

        for line in values:
            dict_values = line.strip().split(';')
            z = dict(zip(header,dict_values))
            data.append(z)

    pprint(data)

if __name__=='__main__':
    main()
