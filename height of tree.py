
from prettytable import PrettyTable
import math

def main():

    data = []

    n = int(input("Enter count of tree: "))
    data = input().split()
    for i in range(n):
        data[i]=float(data[i])
        

    maximum = max(data)
    minimum = min(data)
    k = int(1 + 3.22*math.log(n))
    d = (maximum - minimum)/k

    #محاسبه میانگین
    summation = sum(data)
    avarage = summation/n
    print(avarage)

    #رسم جدول
    table = PrettyTable()
    table.field_names= ["data" ,"f" ,"r","r*100" , "R"]

    #تعریف فروانی برای محاسبه فراوانی تجمعی
    frequency = []  
    cumulative_frequency = 0  

    # تعریف کران بالا و کران پایین برای بازه ها
    for i in range(k):  
        lower_bound = minimum + i * d  
        upper_bound = lower_bound + d  if i < k-1 else maximum
    

        f = sum(1 for height in data if lower_bound <= height <= upper_bound)  
        frequency.append(f)  
 
        r = f / n  
        cumulative_frequency += f  
     
        table.add_row([f"{lower_bound:.1f} - {upper_bound:.1f}", f, r, r * 100, cumulative_frequency])  

    print(table)

if __name__ == "__main__":  
    main()  