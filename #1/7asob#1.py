from datetime import datetime
from unicodedata import name


while True:
    name = input("Enter you name: ")
    if name == "stop":
        break
    birth_year = input("Enter you birth year: ")
    print("hello", name)
    print("You are", 2022 - int(birth_year), "years old.")