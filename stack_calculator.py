def add(stacks,n1,n2):
    n2=stacks.pop()
    n1=stacks.pop()
    print(n1+n2)
def sub(stacks,n1,n2):
    n2=stacks.pop()
    n1=stacks.pop()
    print(n1-n2)
def mult(stacks,n1,n2):
    n2=stacks.pop()
    n1=stacks.pop()
    print(n1*n2)
def div(stacks,n1,n2):
    n2=stacks.pop()
    n1=stacks.pop()
    print(n1/n2)

stacks = []
n1 = ""
n2 = ""

while[True]:
    x=input("Please input number here ")
    if (x=="+"):
        add(stacks,n1,n2)
    elif (x=="-"):
        sub(stacks,n1,n2)
    elif (x=="*"):
        mult(stacks,n1,n2)
    elif (x=="/"):
        div(stacks,n1,n2)
    else:
        y=int(x)
        stacks.append(y)
        print(stacks)
