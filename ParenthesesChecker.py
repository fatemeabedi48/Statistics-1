class Stack:  
    def __init__(self):  
        self.items = []  
    def push(self, item):  
        self.items.append(item)  

    def pop(self):  
        if not self.is_empty(): 
            return self.items.pop() 
        raise IndexError("pop from an empty stack") 

    def is_empty(self):  
        return len(self.items) == 0 

    def size(self):  
        return len(self.items)  

def is_matching_pair(open_char, close_char):  
    return (open_char == '(' and close_char == ')') or \
           (open_char == '{' and close_char == '}') or \
           (open_char == '[' and close_char == ']')  


def ParenthesesChecker(s):  
    stack = Stack()  
    for char in s: 
        if char in '({[':   
            stack.push(char)  
        elif char in ')}]':  
            if stack.is_empty(): 
                return False   
            top = stack.pop()  
            
            if not is_matching_pair(top, char): 
                return False    
    return stack.is_empty() 
 
input_string = input("")  

 
if ParenthesesChecker(input_string):  
    print("true")   
else:  
    print("false")  