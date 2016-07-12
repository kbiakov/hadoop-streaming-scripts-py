""""
Implement Combiner problem in calculating the average time spent by a user on the page.

Mapper writes data in the form of key / value, where key - page address, value - a pair of numbers separated by ";". The first - the number of seconds spent by the user on this page, is equal to 1 second.

Sample Input:
www.facebook.com	100;1
www.google.com	10;1
www.google.com	5;1
www.google.com	15;1
stepic.org	60;1
stepic.org	100;1

Sample Output:
www.facebook.com	100;1
www.google.com	30;3
stepic.org	160;2
""""

from operator import itemgetter
import sys

current_host = None
current_count = 1
current_time = 0
host = None

for line in sys.stdin:
    words = line.strip().split()
    host = words[0]
    words = words[1].split(';')
    time = int(words[0])
        
    if current_host == host:
        current_time += time
        current_count += 1
    else:
        if current_host:
            print('{}\t{}'.format(current_host, "{};{}".format(current_time, current_count)))
        current_time = time
        current_host = host
        current_count = 1

if current_host == host:
    print('{}\t{}'.format(current_host, "{};{}".format(current_time, current_count)))
