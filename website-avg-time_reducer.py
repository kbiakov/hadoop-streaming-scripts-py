""""
Implement reducer in the problem of calculating the average time spent by a user on the page.

Mapper reducer transmits data in the form of key / value, where key - page address, value - the number of seconds spent by the user on this page.

The average time to bring the output to an integer.

Sample Input:
www.facebook.com	100
www.google.com	10
www.google.com	5
www.google.com	15
www.stepic.org	60
www.stepic.org	100

Sample Output:
www.facebook.com	100
www.google.com	10
www.stepic.org	80
""""

from operator import itemgetter
import sys

current_host = None
current_count = 1
current_time = 0
host = None

for line in sys.stdin:
    line = line.strip()
    host, time = line.split('\t', 1)
    time = int(time)
        
    if current_host == host:
        current_time += time
        current_count += 1
    else:
        if current_host:
            print('{}\t{}'.format(current_host, int(current_time/current_count)))
        current_time = time
        current_host = host
        current_count = 1

if current_host == host:
    print('{}\t{}'.format(current_host, int(current_time/current_count)))
