import pandas as pd
from pandas import Series
faculty = pd.read_csv("faculty.csv")
faculty[' degree'] = faculty[' degree'].str.replace('.','').str.strip()
faculty[' title'] = faculty[' title'].str.replace('is ','of ')

#Splitting first and last names
faculty['first name'] = faculty.name.str.split('\s+').str[0]
faculty['last name'] = faculty.name.str.split('\s+').str[-1]

#Create first dictionary
last_names = faculty['last name'].tolist()
first_names = faculty['first name'].tolist()
degrees = faculty[' degree'].tolist()
title = faculty[' title'].tolist()
email = faculty[' email'].tolist()

data = [list(a) for a in zip(last_names, degrees, title, email)]

faculty_dict = {}
for n in range(len(data)):
    if data[n][0] in faculty_dict.keys():
        faculty_dict[data[n][0]].append(data[n][1:])
    else:
        faculty_dict[data[n][0]] = data[n][1:]

#Create second dictionary
full_names = zip(first_names, last_names)
info = [list(b) for b in zip(degrees, title, email)]
professor_dict = dict(zip(full_names, info))

for key, value in sorted(professor_dict.items()):
    print(key, value)
    
#Create keys with last name first
keys = professor_dict.keys()
ln_sort = sorted(keys, key=lambda name: name[1])
for key in ln_sort:
    print(key, professor_dict[key])
