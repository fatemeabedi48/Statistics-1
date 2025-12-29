from _typeshed import Self


class SimpleComputer:  
    def __init__(self):  
        self.memory = [0] * 100  # حافظه ۱۰۰ خانه‌ای  
        self.accumulator = 0  # رجیستر انباشت  
        self.pc = 0  # شمارنده برنامه (Program Counter)  
        self.running = True  # وضعیت برنامه  

    def execute_instruction(self, instruction):  
        parts = instruction.split()  
        command = parts[0].upper()  

        if command == 'AND':  
            self.accumulator &= self.memory[int(parts[1])]  
        elif command == 'ADD':  
            self.accumulator += self.memory[int(parts[1])]  
        elif command == 'LDA':  
            self.accumulator = self.memory[int(parts[1])]  
        elif command == 'STA':  
            self.memory[int(parts[1])] = self.accumulator  
        elif command == 'BUN':  
            self.pc = int(parts[1]) - 1  # -1 برای جبران افزایش بعدی  
        elif command == 'BSA':  
            self.memory[self.pc + 1] = self.pc  
            self.pc = int(parts[1]) - 1  # -1 برای جبران  
        elif command == 'ISZ':  
            self.memory[int(parts[1])] += 1  
            if self.memory[int(parts[1])] == 0:  
                self.pc += 1  # پرش در صورت صفر شدن  
        elif command == 'CLA':  
            self.accumulator = 0  
        elif command == 'HLT':  
            self.running = False  # متوقف کردن برنامه  
        else:  
            print(f'Unknown instruction: {instruction}')  

        self.pc += 1  # افزایش شمارنده برنامه  

    def load_memory(self):  
        while True:  
            try:  
                n = int(input("تعداد خانه‌های حافظه‌ای که می‌خواهید پر کنید (حداکثر 100): "))  
                if 1 <= n <= 100:  
                    break  
                else:  
                    print("لطفاً عددی بین 1 تا 100 وارد کنید.")  
            except ValueError:  
                print("لطفاً یک عدد صحیح وارد کنید.")  
        
        print("مقادیر را برای خانه‌های حافظه وارد کنید.")  
        for i in range(n):  
            while True:  
                try:  
                    value = int(input(f'آدرس {i}: '))  
                    if 0 <= value <= 999:  # محدوده‌ی معتبر  
                        self.memory[i] = value  
                        break  
                    else:  
                        print("لطفاً عددی معتبر بین 0 تا 999 وارد کنید.")  
                except ValueError:  
                    print("لطفاً یک عدد صحیح وارد کنید.")  

    def load_program(self):  
        print("دستورات برنامه را وارد کنید. (برای پایان وارد کردن 'HLT' کنید)")  
        while True:  
            instruction = input("دستور: ")  
            if instruction.upper() == 'HLT':  
                self.memory[self.pc] = 'HLT'  # ذخیره دستور توقف در حافظه  
                break  
            elif instruction.upper() == 'FILL':  
                self.pc += 1  # با دستور FILL به مرحله بعد بروید  
                break  
            self.memory[self.pc] = instruction  
            self.pc += 1  
        self.pc = 0  # بازنشانی شمارنده برنامه به ابتدای برنامه  

    def run(self):  
        while self.running and self.pc < len(self.memory):  
            instruction = self.memory[self.pc]  
            if instruction != 0:  # فقط دستورات غیر صفر اجرا شوند  
                self.execute_instruction(instruction)  

# ایجاد یک شیء از کامپیوتر ساده  
computer = SimpleComputer()  

# وارد کردن مقادیر حافظه  
computer.load_memory()  

# وارد کردن برنامه  
computer.load_program()  

# اجرای برنامه  
computer.run()  

# نمایش نتایج  
print("Memory:", computer.memory)  
print("Accumulator:", computer.accumulator)  
print("Program Counter:", Self.pc)