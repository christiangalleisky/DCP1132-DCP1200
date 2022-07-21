def test():
    str_list = ['B', 'l', 'a', 'k', 'e']
    for i in range (len(str_list)):
        print(str(i))

def rotate(iters, lst):

    i = 0
    
    while(i < iters):
        x = lst.pop()
        lst.insert(0, x)
        i += 1

    return lst

lst = [1,2,3,4,5,6]
print(rotate(3, lst))
