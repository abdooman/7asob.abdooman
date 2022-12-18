stringOfJsonData = '{"name": "Api", "isCat": true, "miceCaught": 0,"felineIQ": null}'

import json

#read json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# write json
ValuePython = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(ValuePython)
print(stringOfJsonData)