from Todo import Todo
import sqlite3
from pprint import pprint
class TodoDAO:
    


    def __init__(self,db_file):
       self._con = sqlite3.connect(db_file)


    def save(self,todo:Todo):
        cur = self._con.cursor()
        cur.execute(f"""
            INSERT INTO todos_tbl (user_id,title,completed) 
            VALUES ({todo.userId},'{todo.title}',{todo.completed})
                
        """)
        self._con.commit()
        
    def findAll(self):
        # all = []
        cur = self._con.cursor()
        res = cur.execute("SELECT * FROM todos_tbl")
        todos = res.fetchall()
        for t in todos:
            todo = Todo(*t)
            yield todo
        #     all.append(todo)
        # return all

    def __del__(self):
        self._con.close()