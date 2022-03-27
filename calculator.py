class Calculator:
    def __init__(self):
        self.input1 = int(input("Enter 1st number(integer):"))  #User input
        self.input2 = int(input("Enter 2nd number(integer):"))
    
    def adder(self):
        return self.input1 + self.input2    #Addition of input1 and input2
    
    def subtractor(self):
        return self.input1 - self.input2    #Subtraction of input1 and input2
    
    def multiplier(self):
        return self.input1 * self.input2    #Muliplication of input1 and input2
    
    def divider(self):
        return self.input1/self.input2      #Division of input1 and input2
    
    def clear(self):
        self.input1 = self.input2 = 0       #Set input1 and input2 to 0
        print("1st input after clear:", self.input1, "\n2nd input after clear:", self.input2)
    
calculation = Calculator()
print("Addition:", calculation.adder())
print("Subtraction:", calculation.subtractor())
print("Multiply:", calculation.multiplier())
print("Divide:", calculation.divider())
calculation.clear()
