__author__ = 'kintien'
'''
print ('hello') x5
'''


#or

for x in range (0,5):
    print('hello')

print(list(range(0,65)))


for x in range(0,5):
    print('hello %s' % x)


wizardslist = ['spider eyes', 'goat teeth', 'smelly breath', 'cat skin', 'dog feet']
for v in wizardslist:
    print(v)
hugeharrypants = ['huge','harry', 'pants']
for d in hugeharrypants:
    print(d)
    print(d)

    for j in hugeharrypants:
        print(j)

foundcoins = 20
magiccoins = 70
stolencoins = 3
coins = foundcoins
for week in range(1,53):
    coins = coins + magiccoins + stolencoins
    print('Week %s = %s' %(week,coins))
'''
step = 0
while step <1000:
    if tired ==True:
        break
    elif badweather ==True:
        break
    else:
        step = step + 1
'''

x= 45
y=80
while x <50 and y <100:
    x= x +1
    y= y+1
    print(x,y)