print('Calculator version 1.0');
print('Enter a simple formula');
class Calculator():
    def __init__ (self, str):  
            self.formula = self.Parse(str)           
    def Parse(self,str):
        l = len(str)
        result = []
        i = 0
        while i<l:
            number = ''
            a = str[i]
            while '0' <= a <= '9':
                number += a  
                i += 1
                if i < l:
                    a = str[i]  
                else:                   
                    break    
            if number != '':
                result.append(number)
            if i < l:
                result.append(a)        
            i += 1    
        return result
    def Mult_Del(self):  
        i = 0  
        while i < len(self.formula):  
            res = 0                       
            if self.formula[i] == "*":                                   
                res = float(self.formula[i-1])*float(self.formula[i+1])
                self.formula.pop(i+1)
                self.formula.pop(i)
                self.formula.pop(i-1)
                self.formula.insert(i-1, res)  
                i= i -2  
            if self.formula[i] == "/":
                if float(self.formula[i+1]) != 0:  
                    # print(type(self.formula[i+1]))                  
                    res = float(self.formula[i-1])/float(self.formula[i+1])
                    self.formula.pop(i+1)
                    self.formula.pop(i)
                    self.formula.pop(i-1)
                    self.formula.insert(i-1, res)  
                    i= i -2  
                else:
                    print("division by zero")        
            i += 1
    def Addition_Substraction(self):  
        i = 0  
        while i < len(self.formula):  
            res = 0                       
            if self.formula[i] == "+":                                   
                res = float(self.formula[i-1])+float(self.formula[i+1])
                self.formula.pop(i+1)
                self.formula.pop(i)
                self.formula.pop(i-1)
                self.formula.insert(i-1, res)  
                i= i -2  
            if self.formula[i] == "-":
                if float(self.formula[i+1]) != 0:  
                    # print(type(self.formula[i+1]))                  
                    res = float(self.formula[i-1])-float(self.formula[i+1])
                    self.formula.pop(i+1)
                    self.formula.pop(i)
                    self.formula.pop(i-1)
                    self.formula.insert(i-1, res)  
                    i= i -2  
            i += 1
    def Calculate(self):
        self.Mult_Del()
        self.Addition_Substraction()
        
a = input();
Formula = Calculator(a);
print(Formula.formula);
Formula.Calculate();
print(Formula.formula);

Formula2 = Calculator("12+3-54/2+33*2");
print(Formula2.formula);
Formula2.Calculate();
print(Formula2.formula)
print("ôûâ")