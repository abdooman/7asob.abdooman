

test = "   Hello, world  "
print(test.upper())

#lower()
test = "HELLO WORLD"
print(test.lower())


#isupper
print(test.isupper())
#islower
print(test.islower())

#title
print(test.title())
#capitalize
print(test.capitalize())

#swapcase
print(test.swapcase())
print('---------------')
#startwith()
print(test.startswith("H"))
#endswith()
print(test.endswith("d"))

#strip()
print(test.strip())


#lstrip()
print(test.lstrip())

#rstrip()
print(test.rstrip())

#zfill
days= "9"
hours= "5"
min= "14"
sec= "45"
print(f'{days.zfill(2)}:{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}') 



#join
list= ["hello", "world"]
print(' abc '.join(list))

#split 
test = "Hello, world"
print(test.split())

#splitlines
test = '''How are you ?
im fine 
thank you '''
print(test.splitlines())

print('----------------------------------------------------------------------------------')



#center()
tab= "hello"
print(tab.center(8))
#ljust()
print(tab.ljust(8))
#rjust()
print(tab.rjust(20))

#expandtabs()
tab2= "hello\tmy name is Khalid\t and i love math"
print(tab2.expandtabs(15))

#index(substring,start,end)
meth= "Hello, pepole"
print(meth.index('pepole',4,))

#finde
meth2="my name is abdullah"
print(meth2.find('e'))
#replace
meth3="my name is ahmad and my friend ahmad "
x=meth3.replace("ahmad", "mohammed",1)
print(x)
