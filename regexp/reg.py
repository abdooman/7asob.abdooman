import re

txt = "My name is Ahmed"

search = re.search("[A-Z]", txt)

print(search)
print(search.span())
print(search.group())

#findall


#sub

txt = "I am a student at Hsoub Academy"
chang = re.sub(r"Hsoub Academy", "Hsoub-Academy", txt)

print(chang)

print('----------------------------------------------')


txt2 = "استئناف-رفع-الملفات-بعد-فقدان-الاتصال-في-جافاسكربت"
txtchange=  re.sub(r'-', ' ',txt2)

print(txtchange)