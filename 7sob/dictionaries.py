#names = ["Ahmed", "Omar", "Sara", "Hoda"]

#salary = [2000, 500, 1500, 700]

#numbers = ['052145672','5002149602', '5547896456', '654789526']

from unicodedata import name


ahmed ={
    'name' : 'Ahmed',
    'salary' : 1500,
    'number' : '052145672',
    'skills' : ['html', 'CSS', 'Python']

}

print(ahmed['skills'])



#birthdays = {'sara': 'Apr 1', 'saed':'Dec12', 'emad':'Mar4', 'tarq': 'Sep 15'}
#while True:
#    print("enter a name: (blank to quit)")
#    name = input()
#    if name == '':
#        break

#    if name in birthdays:
#        print(birthdays[name ]  +  '\nis the birthday of ' + name)

#    else:
#        print('I do not have birthday information for ' + name )
#        print('What is their birthday?')
#        bday = input()
#        birthdays[name] = bday
#        print('Birthday database updated.')

ahmed ={
    'name' : 'Ahmed',
    'salary' : 1500,
    'number' : '052145672',
    'skills' : ['html', 'CSS', 'Python']

}

print(ahmed.items())
print(ahmed.keys())
print(ahmed.values())


abdullrhman = {
    'frontend':{
        1: 'CSS',
        2: 'Boostrap'
    },
    'backend': {
        1: 'PHP',
        2: 'Node.js'

    }
}

print(abdullrhman['frontend'][2])

abdullatif = {
    'name': 'Abdullatif Badnjki',
    'هوايات ': 'السباحة وركوب الخيل والرماية ',
    'المهة': 'طالب'

}

print(abdullatif['name'])