def prod(num):
    product = 1
    for n in list(str(num)):
        product *= int(n)
    return product

def colorful(num):
    num = str(num)
    l = len(num)
    color = {}
    for i in range(0,l+1):
        for j in range(i+1,l+1):
            if (prod(num[i:j]) in color.keys()):
                return False
            else:
                color[prod(num[i:j])] = num[i:j]
    return True


print(colorful(123))