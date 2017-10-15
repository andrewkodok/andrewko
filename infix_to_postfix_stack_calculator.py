math_exp = open ("mathexp.txt" , "r")
read_file = math_exp.read()
InFix = read_file.split()

post_fix = []
operators = []

def add(stacks,n1,n2):
    return(n1+n2)
def sub(stacks,n1,n2):
    return(n1-n2)
def mult(stacks,n1,n2):
    return(n1*n2)
def div(stacks,n1,n2):
    return(n1/n2)

def calculator(x):
    stacks = []
    for i in range (0,len(x)):
        try:
            y=int(x[i])
            stacks.append(y)
            print(stacks)
        except:
            length_stacks=len(stacks)
            if (length_stacks>=2):
                if (x[i]=="+"):
                    n2=stacks.pop()
                    n1=stacks.pop()
                    stacks.append(add(stacks,n1,n2))
                elif (x[i]=="-"):
                    n2=stacks.pop()
                    n1=stacks.pop()
                    stacks.append(sub(stacks,n1,n2))
                elif (x[i]=="*"):
                    n2=stacks.pop()
                    n1=stacks.pop()
                    stacks.append(mult(stacks,n1,n2))

                elif (x[i]=="/"):
                    n2=stacks.pop()
                    n1=stacks.pop()
                    stacks.append(div(stacks,n1,n2))
    return stacks
def check(x):
    if x == "+" or x=="-" or x=="*" or x=="/":
        return "operator"
    elif x == "(":
        return "left_paranthesis"
    elif x == ")":
        return "right_paranthesis"
    else:
        return "operand"

def value(x):
    if x == "+" or x=="-":
        return 2
    elif x == "*" or x=="/":
        return 3
    elif x == "(":
        return 1

def main():
    for a in range (0,len(InFix)):
        type = check(InFix[a])
        if type == "operand":
            post_fix.append(InFix[a])
        elif type == "operator":
            try:
                while value(InFix[a]) <= value(operators[len(operators)-1]):
                    operator_append=operators.pop()
                    post_fix.append(operator_append)
                operators.append(InFix[a])
            except:
                operators.append(InFix[a])
        elif type == "left_paranthesis":
            operators.append(InFix[a])
        elif type == "right_paranthesis":
            while check(operators[len(operators)-1]) != "left_paranthesis":
                operator_pop=operators.pop()
                post_fix.append(operator_pop)
            operators.pop()
    while len(operators)!=0:
        last_operators=operators.pop()
        post_fix.append(last_operators)
main()
print(calculator(post_fix))
