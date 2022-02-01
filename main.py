"""
Given a list of numbers as input. Print numbers that are divisible by 3 but not by 2. Also these numbers should lie in the range of 3 and 99 [inclusive].
Input-> [9,99,999,9999]
Output-> 9 99
"""

ls = [9,99,999,9999]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  if (e%3==0) and (3<=e<=99):
    print(e)
    