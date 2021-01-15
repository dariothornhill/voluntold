import random
import math

students = ["a", "b", "c", "f", "d"]


def pick(n, names):
    arr = names.copy()
    choices = []
    for i in range(n):
        choice = random.randint(0, len(arr) - 1)
        choices.append(arr.pop(choice))
    return choices

# TODO implement better grouping algorithm
def n_groups(n, arr):
    groups = []
    size_min = math.floor(len(arr) / n)
    size_max = math.ceil(len(arr) / n)
    pool = arr.copy()
    while pool:
        size = size_max if ((n - len(groups))  > size_max) else size_min
        print(len(groups))
        chosen = pick(size, pool)
        groups.append(chosen)
        pool = [x for x in pool if x not in chosen]
    return groups


def groups_of(size, arr):
    groups = []
    temp_size = size
    pool = arr.copy()
    while pool:
        temp_size = len(pool) if len(pool) < size else size
        chosen = pick(temp_size, pool)
        groups.append(chosen)
        pool = [x for x in pool if x not in chosen]
    return groups


if __name__ == "__main__":
    print(pick(2, students))
    print(n_group(4, students))
    print(groups_of(4, students))
