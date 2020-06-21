def avoidObstacles(inputArray):
    i = 3
    while True:
        count = 0
        for j in inputArray:
            if j % i != 0:
                count += 1
        if count == len(inputArray):
            return i
        i += 1

#================================================#
#     ^ my answer      ||  most voted answer v   #
#================================================#

def avoidObstacles(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1