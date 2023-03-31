from TodoDAO import TodoDAO
from Todo import Todo
import json
def main():
    dao = TodoDAO("todos.db")

    # with open("todos.json") as f:
    #     data = json.load(f)
    #     print(data)
    #     for data_todo in data:
    #         del data_todo['id']
    #         print(data_todo)
    #         todo = Todo(**data_todo)
    #         dao.save(todo)

    all_todos =dao.findAll()
    print(all_todos)
    print(next(all_todos))
    print(next(all_todos))
    print(next(all_todos))
    print(next(all_todos))
    # print(list(all_todos))
    # for todo in all_todos:
    #     print(todo )

if __name__=='__main__':
    main()
