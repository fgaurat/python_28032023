import json

def main():
    with open('todos.json') as f:
        data = json.load(f)
        print(data[0]['title'])
        print(data[0])

if __name__=='__main__':
    main()
