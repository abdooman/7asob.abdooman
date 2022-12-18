
#from unittest import result


#from operator import le


#numbers = [2, 5, 3, 1, 4]

#result = 1

#for number in numbers:
#    result = number * result

#def new_func(numbers):
#   result = []
#   sum = 0 

#    for number in numbers:
#        sum = sum + number
#        result.append(sum)
#    print(result)

#new_func(numbers)
#--------------------------------------------------------------------------------------------
#numbers = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]
#seen = {}
#dups = []

#for number in numbers:
#    if number not in seen:
#        seen[number] = 1
#    else:
#        if seen[number] == 1:
#           dups.append(number)
#       seen[number] +=1
#print(dups)
#-----------------------------------------------------
#words = ['data', 'science', 'machine', 'learning']
#char_conut = {i: len(i) for i in words}
#print(char_conut)
#---------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grouped_numbers = []
size = 5 
for i in range(0, len(numbers), size):
    grouped_numbers.append(numbers[i:i+size])

print(grouped_numbers)