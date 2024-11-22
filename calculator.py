def add(n1,n2):
    return n1 + n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def subtract(n1,n2):
    return n1 - n2


operations ={
    "*": multiply,
    "/":divide,
    "+":add,
    "-":subtract
}
result=0
is_continue="n"

def calculation(first_num):
    global is_continue
    global result
    for operation in operations:
        print(operation)
    operator=input("Enter what operation do you want:")
    second_num=float(input("Enter your second number:"))
    result=operations[operator](first_num,second_num)
    print(f"{first_num} {operator} {second_num} = {result}")
    return input(f"Type 'y' to continue calculating with {result},type 'n' to start new calculation or type 'e' to end your operation:")


while True:
    if is_continue=="n":
        first_num=float(input("Enter your first number:"))
        is_continue=calculation(first_num)
    elif is_continue=="y":
        first_num=result
        is_continue=calculation(first_num) 
    elif is_continue=="e":
        print("Goodbye.")
        break       




       
            

           


