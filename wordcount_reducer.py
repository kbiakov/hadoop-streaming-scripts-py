""""
Write a program that implements the reducer for Word Count tasks in Hadoop Streaming.

Sample Input:
cogitare	1
est	1
est	1
est	1
militate	1
potentia	1
Scientia	1
Vivere	1
Vivere	1

Sample Output:
cogitare	1
est	3
militate	1
potentia	1
Scientia	1
Vivere	2
""""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
        
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}'.format(current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print('{}\t{}'.format(current_word, current_count))
