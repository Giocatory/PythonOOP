import sys


def is_full_house(args: list):
    my_set = set(args)
    my_list = list(my_set)
    if len(my_set) == 2 and (args.count(my_list[0]) == 2 or args.count(my_list[0]) == 3) and (args.count(my_list[1]) == 2 or args.count(my_list[1]) == 3):
        return True
    else:
        return False


lst = ["10", "J", "10", "10", "10"]
result = is_full_house(lst)
print(result)
