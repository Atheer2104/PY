import datetime

name = input("What's your name: ")

age = int(input("How old are you: "))

years = 100 - age
now = datetime.datetime.now()
currentYear = now.year
print(name + " you will be 100 years old in the year " + str(currentYear + years))
