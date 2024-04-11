def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def get_odd_numbers(list):
    for i in list:
        if is_odd(i) == False:
            list.remove(i)
    return list

print(get_odd_numbers([1,2,3,4,5,6, 7,8,9,10]))

stack = [2,3,4]
print(stack.pop())