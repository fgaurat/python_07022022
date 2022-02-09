#!/usr/local/opt/python@3.9/bin/python3
print("Hello World")

# REPL
# Read Eval Print Loop

# TheWorldIsFlat => PascalCase, UpperCamelCase
# theWorldIsFlat => camelCase
# the_world_is_flat => snake_case




the_world_is_flat = False
print(type(the_world_is_flat))

if the_world_is_flat:
    print("Be careful not to fall off!")
    print("fin")


s = "hello, l'orage gronde"
s2 = 'hello, l\'orage gronde'
s3 = 'valeur de s : "hello" '
print(s)
print(s2)
print(s3)

s4 = "valeur 1\nvaleur 2"
print(s4)
s5 = "valeur 1\tvaleur 2"
print(s5)
p = "c:\\tutoriel\\new"
print(p)
p1 = r"c:\tutoriel\new"
print(p)

s6 = """
    valeur 1
    valeur 2
"""
print(s6)

print(50*'-')

a = "2"
int_a = int(a)
print(type(int_a))
print(type("toto"))
print("la valeur de a : "+str(a))


