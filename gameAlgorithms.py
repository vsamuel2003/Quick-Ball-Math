
def answerQuestion(question):
    evalList = evalQuestion(question,[])
    answer = float(evalList[-1].split()[-1])
    return answer

def findNextOperation(s):
    pemdas = ['^',('x','/',"%"),'+']
    for operation in pemdas:
        if isinstance(operation,tuple):
            for term in s:
                if term in operation:
                    return term
        else:
            if operation in s:
                return operation
    return None

def findNumbers(s,operation):
    firstBound = 0
    secondBound = s.index(operation)
    thirdBound = s.index(operation) + 1
    fourthBound = len(s)
    index1 = s.index(operation) - 1
    index2 = s.index(operation) + 1
    
    while index1 > 0:
        if s[index1].isdigit() == False and s[index1]!= "." and s[index1] != "-":
            firstBound = index1 + 1
            break
        index1 -= 1
            
    while index2 < len(s):
        if s[index2].isdigit() == False and s[index2]!= "." and s[index2] != "-":
            fourthBound = index2 
            break
        index2 += 1

    firstNum = float(s[firstBound:secondBound])
    secondNum = float(s[thirdBound:fourthBound])
    
    return (firstNum,secondNum)

def evalQuestion(s,evalList = []):
    if findNextOperation(s) == None:
        if s.count("abs") > 0:
            answer = float(s[4:-1])
            if answer < 0:
                answer *= -1
            evalList.append(f'= {answer:.1f}')
        return evalList
    
    elif s.count("min") > 0:
        questions = s[4:-1].split(',')
        
        tempMinList = []
        firstEvalList = evalQuestion(questions[0],[])
        tempMinList.append(f'{questions[0]} =')
        tempMinList.append(firstEvalList)
        
        secondEvalList = evalQuestion(questions[1],[])
        tempMinList.append(f'{questions[1]} =')
        tempMinList.append(secondEvalList)
        
        firstAnswer = answerQuestion(questions[0])
        secondAnswer = answerQuestion(questions[1])
        if secondAnswer < firstAnswer:
            tempMinList.append(f'min({firstAnswer},{secondAnswer}) = {secondAnswer:.1f}')
        else:
            tempMinList.append(f'min({firstAnswer},{secondAnswer}) = {firstAnswer:.1f}')
        
        minList = []
        for step in tempMinList:
            if isinstance(step,list):
                for i in step:
                    minList.append(i)
            else:
                minList.append(step)
            
        return minList
    
    elif s.count("max") > 0:
        questions = s[4:-1].split(',')
        
        tempMaxList = []
        firstEvalList = evalQuestion(questions[0],[])
        tempMaxList.append(f'{questions[0]} =')
        tempMaxList.append(firstEvalList)
        
        secondEvalList = evalQuestion(questions[1],[])
        tempMaxList.append(f'{questions[1]} =')
        tempMaxList.append(secondEvalList)
        
        firstAnswer = answerQuestion(questions[0])
        secondAnswer = answerQuestion(questions[1])
        if secondAnswer > firstAnswer:
            tempMaxList.append(f'max({firstAnswer},{secondAnswer}) = {secondAnswer:.1f}')
        else:
            tempMaxList.append(f'max({firstAnswer},{secondAnswer}) = {firstAnswer:.1f}')
        
        maxList = []
        for step in tempMaxList:
            if isinstance(step,list):
                for i in step:
                    maxList.append(i)
            else:
                maxList.append(step)
            
        return maxList
                           
    else:
        operation = findNextOperation(s)
        firstNum,secondNum = findNumbers(s,operation)
        
        if operation == "^":
            answer = firstNum ** secondNum
            s = s.replace(str(firstNum)+operation+str(secondNum),str(answer))
            evalList.append(f'= {s}')
            return evalQuestion(s,evalList)
        
        elif operation == "x":
            answer = firstNum * secondNum
            s = s.replace(str(firstNum)+operation+str(secondNum),str(answer))
            evalList.append(f'= {s}')
            return evalQuestion(s,evalList)
        
        elif operation == "/":
            answer = firstNum / secondNum
            s = s.replace(str(firstNum)+operation+str(secondNum),str(answer))
            evalList.append(f'= {s}')
            return evalQuestion(s,evalList)
        
        elif operation == "%":
            answer = firstNum % secondNum
            s = s.replace(str(firstNum)+operation+str(secondNum),str(answer))
            evalList.append(f'= {s}')
            return evalQuestion(s,evalList)
        
        elif operation == "+":
            answer = firstNum + secondNum
            s = s.replace(str(firstNum)+operation+str(secondNum),str(answer))
            evalList.append(f'= {s}')
            return evalQuestion(s,evalList)
        

#taken from the 15-112 Notes
def almostEqual(d1, d2, epsilon=10**-7): 
    return (abs(d2 - d1) < epsilon)
        
def evalQuestionString(s):
    evalList = evalQuestion(s,[])
    r = ""
    for step in evalList:
        r += step + "\n"
    return r

def timeMultiplier(question):
    termCounter = []
    pemdas = ['^','x','/',"%",'+']
    for i in pemdas:
        termCounter.append(question.count(i))
    
    timeMultiplier = ((termCounter[0] * 1.7) + (termCounter[1]) + 
                        (termCounter[2]) + (termCounter[3]) + 
                        (termCounter[4] * 0.7))
    return timeMultiplier



