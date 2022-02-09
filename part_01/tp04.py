# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

l =['Valeur 1','Valeur 2','Valeur 3','Valeur 4']

# for each; pour chaque valeur de la liste
for v in l:
    print(v)

for i in range(len(l)):
    print(i,l[i])
print(50*"-")

for i,v in enumerate(l):
    print(i,v)



# for i in "toto":
#     print(i)


# l1 = list(range(3))
# print(range(3))
# print(l1)


# for i in range(5,10,2.3):
#     print(i)


print(50*'-')

l = [1,2,3,4,5]

somme = 0
for i in l:
    print(somme,i)
    somme+=i # somme = somme+i

print(somme)

# => 15



print(50*'-')




the_values = [2,5,6,7,1,2]



for value in the_values:
    print(value)
    if value == 6:
        print("ok!")
        break
else:
    print("pas trouvé")

print(50*'-')

for value in the_values:
    if value == 6:
        pass

    print(value)


a =2
b=3
if a==2 | b==3:
    print('ok if')