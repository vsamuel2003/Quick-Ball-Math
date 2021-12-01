from cmu_112_graphics import *
from gameAlgorithms import *
import random
from logs import Logs


def appStarted(app):
    app.score = 0
    app.margin = max(app.height,app.width)//10
    app.logWidth = app.width//7
    app.logHeight = app.height//20
    app.logs = []
    app.innerMargin = app.margin//10
    app.r = 10
    app.cx = app.width/2
    app.cy = app.height - app.innerMargin - app.logHeight - app.r
    app.timerDelay = 200
    app.timerCounter = 0
    app.gameStarted = False
    app.userAnswer = ""
    app.gameOver = False
    app.gamePaused = False
    app.pausedLog = None
    app.clicked = False
    app.evalDisplayed = False
    app.residentLog = None
    app.scroller = 0
    app.centerLine = (app.height + app.margin)/2
    app.jumpLog = None
    app.powerJump = False
    app.type = ""
    app.afterClicked = False

def changeAllLogPositions(app,change):
    for log in app.logs:
        log.changePosition(0,-1 * change)

def keyPressed(app,event):
    possibleInputs = ['0','1','2','3','4','5','6','7','8','9']

    if event.key == "i":
        import mainMenu
        mainMenu.runMenu()   

    if event.key == "Enter":
        for log in app.logs:
            expected = answerQuestion(log.getQuestion())
            given = float(app.userAnswer)
            if almostEqual(expected,given):
                app.gameStarted = True
                logPosition = log.getPosition()
                app.cx = logPosition[0] + app.logWidth/2
                app.cy = app.centerLine - app.r
                app.scroller = logPosition[1] - app.centerLine
                changeAllLogPositions(app,app.scroller)
                log.changeResidencyStatus()
                app.residentLog = log
                app.score += 1
                
                #the general idea and set up of side scroller was from the 
                #CMU 112 class notes
                if log.isPowerUp():
                    newHeight = -0.5 * app.height
                    newLog = Logs(logPosition[0],newHeight,False)
                    app.logs.append(newLog)
                    app.jumpLog = newLog
                    app.scroller = newLog.getPosition()[1] - app.centerLine
                    app.powerJump = True
                    app.score += 10
        app.userAnswer = ""
        app.type = ""

    elif event.key in possibleInputs or event.key == "." or event.key == "-":
        app.userAnswer += event.key
        app.type += event.key
    
    if event.key == "r":
        appStarted(app)

def mousePressed(app,event):
    if app.gameOver:
        for log in app.logs:
            if (log.getPosition()[0] <= event.x <= log.getPosition()[0] + 
                app.logWidth and log.getPosition()[1]<=event.y<=log.getPosition()[1] 
                + app.logHeight):

                app.afterClicked = True
                if log.paused():
                    app.gamePaused = False
                    app.clicked = False
                    log.changePause()
                else:
                    app.gamePaused = True
                    log.changePause()
                    app.pausedLog = log
                    app.clicked = True


def timerFired(app):
    if app.gameOver == False and app.gamePaused == False:
        app.timerCounter += app.timerDelay
        if app.powerJump == False:

            if app.timerCounter % 1000 == 0:
                startingX = random.randrange(app.innerMargin,app.width-app.logWidth)
                app.logs.append(Logs(startingX,-1 * app.height,False))
            for log in app.logs:
                logAttributes = log.getPosition()
                distChange = log.getTimeChange()
                log.changePosition(0, distChange)
                if logAttributes[1] + app.logHeight >= (app.height-app.innerMargin):
                    app.logs.remove(log)
            
            if app.gameStarted:
                app.cy += app.residentLog.getTimeChange()
                if app.cy >= app.height - app.innerMargin:
                    app.gameOver = True
        else:
            jumpAmount = app.scroller/30
            for log in app.logs:
                logAttributes = log.getPosition()
                log.changePosition(0,-1 * jumpAmount)
                if logAttributes[1] + app.logHeight >= (app.height-app.innerMargin):
                    app.logs.remove(log)
            if almostEqual(app.jumpLog.getPosition()[1], app.centerLine):
                app.jumpLog.changeResidencyStatus()
                app.residentLog = app.jumpLog
                app.powerJump = False


def drawCircle(app,canvas):
    canvas.create_oval(app.cx-app.r,
                        app.cy-app.r,
                        app.cx+app.r,
                        app.cy+app.r,
                        fill = "white")

