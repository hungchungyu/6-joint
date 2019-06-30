def add(a,b,c):
    d = a+b+c
    print(d)

def number(one, two, three):
    add(one,two,three)
    return {"NO1":one, "NO2":two, "NO3":three}

print(number(1,2,3))