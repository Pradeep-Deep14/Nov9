number = 8
def adder(integer):
    print(number)
    number=10
    print(number + integer)
adder(5)

#unbound Local Error

number = 8
def adder(integer):
    print(number)
    print(number + integer)
adder(5)

#8 13