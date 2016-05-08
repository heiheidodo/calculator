#!/usr/bin/python
#Sheng Zhou

PF1 = "124*+3-22+3/2/3*"
PF2 = "65-4*54/7*+9-9-"
global tos
tos = -1
             
def push(stack, element):
    global tos
    tos += 1
    stack[tos] = element
    	
def pop(stack):
    global tos
    top = stack[tos]
    tos -= 1
    return top
	
def calculator(expression):
    global tos
    length = len(expression)
    stack = [' '] * length

    def add(a, b):
    	return a + b
    def sub(a, b):
    	return a - b
    def mult(a, b):
        return a * b
    def dnvnde(a, b):
        return a / b
	
    for n in expression:
        if n == "*":
            b = pop(stack)
            a = pop(stack)
            top = mult(float(b), float(a))
            push(stack, top)
        elif n == "/":
            b = pop(stack)
            a = pop(stack)
            top = dnvnde(float(a), float(b))
            push(stack, top)
        elif n == "+":
            b = pop(stack)
            a = pop(stack)
            top = add(float(b), float(a))
            push(stack, top)
        elif n == "-":
            b = pop(stack)
            a = pop(stack)
            top = sub(float(a), float(b))
            push(stack, top)
        
        else:
            push(stack, n)
    print(stack[0])
    tos = -1
    
calculator(PF1)
calculator(PF2)
calculator("64-1-2-3-4-")
