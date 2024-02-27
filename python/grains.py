def square(number):
    if isNumberAcceptable(number):
        tot = 1
        if number == 1:
            tot = 1
        else:
            for i in range (1,number):
                tot *= 2
        return tot
        


def total():
    tot = 0
    for i in range (1,65):
        tot += square(i)
    return tot

def isNumberAcceptable(number):
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    else:
        return True