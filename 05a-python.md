# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are both used to store multiple pieces of information within one variable. Tuples are immutable, so you will not be able to change the values once you create it. Lists are changeable. You can use tuples in a dictionary, but not lists because a dictionary stores information to those key values and would need them to stay constant to use them as a reference.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> They both hold multiple values. Lists can be indexed and keep order while sets are unordered without indexes unable to have duplicate data. 
Example of list: 
  weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
Example of set: 
  cart = set(['apple', 'banana', 'spam', 'ketchup', 'eggs'])
Finding an element is faster in a set because it is hashabale.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is a tool for building functions and similar to anonymous functions. It is typically used to write functions that are only used once.
Syntax: lambda input: function_want_returned
Example to sort x by last character: 
  x_last = sorted(x, key=lambda x: x[-1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow sequences to be built from other iterables, typically new list based on other lists.

'map' will apply an operation to each item. Syntax: map(function, sequence)
example:  doubled = map(lambda x: x*2, numbers)

equivalent for loop:
  def map(function, sequence):
    result = []
    for x in sequence:
      result.append (function(x))
    return result
    
example of doubled as a for loop:
  numbers = [1, 2, 3, 4, 5]
  doubled = []
  for number in numbers:
    doubled.append(numbers*2)

'filter' will keep the element that returns True. Syntax: filter(function, iterable)
keep positive numbers: pos = filter(lambda x: x>0, numbers)

equivalent for loop:
  def filter(function, iterable):
    result = []
    for x in iterable:
      if (function):
        result.append (x)
    return result

equivalent of keep positive numbers as a for loop:
  pos = []
  for x in numbers:
    if (x>0):
      numbers.append(x)
  return pos

It is a lot easier, compact, and elegant to use the built in 'map' and 'filter' functions.

Set comprehension for removing duplicate names: 
{name[0].upper() + name[1:].lower() for name in names}

Dictionary comprehension for counting letters in words: 
{letter : word.count(letter) for letter in word}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
