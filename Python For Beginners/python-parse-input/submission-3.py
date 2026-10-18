from typing import List

def read_integers() -> List[int]:
    num = input()
    str_ng = num.split(",")

    intf = []
    for i in str_ng:
        intf.append(int(i))
    return intf


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
