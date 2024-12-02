import art

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():
    print(art.logo)
    should_accumilate=True
    num1=float(input("what is the first number:"))
    while should_accumilate:
        for symbol in operations:
            print(symbol)
        operating_symbol=input("pick an operation :")
        num2=float(input("what is next number:"))
        answer=operations[operating_symbol](num1,num2)
        print(f"{num1}{operating_symbol}{num2}={answer}")
        choice=input(f"Type 'y' to continue calculating with {answer},or Type 'n' for new calculation").lower()
        if choice=='y':
            num1=answer
        else:
            should_accumilate=False
            print("\n"*20)
            calculator()

calculator()

