import csv 
import json
from pprint import pprint

def main():
    with open('todos_module_csv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)


def main_write_csv():
    data = []
    with open('todos.json') as f:
        data = json.load(f)

    with open('todos_module_csv.csv', 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)





if __name__=='__main__':
    main()
