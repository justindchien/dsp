import pandas as pd
from pandas import Series
faculty = pd.read_csv("faculty.csv")
#Removing all random . from degree names
faculty[' degree'] = faculty[' degree'].str.replace('.','')

#Splitting multiple degrees into their own rows
degree_split = faculty[' degree'].str.strip().str.split(' ').apply(Series, 1).stack()
degree_split.index = degree_split.index.droplevel(-1)
degree_split.name = ' degree'
degree_split

#Replacing degree column
faculty2 = faculty
del faculty2[' degree']
deg_faculty = faculty2.join(degree_split)

#Counting degree occurance
pd.value_counts(deg_faculty[' degree'].values, sort=False)

#Fix one typo and counting faculty titles
faculty[' title'] = faculty[' title'].str.replace('is ','of ')
pd.value_counts(faculty[' title'].values, sort=False)

#Printing email list
emails = faculty[' email'].tolist()
print(emails)

#Printing unique domains of emails in list
domains = []
for email in emails:
    domains.append(email[email.index("@"):])
unique_domains = set(domains)
domains = list(unique_domains)
print(domains)
