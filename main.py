def _is_simple_num(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def simple_nums_in_range(minimum, maximum):
    prime_list = []
    for num in range(minimum, maximum + 1):
        if _is_simple_num(num):
            prime_list.append(num)
    return prime_list
