from copy import deepcopy


def getTotalX(a, b):
    num_between_good = set()
    num_between_wrong = set()
    for num in range(1, sorted(b)[0]+1):
        for num_a in a:
            if num % num_a == 0:
                num_between_good.add(num)
            else:
                num_between_wrong.add(num)
    only_good_after_checking_a = num_between_good.difference(num_between_wrong)
    final_check_after_b_good = set()
    final_check_after_b_wrong = set()
    for num in only_good_after_checking_a:
        for num_b in b:
            if num_b % num == 0:
                final_check_after_b_good.add(num)
            else:
                final_check_after_b_wrong.add(num)
    return len(final_check_after_b_good.difference(final_check_after_b_wrong))



getTotalX([3, 9, 6], [36, 72])
