class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None  

class LinkedList:  
    def __init__(self):  
        self.head = None  

    def append(self, data):  
        new_node = Node(data)  
        if not self.head:  
            self.head = new_node  
            return  
        last = self.head  
        while last.next:  
            last = last.next  
        last.next = new_node  

    def remove_middle(self):  
        if not self.head:  
            return None  
        
        slow = self.head  
        fast = self.head  
        prev = None  
        
        while fast and fast.next:  
            prev = slow  
            slow = slow.next  
            fast = fast.next.next  
        
        if prev:  
            prev.next = slow.next  
        
        return slow.data if slow else None  

    def display(self):  
        current = self.head  
        elements = []  
        while current:  
            elements.append(str(current.data))  
            current = current.next  
        return ' '.join(elements)   

if __name__ == "__main__":  
    linked_list = LinkedList()  
    
    numbers_input = input("")  
    numbers = map(int, numbers_input.split())  
    
    for number in numbers:  
        linked_list.append(number)  

    middle_value = linked_list.remove_middle()  

    print(linked_list.display())  
    
   