def drawBoard(app,canvas):
    canvas.create_rectangle(0,
                            app.margin,
                            app.width,
                            app.height,
                            fill="black")

    canvas.create_rectangle(app.innerMargin,
                            app.margin+app.innerMargin,
                            app.width-app.innerMargin,
                            app.height-app.innerMargin,
                            fill="white")

def drawLogs(app,canvas):
    for log in app.logs:
        logAttributes = log.getPosition()
        if log.paused() == False:
            if logAttributes[1] >= app.margin+app.innerMargin:
                if log.isPowerUp():
                    canvas.create_rectangle(logAttributes[0],
                                            logAttributes[1],
                                            logAttributes[0]+app.logWidth,
                                            logAttributes[1]+app.logHeight,
                                            fill = 'yellow')
                else:
                    canvas.create_rectangle(logAttributes[0],
                                            logAttributes[1],
                                            logAttributes[0]+app.logWidth,
                                            logAttributes[1]+app.logHeight,
                                            fill = 'brown')
        else:
          canvas.create_rectangle(logAttributes[0],
                                    logAttributes[1],
                                    logAttributes[0]+app.logWidth,
                                    logAttributes[1]+app.logHeight,
                                    fill = 'red')  

        question = log.getQuestion()
        if logAttributes[1] >= app.margin+app.innerMargin:
            if log.isPowerUp():
                canvas.create_text(logAttributes[0]+ app.logWidth/2,
                                logAttributes[1]+app.logHeight/2,
                                text = question,
                                font = "Times 8 italic bold",
                                fill = "black")
            else:
                canvas.create_text(logAttributes[0]+ app.logWidth/2,
                                logAttributes[1]+app.logHeight/2,
                                text = question,
                                font = "Times 8 italic bold",
                                fill = "white")

def drawGameOver(app,canvas):
    canvas.create_rectangle(0,
                            3*app.height/7,
                            app.width,
                            4*app.height/7,
                            fill = 'red')

    canvas.create_text(app.width/2,
                        app.height/2,
                        text = f'GAME OVER -- Final Score: {app.score}',
                        fill = 'white')

def drawEvalSteps(app,canvas):
    evalMargin = min(app.width,app.height)//5
    textWidth = (app.width)/2
    textHeight = (app.height)/2
    if app.pausedLog != None:
        canvas.create_rectangle(app.innerMargin + evalMargin,
                                app.margin + app.innerMargin + evalMargin,
                                app.width - app.innerMargin - evalMargin,
                                app.height - app.innerMargin - evalMargin,
                                fill = 'white')
        canvas.create_text(textWidth,
                        app.margin + 3*app.innerMargin + evalMargin,
                        text = app.pausedLog.getQuestion(),
                        fill = "black")
        textHeight += 30
        evalString = evalQuestionString(app.pausedLog.getQuestion())
        
        canvas.create_text(textWidth,
                            textHeight,
                            text = evalString,
                            fill = 'black')
def drawBackground(app,canvas):
    canvas.create_rectangle(app.innerMargin,
                            app.margin + app.innerMargin,
                            app.width - app.innerMargin,
                            app.height-app.innerMargin,
                            fill = "light blue")
    if app.gameStarted == False:
        canvas.create_rectangle(app.cx - app.logWidth/2,
                                app.cy + app.r,
                                app.cx + app.logWidth/2,
                                app.cy + app.r + app.logHeight,
                                fill = 'black')
    boardWidth = app.width - 2 * app.innerMargin
    canvas.create_rectangle(app.innerMargin,
                            app.margin + app.innerMargin,
                            boardWidth/10,
                            app.height - app.innerMargin,
                            fill = "brown")
    
    canvas.create_rectangle(app.width - app.innerMargin - boardWidth/10,
                            app.margin + app.innerMargin,
                            app.width - app.innerMargin,
                            app.height - app.innerMargin,
                            fill = "brown")
    
def drawCurrentType(app,canvas):
    canvas.create_text (app.width/2,
                        2*app.margin/3,
                        text = f'Current Type = {app.type}',
                        font = "Times 10 italic bold")
    

def redrawAll(app,canvas):
    canvas.create_text(app.width//2,
                         app.margin//3,
                         text = f'Score = {app.score}',
                         font = "Times 20 italic bold")
    drawBoard(app,canvas)
    drawBackground(app,canvas)
    drawCircle(app,canvas)
    drawLogs(app,canvas)
    drawCurrentType(app,canvas)

    if app.gameOver and app.afterClicked == False:
        drawGameOver(app,canvas)
        
    
    if app.gamePaused:
        if app.clicked:
            drawEvalSteps(app,canvas)

def runGame():
    runApp(width=744,height=646)


