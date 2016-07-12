""""
Write a program that implements a mapper for Word Count tasks in Hadoop Streaming.

Sample Input:
Vivere est cogitare
Vivere militate est
Scientia potentia est

Sample Output:
Vivere	1
est	1
cogitare	1
Vivere	1
militate	1
est	1
Scientia	1
potentia	1
est	1
""""

import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print('{}\t{}'.format(word, 1))
        