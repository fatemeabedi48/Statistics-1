class SimpleQueue:  
    def __init__(self):  
        self.items = []  

    def enqueue(self, item):  
        self.items.append(item)  

    def dequeue(self):  
        return self.items.pop(0) if self.items else None  
    
    def size(self):  
        return len(self.items)  

def max_sum_of_consecutive_m(incomes, m):  
    window = SimpleQueue()  
    current_sum = 0  
    max_sum = float('-inf')  

    for income in incomes:  
        window.enqueue(income)  
        current_sum += income  

        if window.size() > m:  
            current_sum -= window.dequeue()   

        if window.size() == m:  
            max_sum = max(max_sum, current_sum)   

    return max_sum  

 
n, m = map(int, input("").split())  
incomes = list(map(int, input("").split()))  

 
result = max_sum_of_consecutive_m(incomes, m)  
print(result)