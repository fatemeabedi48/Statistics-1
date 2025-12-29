from prettytable import PrettyTable  
from collections import Counter 

data = []
n = int(input("Enter count of data:"))

for i in range(n):
    Blood_type = input("Enter your blood type: ")
    data.append(Blood_type)

 
frequency = Counter(data)  
 
table = PrettyTable()  
 
table.field_names= ["data" ,"f" ,"r","r*100" , "R"]

cumulative_frequency = 0

for item, count in frequency.items():  
    cumulative_frequency += count
    table.add_row([item, count , count/n , (count/n)*100 , cumulative_frequency])

 
print(table)