import requests

from Todo import Todo
from TodoDAO import TodoDAO
import configparser
import argparse

def main():
    parser = argparse.ArgumentParser(description='TP read and write DB.')
    parser.add_argument('config_file',help="Configuration file")
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read(args.config_file)


    data_file = config['DB']['data_file']
    # url = "http://jsonplaceholder.typicode.com/todos"
    # r = requests.get(url)
    # todos = r.json()

    dao = TodoDAO(data_file)
    # for todo in todos:
    #     # obj = Todo(id=todo['id'],title=todo['title'],...)
    #     obj = Todo(**todo)
    #     print(obj)
    #     dao.save(obj)

    list_todos = dao.findAll()

    for todo in list_todos:
        print(todo)


if __name__ == '__main__':
    main()