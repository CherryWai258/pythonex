a=int(input("Give me your number:"))
b=int(input("Give me your number:"))
c=input("Give me  your function(+,-,*,/):")

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)    
    if c=="+":
        add(a,b)
    elif c=="-":
        sub(a,b)
    elif c=="*":
        mul(a,b)
    elif c=="/":
        div(a,b)