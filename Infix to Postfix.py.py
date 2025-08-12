OPERATORS=set(['+','-','*','/','(',')','^'])
PRIORITY={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
    stack=[]
    output=' '
    for ch in expression:
        if ch not in OPERATORS:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='('  and PRIORITY [ch]<=PRIORITY[stack[-1]]:
                    output+=stack.pop()
            stack.append(ch)
    while stack:
            output+=stack.pop()
    return output
expression=input("Enter Infix Expression:")
print("Infix Expression:",expression)
print("Postfix Expression:",infix_to_postfix(expression))
            
                
