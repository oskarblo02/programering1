korv = (1, 3, 4, 5, 6, 7, 6, 2, 3)

def sum2(a, b):
    return a + b

def mean2(a, b):
    return (a + b)/2

def sumlist(korv):
    return sum(korv) 

def medellist(korv):
    return sum(korv) / len(korv)

def sum_my_list(my_list):
    result = 0
    for x in my_list:
        result = result + x
    return result

def create_greeting(name):
    return "hejsan " + name + "!, hur e läget?"


print(sum2(2, 3))
print(mean2(12, 27))
print(sumlist(korv))
print(medellist(korv))
print((sum_my_list(korv)))
print(create_greeting(input("vad heter du?")))