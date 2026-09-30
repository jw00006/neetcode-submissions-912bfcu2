from typing import List

def read_integers() -> List[int]:
    line = input()
    int_list = [int(x) for x in line.split(",")]
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
