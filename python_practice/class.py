class Caculator:
    name = '3310'
    price = 'very expensive'
    def add(a,b):
        c = a+b
        print("Ans",c)
    def minus(a,b):
        c = a-b
        print("Ans",c)
    def multiple(a,b):
        c = a*b
        print("Ans",c)
    def divide(a,b):
        c = a/b
        print("Ans",c)

print("Name",Caculator.name)
print("Price",Caculator.price)

Caculator.add(1,2)
Caculator.minus(3,4)
Caculator.multiple(5,6)
Caculator.divide(7,8)

