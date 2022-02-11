import requests

from Todo import Todo

def main():
    url = "http://jsonplaceholder.typicode.com/todos"
    
    r = requests.get(url)
    todos = r.json()

    dao = TodoDAO("todos_database.db")
    for todo in todos:
        # obj = Todo(id=todo['id'],title=todo['title'],...)
        obj = Todo(**todo)
        print(obj)
        dao.save(obj)
        


if __name__ == '__main__':
    main()