# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if (count >= 10):
        number = 'many'
    else:
        number = count
    return ("Number of donuts: " + str(number))

    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    new = []
    if (len(s) >= 2):
        new.append(s[0])
        new.append(s[1])
        new.append(s[len(s)-2])
        new.append(s[len(s)-1])
    return "".join(new)

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
    new = []
    new.append(s[0])
    for x in s[1:]:
        if (x == s[0]):
            new.append("*")
        else:
            new.append(x)
    return "".join(new)
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
    new = []
    new.append(b[0])
    new.append(b[1])
    for x in a[2:]:
        new.append(x)
    new.append(" ")
    new.append(a[0])
    new.append(a[1])
    for y in b[2:]:
        new.append(y)
    return "".join(new)

    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if (len(s) >=3):
        if (s[-3]=='i' and s[-2]=='n' and s[-1]=='g'):
            new = s+"ly"
        else:
            new = s+"ing"
    else:
        new = s
    return new
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    not_pos = s.find('not')
    bad_pos = s.find('bad')
    if not_pos < bad_pos:
        new = s[:not_pos] + 'good' +s[bad_pos+3:]
        return new
    else:
        return s
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


import math
def front_back(a,b):
    if (len(a)%2 == 0):
        a_half = int(len(a)/2)
    else:
        a_half = int(math.ceil(len(a)/2))
    if (len(b)%2 == 0):
        b_half = int(len(b)/2)
    else:
        b_half = int(math.ceil(len(b)/2))

    a_front = a[:a_half]
    a_back = a[a_half:]
    b_front = b[:b_half]
    b_back = b[b_half:]

    return a_front + b_front + a_back + b_back
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
