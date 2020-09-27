from bangtal import *
import time

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene = Scene("퍼즐게임", "images/flower.png")

background = Object("images/flower_bg.png")
background.locate(scene, 0, 0)

startButton = Object('images/start.png')
startButton.locate(scene, 590, 370)
startButton.show()

endButton = Object('images/end.png')
endButton.locate(scene, 590, 320)
endButton.show()

bestTime = 0
startTime = 0
endTime = 0
curTime = 3600

truePos = [(370, 450), (550, 450), (730, 450), (370, 270), (550, 270), (730, 270), (370, 90), (550, 90), (730, 90)]
shufflePos = []

puzzles = []
blank = Object('images/blank.png')
blankPos = 0
for i in range(8):
    puzzle = Object('images/flower' + str(i + 1) + '.png')
    puzzles.append(puzzle)
puzzles.append(blank)

def setPos(pos):
    for i in range(9):
        puzzles[i].locate(scene, pos[i][0], pos[i][1])

def showPuzzles():
    background.show()
    for i in range(9):
        puzzles[i].show()

def startButton_onMouse(x, y, action):
    global blankPos, shufflePos

    startTime = time.time()
    startButton.hide()
    endButton.hide()
    blankPos = truePos[8]
    shufflePos = [truePos[1], truePos[0], truePos[4], truePos[7], truePos[6], blankPos, truePos[3], truePos[2], truePos[5]]
    setPos(shufflePos)
    showPuzzles()
    print(blankPos[0], blankPos[1])
startButton.onMouseAction = startButton_onMouse

def endPuzzle():
    global shufflePos
    for i in range(9):
        if shufflePos[i] != truePos[i]:
            return False
    return True

def endButton_onMouse(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouse

def puzzle_onMouseAction(x, y, action):
    global blankPos, shufflePos, startTime, endTime, curTime, bestTime
    print(x, y)

    showPuzzles()

    if endPuzzle():
        endTime = time.time()
        curTime = round(endTime - startTime, 1)
        showMessage(str(curTime) + "초")
        if curTime < bestTime:
            showMessage("최단 기록 갱신! 축하합니다!")
            bestTime = curTime
        startButton.setImage('images/restart.png')
        startButton.show()
        endButton.show()
for puzzle in puzzles:
    puzzle.onMouseAction = puzzle_onMouseAction

startGame(scene)