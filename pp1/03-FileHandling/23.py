import re
with open('03-FileHandling/land.txt') as file:
    temp = re.findall('\d', file.read())
temp = [int(i) for i in temp]
print(sum(temp))
