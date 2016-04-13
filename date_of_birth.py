# take a user entered date of birth and name and return the age of that person

import datetime

dob_dictionary = {}

count = 0


while count < 1:
    name = input("Enter a name:")
    valid_dob = False
    while not valid_dob:
        try:
            dob = input("Enter a DOB:(use spaces)")
            dob = dob.split()
            dob[0] = int(dob[0])
            dob[1] = int(dob[1])
            dob[2] = int(dob[2])
            dob_dictionary[name] = dob
            count += 1
            valid_dob = True
        except ValueError:
            print("Enter a correct value")
        except IndexError:
            print("Enter a correct value")

current_date = datetime.date.today().year

for name in dob_dictionary:
    age = current_date - dob_dictionary[name][2]
    print(name, "is ", age, "years old")