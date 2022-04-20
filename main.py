

class Bmi:
    def __init__(self,mass,height,bmi):
        self.wht = mass
        self.ht = height
        self.bmi = bmi

    
    @property
    def finding_bmi(self):
        self.bmi = self.wht/(self.ht ** 2)
        self.bmi = round(self.bmi , 1) 
        return self.bmi


mass = float(input("Enter your weight : "))
height = float(input("Enter your height : "))
calc_bmi = Bmi(mass,height,0)

BMI = calc_bmi.finding_bmi

# print(type((calc_bmi.finding_bmi)))
class Detecting:
    
    def detec():
        if BMI < 18.5:
            return "You are Under Weight"
        elif BMI < 25:
            return "You have a normal weight"
        elif BMI < 30:
            return "You are Over Weight"
        else:
            return "You are Obese"


res = Detecting
print(res.detec())