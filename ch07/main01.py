

def main():
    d ={ 
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    k = "id"
    s = f'id : {d[k]},title:{d["title"]}'
    print(s)

    # s= "id: {0}, title: {1}".format(d['id'], d['title']) 
    s= "id: {}, title: {}".format(d['id'], d['title'])# respecte l'ordre
    print(s)
    s= "id: {the_id}, title: {the_title}".format(the_id=d['id'], the_title=d['title'])# respecte l'ordre
    print(s)
    s= "id: {id}, title: {title}".format(id=d['id'], title=d['title'])# respecte l'ordre
    print(s)
    s= "title: {title}, id: {id}".format(**d) # .format(id=d['id'], title=d['title'], completed=['completed'])
    print(s)

    l = [10,20,30]
    
    s = "{}, {}".format(*l)# "{0}, {1}".format(10,20,30)
    
    print(s)

if __name__ == '__main__':
    main()