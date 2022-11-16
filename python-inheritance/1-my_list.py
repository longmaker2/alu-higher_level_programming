#!/usr/bin/python3
'''The List functions are inherited by this file'''


class MyList(list):
    '''This Class Inherits Function List'''

    def print_sorted(self):
        '''the code below prints the list In a sorted manner '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
