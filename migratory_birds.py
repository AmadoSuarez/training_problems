#!/bin/python3

import sys
from collections import Counter
def migratoryBirds(n, ar):
    # Complete this function
    count = Counter(ar)
    return count.most_common(1)[0][0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
