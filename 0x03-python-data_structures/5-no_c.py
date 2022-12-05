#!/usr/bin/python3
def no_c(my_string):
    """This method returns a 'new_string' through mapping of the old strings charcters"""
    new_string = my_string.translate({ord(letter): None for letter in 'cC'})
    return new_string
