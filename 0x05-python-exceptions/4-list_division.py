#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for x in range(list_length):
        try:
            newlist.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            newlist.append(0)
            continue
        except ArithmeticError:
            print("division by 0")
            newlist.append(0)
            continue
        except IndexError:
            print("out of range")
            newlist.append(0)
            continue
        finally:
            pass
    return newlist
