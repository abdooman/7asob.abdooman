#get

ahmed ={
    'name' : 'Ahmed',
    'salary' : 1500,
    'number' : '052145672',
    'skills' : ['html', 'CSS', 'Python']

}
print(ahmed['name'] + ' he take ' + str(ahmed['salary']))

#set default

print(ahmed.setdefault('name', 'sara'))
print(ahmed)
