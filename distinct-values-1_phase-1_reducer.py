""""
Implement a reducer of the phase 1 problem Distinct Values v1.

Reducer receives input data by mapper from the previous step.

Sample Input:
1,a	1
1,b	1
1,b	1
2,a	1
2,d	1
2,e	1
3,a	1
3,b	1

Sample Output:
1,a
1,b
2,a
2,d
2,e
3,a
3,b
""""

import sys

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

mylist = []
    
for line in sys.stdin:
    mylist.append(line.split()[0])
    
for pair in enumerate(uniq(mylist)):
    print(pair[1])
    