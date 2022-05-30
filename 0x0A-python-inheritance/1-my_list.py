#!/usr/bin/python3
"""Module 1-my_list.py 
create  a class MY_list that inhert from list
"""

class MyList(list):
    """that inhert from class list"""

    def print_sorted(self):

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
