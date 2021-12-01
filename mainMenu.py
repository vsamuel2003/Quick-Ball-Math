from cmu_112_graphics import *
import gameGraphics 
import practice

def appStarted(app):
    app.margin = app.height/6
    app.instructions = False

def keyPressed(app,event):
    if event.key == "i":
        app.instructions = False

def mousePressed(app,event):
    if (app.width/3 <= event.x <= 2*app.width/3 and 
        app.margin <= event.y <= app.height/6 + app.margin):
        gameGraphics.runGame()
    
    elif (app.width/3 <= event.x <= 2*app.width/3 and 
        app.height/4 + app.margin <= event.y <= 8*app.height/20 + app.margin):
        practice.runGame()
    
    elif (app.width/3 <= event.x <= 2*app.width/3 and 
          app.height/2 + app.margin <= event.y <= 4*app.height/6 + app.margin):
        app.instructions = True

#credits to the Ninja to the Stars game from which the background design and 
#game general design were taken
def drawTitle(app,canvas):
    canvas.create_text(app.width/2,
                        app.height/10,
                        text = 'Quick Math Ball',
                        font = "Times 40 italic bold",
                        fill = 'black')

def drawMenuFeatures(app,canvas):
    canvas.create_rectangle(app.width/3,
                            app.margin,
                            2*app.width/3,
                            app.height/6 + app.margin,
                            fill = "white")
    canvas.create_text(app.width/2,
                        app.height/12 + app.margin,
                        text = "Click Here to Begin the Game",
                        fill = "black")
    
    canvas.create_rectangle(app.width/3,
                            app.height/4 + app.margin,
                            2*app.width/3,
                            8*app.height/20 + app.margin,
                            fill = "white")
    canvas.create_text(app.width/2,
                        13*app.height/40 + app.margin,
                        text = "Click Here to Begin the Practice Game",
                        fill = "black")
    
    canvas.create_rectangle(app.width/3,
                            app.height/2 + app.margin,
                            2*app.width/3,
                            4*app.height/6 + app.margin,
                            fill = "white")
    canvas.create_text(app.width/2,
                        3.5*app.height/6 + app.margin,
                        text = "Click Here to Read Instructions",
                        fill = "black")

def drawInstructions(app,canvas):
    instructions = '''
The Objective of this game is to get the highest number of points as possible
- Jumping onto a log will reward one point

- Yellow logs are power up logs. Jumping on these logs will not only give you
  ten extra points but will also move you up in the game

- To enter an answer, type the answer in decimal form and click enter

- You must answer questions fast because if you are on a log that falls of 
  the bottom of the screen the game is over

- When the game is over you will have the option to click on any log on the 
  screen to get step by step instructions on how to answer the question

- Clicking "r" at any time will reset the game and start over

- Clicking "i" at anytime will send you back to the main menu

- The Practice Game mode is the same as the regular game with the exception that
 pressing the space bar will pause the game at anytime and you can click on a 
 log at anytime to reveal the answer
'''

    canvas.create_rectangle(0,
                            0,
                            app.width,
                            app.height,
                            fill = "white")
    canvas.create_text(app.width/2,
                       app.height/2,
                       text = instructions,
                       fill = "black")

def redrawAll(app,canvas):
    if app.instructions == False:
        drawTitle(app,canvas)
        drawMenuFeatures(app,canvas)
    else:
        drawInstructions(app,canvas)

def runMenu():
    runApp(width=744,height=646)

runMenu()


