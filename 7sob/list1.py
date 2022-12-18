import imp
from winreg import EnableReflectionKey


list = ["Ahmad", "Mohammad", "Zyad", "Sara", "Abdooman"]

for i in range(5):
    print(list)


print(list[2:4])

for i in range(5):
    print(list[i])


for index,item in enumerate(list):
    print(f'index {index} was in list {item}  ')

import random
list = ["Ahmad", "Mohammad", "Zyad", "Sara", "Abdooman"]
print(random.choice(list))
random.shuffle(list)
print(list)