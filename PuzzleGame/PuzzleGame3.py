from bangtal import *
import time
import random

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene = Scene("퍼즐게임3", "images/배경.png")

def find_index(object):
    for index in range(16):
        if game_board[index] == object:
            return index

def movable(index):
    if index < 0: return False
    if index > 15: return False
    if index % 4 > 0 and index - 1 == blank: return True
    if index % 4 < 3 and index + 1 == blank: return True
    if index > 3 and index - 4 == blank: return True
    if index < 12 and index + 4 == blank: return True
    return False

def move(index):
    global blank
    game_board[index].locate(scene, 300 + 150*(blank%4), 470 - 150*(blank//4))
    game_board[blank].locate(scene, 300 + 150*(index%4), 470 - 150*(index//4))
    
    game_board[index], game_board[blank] = game_board[blank], game_board[index]
    blank = index

def completed():
    for index in range(16):
        if game_board[index] != init_board[index]: return False
    return True

delta = [1, -1, -4, 4]
def random_move():
    while True:
        index = blank + delta[random.randrange(4)]
        if movable(index): break
    move(index)

def onMouseAction_piece(object):
    index = find_index(object)

    if movable(index):
        move(index)

        if completed():
            showMessage("Completed!!")

game_board = []
init_board = []
for index in range(16):
    piece = Object("images/" + str(index + 1) + ".png")
    piece.locate(scene, 300 + 150*(index%4), 470 - 150*(index//4))
    piece.show()

    #def onMouseAction_piece(x, y, action, object = piece):
    #    index = find_index(object)

    #    if movable(index):
    #        move(index)

    #        if completed():
    #            showMessage("Completed!!")

    #piece.onMouseAction = onMouseAction_piece
    piece.onMouseAction = lambda x, y, action, object=piece : onMouseAction_piece(object)

    game_board.append(piece)
    init_board.append(piece)

blank = 15
game_board[15].hide()

count = 5
timer = Timer(1)
def onTimeout():
    random_move()

    global count
    count = count - 1
    if count > 0:
        timer.set(0.1)
        timer.start()
timer.onTimeout = onTimeout
timer.start()

startGame(scene)