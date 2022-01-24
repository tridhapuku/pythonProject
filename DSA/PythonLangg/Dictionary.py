

lis = [{'name': 'Nandini', 'age': 20} , \
       {'name' : 'Manjit' , 'age': 20} , \
       {'name': 'Nikhil' , 'age' : 19} , \
       {'name': 'Akbar' , 'age' : 40}]

print(lis)
print(len(lis))
print(lis[0]['name'] + ' , ' + str(lis[0]['age']))
# for i in range(len(lis)):
#        print(lis[i]['name'])

for i in range(len(lis)):
       print()
       for key in lis[i]:
              print(lis[i][key], end = ' ')


print(type(lis))
print('sorting lis by age')
SortedLis = sorted(lis, key = lambda i: i['age'])
print(SortedLis)

SortedLisName = sorted(lis, key= lambda i:i['name'])
print(SortedLisName)

SortedLis2Keys = sorted(lis , key= lambda i: (i['name'] ,i['age'] ))
print(SortedLis2Keys)