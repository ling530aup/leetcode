from typing import List
from collections import Counter

'''
待解决

'''
def leastInterval(tasks: List[str], n: int) -> int:
    ls = []
    count = Counter(tasks)
    for task_name in Counter(tasks):
        ls.append([count[task_name], task_name, 0])

    print(ls)

    while ls:
        ls = sorted(ls, key=lambda x: x[0])
        flag = True
        print(ls)
        for j in range(len(ls)):

            if ls[j][2] == 0:
                ls[j][0] -= 1
                ls[j][2] = n
                flag = False
                print(f'-> {ls[j][1]}')

                if ls[j][0] == 0:
                    ls.remove(ls[j])
                break
        if flag:
            print("Wait")
        for item in ls[1:]:
            if item[2] != 0:
                item[2] -= 1


if __name__ == '__main__':
    leastInterval(["A", "A", "A", "B", "B", "B"], 2)
