# List Sort in Python

# Using sort method
l1 = [5, 10, 15, 1]
l1.sort()
print(l1)

l2 = [1, 5, 3, 10]
l2.sort(reverse=True)
print(l2)

l3 = ['gfg', 'ide', 'courses']
l3.sort()
print(l3)

def myFun(s):
    return len(s)


l = ['gfg', 'courses', 'python']
l.sort(key=myFun)
print(l)

l.sort(key=myFun, reverse=True)
print(l)

#  The below example sorts the list in increasing order based on the first value of pair.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def myFun(p):
    return p.x

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)
    
# Another
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x


l = [Point(1, 15), Point(10, 5), Point(5, 8)]
l.sort()

for i in l:
    print(i.x, i.y)
    
# Below code sort the list based on first value of pair and if first values are same in some pairs then it will sort them based on second value of pair.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):

        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x


l = [Point(1, 15), Point(10, 5), Point(1, 8)]
l.sort()

for i in l:
    print(i.x, i.y)