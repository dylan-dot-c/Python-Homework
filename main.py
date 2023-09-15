def hello_name(user_name: str):
    print("Hello " + user_name)


def first_odds():
    # range(start, end, step)
    for i in range(1, 101, 2):
        print(i)

def max_num_in_list(a_list: list):
    x = a_list[0]
    for i in a_list:
        if i > x:
            x = i
    return x

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def is_consecutive(a_list: list):
    for i in range(len(a_list)):
        if i + 1 == len(a_list):
            continue
        if a_list[i] + 1 == a_list[i + 1]:
            continue
        else:
            return False
            # break
    else:
        return True
    
# Testing
# hello_name("Dylan Heslop")
# first_odds()
# print(is_leap_year(2000))
# print(max_num_in_list([14,12,65,12,8,54,23,56,87,43,21,0]))
# print(is_consecutive([1, 2, 3, 4, 5, 6, 7]))