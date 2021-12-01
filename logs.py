import random
from gameAlgorithms import *
class Logs(object):
    #consider functions to only be called by constructor
    def __init__(self,cx,cy,resident):
        self.cx = cx
        self.cy = cy
        self.isResident = resident
        self.problemDeterminer = random.randint(1,5)
        self.powerUpDeterminer = random.randint(1,10)
        self.numTerms = random.randint(2,3)
        self.operations = ['^','x','/',"%",'+']
        self.terms = []
        self.pause = False
        self.eval = False
        self.powerUp = False

        if self.powerUpDeterminer == 2:
            self.powerUp = True

    
        if self.problemDeterminer == 3:
            for term in range(self.numTerms):
                randNum = float(random.randint(-10,10))
                while randNum == 0:
                    randNum = float(random.randint(-10,10))
                self.terms.append(randNum)
            self.question = "abs("
            for i in range(len(self.terms)-1):
                upperBound = len(self.operations)-1
                operation = self.operations[random.randint(0,upperBound)]
                if (operation == "^" and self.terms[i] > 3.0
                     or self.terms[i+1] > 3.0):
                     while operation == "^":
                         operation=self.operations[random.randint(0,upperBound)]
                self.question += str(self.terms[i]) + operation
            self.question += str(self.terms[-1])
            self.question += ")"
        
        elif self.problemDeterminer == 4:
            for term in range(4):
                randNum = float(random.randint(-10,10))
                while randNum == 0:
                    randNum = float(random.randint(-10,10))
                self.terms.append(randNum)
            self.question = "min("

            upperBound = 1
            operation = self.operations[random.randint(0,upperBound)]
            if (operation == "^" and self.terms[0] > 3.0
                    or self.terms[1] > 3.0):
                    while operation == "^":
                        operation=self.operations[random.randint(0,upperBound)]
            self.question += str(self.terms[0]) + operation
            self.question += str(self.terms[1])
            self.question += ','
            operation = self.operations[random.randint(0,upperBound)]
            if (operation == "^" and self.terms[2] > 3.0
                    or self.terms[3] > 3.0):
                    while operation == "^":
                        operation=self.operations[random.randint(0,upperBound)]
            self.question += str(self.terms[2]) + operation
            self.question += str(self.terms[3])

            self.question += ")"
        
        elif self.problemDeterminer == 5:
            for term in range(4):
                randNum = float(random.randint(-10,10))
                while randNum == 0:
                    randNum = float(random.randint(-10,10))
                self.terms.append(randNum)
            self.question = "max("
            upperBound = 1
            operation = self.operations[random.randint(0,upperBound)]
            if (operation == "^" and self.terms[0] > 3.0
                    or self.terms[1] > 3.0):
                    while operation == "^":
                        operation=self.operations[random.randint(0,upperBound)]
            self.question += str(self.terms[0]) + operation
            self.question += str(self.terms[1])
            self.question += ','
            operation = self.operations[random.randint(0,upperBound)]
            if (operation == "^" and self.terms[2] > 3.0
                    or self.terms[3] > 3.0):
                    while operation == "^":
                        operation=self.operations[random.randint(0,upperBound)]
            self.question += str(self.terms[2]) + operation
            self.question += str(self.terms[3])

            self.question += ")"


        else:
            for term in range(self.numTerms):
                randNum = float(random.randint(-10,10))
                while randNum == 0:
                    randNum = float(random.randint(-10,10))
                self.terms.append(randNum)

            self.question = ""
            for i in range(len(self.terms)-1):
                upperBound = len(self.operations)-1
                operation = self.operations[random.randint(0,upperBound)]
                if (operation == "^" and self.terms[i] > 3.0 
                     or self.terms[i] < -3.0 or self.terms[i+1] > 3.0 
                     or self.terms[i+1] < -3.0):
                     while operation == "^":
                         operation=self.operations[random.randint(0,upperBound)]
                self.question += str(self.terms[i]) + operation
            self.question += str(self.terms[-1])
    
    def isPowerUp(self):
        return self.powerUp
    
    def changePosition(self,x,y):
        self.cx += x
        self.cy += y
    
    def getQuestion(self):
        return self.question
    
    def getPosition(self):
        return (self.cx,self.cy)

    def changeResidencyStatus(self):
        if self.isResident:
            self.isResident = False
        else:
            self.isResident = True

    def getResidenceStatus(self):
        return self.isResident
    
    def changePause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True
    
    def paused(self):
        return self.pause
    
    def getTimeChange(self):
        question = self.question
        self.timeChange = timeMultiplier(question)
        return 15/self.timeChange
    

    def __eq__(self,other):
        return (isinstance(other,Logs) and self.cx == other.cx 
                and self.cy == other.cy)
