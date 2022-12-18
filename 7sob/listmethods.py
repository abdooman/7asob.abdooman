#append and insert

from traceback import print_list


list = ["Ahmad", "Mohammad", "Zyad", "Sara", "Abdooman"]
list.append("yzen")
print(list)

list.insert(1,"Hoda")
print(list)

#print(#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##   )

#extend
oldEmployess = ["alaa","osama"]
list.extend(oldEmployess)
print(list)

#remove
list = ["Ahmad", "Mohammad", "Zyad", "Sara", "Abdooman"]
list.remove("Ahmad")
print(list)
#del statement
del list [3]
print(list)

#sort
list.sort()
print(list)

#revers
list.reverse()
print(list)

#pop
list.pop(2)
print(list)

print("----------------------------------------------------------------------")

list = ["Ahmad", "Mohammad", "Zyad", "Sara", "Abdooman", "Zyad"]

#index
print(list.index("Sara"))


#count
print(list.count("Zyad"))
#copy
txt = list.copy()
print(txt)
print(list)

#clear
list.clear()
print(list)
